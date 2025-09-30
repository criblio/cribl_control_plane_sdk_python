
"""
 Cribl Edge Configuration Example
 
 This example demonstrates how to programmatically create and configure a 
 complete data pipeline in Cribl Edge using the Control Plane SDK.
 
 This example creates:
 
 1. A Fleet to manage the configuration.
 2. A Syslog Source to receive data on port 9021.
 3. An Amazon S3 Destination to store processed data.
 4. A Pipeline that filters events and keeps only data in the "eventSource" 
 and "eventID" fields.
 5. A Route that connects the Source to the Pipeline and Destination.
 
 This example also deploys the configuration to the Fleet to make it active.
 
 Data flow: Syslog Source → Route → Pipeline → Amazon S3 Destination

 This example includes error handling and checks for existing resources.
 
 Prerequisites:
 - An .env file that is configured with your credentials.
 - Your AWS S3 values for AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, and 
 AWS_REGION.
 - An Enterprise License on the server.
"""

import asyncio
from cribl_control_plane.models import (
    ConfigGroup,
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
    ProductsCore
)
from auth import base_url, create_cribl_client


FLEET_ID = "my-fleet"

# Syslog Source configuration
SYSLOG_PORT = 9021

# Amazon S3 Destination configuration: Replace the placeholder values
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

# Fleet configuration
my_fleet = ConfigGroup(
    on_prem=True,
    worker_remote_access=True,
    is_fleet=True,
    is_search=False,
    id=FLEET_ID
)

# Syslog Source configuration
syslog_source = InputSyslogSyslog2(
    id="my-syslog-source",
    type=InputSyslogType2.SYSLOG,
    tcp_port=SYSLOG_PORT,
    tls=InputSyslogTLSSettingsServerSide2(disabled=True)
)

# Amazon S3 Destination configuration
s3_destination = OutputS3(
    id="my-s3-destination",
    type=OutputS3Type.S3,
    bucket=AWS_BUCKET_NAME,
    region=AWS_REGION,
    aws_secret_key=AWS_SECRET_KEY,
    aws_api_key=AWS_API_KEY,
    compress=OutputS3Compression.GZIP,
    compression_level=OutputS3CompressionLevel.BEST_SPEED,
    empty_dir_cleanup_sec=300
)

# Pipeline configuration: filter events and keep only data in the "eventSource" and "eventID" fields
pipeline = Pipeline(
    id="my-pipeline",
    conf=Conf(
        async_func_timeout=1000,
        functions=[
            PipelineFunctionConf(
                filter_="true",
                conf=FunctionSpecificConfigs.model_validate({  # type: ignore
                    "remove": ["*"],
                    "keep": ["eventSource", "eventID"]
                }),
                id="eval",
                final=True
            )
        ]
    )
)

# Route configuration: route data from the Source to the Pipeline and Destination
route = RoutesRoute(
    final=False,
    id="my-route",
    name="my-route",
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_=f"__inputId=='{syslog_source.id}'",
    description="This is my new Route"
)

group_url = f"{base_url}/m/{my_fleet.id}"


async def main():
    # Initialize Cribl client
    cribl = await create_cribl_client()

    # Verify that Fleet doesn't already exist
    fleet_response = cribl.groups.get(
        id=my_fleet.id,
        product=ProductsCore.EDGE
    )
    if fleet_response.items and len(fleet_response.items) > 0:
        print(f"⚠️ Fleet already exists: {my_fleet.id}. Try a different Fleet ID.")
        return

    # Create Fleet
    cribl.groups.create(
        product=ProductsCore.EDGE,
        id=my_fleet.id,
        on_prem=my_fleet.on_prem,
        worker_remote_access=my_fleet.worker_remote_access,
        is_fleet=my_fleet.is_fleet,
        is_search=my_fleet.is_search
    )
    print(f"✅ Fleet created: {my_fleet.id}")

    # Create Syslog Source
    cribl.sources.create(
        request=syslog_source,
        server_url=group_url
    )
    print(f"✅ Syslog source created: {syslog_source.id}")

    # Create Amazon S3 Destination
    cribl.destinations.create(
        request=s3_destination,
        server_url=group_url
    )
    print(f"✅ Amazon S3 Destination created: {s3_destination.id}")

    # Create Pipeline
    cribl.pipelines.create(
        id=pipeline.id,
        conf=pipeline.conf,
        server_url=group_url
    )
    print(f"✅ Pipeline created: {pipeline.id}")

    # Add Route to Routing table
    routes_list_response = cribl.routes.list(
        server_url=group_url
    )
    if not routes_list_response.items or len(routes_list_response.items) == 0:
        raise Exception("No Routes found")
    
    routes = routes_list_response.items[0]
    if not routes or not routes.id:
        raise Exception("No Routes found")
    
    routes.routes = [route] + (routes.routes or [])
    cribl.routes.update(
        id_param=routes.id,
        id=routes.id,
        routes=routes.routes,
        server_url=group_url
    )
    print(f"✅ Route added: {route.id}")

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        group_id=my_fleet.id,
        message="Commit for Edge example",
        effective=True,
        files=["."]
    )
    
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the fleet: {my_fleet.id}, commit ID: {version}")

    # Deploy configuration changes
    cribl.groups.deploy(
        product=ProductsCore.EDGE,
        id=my_fleet.id,
        version=version
    )
    print(f"✅ Fleet changes deployed: {my_fleet.id}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
