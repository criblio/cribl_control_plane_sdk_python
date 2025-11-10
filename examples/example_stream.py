"""
Cribl Stream Configuration Example

This example demonstrates how to programmatically create and configure a 
complete data pipeline in Cribl Stream using the Control Plane SDK.

This example creates:

1. A Worker Group to manage the configuration.
2. A TCP JSON source to receive data on port 9020.
3. A Filesystem Destination to store processed data.
4. A Pipeline that filters events and keeps only data in the "name" 
field.
5. A Route that connects the Source to the Pipeline and Destination.

This example also deploys the configuration to the Worker Group to make it 
active.

Data flow: TCP JSON Source → Route → Pipeline → Filesystem Destination

The example includes error handling and checks for existing resources.

Prerequisites:
- An .env file that is configured with your credentials.
- An Enterprise License on the server.
"""

import asyncio
from cribl_control_plane.models import (
    ConfigGroup,
    InputTcpjsonTcpjson3,  # Part of InputTcpjson union type
    TypeTcpjsonOption,
    AuthType2Options,
    OutputFilesystemFilesystem1,  # Part of OutputFilesystem union type
    OutputFilesystemType1,
    Pipeline,
    RoutesRoute,
    Conf,
    PipelineFunctionConf,
    FunctionSpecificConfigs,
    ProductsCore
)
from auth import base_url, create_cribl_client


PORT = 9020
AUTH_TOKEN = "4a4b3663-7a57-7369-7632-795553573668"
WORKER_GROUP_ID = "my-worker-group"

my_worker_group = ConfigGroup(
    id=WORKER_GROUP_ID,
    description="My Worker Group",
    on_prem=True
)

# TCP JSON Source configuration
# Using InputTcpjsonTcpjson3 which is part of InputTcpjson union type
tcp_json_source = InputTcpjsonTcpjson3(
    id="my-tcp-json",
    type=TypeTcpjsonOption.TCPJSON,
    port=PORT,
    auth_type=AuthType2Options.MANUAL,
    auth_token=AUTH_TOKEN
)

# Filesystem Destination configuration
# Using OutputFilesystemFilesystem1 which is part of OutputFilesystem union type
file_system_destination = OutputFilesystemFilesystem1(
    id="my-fs-destination",
    type=OutputFilesystemType1.FILESYSTEM,
    dest_path="/tmp/my-output"
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
    output=file_system_destination.id,
    filter_="__inputId=='tcpjson:my-tcp-json'",
    description="This is my new Route"
)

group_url = f"{base_url}/m/{my_worker_group.id}"


async def main():
    # Initialize Cribl client
    cribl = await create_cribl_client()

    # Verify that Worker Group doesn't already exist
    worker_group_response = cribl.groups.get(
        id=my_worker_group.id,
        product=ProductsCore.STREAM
    )
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"⚠️ Worker Group already exists: {my_worker_group.id}. Try different group id.")
        return

    # Create Worker Group
    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=my_worker_group.id,
        description=my_worker_group.description,
        on_prem=my_worker_group.on_prem
    )
    print(f"✅ Worker Group created: {my_worker_group.id}")

    # Create TCP JSON Source
    cribl.sources.create(
        request=tcp_json_source,
        server_url=group_url
    )
    print(f"✅ Tcp Json Source created: {tcp_json_source.id}")

    # Create Filesystem Destination
    cribl.destinations.create(
        request=file_system_destination,
        server_url=group_url
    )
    print(f"✅ Filesystem Destination created: {file_system_destination.id}")

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
        group_id=my_worker_group.id,
        message="Commit for Stream example",
        effective=True,
        files=["."]
    )
    
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {my_worker_group.id}, commit ID: {version}")

    # Deploy configuration changes
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=my_worker_group.id,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {my_worker_group.id}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
