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

from cribl_control_plane.models import ProductsCore, Security, SchemeClientOauth

ORG_ID = "your-org-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_NAME = "your-workspace-name"
WORKER_GROUP_ID = "your-cloud-worker-group-id"  # Use the same Worker Group ID as in previous examples

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

    # Construct the worker group URL
    group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        message="Commit for Cribl Stream example",
        effective=True,
        files=["."],
        server_url=group_url
    )
    
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy configuration changes
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

