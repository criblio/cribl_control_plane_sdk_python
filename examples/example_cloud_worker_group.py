"""
Cloud Worker Group Management Example

This example demonstrates how to create and manage a cloud-based worker group
in Cribl Stream using the Control Plane SDK. It shows:

1. Creates a cloud worker group with AWS provider configuration with
   24MB/s max estimated ingest rate / 9 worker processes
2. Verifies the worker group doesn't already exist
3. Scales the worker group up to 48MB/s max estimated ingest rate / 21 worker processes
4. Provisions the worker group to activate cloud resources

Check this documentation for more details about ingest rates and provisioning:
  https://docs.cribl.io/stream/cloud-workers/#create-a-cloud-worker-group

Prerequisites: Configure cloud environment variables: ORG_ID, CLIENT_ID, CLIENT_SECRET, WORKSPACE_NAME
How to get these values: https://docs.cribl.io/api/#criblcloud

Note: This example is for cloud deployments only and does not require a .env
file configuration to run.
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
    estimated_ingest_rate=2048,  # 24MB/s Max est ingest rate / 9 Worker Processes
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

    # Verify worker group doesn't already exist
    worker_group_response = cribl.groups.get(
        id=group.id,
        product="stream"
    )
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"⚠️ Worker Group already exists: {group.id}. Try different group id.")
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

    # Scale and provision the worker group
    group.estimated_ingest_rate = 4096  # 48MB/s Max est ingest rate / 21 Worker Processes
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
