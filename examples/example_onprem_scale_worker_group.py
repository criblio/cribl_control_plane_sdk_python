"""
Scale (Optimize) Worker Process settings

- Verifies that an on-prem Worker Group exists in Cribl Stream.
- Reads current system settings for the Worker Group.
- Applies optimized Worker Process settings.
- Updates system settings, commits, deploys, and restarts the Worker Group so
that Workers pick up the changes.

NOTE: This example is for on-prem deployments only.

Required to use this example:
- An Enterprise license.
- A server URL, which is used to build the base URL for the SDK calls.
- A username and password, which are used to authenticate the SDK calls.
The username and password credentials are sensitive information and should
be kept private.
- An existing Worker Group to scale.

The Cribl documentation provides more information about optimizing Worker Processes:
https://docs.cribl.io/stream/scaling/#optimize-a-distributed-deployment-or-hybrid-group
"""

# Import block
# Imports asyncio so that the file can await the on-prem token request and
# other asynchronous control plane calls (settings read/update, commit, deploy,
# restart).
#
# Imports CriblControlPlane as the API client from the cribl_control_plane
# SDK package.
#
# Imports Security (Bearer token wrapper after username/password login),
# ProductsCore for product identifiers, WorkersTypeSystemSettingsConf for
# Worker Process tuning fields, and other API payloads from the
# cribl_control_plane.models subpackage.
import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    Security,
    WorkersTypeSystemSettingsConf,
)

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and other blocks. 
# Replace the placeholder values before executing this file.
ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
WORKER_GROUP_ID = "your-worker-group-id"

# URL block
# Builds the base URL and Worker Group-specific URL to use for the API requests
# that this file makes using the ONPREM_SERVER_URL and WORKER_GROUP_ID provided
# in the user-supplied parameters block. The Worker Group URL is used for
# system settings and commit calls.
base_url = f"{ONPREM_SERVER_URL}/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Workflow block
# The async function that contains the full automation and runs when you
# execute this file. Authenticates using your username and password, verifies
# the Worker Group, reads and updates system settings for Worker Processes,
# commits and deploys the configuration, then restarts the Worker Group.
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

    # Verify Worker Group block
    # Fetches the Worker Group using WORKER_GROUP_ID from the user-supplied
    # parameters block and exits if it does not exist so that scaling does 
    # not run against a missing Worker Group.
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if not worker_group_response.items or len(worker_group_response.items) == 0:
        print(f"⚠️ Worker Group not found: {WORKER_GROUP_ID}. Please create it first.")
        return
    print(f"✅ Found Worker Group: {WORKER_GROUP_ID}")

    # Get system settings block
    # Loads the current Cribl system settings for the Worker Group using
    # group_url from the URL block. Raises an exception if no settings row is
    # returned. Prints the current Worker Process count, memory, and minimum
    # settings for visibility before changes.
    current_settings = cribl.system.settings.cribl.list(server_url=group_url)
    current_conf = current_settings.items[0] if current_settings.items else None

    if not current_conf:
        raise Exception("Failed to retrieve current system settings")

    print(f"📊 Current Worker Process settings:")
    print(f"   Worker Process count: {current_conf.workers.count}")
    print(f"   Memory: {current_conf.workers.memory} MB")
    print(f"   Minimum Worker Processes: {current_conf.workers.minimum}")

    # Optimize Worker Process settings block
    # Builds WorkersTypeSystemSettingsConf for an example host: 
    # Process count = -3 (six physical cores hyperthreaded for 12 vCPUs; 
    # reserves 2 cores for system/API overhead plus 1 for the load 
    # balancer process)
    # Memory: 2048 MB (default; 2 GB per Worker Process)
    # Minimum: 2 (spawn at least two Worker Processes)
    workers_config = WorkersTypeSystemSettingsConf(
        count=-3,  # Negative number specifies the number of CPU cores to reserve for system/API overhead
        memory=2048,  # Amount of heap memory available to each Worker Process, in MB
        minimum=2,  # Minimum number of Worker Processes to spawn
    )

    # Update system settings block
    # Copies the current system configuration and replaces the workers
    # section with workers_config from the optimize Worker Process settings
    # block, then persists the merged configuration with system.settings.cribl.update
    # using group_url from the URL block.
    updated_conf = current_conf.model_copy(update={"workers": workers_config})
    cribl.system.settings.cribl.update(
        **updated_conf.model_dump(exclude_none=False),
        server_url=group_url,
    )
    print(f"\n✅ Worker Process settings optimized:")
    print(f"   Worker Process count: {workers_config.count}")
    print(f"   Memory: {workers_config.memory} MB per Worker Process")
    print(f"   Minimum Worker Processes: {workers_config.minimum}")

    # Commit block
    # Records a new version of the Worker Group configuration, marks that
    # version as effective, and captures the commit ID to use in the Deploy
    # block. Raises an exception if the API returns no commit. Otherwise, prints
    # a confirmation message.
    commit_response = cribl.versions.commits.create(
        message="Optimize Worker Process settings",
        effective=True,
        files=["."],
        server_url=group_url,
    )
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")

    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the Worker Group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from the
    # Commit block) to the Cribl Stream Worker Group so that Workers load and run
    # that version, then prints a confirmation message.
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version,
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

    # Restart Worker Group block
    # Triggers a restart for the Worker Group using group_url from the URL block
    # so that Workers reload with the deployed system settings.
    print(f"\n🔄 Restarting Worker Group to apply changes...")
    cribl.system.settings.restart(server_url=group_url)
    print(f"✅ Worker Group restarted successfully")


# Script entry block
# Starts the async function main() with the standard library helper
# asyncio.run and prints an error message if the run fails. Runs only when you
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
