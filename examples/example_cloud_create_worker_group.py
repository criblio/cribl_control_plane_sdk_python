"""
Create a Worker Group

- Creates a new Worker Group in Cribl Stream.
- Commits and deploys the Worker Group configuration to make it active.

NOTE: This example is for Cribl.Cloud deployments only.

Required to use this example:
- A Cribl.Cloud Enterprise account.
- A Cribl.Cloud Organization ID and Workspace name, which are used to build the 
base URL for the SDK calls.
- The Client ID and Secret for a Cribl.Cloud API Credential, which are used to 
authenticate the SDK calls. To get the Client ID and Secret, follow 
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. The Client ID 
and Secret are sensitive information and should be kept private.
"""

# Import block
# Imports asyncio so that the file can run an asynchronous control plane 
# sequence for authentication and creating and deploying a Worker Group.
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
    ConfigGroup,
    ConfigGroupCloud,
    CloudProvider,
    Security,
    SchemeClientOauth,
    ProductsCore,
    EstimatedIngestRateOptionsConfigGroup,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and Worker Group 
# definition block. Replace the placeholder values before executing 
# this file.
ORG_ID = "your-org-id"  # Replace with the Organization ID
WORKSPACE_NAME = "your-workspace-name"  # Replace with the Workspace name
WORKER_GROUP_ID = "your-group"  # Replace with the ID to use for the new Worker Group

CLIENT_ID = "your-client-id"  # Replace with the Client ID for the API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the Client Secret for the API Credential

# URL block
# Builds the base URL and Worker Group-specific URL to use for the 
# API requests that this file makes using the ORG_ID, WORKSPACE_NAME, 
# and WORKER_GROUP_ID provided in the user-supplied parameters block.
base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Estimated ingest rate block
# Sets the maximum estimated ingest throughput tier for the new Worker Group
# using EstimatedIngestRateOptionsConfigGroup. RATE24_MB_PER_SEC is the 24 MB/s
# tier, equivalent to 24 MB/s maximum estimated ingest rate with 9 Worker 
# Processes. This value is passed as estimated_ingest_rate to groups.create in
# the Create Worker Group block.
ESTIMATED_INGEST_RATE = EstimatedIngestRateOptionsConfigGroup.RATE24_MB_PER_SEC

# Worker Group definition block
# The configuration for a new Worker Group that uses the WORKER_GROUP_ID 
# provided in the user-supplied parameters block. The settings in this
# configuration are passed to groups.create in the Create Worker Group block, 
# with ESTIMATED_INGEST_RATE from the estimated ingest rate block.
group = ConfigGroup(
    id=WORKER_GROUP_ID,
    name="my-worker-group",
    description="Cribl.Cloud Worker Group",
    cloud=ConfigGroupCloud(provider=CloudProvider.AWS, region="us-west-2"),
    worker_remote_access=True,
    is_fleet=False,
    is_search=False,
    on_prem=False,
    provisioned=False,
)

# Workflow block
# The async function that contains the full automation and runs when you 
# execute this file. Authenticates using your Cribl.Cloud API Credentials, 
# creates the Worker Group, and commits and deploys the configuration.
async def main():
    # Authentication block
    # Creates an OAuth client (SchemeClientOauth) that exchanges CLIENT_ID and 
    # CLIENT_SECRET from the user-supplied parameters block for a Bearer 
    # token and wraps the client in Security.
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

    # Create Worker Group block
    # Checks for a Worker Group with the WORKER_GROUP_ID provided in the 
    # user-supplied parameters block and exits if it already exists. 
    # Otherwise, creates the Worker Group using settings from the Worker Group 
    # definition block and ESTIMATED_INGEST_RATE from the Estimated ingest 
    # rate block and prints a confirmation message.
    worker_group_response = cribl.groups.get(id=group.id, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(f"❌ Worker Group already exists: {group.id}. Try a different group ID.")
        return

    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=group.id,
        name=group.name,
        description=group.description,
        cloud=group.cloud,
        worker_remote_access=group.worker_remote_access,
        is_fleet=group.is_fleet,
        is_search=group.is_search,
        on_prem=group.on_prem,
        estimated_ingest_rate=ESTIMATED_INGEST_RATE,
        provisioned=group.provisioned,
    )
    print(f"✅ Worker Group created: {group.id}")

    # Commit block
    # Records a new version of the Worker Group configuration, marks that 
    # version as effective, and captures the commit ID to use in the 
    # Deploy block. Raises an exception if the API returns no commit. 
    # Otherwise, prints a confirmation message.
    commit_response = cribl.versions.commits.create(
        message="Commit for create Worker Group example",
        effective=True,
        files=["."],
        server_url=group_url,
    )

    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")

    version = commit_response.items[0].commit
    print(
        f"✅ Committed configuration changes to the group: {group.id}, "
        f"commit ID: {version}"
    )

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from 
    # the Commit block) to the Cribl Stream Worker Group so that Workers load 
    # and run that version, then prints a confirmation message.
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=group.id,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {group.id}")

# Script entry block
# Starts the async function main() with the standard library helper 
# asyncio.run and prints an error message if the run fails. Runs only when you 
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

