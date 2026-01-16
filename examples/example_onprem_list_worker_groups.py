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

base_url = f"{ONPREM_SERVER_URL}/api/v1"

async def main():
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Retrieve and list all Worker Groups
    worker_groups_response = cribl.groups.list(product=ProductsCore.STREAM)

    if worker_groups_response.items:
        print(f"✅ List of Worker Group Configurations:")
        for group in worker_groups_response.items:
            print(group)  # Print the entire configuration for each Worker Group
    else:
        print(f"❌ No Worker Groups found.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

