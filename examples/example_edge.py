"""
Cribl Stream Configuration Example

This example demonstrates how to programmatically create and configure a complete
data pipeline in Cribl Edge using the Control Plane SDK. It creates:

1. A Fleet to manage the configuration
2. A Syslog source to receive data on port 9021
3. An Amazon S3 destination to store processed data
4. A pipeline that filters events to keep only eventSource and eventID fields
5. A route that connects the source to the pipeline and destination
6. Deploys the configuration to the fleet to make it active

Data flow: Syslog Source → Route → Pipeline → S3 Destination

The example includes proper error handling, checks for existing resources,
and automatically deploys the configuration to make it active.

Prerequisites:
- Configure your .env file with appropriate credentials
- Update AWS S3 configuration values (AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, AWS_REGION)
- Requires Enterprise License on the server
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
    InputSyslogTLSSettingsServerSide2
)
from auth import base_url, create_cribl_client


FLEET_ID = "my-fleet"

# Syslog source configuration
SYSLOG_PORT = 9021

# Amazon S3 destination configuration
# [ UPDATE THESE VALUES ]
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

my_fleet = ConfigGroup(
    on_prem=True,
    worker_remote_access=True,
    is_fleet=True,
    is_search=False,
    id=FLEET_ID
)

syslog_source = InputSyslogSyslog2(
    id="my-syslog-source",
    type=InputSyslogType2.SYSLOG,
    tcp_port=SYSLOG_PORT,
    tls=InputSyslogTLSSettingsServerSide2(disabled=True)
)

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

# Pipeline configuration: filters events to keep only eventSource and eventID fields
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

route = RoutesRoute(
    final=False,
    id="my-route",
    name="my-route",
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_=f"__inputId=='{syslog_source.id}'",
    description="This is my new route"
)

group_url = f"{base_url}/m/{my_fleet.id}"


async def main():
    # Initialize Cribl client
    cribl = await create_cribl_client()

    # Verify fleet doesn't already exist
    fleet_response = cribl.groups.get(
        id=my_fleet.id,
        product="edge"
    )
    if fleet_response.items and len(fleet_response.items) > 0:
        print(f"⚠️ Fleet already exists: {my_fleet.id}. Try different fleet id.")
        return

    # Create Fleet
    cribl.groups.create(
        product="edge",
        id=my_fleet.id,
        on_prem=my_fleet.on_prem,
        worker_remote_access=my_fleet.worker_remote_access,
        is_fleet=my_fleet.is_fleet,
        is_search=my_fleet.is_search
    )
    print(f"✅ Fleet created: {my_fleet.id}")

    # Create Syslog source
    cribl.sources.create(
        request=syslog_source,
        server_url=group_url
    )
    print(f"✅ Syslog source created: {syslog_source.id}")

    # Create S3 destination
    cribl.destinations.create(
        request=s3_destination,
        server_url=group_url
    )
    print(f"✅ S3 destination created: {s3_destination.id}")

    # Create pipeline
    cribl.pipelines.create(
        id=pipeline.id,
        conf=pipeline.conf,
        server_url=group_url
    )
    print(f"✅ Pipeline created: {pipeline.id}")

    # Add route to routing table
    routes_list_response = cribl.routes.list(
        server_url=group_url
    )
    if not routes_list_response.items or len(routes_list_response.items) == 0:
        raise Exception("No routes found")
    
    routes = routes_list_response.items[0]
    if not routes or not routes.id:
        raise Exception("No routes found")
    
    routes.routes = [route] + (routes.routes or [])
    cribl.routes.update(
        id_param=routes.id,
        id=routes.id,
        routes=routes.routes,
        server_url=group_url
    )
    print(f"✅ Route inserted: {route.id}")

    # Deploy configuration changes
    response = cribl.groups.configs.versions.get(
        id=my_fleet.id,
        product="edge"
    )
    if not response.items:
        raise Exception("No version found")
    
    version = response.items[0]

    cribl.groups.deploy(
        product="edge",
        id=my_fleet.id,
        version=version
    )
    print(f"✅ Fleet changes deployed: {my_fleet.id}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
