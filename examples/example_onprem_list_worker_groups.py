"""
List Worker Groups

- Lists all Worker Group configurations for Cribl Stream.

NOTE: This example is for on-prem deployments only.

Required to use this example:
- A server URL, which is used to build the base URL for the SDK calls.
- A username and password, which are used to authenticate the SDK calls.
The username and password credentials are sensitive information and should
be kept private.
"""

# Import block
# Imports asyncio so that the file can await the on-prem token request and
# other asynchronous control plane calls (listing Worker Groups).
#
# Imports CriblControlPlane as the API client from the cribl_control_plane
# SDK package.
#
# Imports Security (Bearer token wrapper after username/password login),
# ProductsCore for product identifiers, and other API payloads from the
# cribl_control_plane.models subpackage.
import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    Security,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and List Worker Groups
# block. Replace the placeholder values before executing this file.
ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password

# URL block
# Builds the base URL to use for the API requests that this file makes using the
# ONPREM_SERVER_URL provided in the user-supplied parameters block.
base_url = f"{ONPREM_SERVER_URL}/api/v1"

# Workflow block
# The async function that contains the full automation and runs when you
# execute this file. Authenticates using your username and password and lists
# Worker Groups for Cribl Stream.
async def main():
    # Authentication block
    # Constructs CriblControlPlane with the base_url from the URL block and
    # calls the on-prem authentication endpoint with the username and password
    # from the user-supplied parameters block.
    # Retrieves the Bearer token from the on-prem authentication endpoint
    # response and wraps the token in Security.
    # Reconstructs CriblControlPlane as an authenticated SDK client using the
    # same base_url and Security (which holds the Bearer token).
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
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
