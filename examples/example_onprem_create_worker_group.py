"""
Create a Worker Group

- Creates a new Worker Group in Cribl Stream.

NOTE: This example is for on-prem deployments only.

Required to use this example:
- An Enterprise license.
- A server URL, which is used to build the base URL for the SDK calls.
- A username and password, which are used to authenticate the SDK calls. 
The username and password credentials are sensitive information and should 
be kept private.
"""

# Import block
# Imports asyncio so that the file can await the on-prem token request and 
# other asynchronous control plane calls (Worker Group create, commit, deploy).
#
# Imports CriblControlPlane as the API client from the cribl_control_plane 
# SDK package.
#
# Imports Security (Bearer token wrapper after username/password login), 
# generated model types for Cribl Stream resources, ProductsCore for 
# product identifiers, and other API payloads from the 
# cribl_control_plane.models subpackage.
import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import ProductsCore, Security

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and Worker Group 
# configuration block. Replace the placeholder values before executing 
# this file.
ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
WORKER_GROUP_ID = "your-worker-group-id"

# URL block
# Builds the base URL and Worker Group-specific URL to use for the 
# API requests that this file makes using the ONPREM_SERVER_URL and 
# WORKER_GROUP_ID provided in the user-supplied parameters block.
base_url = f"{ONPREM_SERVER_URL}/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Workflow block
# The async function that contains the full automation and runs when you 
# execute this file. Authenticates using your username and password, 
# creates the Worker Group, and commits and deploys the configuration.
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

    # Create Worker Group block
    # Checks for a Worker Group with the WORKER_GROUP_ID provided in the 
    # user-supplied parameters block and exits if it already exists. 
    # Otherwise, creates the Worker Group and prints a confirmation message.
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"❌ Worker Group already exists: {WORKER_GROUP_ID}. Try a different group ID.")
        return

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

    # Commit block
    # Records a new version of the Worker Group configuration, marks that 
    # version as effective, and captures the commit ID to use in the 
    # Deploy block. Raises an exception if the API returns no commit. 
    # Otherwise, prints a confirmation message.
    commit_response = cribl.versions.commits.create(
        message="Commit for Cribl Stream example for creating a Worker Group",
        server_url=group_url,
        effective=True,
        files=["."],
    )
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from 
    # the Commit block) to the Cribl Stream Worker Group so that Workers load 
    # and run that version, then prints a confirmation message.
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

# Script entry block
# Starts the async function main() with the standard library helper 
# asyncio.run and prints an error message if the run fails. Runs only when you 
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
