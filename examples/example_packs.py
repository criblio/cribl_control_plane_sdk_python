"""
Cribl Packs Integration Example

This example demonstrates how to install and configure a Cribl Pack using the 
Control Plane SDK. It installs the Palo Alto Networks pack from GitHub and 
creates a complete data pipeline within the pack:

1. Installs the Palo Alto Networks pack from a remote URL
2. Creates a TCP JSON source to receive data on port 9020
3. Creates an Amazon S3 destination for data storage
4. Creates a pipeline that filters events to keep only the "name" field
5. Creates a route connecting the source to the pipeline and destination

Data flow: TCP JSON Source → Route → Pipeline → S3 Destination

Note: This example creates resources within the pack but does not commit
or deploy the configuration to a worker group.

Prerequisites: 
- Configure your .env file with appropriate credentials
- Create a worker group with the configured WORKER_GROUP_ID
- Update AWS S3 configuration values (AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, AWS_REGION)
"""

import asyncio
from cribl_control_plane.models import (
    InputTcpjson,
    InputTcpjsonType,
    InputTcpjsonAuthenticationMethod,
    OutputS3,
    OutputS3Type,
    OutputS3Compression,
    OutputS3CompressionLevel,
    Pipeline,
    RoutesRoute,
    Conf,
    PipelineFunctionConf,
    FunctionSpecificConfigs
)
from auth import base_url, create_cribl_client

# Define the worker group id
WORKER_GROUP_ID = "default"

# Pack to install
PACK_URL = "https://github.com/criblpacks/cribl-palo-alto-networks/releases/download/1.1.5/cribl-palo-alto-networks-d6bc6883-1.1.5.crbl"
PACK_ID = "cribl-palo-alto-networks"


# TCP JSON source configuration
AUTH_TOKEN = "4a4b3663-7a57-7369-7632-795553573668"
PORT = 9020

# Amazon S3 destination configuration
# [ UPDATE THESE VALUES ]
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

group_url = f"{base_url}/m/{WORKER_GROUP_ID}"
pack_url = f"{group_url}/p/{PACK_ID}"

# TCP JSON source configuration
tcp_json_source = InputTcpjson(
    id="my-tcp-json",
    type=InputTcpjsonType.TCPJSON,
    port=PORT,
    auth_type=InputTcpjsonAuthenticationMethod.MANUAL,
    auth_token=AUTH_TOKEN
)

# Amazon S3 destination configuration
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

# Pipeline configuration: filters events to keep only the "name" field
pipeline = Pipeline(
    id="my-pipeline",
    conf=Conf(
        async_func_timeout=1000,
        functions=[
            PipelineFunctionConf(
                filter_="true",
                conf=FunctionSpecificConfigs.model_validate({  # type: ignore
                    "remove": ["*"],
                    "keep": ["name"]
                }),
                id="eval",
                final=True
            )
        ]
    )
)

# Route configuration: routes data from the source to the pipeline and destination
route = RoutesRoute(
    final=False,
    id="my-route",
    name="my-route",
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_="__inputId=='tcpjson:my-tcp-json'",
    description="This is my new route"
)


async def main():
    cribl = await create_cribl_client()

    # Install pack from URL
    cribl.packs.install(
        request={
            "source": PACK_URL,
            "id": PACK_ID
        },
        server_url=group_url
    )
    print(f"✅ Installed pack \"{PACK_ID}\" from: {PACK_URL}")

    # Create TCP JSON source in pack
    cribl.sources.create(
        request=tcp_json_source,
        server_url=pack_url
    )
    print(f"✅ Created tcp json source: {tcp_json_source.id} in pack: \"{PACK_ID}\"")

    # Create s3 destination in pack
    cribl.destinations.create(
        request=s3_destination,
        server_url=pack_url
    )
    print(f"✅ Created s3 destination: {s3_destination.id} in pack: \"{PACK_ID}\"")

    # Create pipeline in pack
    cribl.pipelines.create(
        id=pipeline.id,
        conf=pipeline.conf,
        server_url=pack_url
    )
    print(f"✅ Created pipeline: {pipeline.id} in pack: \"{PACK_ID}\"")

    # Add route to routing table in pack
    routes_list_response = cribl.routes.list(
        server_url=pack_url
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
        server_url=pack_url
    )
    print(f"✅ Route inserted: {route.id} in pack: {PACK_ID}")
    print("ℹ️ This example does not commit / deploy the configuration to the worker group.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
