"""
Cribl Stream Configuration Example

This example demonstrates how to programmatically create and configure a complete
data pipeline in Cribl Stream using the Control Plane SDK. It creates:

1. A worker group to manage the configuration
2. A TCP JSON source to receive data on port 9020
3. A filesystem destination to output processed data
4. A pipeline that filters events to keep only the "name" field
5. A route that connects the source to the pipeline and destination
6. Deploys the configuration to the worker group to make it active

Data flow: TCP JSON Source → Route → Pipeline → File Destination

The example includes proper error handling, checks for existing resources,
and automatically deploys the configuration to make it active.

Prerequisites:
- Configure your .env file
- Requires Enterprise License on the server
"""

import asyncio
from cribl_control_plane.models import (
    ConfigGroup,
    InputTcpjson,
    InputTcpjsonType,
    InputTcpjsonAuthenticationMethod,
    OutputFilesystem,
    OutputFilesystemType,
    Pipeline,
    RoutesRoute,
    Conf,
    PipelineFunctionConf,
    FunctionSpecificConfigs
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

tcp_json_source = InputTcpjson(
    id="my-tcp-json",
    type=InputTcpjsonType.TCPJSON,
    port=PORT,
    auth_type=InputTcpjsonAuthenticationMethod.MANUAL,
    auth_token=AUTH_TOKEN
)

file_system_destination = OutputFilesystem(
    id="my-fs-destination",
    type=OutputFilesystemType.FILESYSTEM,
    dest_path="/tmp/my-output"
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

route = RoutesRoute(
    final=False,
    id="my-route",
    name="my-route",
    pipeline=pipeline.id,
    output=file_system_destination.id,
    filter_="__inputId=='tcpjson:my-tcp-json'",
    description="This is my new route"
)

group_url = f"{base_url}/m/{my_worker_group.id}"


async def main():
    # Initialize Cribl client
    cribl = await create_cribl_client()

    # Verify worker group doesn't already exist
    worker_group_response = cribl.groups.get(
        id=my_worker_group.id,
        product="stream"
    )
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"⚠️ Worker Group already exists: {my_worker_group.id}. Try different group id.")
        return

    # Create worker group
    cribl.groups.create(
        product="stream",
        id=my_worker_group.id,
        description=my_worker_group.description,
        on_prem=my_worker_group.on_prem
    )
    print(f"✅ Worker Group created: {my_worker_group.id}")

    # Create TCP JSON source
    cribl.sources.create(
        request=tcp_json_source,
        server_url=group_url
    )
    print(f"✅ Tcp Json Source created: {tcp_json_source.id}")

    # Create file destination
    cribl.destinations.create(
        request=file_system_destination,
        server_url=group_url
    )
    print(f"✅ File Destination created: {file_system_destination.id}")

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
        id=my_worker_group.id,
        product="stream"
    )
    if not response.items:
        raise Exception("No version found")
    
    version = response.items[0]

    cribl.groups.deploy(
        product="stream",
        id=my_worker_group.id,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {my_worker_group.id}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
