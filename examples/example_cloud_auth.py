"""
Cloud Authentication Example

This example demonstrates how to authenticate with Cribl Cloud using OAuth2
client credentials flow. It shows the authentication process:

1. Creates an SDK client with OAuth2 client credentials configuration
2. Automatically handles token exchange and refresh
3. Validates the connection by checking server health status

Prerequisites: Configure cloud environment variables: ORG_ID, CLIENT_ID, CLIENT_SECRET, WORKSPACE_NAME, CRIBL_DOMAIN
How to get these values: https://docs.cribl.io/api/#criblcloud

Note: This example is for cloud deployments only and does not require a .env
file configuration to run.
"""

import asyncio
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security, SchemeClientOauth


# Cloud configuration - UPDATE THESE VALUES
ORG_ID = "your-org-id"  # Replace with your organization ID
CLIENT_ID = "your-client-id"  # Replace with your OAuth2 client ID
CLIENT_SECRET = "your-client-secret"  # Replace with your OAuth2 client secret
WORKSPACE_NAME = "main"  # Replace with your workspace name

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"


async def main():
    # Create authenticated client with OAuth2
    client_oauth = SchemeClientOauth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_url="https://login.cribl.cloud/oauth/token",
        audience="https://api.cribl.cloud"
    )
    
    security = Security(client_oauth=client_oauth)
    client = CriblControlPlane(
        server_url=base_url,
        security=security
    )
    print("✅ Cribl SDK client created for cloud deployment")

    # Validate connection, try to list all git branches
    response = await client.versions.branches.list_async()
    branches = "\n\t".join([branch.id for branch in (response.items or [])])
    print(f"✅ Client works! Your list of branches:\n\t{branches}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        status_code = getattr(error, 'status_code', None)
        if status_code == 401:
            print("⚠️ Authentication failed! Check your CLIENT_ID and CLIENT_SECRET.")
        elif status_code == 429:
            print("⚠️ Uh oh, you've hit the rate limit! Try again in a few seconds.")
        else:
            print(f"❌ Something went wrong: {error}")
