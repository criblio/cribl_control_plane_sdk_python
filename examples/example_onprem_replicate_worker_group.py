"""
On-Prem Replicate Worker Group Example

This example demonstrates how to replicate an on-prem Worker Group in 
Cribl Stream.

This example performs the following operations:

1. Connects to Cribl Stream and authenticates.
2. Verifies that the source Worker Group (SOURCE_WORKER_GROUP_ID) exists.
3. Verifies that a Worker Group with the specified REPLICA_WORKER_GROUP_ID does
   not already exist.
4. Creates a new Worker Group that replicates the specified source Worker Group.
5. Commits the configuration changes to the new Worker Group.
6. Deploys the configuration changes to the new Worker Group.

Prerequisites:
- Replace the placeholder values for ONPREM_SERVER_URL, ONPREM_USERNAME, and
  ONPREM_PASSWORD with your server URL and credentials. Your credentials are
  sensitive information and should be kept private.
- Replace the WORKER_GROUP_ID and REPLICA_WORKER_GROUP_ID placeholder values 
  with the Worker Group IDs that you want to use.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import ProductsCore, Security

ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
SOURCE_WORKER_GROUP_ID = "my-worker-group" # The id of the Worker Group to clone
REPLICA_WORKER_GROUP_ID = "my-replica-worker-group" # The id to use for the replica Worker Group
base_url = f"{ONPREM_SERVER_URL}/api/v1"
replica_group_url = f"{base_url}/m/{REPLICA_WORKER_GROUP_ID}"

async def main() -> None:
    # Initialize Cribl client
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Verify that the source Worker Group exists
    source_group_response = cribl.groups.get(id=SOURCE_WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if not source_group_response.items or len(source_group_response.items) == 0:
        print(f"❌ Source Worker Group not found: {SOURCE_WORKER_GROUP_ID}. Create the source Worker Group first.")
        return
    # Verify that the replica Worker Group does not exist
    replica_group_response = cribl.groups.get(id=REPLICA_WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if replica_group_response.items and len(replica_group_response.items) > 0:
        print(f"❌ Replica Worker Group already exists: {REPLICA_WORKER_GROUP_ID}. Try a different group ID.")
        return

    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=REPLICA_WORKER_GROUP_ID,
        name="my-replica-worker-group",
        description=f"Worker Group cloned from {SOURCE_WORKER_GROUP_ID} with identical configuration",
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        on_prem=True,
        source_group_id=SOURCE_WORKER_GROUP_ID,
    )

    print(f"✅ Worker Group replicated: {REPLICA_WORKER_GROUP_ID} (cloned from {SOURCE_WORKER_GROUP_ID})")

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        message="Commit for Cribl Stream example for replicating a Worker Group",
        server_url=replica_group_url,
        effective=True,
        files=["."],
    )
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {REPLICA_WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy configuration changes to the Worker Group
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=REPLICA_WORKER_GROUP_ID,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {REPLICA_WORKER_GROUP_ID}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        message = str(error)
        print(f"❌ Something went wrong: {message}")
