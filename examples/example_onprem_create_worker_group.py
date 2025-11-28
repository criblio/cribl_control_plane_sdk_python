"""
Replace the placeholder values for ONPREM_SERVER_URL, ONPREM_USERNAME, and
ONPREM_PASSWORD with your server URL and credentials. Your credentials are
sensitive information and should be kept private.

NOTE: This example is for on-prem deployments only.
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

    token = response.token
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

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

