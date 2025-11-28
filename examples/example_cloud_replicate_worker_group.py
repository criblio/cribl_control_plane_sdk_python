import asyncio

from typing import Optional

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    CloudProvider,
    ConfigGroup,
    ConfigGroupCloud,
    GroupCreateRequestEstimatedIngestRate,
    ProductsCore,
    SchemeClientOauth,
    Security,
)

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"
SOURCE_WORKER_GROUP_ID = "my-worker-group" # The id of the Worker Group to clone
REPLICA_WORKER_GROUP_ID = "my-replica-worker-group" # The id to use for the replica Worker Group

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"

async def main() -> None:
    """Main function that demonstrates Worker Group replication"""
    client_oauth = SchemeClientOauth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_url="https://login.cribl.cloud/oauth/token",
        audience="https://api.cribl.cloud",
    )

    security = Security(client_oauth=client_oauth)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    try:
        # Verify that the source Worker Group exists
        source_group_response = cribl.groups.get(id=SOURCE_WORKER_GROUP_ID, product=ProductsCore.STREAM)
        if not source_group_response.items or len(source_group_response.items) == 0:
            print(f"❌ Source Worker Group not found: {SOURCE_WORKER_GROUP_ID}. Create the source Worker Group first.")
            exit(1)

        # Replicate the Worker Group
        replicate_worker_group(cribl, SOURCE_WORKER_GROUP_ID)

    except Exception as error:
        message = str(error)
        print(f"Error: {message}")
        exit(1)

def replicate_worker_group(
    cribl: CriblControlPlane, source_id: str
) -> Optional[ConfigGroup]:
    """
    Replicates a Worker Group with a unique ID
    """
    # Verify that the replica Worker Group does not exist
    replica_group_response = cribl.groups.get(id=REPLICA_WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if replica_group_response.items and len(replica_group_response.items) > 0:
        print(f"❌ Replica Worker Group already exists: {REPLICA_WORKER_GROUP_ID}. Try a different group ID.")
        return
    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=REPLICA_WORKER_GROUP_ID,
        name="my-replica-worker-group",
        description=f"Worker Group cloned from {source_id} with identical configuration",
        cloud=ConfigGroupCloud(provider=CloudProvider.AWS, region="us-east-1"),
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        on_prem=False,
        estimated_ingest_rate=GroupCreateRequestEstimatedIngestRate.RATE24_MB_PER_SEC,  # Equivalent to 24 MB/s maximum estimated ingest rate with 9 Worker Processes
        source_group_id=source_id,
    )
    print(f"✅ Worker Group replicated: {REPLICA_WORKER_GROUP_ID} (cloned from {source_id})")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        message = str(error)
        print(f"❌ Something went wrong: {message}")

