"""
On-Prem Create Worker Group Example

This example demonstrates how to create an on-prem Worker Group in Cribl Stream.

This example performs the following operations:

1. Connects to Cribl Stream and authenticates.
2. Verifies that a Worker Group with the specified ID does not already exist.
3. Creates the Worker Group.
4. Commits the configuration changes to the Worker Group.
5. Deploys the configuration changes to the Worker Group.

Prerequisites:
- Replace the placeholder values for ONPREM_SERVER_URL, ONPREM_USERNAME, and
  ONPREM_PASSWORD with your server URL and credentials. Your credentials are
  sensitive information and should be kept private.
- Replace the WORKER_GROUP_ID placeholder value with the Worker Group ID that 
  you want to use.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import ProductsCore, Security

ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
WORKER_GROUP_ID = "your-worker-group-id"

base_url = f"{ONPREM_SERVER_URL}/api/v1"

async def main():
    # Initialize Cribl client
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Verify that Worker Group doesn't already exist
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"❌ Worker Group already exists: {WORKER_GROUP_ID}. Try a different group ID.")
        return

    # Create the Worker Group
    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        name="my-worker-group",
        description="My Worker Group description",
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        on_prem=True,
    )
    print(f"✅ Worker Group created: {WORKER_GROUP_ID}")

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        group_id=WORKER_GROUP_ID,
        message="Create Worker Group",
        effective=True,
        files=["."],
    )
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy configuration changes to the Worker Group
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
