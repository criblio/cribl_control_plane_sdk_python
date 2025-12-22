"""
Replace the placeholder values for ONPREM_SERVER_URL, ONPREM_USERNAME, and
ONPREM_PASSWORD with your server URL and credentials. Your credentials are
sensitive information and should be kept private.

NOTE: This example is for on-prem deployments only.

Prerequisites:
- Your AWS S3 values for AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, and
AWS_REGION.
- An Enterprise License on the server.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    Security,
    ProductsCore,
    CreateInputInputSyslogSyslog2,
    CreateInputInputSyslogType2,
    CreateOutputOutputS3,
    CreateOutputTypeS3,
    CreateOutputCompressionS3,
    CompressionLevelS3,
    Pipeline,
    RoutesRoute,
    PipelineConf,
    ConfInput,
    PipelineFunctionEval,
    PipelineFunctionEvalID,
    PipelineFunctionConf,
    FunctionConfSchemaEval,
    CreateInputInputSyslogTLSSettingsServerSide2,
)
from typing import List, cast

ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
WORKER_GROUP_ID = "your-worker-group-id"

# Syslog Source configuration
SYSLOG_PORT = 9021

# S3 Destination configuration: Replace the placeholder values
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

base_url = f"{ONPREM_SERVER_URL}/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Syslog Source configuration
syslog_source = CreateInputInputSyslogSyslog2(
    id="in-syslog-9021",
    type=CreateInputInputSyslogType2.SYSLOG,
    tcp_port=SYSLOG_PORT,
    tls=CreateInputInputSyslogTLSSettingsServerSide2(disabled=True),
)

# S3 Destination configuration
s3_destination = CreateOutputOutputS3(
    id="out_s3",
    type=CreateOutputTypeS3.S3,
    bucket=AWS_BUCKET_NAME,
    region=AWS_REGION,
    aws_secret_key=AWS_SECRET_KEY,
    aws_api_key=AWS_API_KEY,
    compress=CreateOutputCompressionS3.GZIP,
    compression_level=CompressionLevelS3.BEST_SPEED,
    empty_dir_cleanup_sec=300,
)

# Pipeline configuration: filter events and keep only data in the "eventSource" and "eventID" fields
pipeline = Pipeline(
    id="my_pipeline",
    conf=PipelineConf(
        async_func_timeout=1000,
        functions=cast(
            List[PipelineFunctionConf],
            [
                PipelineFunctionEval(
                    filter_="true",
                    conf=FunctionConfSchemaEval(
                        remove=["*"],
                        keep=["eventSource", "eventID"],
                    ),
                    id=PipelineFunctionEvalID.EVAL,
                    final=True,
                )
            ],
        ),
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
    # Initialize Cribl client
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
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
        on_prem=True,
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
    )
    print(f"✅ Worker Group created: {WORKER_GROUP_ID}")

    # Create Syslog Source
    cribl.sources.create(request=syslog_source, server_url=group_url)
    print(f"✅ Syslog source created: {syslog_source.id}")

    # Create S3 Destination
    cribl.destinations.create(request=s3_destination, server_url=group_url)
    print(f"✅ S3 Destination created: {s3_destination.id}")

    # Create Pipeline
    cribl.pipelines.create(id=pipeline.id, conf=ConfInput.model_validate(pipeline.conf.model_dump()), server_url=group_url)
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

