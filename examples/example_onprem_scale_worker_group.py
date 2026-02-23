"""
On-Prem/Hybrid Worker Group Process Optimization Example

This example demonstrates how to optimize Worker Process settings for an 
existing on-prem or hybrid Worker Group in Cribl Stream using the Control Plane SDK, 
following the scaling guidelines from the Cribl documentation.

This example performs the following operations:

1. Connects to an existing on-prem or hybrid Worker Group.
2. Retrieves the current system settings for the Worker Group.
3. Optimizes Worker Process settings following the scaling documentation:
   - Process count: -2 (to reserve two CPU cores for system/API overhead)
   - Memory: 2048 MB (2 GB per Worker Process)
   - Minimum Worker Process count: 2 (to spawn at least two Worker Processes)
4. Updates the Worker Group's system settings with the optimized configuration.
5. Commits the configuration changes to the Worker Group.
6. Deploys the configuration changes to the Worker Group.
7. Restarts the Worker Group to apply the changes.

The Cribl documentation provides more information about optimizing Worker Processes:
https://docs.cribl.io/stream/scaling/#optimize-a-distributed-deployment-or-hybrid-group

Prerequisites:
- Replace the placeholder values for ONPREM_SERVER_URL, ONPREM_USERNAME, and
  ONPREM_PASSWORD with your server URL and credentials. Your credentials are
  sensitive information and should be kept private.
- Replace WORKER_GROUP_ID with your actual Worker Group ID.
"""

import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    Security,
    WorkersTypeSystemSettingsConf,
)

ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password
WORKER_GROUP_ID = "your-worker-group-id"

base_url = f"{ONPREM_SERVER_URL}/api/v1"

async def main():
    # Initialize Cribl client
    cribl = CriblControlPlane(server_url=base_url)

    response = await cribl.auth.tokens.get_async(
        username=ONPREM_USERNAME, password=ONPREM_PASSWORD
    )

    token = response.result.token
    security = Security(bearer_auth=token)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Construct the base URL for the Worker Group
    group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

    # Verify that Worker Group exists
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if not worker_group_response.items or len(worker_group_response.items) == 0:
        print(f"⚠️ Worker Group not found: {WORKER_GROUP_ID}. Please create it first.")
        return
    print(f"✅ Found Worker Group: {WORKER_GROUP_ID}")

    # Get current system settings to preserve existing configuration
    current_settings = cribl.system.settings.cribl.list(server_url=group_url)
    current_conf = current_settings.items[0] if current_settings.items else None
    
    if not current_conf:
        raise Exception("Failed to retrieve current system settings")

    print(f"📊 Current Worker Process settings:")
    print(f"   Worker Process count: {current_conf.workers.count}")
    print(f"   Memory: {current_conf.workers.memory} MB")
    print(f"   Minimum Worker Processes: {current_conf.workers.minimum}")

    # Configure Worker Process settings following scaling documentation
    # For x86 hyperthreaded CPUs: Process count = -2 (default; reserves 2 CPU cores for system/API overhead)
    # Memory: 2048 MB (default; 2 GB per Worker Process)
    # Minimum: 2 (spawn at least two Worker Processes)
    workers_config = WorkersTypeSystemSettingsConf(
        count=-2,  # Negative number specifies the number of CPU cores to reserve for system/API overhead
        memory=2048,  # Amount of heap memory available to each Worker Process, in MB
        minimum=2,  # Minimum number of Worker Processes to spawn
    )

    # Update system settings with the optimized configuration for Worker Processes
    # Preserve other settings from the current configuration
    updated_conf = current_conf.model_copy(update={"workers": workers_config})
    cribl.system.settings.cribl.update(
        **updated_conf.model_dump(exclude_none=False),
        server_url=group_url,
    )
    print(f"\n✅ Worker Process settings optimized:")
    print(f"   Worker Process count: {workers_config.count}")
    print(f"   Memory: {workers_config.memory} MB per Worker Process")
    print(f"   Minimum Worker Processes: {workers_config.minimum}")

    # Commit configuration changes
    commit_response = cribl.versions.commits.create(
        message="Optimize Worker Process settings",
        effective=True,
        files=["."],
        server_url=group_url
    )
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the Worker Group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy configuration changes to the Worker Group
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

    # Restart the Worker Group to apply the changes
    print(f"\n🔄 Restarting Worker Group to apply changes...")
    cribl.system.settings.restart(server_url=group_url)
    print(f"✅ Worker Group restarted successfully")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
