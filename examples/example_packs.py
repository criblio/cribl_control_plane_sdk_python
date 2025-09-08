"""
Cribl Packs Integration Example

This example demonstrates how to install and configure a Cribl Pack using the 
Control Plane SDK. It installs the Palo Alto Networks Pack from GitHub and 
creates a complete data pipeline within the Pack.

1. Install the Palo Alto Networks Pack from a remote URL.
2. Create a TCP JSON Source to receive data on port 9020.
3. Create an Amazon S3 Destination for data storage.
4. Create a Pipeline that filters events and keeps only data in the "name" 
field.
5. Create a Route that connects the Source to the Pipeline and Destination.

Data flow: TCP JSON Source → Route → Pipeline → Amazon S3 Destination

NOTE: This example creates resources within the Pack but does not commit
or deploy the configuration to a Worker Group.

Prerequisites: 
- An .env file that is configured with your credentials.
- A Worker Group whose ID matches the configured WORKER_GROUP_ID value.
- Your AWS S3 values for AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, and 
AWS_REGION.
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


# TCP JSON Source configuration
AUTH_TOKEN = "4a4b3663-7a57-7369-7632-795553573668"
PORT = 9020

# Amazon S3 Destination configuration: Replace the placeholder values
AWS_API_KEY = "your-aws-api-key"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-aws-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your S3 bucket region

group_url = f"{base_url}/m/{WORKER_GROUP_ID}"
pack_url = f"{group_url}/p/{PACK_ID}"

# TCP JSON Source configuration
tcp_json_source = InputTcpjson(
    id="my-tcp-json",
    type=InputTcpjsonType.TCPJSON,
    port=PORT,
    auth_type=InputTcpjsonAuthenticationMethod.MANUAL,
    auth_token=AUTH_TOKEN
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

# Pipeline configuration: filter events and keep only data in the "name" field
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

# Route configuration: route data from the Source to the Pipeline and Destination
route = RoutesRoute(
    final=False,
    id="my-route",
    name="my-route",
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_="__inputId=='tcpjson:my-tcp-json'",
    description="This is my new Route"
)


async def main():
    cribl = await create_cribl_client()

    # Install Pack from URL
    cribl.packs.install(
        request={
            "source": PACK_URL,
            "id": PACK_ID
        },
        server_url=group_url
    )
    print(f"✅ Installed Pack \"{PACK_ID}\" from: {PACK_URL}")

    # Create TCP JSON Source in Pack
    cribl.sources.create(
        request=tcp_json_source,
        server_url=pack_url
    )
    print(f"✅ Created TCP JSON Source: {tcp_json_source.id} in Pack: \"{PACK_ID}\"")

    # Create Amazon S3 Destination in Pack
    cribl.destinations.create(
        request=s3_destination,
        server_url=pack_url
    )
    print(f"✅ Created Amazon S3 Destination: {s3_destination.id} in Pack: \"{PACK_ID}\"")

    # Create Pipeline in Pack
    cribl.pipelines.create(
        id=pipeline.id,
        conf=pipeline.conf,
        server_url=pack_url
    )
    print(f"✅ Created Pipeline: {pipeline.id} in Pack: \"{PACK_ID}\"")

    # Add Route to Routing table in Pack
    routes_list_response = cribl.routes.list(
        server_url=pack_url
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
        server_url=pack_url
    )
    print(f"✅ Added Route: {route.id} in Pack: {PACK_ID}")
    print("ℹ️ This example does not commit or deploy the configuration to the Worker Group.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
