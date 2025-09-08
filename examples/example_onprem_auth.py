"""
On-Premises Authentication Example

This example demonstrates how to authenticate with an on-premises Cribl instance
using username and password credentials. It shows the two-step authentication process:

1. Authenticates with username/password to obtain a bearer token
2. Creates a new SDK client using the obtained token for API calls
3. Validates the connection by checking server health status

Prerequisites: Configure the on-premises server URL, username, and password

Note: This example is for onprem deployments only and does not require a .env
file configuration to run.
"""

import asyncio
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security


ONPREM_SERVER_URL = "http://localhost:9000"
ONPREM_USERNAME = "admin"
ONPREM_PASSWORD = "admin"

BASE_URL = f"{ONPREM_SERVER_URL}/api/v1"


async def main():
    # Retrieve authentication token
    client = CriblControlPlane(server_url=BASE_URL)
    response = await client.auth.tokens.get_async(
        username=ONPREM_USERNAME,
        password=ONPREM_PASSWORD
    )
    token = response.token
    print(f"✅ Authenticated with on-premises server, token: {token}")

    # Create authenticated client
    security = Security(bearer_auth=token)
    client = CriblControlPlane(
        server_url=BASE_URL,
        security=security
    )
    print("✅ Cribl SDK client created for on-premises server")

    # Validate connection, try to list all git branches
    response = await client.versions.branches.list_async()
    branches = "\n\t".join([branch.id for branch in (response.items or [])])
    print(f"✅ Client works! Your list of branches:\n\t{branches}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        status_code = getattr(error, 'status_code', None)
        if status_code == 429:
            print("⚠️ Uh oh, you've hit the rate limit! Try again in a few seconds.")
        else:
            print(f"❌ Something went wrong: {error}")
