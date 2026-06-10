"""
Scale (Provision) a Worker Group

- Verifies that a Worker Group exists in Cribl Stream.
- Updates estimated ingest rate and provisioning for the Worker Group.
- Commits and deploys the Worker Group configuration to make it active.

NOTE: This example is for Cribl.Cloud deployments only.

Required to use this example:
- A Cribl.Cloud Enterprise account (if you are scaling a non-default Worker Group).
- A Cribl.Cloud Organization ID and Workspace name, which are used to build the
base URL for the SDK calls.
- The Client ID and Secret for a Cribl.Cloud API Credential, which are used to
authenticate the SDK calls. To get the Client ID and Secret, follow
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. The Client ID
and Secret are sensitive information and should be kept private.
- An existing Worker Group ID (WORKER_GROUP_ID) to scale.
"""

# Import block
# Imports asyncio so that the file can run an asynchronous control plane
# sequence for authentication, scaling a Worker Group, and committing and
# deploying the configuration.
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
    EstimatedIngestRateOptionsConfigGroup,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and Scale Worker Group
# block. Replace the placeholder values before executing this file.
ORG_ID = "your-org-id"  # Replace with the Organization ID
WORKSPACE_NAME = "your-workspace-name"  # Replace with the Workspace name
WORKER_GROUP_ID = "your-cloud-worker-group-id"  # Replace with the Worker Group ID to scale

CLIENT_ID = "your-client-id"  # Replace with the Client ID for the API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the Client Secret for the API Credential

# URL block
# Builds the base URL and Worker Group-specific URL to use for the API requests
# that this file makes using the ORG_ID, WORKSPACE_NAME, and WORKER_GROUP_ID
# from the user-supplied parameters block. The Worker Group URL is used for the
# Commit block.
base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Estimated ingest rate block
# Target tier after scaling, using EstimatedIngestRateOptionsConfigGroup.
# RATE48_MB_PER_SEC is the 48 MB/s tier, equivalent to 48 MB/s maximum estimated
# ingest rate with 21 Worker Processes. This value is written to
# estimated_ingest_rate in the Scale Worker Group block.
SCALED_ESTIMATED_INGEST_RATE = EstimatedIngestRateOptionsConfigGroup.RATE48_MB_PER_SEC

# Workflow block
# The async function that contains the full automation and runs when you
# execute this file. Authenticates using your Cribl.Cloud API Credentials,
# verifies the Worker Group, updates scaling fields, and commits and deploys the
# configuration.
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

    # Verify Worker Group block
    # Fetches the Worker Group using WORKER_GROUP_ID from the user-supplied
    # parameters block and exits if it does not exist so that scaling does 
    # not run against a missing Worker Group.
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if not worker_group_response.items or len(worker_group_response.items) == 0:
        print(f"❌ Worker Group not found: {WORKER_GROUP_ID}. Create the Worker Group first.")
        return

    group = worker_group_response.items[0]
    if not group or not group.id:
        print(f"❌ Worker Group not found: {WORKER_GROUP_ID}. Create the Worker Group first.")
        return

    # Scale Worker Group block
    # Sets estimated_ingest_rate to SCALED_ESTIMATED_INGEST_RATE from the Estimated
    # ingest rate block and provisioned to True, then persists the Worker Group with
    # groups.update and prints a confirmation message.
    group.estimated_ingest_rate = SCALED_ESTIMATED_INGEST_RATE
    group.provisioned = True

    cribl.groups.update(
        product=ProductsCore.STREAM,
        id=group.id,
        id_param=group.id,
        name=group.name,
        description=group.description,
        cloud=group.cloud,
        worker_remote_access=group.worker_remote_access,
        is_fleet=group.is_fleet,
        is_search=group.is_search,
        on_prem=group.on_prem,
        estimated_ingest_rate=group.estimated_ingest_rate,
        provisioned=group.provisioned,
    )
    print(f"✅ Worker Group scaled and provisioned: {group.id}")

    # Commit block
    # Records a new version of the Worker Group configuration, marks that
    # version as effective, and captures the commit ID to use in the Deploy
    # block. Raises an exception if the API returns no commit. Otherwise, prints
    # a confirmation message.
    commit_response = cribl.versions.commits.create(
        message="Commit for scale Worker Group example",
        effective=True,
        files=["."],
        server_url=group_url,
    )

    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")

    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {group.id}, commit ID: {version}")

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from the
    # Commit block) to the Cribl Stream Worker Group so that Workers load and run
    # that version, then prints a confirmation message.
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
