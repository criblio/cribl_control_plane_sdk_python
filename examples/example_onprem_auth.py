"""
On-Prem Authentication Example

This example demonstrates the authentication process for an on-prem Cribl
instance using username and password credentials.

1. Authenticate with your username and password to obtain a Bearer token.
2. Create an SDK client that uses the Bearer token for API calls.
3. Validate the connection by checking the server health status and listing 
all git branches.

Prerequisites: Replace the placeholder values for ONPREM_SERVER_URL 
ONPREM_USERNAME, and ONPREM_PASSWORD with your server URL and credentials. 
Your credentials are sensitive information and should be kept private. 

NOTE: This example is for on-prem deployments only. It does not require .env 
file configuration.
"""

import asyncio
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security

# On-prem configuration: Replace the placeholder values
ONPREM_SERVER_URL = "http://localhost:9000" # Replace with your server URL
ONPREM_USERNAME = "admin" # Replace with your username
ONPREM_PASSWORD = "admin" # Replace with your password

BASE_URL = f"{ONPREM_SERVER_URL}/api/v1"


async def main():
    # Retrieve Bearer token for authentication
    client = CriblControlPlane(server_url=BASE_URL)
    response = await client.auth.tokens.get_async(
        username=ONPREM_USERNAME,
        password=ONPREM_PASSWORD
    )
    token = response.result.token
    print(f"✅ Authenticated with on-prem server, token: {token}")

    # Create authenticated SDK client
    security = Security(bearer_auth=token)
    client = CriblControlPlane(
        server_url=BASE_URL,
        security=security
    )
    print("✅ Cribl SDK client created for on-prem server")

    # Validate connection and list all git branches
    response = await client.versions.branches.list_async()
    branches = "\n\t".join([branch.id for branch in (response.items or [])])
    print(f"✅ Client works! Your list of branches:\n\t{branches}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        HTTP_STATUS = getattr(error, 'status_code', None)
        if HTTP_STATUS == 429:
            print("⚠️ Uh oh, you've reached the rate limit! Try again in a few seconds.")
        else:
            print(f"❌ Something went wrong: {error}")
