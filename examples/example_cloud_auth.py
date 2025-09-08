"""
Cribl.Cloud Authentication Example

This example demonstrates how to authenticate with Cribl Cloud using OAuth2
client credentials flow. It shows the authentication process:

This example demonstrates the Cribl.Cloud authentication process using OAuth2 credentials.

1. Create an SDK client with OAuth2 client credentials.
2. Automatically handle token exchange and refresh.
3. Validate the connection by checking the server health status and listing 
all git branches.
 
Prerequisites: Replace the placeholder values for ORG_ID, CLIENT_ID, 
CLIENT_SECRET, and WORKSPACE_NAME with your Organization ID, Client ID and 
Secret, and Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, 
follow the steps at https://docs.cribl.io/api/#criblcloud. Your Client ID 
and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only. It does not require 
.env file configuration.
"""

import asyncio
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security, SchemeClientOauth


# Cribl.Cloud configuration: Replace the placeholder values
ORG_ID = "your-org-id"  # Replace with your Organization ID
CLIENT_ID = "your-client-id"  # Replace with your OAuth2 Client ID
CLIENT_SECRET = "your-client-secret"  # Replace with your OAuth2 Client Secret
WORKSPACE_NAME = "main"  # Replace with your Workspace name

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"


async def main():
    # Create authenticated SDK client with OAuth2
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
    print("✅ Cribl SDK client created for Cribl.Cloud deployment")

    # Validate connection, and list all git branches
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
            print("⚠️ Uh oh, you've reached the rate limit! Try again in a few seconds.")
        else:
            print(f"❌ Something went wrong: {error}")
