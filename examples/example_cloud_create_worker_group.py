"""
Replace the placeholder values for ORG_ID, CLIENT_ID, CLIENT_SECRET,
and WORKSPACE_NAME with your Organization ID, Client ID and Secret, and
Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, follow the steps
at https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.

Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ConfigGroup,
    ConfigGroupCloud,
    CloudProvider,
    Security,
    SchemeClientOauth,
    ProductsCore,
    EstimatedIngestRateOptionsConfigGroup,
)

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"
WORKER_GROUP_ID = "your-cloud-worker-group-id"

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"

# Equivalent to 24 MB/s maximum estimated ingest rate with 9 Worker Processes
ESTIMATED_INGEST_RATE = EstimatedIngestRateOptionsConfigGroup.RATE24_MB_PER_SEC

group = ConfigGroup(
    id=WORKER_GROUP_ID,
    name="my-worker-group",
    description="Cribl.Cloud Worker Group",
    cloud=ConfigGroupCloud(provider=CloudProvider.AWS, region="us-west-2"),
    worker_remote_access=True,
    is_fleet=False,
    is_search=False,
    on_prem=False,
    provisioned=False,
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
    worker_group_response = cribl.groups.get(id=group.id, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"❌ Worker Group already exists: {group.id}. Try a different group ID.")
        return

    # Create the worker group
    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=group.id,
        name=group.name,
        description=group.description,
        cloud=group.cloud,
        worker_remote_access=group.worker_remote_access,
        is_fleet=group.is_fleet,
        is_search=group.is_search,
        on_prem=group.on_prem,
        estimated_ingest_rate=ESTIMATED_INGEST_RATE,
        provisioned=group.provisioned,
    )
    print(f"✅ Worker Group created: {group.id}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
