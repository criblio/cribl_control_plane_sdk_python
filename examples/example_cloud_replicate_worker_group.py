"""
Replicate a Worker Group

- Verifies that a source Worker Group exists in Cribl Stream.
- Creates a replica Worker Group cloned from the source with the 
same configuration.
- Commits and deploys the replica Worker Group configuration to make it active.

NOTE: This example is for Cribl.Cloud deployments only.

Required to use this example:
- A Cribl.Cloud Enterprise account.
- A Cribl.Cloud Organization ID and Workspace name, which are used to build the
base URL for the SDK calls.
- The Client ID and Secret for a Cribl.Cloud API Credential, which are used to
authenticate the SDK calls. To get the Client ID and Secret, follow
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. The Client ID
and Secret are sensitive information and should be kept private.
- An existing Worker Group to replicate.
"""

# Import block
# Imports asyncio so that the file can run an asynchronous control plane
# sequence for authentication, replicating a Worker Group, and committing and
# deploying the replica configuration.
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
    CloudProvider,
    ConfigGroupCloud,
    EstimatedIngestRateOptionsConfigGroup,
    ProductsCore,
    SchemeClientOauth,
    Security,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and Replicate Worker
# Group block. Replace the placeholder values before executing this file.
ORG_ID = "your-org-id"  # Replace with the Organization ID
WORKSPACE_NAME = "your-workspace-name"  # Replace with the Workspace name
SOURCE_WORKER_GROUP_ID = "my-worker-group"  # Replace with the ID of the Worker Group to clone
REPLICA_WORKER_GROUP_ID = "my-replica-worker-group"  # Replace with the ID for the new replica Worker Group

CLIENT_ID = "your-client-id"  # Replace with the Client ID for the API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the Client Secret for the API Credential

# URL block
# Builds the base URL and replica Worker Group-specific URL to use for the API
# requests that this file makes using the ORG_ID, WORKSPACE_NAME, and
# REPLICA_WORKER_GROUP_ID from the user-supplied parameters block.
base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"
group_url = f"{base_url}/m/{REPLICA_WORKER_GROUP_ID}"

# Estimated ingest rate block
# Sets the maximum estimated ingest throughput tier for the replica Worker Group
# using EstimatedIngestRateOptionsConfigGroup. RATE24_MB_PER_SEC is the 24 MB/s
# tier, equivalent to 24 MB/s maximum estimated ingest rate with 9 Worker
# Processes. This value is passed as estimated_ingest_rate to groups.create in
# the Replicate Worker Group block.
ESTIMATED_INGEST_RATE = EstimatedIngestRateOptionsConfigGroup.RATE24_MB_PER_SEC

# Workflow block
# The async function that contains the full automation and runs when you
# execute this file. Authenticates using your Cribl.Cloud API Credentials,
# verifies the source Worker Group, creates the replica, and commits and deploys
# the replica configuration.
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

    # Verify source Worker Group block
    # Fetches the source Worker Group using SOURCE_WORKER_GROUP_ID from the
    # user-supplied parameters block. Exits with a message if the group does not
    # exist so replication does not run without a valid clone source.
    source_group_response = cribl.groups.get(
        id=SOURCE_WORKER_GROUP_ID, product=ProductsCore.STREAM
    )
    if not source_group_response.items or len(source_group_response.items) == 0:
        print(f"❌ Source Worker Group not found: {SOURCE_WORKER_GROUP_ID}. Create the source Worker Group first.")
        return

    # Replicate Worker Group block
    # Checks for a Worker Group with REPLICA_WORKER_GROUP_ID from the user-supplied
    # parameters block and exits if it already exists. Otherwise, creates the
    # replica using groups.create with source_group_id set to the source Worker
    # Group ID, cloud settings, and ESTIMATED_INGEST_RATE from the Estimated
    # ingest rate block, then prints a confirmation message.
    replica_group_response = cribl.groups.get(
        id=REPLICA_WORKER_GROUP_ID, product=ProductsCore.STREAM
    )
    if replica_group_response.items and len(replica_group_response.items) > 0:
        print(f"❌ Replica Worker Group already exists: {REPLICA_WORKER_GROUP_ID}. Try a different Worker Group ID.")
        return

    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=REPLICA_WORKER_GROUP_ID,
        name="my-replica-worker-group",
        description=f"Worker Group cloned from {SOURCE_WORKER_GROUP_ID} with identical configuration",
        cloud=ConfigGroupCloud(provider=CloudProvider.AWS, region="us-east-1"),
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        on_prem=False,
        estimated_ingest_rate=ESTIMATED_INGEST_RATE,
        source_group_id=SOURCE_WORKER_GROUP_ID,
    )
    print(f"✅ Worker Group replicated: {REPLICA_WORKER_GROUP_ID} (cloned from {SOURCE_WORKER_GROUP_ID})")

    # Commit block
    # Records a new version of the replica Worker Group configuration, marks that
    # version as effective, and captures the commit ID to use in the Deploy
    # block. Raises an exception if the API returns no commit. Otherwise, prints
    # a confirmation message. Uses group_url from the URL block.
    commit_response = cribl.versions.commits.create(
        message="Commit for replicate Worker Group example",
        effective=True,
        files=["."],
        server_url=group_url,
    )

    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")

    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {REPLICA_WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from the
    # Commit block) to the Cribl Stream replica Worker Group so that Workers load
    # and run that version, then prints a confirmation message.
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=REPLICA_WORKER_GROUP_ID,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {REPLICA_WORKER_GROUP_ID}")


# Script entry block
# Starts the async function main() with the standard library helper
# asyncio.run and prints an error message if the run fails. Runs only when you
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
