"""
Cribl.Cloud Lake Dataset with Search Pack Example

This example demonstrates how to install a Search Pack and create a Lake Dataset 
using the Control Plane SDK with Cribl.Cloud authentication.

The example:
1. Installs the AWS VPC Flow Logs Search Pack from Cribl Packs Dispensary
2. Creates a Lake Dataset with basic configuration

Prerequisites: Replace the placeholder values for ORG_ID, CLIENT_ID, 
CLIENT_SECRET, and WORKSPACE_NAME with your Organization ID, Client ID and 
Secret, and Workspace name. To get your CLIENT_ID and CLIENT_SECRET values, 
follow the steps at https://docs.cribl.io/api/#criblcloud. Your Client ID 
and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud deployments only. It does not require 
.env file configuration.
"""

import asyncio
from auth import AuthCloud, CloudConfiguration


# Cribl.Cloud configuration: Replace the placeholder values
ORG_ID = "your-org-id"  # Replace with your Organization ID
CLIENT_ID = "your-client-id"  # Replace with your OAuth2 Client ID
CLIENT_SECRET = "your-client-secret"  # Replace with your OAuth2 Client Secret
WORKSPACE_NAME = "your-workspace-name"  # Replace with your Workspace name

# AWS VPC Flow Logs Search Pack from Cribl Packs Dispensary
PACK_URL = "https://packs.cribl.io/dl/cribl-search-aws-vpc-flow-logs/0.1.1/cribl-search-aws-vpc-flow-logs-0.1.1.crbl"
PACK_ID = "cribl-search-aws-vpc-flow-logs"

LAKE_ID = "default"
DATASET_ID = "aws-vpc-flow-logs-dataset"


async def main():
    auth = AuthCloud(CloudConfiguration(
        org_id=ORG_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        workspace_name=WORKSPACE_NAME
    ))
    cribl = await auth.get_client()

    # Construct URLs for pack installation
    search_group_url = auth.get_search_group_url()

    # Install AWS VPC Flow Logs Search Pack
    cribl.packs.install(
        request={
            "source": PACK_URL,
            "id": PACK_ID,
        },
        server_url=search_group_url
    )
    print(f"✅ Installed Search Pack \"{PACK_ID}\" from Cribl Packs Dispensary")

    # Create lake dataset
    cribl.lake_datasets.create(
        lake_id=LAKE_ID,
        id=DATASET_ID,
        retention_period_in_days=30,
        http_da_used=False,
        storage_location_id="cribl_lake",
    )

    print(f"✅ Created Lake Dataset: {DATASET_ID}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
