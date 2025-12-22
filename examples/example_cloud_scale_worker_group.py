"""
Replace the placeholder values for ORG_ID, CLIENT_ID, CLIENT_SECRET,
and WORKSPACE_NAME with your Organization ID, Client ID and Secret, and
Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, follow the steps
at https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.

Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only.
"""

import asyncio

from typing import Optional

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ConfigGroup,
    ProductsCore,
    SchemeClientOauth,
    Security,
    ConfigGroupEstimatedIngestRate,
)

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"
WORKER_GROUP_ID = "your-cloud-worker-group-id"  # Use the same Worker Group ID as in the previous example

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"

def resolve_group(cribl, group_id: str, product: ProductsCore) -> Optional[ConfigGroup]:
    resp = cribl.groups.get(id=group_id, product=product)

    # Case 1: List-style wrapper with items
    items = getattr(resp, "items", None)
    if items:
        return items[0]

    # Case 2: Direct ConfigGroup object
    if isinstance(resp, ConfigGroup):
        return resp

    # Nothing found or unexpected shape
    return None

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

    # Verify that Worker Group already exists
    group = resolve_group(cribl, WORKER_GROUP_ID, ProductsCore.STREAM)
    if group is None:
        print(f"Worker Group {WORKER_GROUP_ID} not found.")
    else:
        # Scale and provision the Worker Group
        # Equivalent to 48 MB/s maximum estimated ingest rate with 21 Worker Processes
        group.estimated_ingest_rate = ConfigGroupEstimatedIngestRate.RATE48_MB_PER_SEC
        group.provisioned = True

        cribl.groups.update(
            product=ProductsCore.STREAM,
            id=group.id,
            id_param=group.id,
            name=group.name,
            description=group.description,
            cloud=group.cloud,
            worker_remote_access=group.worker_remote_access,
            is_fleet=group.is_fleet,
            is_search=group.is_search,
            on_prem=group.on_prem,
            estimated_ingest_rate=group.estimated_ingest_rate,
            provisioned=group.provisioned,
        )
        print(f"✅ Worker Group scaled and provisioned: {group.id}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

