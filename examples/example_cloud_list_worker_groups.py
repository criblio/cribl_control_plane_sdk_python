"""
Replace the placeholder values for ORG_ID, CLIENT_ID, CLIENT_SECRET,
and WORKSPACE_NAME with your Organization ID, Client ID and Secret, and
Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, follow the steps
at https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.

Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (ProductsCore, SchemeClientOauth,
                                        Security)

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"

base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"

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

