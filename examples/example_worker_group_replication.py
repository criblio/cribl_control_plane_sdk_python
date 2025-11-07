"""
Cribl Worker Group Replication Example

This example demonstrates how to programmatically replicate an existing 
Worker Group configuration using the Control Plane SDK.

This example performs the following operations:

1. Retrieves a list of all Worker Groups in Cribl Stream.
2. Selects the first Worker Group in the list as the source Worker Group 
to replicate.
3. Retrieves the complete configuration of the source Worker Group.
4. Creates a new Worker Group that uses the same configuration as the source 
Worker Group. The replica Worker Group has a unique ID and a name and 
description that identify it as a replica.

Data flow: Source Worker Group → Configuration Extraction → New Worker Group Creation

Prerequisites:
- An .env file configured with your authentication credentials.
- At least one existing Worker Group in Cribl Stream.
- API Bearer token with Permissions that include creating Worker Groups.
"""

import asyncio
import sys
from typing import Optional
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import (ConfigGroup, ProductsCore, GroupCreateRequestEstimatedIngestRate)
from auth import create_cribl_client


async def main() -> None:
    """Main function that demonstrates Worker Group replication"""
    try:
        # Initialize Cribl client
        cribl_client = await create_cribl_client()

        # Get the first listed Worker Group
        worker_groups = cribl_client.groups.list(product=ProductsCore.STREAM)
        
        if worker_groups.items and len(worker_groups.items) > 0:
            first_worker_group = worker_groups.items[0]
            print(f"Replicating Worker Group: {first_worker_group.id}")
            
            # Replicate the first listed Worker Group
            replicate_worker_group(cribl_client, first_worker_group.id)
        else:
            print('No Worker Group found. Create at least one Worker Group before trying again.')
            sys.exit(1)

    except Exception as error:
        error_message = str(error)
        print(f'Error: {error_message}')
        sys.exit(1)


def replicate_worker_group(client: CriblControlPlane, source_id: str) -> Optional[ConfigGroup]:
    """
    Replicates a Worker Group with a unique ID:

    - Retrieve the source Worker Group configuration
    - Generate a unique ID and name to use for the replica Worker Group
    - Filter out read-only fields from the source Worker Group configuration
    - Create the replica Worker Group with proper metadata

    Args:
        client: Cribl client instance
        source_id: ID of the Worker Group to replicate

    Returns:
        The created replica ConfigGroup or None if creation fails

    Raises:
        Exception: If the source Worker Group is not found or creation fails
    """
    try:
        # Retrieve the source Worker Group configuration
        source_response = client.groups.get(
            id=source_id,
            product=ProductsCore.STREAM
        )

        if not source_response.items or len(source_response.items) == 0:
            raise Exception(f"Worker Group '{source_id}' not found")

        source = source_response.items[0]

        # Generate a unique ID and name for the replica Worker Group
        replica_id = f"{source_id}-replica"
        replica_name = f"{source.name}-replica" if source.name else f"{source_id}-replica"

        # Create the replica Worker Group by copying the configuration of the source Worker Group
        # Filter out read-only fields like config_version, lookup_deployments, and worker_count
        result = client.groups.create(
            product=ProductsCore.STREAM,
            id=replica_id,
            name=replica_name,
            description=f"Replica of '{source_id}'",
            on_prem=source.on_prem,
            worker_remote_access=source.worker_remote_access,
            cloud=source.cloud,
            provisioned=source.provisioned,
            is_fleet=source.is_fleet,
            is_search=source.is_search,
            estimated_ingest_rate=GroupCreateRequestEstimatedIngestRate(source.estimated_ingest_rate.value) if source.estimated_ingest_rate else None,
            inherits=source.inherits,
            max_worker_age=source.max_worker_age,
            streamtags=source.streamtags,
            tags=source.tags,
            upgrade_version=source.upgrade_version
        )
        
        if result.items and len(result.items) > 0:
            created = result.items[0]
            print(f"✅ Worker Group replicated: {created.id}")
            return created
        raise Exception('Failed to create replica Worker Group')

    except Exception as error:
        error_msg = str(error)
        print(f"Failed to replicate Worker Group: {error_msg}")
        raise error


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f'Something went wrong: {error}')
