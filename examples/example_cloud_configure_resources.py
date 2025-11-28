"""
Replace the placeholder values for ORG_ID, CLIENT_ID, CLIENT_SECRET,
and WORKSPACE_NAME with your Organization ID, Client ID and Secret, and
Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, follow the steps
at https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.

Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only.

Prerequisites:
- Your AWS S3 values for AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, and
AWS_REGION.
- An Enterprise License on the server.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    InputSyslogSyslog2,
    InputSyslogType2,
    OutputS3,
    OutputS3Type,
    OutputS3Compression,
    OutputS3CompressionLevel,
    Pipeline,
    RoutesRoute,
    Conf,
    PipelineFunctionConf,
    FunctionSpecificConfigs,
    InputSyslogTLSSettingsServerSide2,
    Security,
    SchemeClientOauth,
    ConfigGroupCloud,
    CloudProvider,
    GroupCreateRequestEstimatedIngestRate
)

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"
WORKER_GROUP_ID = "my-group"

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Syslog Source configuration
SYSLOG_PORT = 9021

# S3 Destination configuration: Replace the placeholder values
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

# Syslog Source configuration
syslog_source = InputSyslogSyslog2(
    id="in-syslog-9021",
    type=InputSyslogType2.SYSLOG,
    tcp_port=SYSLOG_PORT,
    tls=InputSyslogTLSSettingsServerSide2(disabled=True),
)

# S3 Destination configuration
s3_destination = OutputS3(
    id="out_s3",
    type=OutputS3Type.S3,
    bucket=AWS_BUCKET_NAME,
    region=AWS_REGION,
    aws_secret_key=AWS_SECRET_KEY,
    aws_api_key=AWS_API_KEY,
    compress=OutputS3Compression.GZIP,
    compression_level=OutputS3CompressionLevel.BEST_SPEED,
    empty_dir_cleanup_sec=300,
)

# Pipeline configuration: filter events and keep only data in the "eventSource" and "eventID" fields
pipeline = Pipeline(
    id="my_pipeline",
    conf=Conf(
        async_func_timeout=1000,
        functions=[
            PipelineFunctionConf(
                filter_="true",
                conf=FunctionSpecificConfigs.model_validate(
                    {  # type: ignore
                        "remove": ["*"],
                        "keep": ["eventSource", "eventID"],
                    }
                ),
                id="eval",
                final=True,
            )
        ],
    ),
)

# Route configuration: route data from the Source to the Pipeline and Destination
route = RoutesRoute(
    final=False,
    id="my_route",
    name="my_route",
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_=f"__inputId=='{syslog_source.id}'",
    description="This is my new Route",
)

async def main():
    # Create authenticated SDK client
    client_oauth = SchemeClientOauth(
      client_id=CLIENT_ID,
      client_secret=CLIENT_SECRET,
      token_url="https://login.cribl.cloud/oauth/token",
      audience="https://api.cribl.cloud",
    )

    security = Security(client_oauth=client_oauth)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Verify that Worker Group doesn't already exist
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(
            f"❌ Worker Group already exists: {WORKER_GROUP_ID}. Try a different Worker Group ID."
        )
        return

    # Create Worker Group
    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        on_prem=False,
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        name=WORKER_GROUP_ID,
        estimated_ingest_rate=GroupCreateRequestEstimatedIngestRate.RATE12_MB_PER_SEC,
        cloud=ConfigGroupCloud(
            provider=CloudProvider.AWS,
            region="us-east-1"
        ),
    )
    print(f"✅ Worker Group created: {WORKER_GROUP_ID}")

    # Create Syslog Source
    cribl.sources.create(request=syslog_source, server_url=group_url)
    print(f"✅ Syslog source created: {syslog_source.id}")

    # Create S3 Destination
    cribl.destinations.create(request=s3_destination, server_url=group_url)
    print(f"✅ S3 Destination created: {s3_destination.id}")

    # Create Pipeline
    cribl.pipelines.create(id=pipeline.id, conf=pipeline.conf, server_url=group_url)
    print(f"✅ Pipeline created: {pipeline.id}")

    # Add Route to Routing table
    routes_list_response = cribl.routes.list(server_url=group_url)
    if not routes_list_response.items or len(routes_list_response.items) == 0:
        raise Exception("No Routes found")

    routes = routes_list_response.items[0]
    if not routes or not routes.id:
        raise Exception("No Routes found")

    routes.routes = [route] + (routes.routes or [])
    cribl.routes.update(
        id_param=routes.id, id=routes.id, routes=routes.routes, server_url=group_url
    )
    print(f"✅ Route added: {route.id}")

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        group_id=WORKER_GROUP_ID,
        message="Commit for Cribl Stream example",
        effective=True,
        files=["."]
    )
    
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy configuration changes
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

