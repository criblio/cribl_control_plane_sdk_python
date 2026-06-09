"""
List Worker Groups

- Lists all Worker Group configurations for Cribl Stream in a Workspace.

NOTE: This example is for Cribl.Cloud deployments only.

Required to use this example:
- A Cribl.Cloud Organization ID and Workspace name, which are used to build the
base URL for the SDK calls.
- The Client ID and Secret for a Cribl.Cloud API Credential, which are used to
authenticate the SDK calls. To get the Client ID and Secret, follow
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. The Client ID
and Secret are sensitive information and should be kept private.
"""

# Import block
# Imports asyncio so that the file can run an asynchronous control plane
# sequence for authentication and listing Worker Groups.
#
# Imports CriblControlPlane as the API client from the cribl_control_plane
# SDK package.
#
# Imports model classes that provide the Python types used for Cribl Stream
# resource configurations and API payloads in this file from the
# cribl_control_plane.models subpackage.
import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    SchemeClientOauth,
    Security,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and List Worker Groups
# block. Replace the placeholder values before executing this file.
ORG_ID = "your-org-id"  # Replace with the Organization ID
WORKSPACE_NAME = "your-workspace-name"  # Replace with the Workspace name

CLIENT_ID = "your-client-id"  # Replace with the Client ID for the API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the Client Secret for the API Credential

# URL block
# Builds the base URL to use for the API requests that this file makes using the
# ORG_ID and WORKSPACE_NAME provided in the user-supplied parameters block.
base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"

# Workflow block
# The async function that contains the full automation and runs when you
# execute this file. Authenticates using your Cribl.Cloud API Credentials and
# lists Worker Groups for Cribl Stream.
async def main():
    # Authentication block
    # Creates an OAuth client (SchemeClientOauth) that exchanges CLIENT_ID and
    # CLIENT_SECRET from the user-supplied parameters block for a Bearer token
    # and wraps the client in Security.
    # Constructs the SDK client CriblControlPlane to make authenticated API
    # requests using the base_url from the URL block and Security, which holds
    # the Bearer token.
    client_oauth = SchemeClientOauth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_url="https://login.cribl.cloud/oauth/token",
        audience="https://api.cribl.cloud",
    )

    security = Security(client_oauth=client_oauth)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # List Worker Groups block
    # Calls groups.list for Cribl Stream (ProductsCore.STREAM). If the response
    # includes items, prints each Worker Group configuration; otherwise prints
    # that no Worker Groups were found.
    worker_groups_response = cribl.groups.list(product=ProductsCore.STREAM)

    if worker_groups_response.items:
        print(f"✅ List of Worker Group Configurations:")
        for group in worker_groups_response.items:
            print(group)  # Print the entire configuration for each Worker Group
    else:
        print(f"❌ No Worker Groups found.")

# Script entry block
# Starts the async function main() with the standard library helper
# asyncio.run and prints an error message if the run fails. Runs only when you
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
