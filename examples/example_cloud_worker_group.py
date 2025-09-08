""""
Cribl.Cloud Worker Group Management Example

This example demonstrates how to create and manage a Cribl.Cloud-based 
Worker Group in Cribl Stream using the Control Plane SDK.

1. Create a Cribl.Cloud Worker Group using the AWS provider configuration. 
Set the maximum estimated ingest rate to 24 MB/s and configure 9 
Worker Processes.
2. Verify that the Worker Group doesn't already exist.
3. Scale up the Worker Group to 48 MB/s maximum estimated ingest rate and 
21 Worker Processes.
4. Provision the Worker Group to activate Cribl.Cloud resources.

The Cribl documentation provides more information about ingest rates and 
provisioning: 
https://docs.cribl.io/stream/cloud-workers/#create-a-cloud-worker-group

Prerequisites: Replace the placeholder values for ORG_ID, CLIENT_ID, 
CLIENT_SECRET, and WORKSPACE_NAME with your Organization ID, Client ID and 
Secret, and Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, 
follow the steps at https://docs.cribl.io/api/#criblcloud. Your Client ID 
and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only. It does not require 
.env file configuration.
"""


import asyncio
from cribl_control_plane.models import ConfigGroup, ConfigGroupCloud, CloudProvider
from auth import AuthCloud, CloudConfiguration


ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"

WORKER_GROUP_ID = "your-cloud-worker-group-id"

group = ConfigGroup(
    on_prem=False,
    worker_remote_access=True,
    cloud=ConfigGroupCloud(
        provider=CloudProvider.AWS,
        region="us-east-1"
    ),
    provisioned=False,
    is_fleet=False,
    is_search=False,
    estimated_ingest_rate=2048,  # Equivalent to 24 MB/s maximum estimated ingest rate with 9 Worker Processes
    id=WORKER_GROUP_ID,
    name="my-aws-worker-group"
)


async def main():
    auth = AuthCloud(CloudConfiguration(
        org_id=ORG_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        workspace_name=WORKSPACE_NAME
    ))
    cribl = await auth.get_client()

    # Verify that Worker Group doesn't already exist
    worker_group_response = cribl.groups.get(
        id=group.id,
        product="stream"
    )
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"⚠️ Worker Group already exists: {group.id}. Try a different group ID.")
        return

    # Create the worker group
    cribl.groups.create(
        product="stream",
        id=group.id,
        on_prem=group.on_prem,
        worker_remote_access=group.worker_remote_access,
        cloud=group.cloud,
        provisioned=group.provisioned,
        is_fleet=group.is_fleet,
        is_search=group.is_search,
        estimated_ingest_rate=group.estimated_ingest_rate,
        name=group.name
    )
    print(f"✅ Worker Group created: {group.id}")

    # Scale and provision the Worker Group
    group.estimated_ingest_rate = 4096  # Equivalent to 48 MB/s maximum estimated ingest rate with 21 Worker Processes
    group.provisioned = True
    cribl.groups.update(
        product="stream",
        id=group.id,
        id_param=group.id,
        on_prem=group.on_prem,
        worker_remote_access=group.worker_remote_access,
        cloud=group.cloud,
        provisioned=group.provisioned,
        is_fleet=group.is_fleet,
        is_search=group.is_search,
        estimated_ingest_rate=group.estimated_ingest_rate,
        name=group.name
    )
    print(f"✅ Worker Group scaled and provisioned: {group.id}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
