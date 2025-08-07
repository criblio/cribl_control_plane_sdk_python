# cribl_control_plane_sdk_python
<!-- Start Summary [summary] -->
## Summary

Cribl API Reference: This API Reference lists available REST endpoints, along with their supported operations for accessing, creating, updating, or deleting resources. See our complementary product documentation at [docs.cribl.io](http://docs.cribl.io).
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [cribl_control_plane_sdk_python](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#criblcontrolplanesdkpython)
  * [SDK Installation](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#retries)
  * [Error Handling](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#error-handling)
  * [Custom HTTP Client](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#resource-management)
  * [Debugging](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install cribl-control-plane
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add cribl-control-plane
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from cribl-control-plane python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "cribl-control-plane",
# ]
# ///

from cribl_control_plane import CriblControlPlane

sdk = CriblControlPlane(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
        "cache_ref": "<value>",
        "created_at": 7795.06,
        "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
        "migration_query_id": "<id>",
        "retention_in_days": 1466.58,
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
        "datatypes": [
            "<value 1>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": True,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 4334.7,
                "finished_at": 6811.22,
                "latest_scanned_time": 5303.3,
                "object_count": 9489.04,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from cribl_control_plane import CriblControlPlane, models
import os

async def main():

    async with CriblControlPlane(
        server_url="https://api.example.com",
        security=models.Security(
            bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
        ),
    ) as ccp_client:

        res = await ccp_client.lake_datasets.create_async(lake_id="<id>", id="<id>", accelerated_fields=[
            "<value 1>",
            "<value 2>",
        ], bucket_name="<value>", cache_connection={
            "accelerated_fields": [
                "<value 1>",
                "<value 2>",
            ],
            "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
            "cache_ref": "<value>",
            "created_at": 7795.06,
            "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
            "migration_query_id": "<id>",
            "retention_in_days": 1466.58,
        }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
            "datatypes": [
                "<value 1>",
            ],
            "metadata": {
                "earliest": "<value>",
                "enable_acceleration": True,
                "field_list": [
                    "<value 1>",
                    "<value 2>",
                ],
                "latest_run_info": {
                    "earliest_scanned_time": 4334.7,
                    "finished_at": 6811.22,
                    "latest_scanned_time": 5303.3,
                    "object_count": 9489.04,
                },
                "scan_mode": models.ScanMode.DETAILED,
            },
        }, storage_location_id="<id>", view_name="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name           | Type   | Scheme       | Environment Variable             |
| -------------- | ------ | ------------ | -------------------------------- |
| `bearer_auth`  | http   | HTTP Bearer  | `CRIBLCONTROLPLANE_BEARER_AUTH`  |
| `client_oauth` | oauth2 | OAuth2 token | `CRIBLCONTROLPLANE_CLIENT_OAUTH` |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
        "cache_ref": "<value>",
        "created_at": 7795.06,
        "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
        "migration_query_id": "<id>",
        "retention_in_days": 1466.58,
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
        "datatypes": [
            "<value 1>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": True,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 4334.7,
                "finished_at": 6811.22,
                "latest_scanned_time": 5303.3,
                "object_count": 9489.04,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [auth](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/authsdk/README.md)

* [fetch_token](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/authsdk/README.md#fetch_token) - Log in and fetch an authentication token


### [deployments](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/deployments/README.md)

* [get_summary](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/deployments/README.md#get_summary) - Retrieve a summary of the Distributed deployment

### [destinations](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#list) - List all Destinations
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#create) - Create a Destination
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get) - Retrieve a Destination
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#update) - Update a Destination
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#delete) - Delete a Destination
* [clear_persistent_queue](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#clear_persistent_queue) - Clear the persistent queue for a Destination
* [get_persistent_queue_status](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get_persistent_queue_status) - Retrieve information about the latest job to clear the persistent queue for a Destination
* [get_sample_data](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get_sample_data) - Retrieve sample event data for a Destination
* [create_sample_data](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#create_sample_data) - Send sample event data to a Destination

### [groups](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md)

* [get_config_version](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_config_version) - Retrieve the configuration version for a Worker Group or Edge Fleet
* [create_by_product](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#create_by_product) - Create a Worker Group or Edge Fleet for the specified Cribl product
* [get_by_product](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_by_product) - List all Worker Groups or Edge Fleets for the specified Cribl product
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#delete) - Delete a Worker Group or Edge Fleet
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get) - Retrieve a Worker Group or Edge Fleet
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#update) - Update a Worker Group or Edge Fleet
* [deploy_commits](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#deploy_commits) - Deploy commits to a Worker Group or Edge Fleet
* [get_team_access_control_list_by_product](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_team_access_control_list_by_product) - Retrieve the Access Control List (ACL) for teams with permissions on a Worker Group or Edge Fleet for the specified Cribl product
* [get_access_control_list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_access_control_list) - Retrieve the Access Control List (ACL) for a Worker Group or Edge Fleet

### [health_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/healthinfo/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/healthinfo/README.md#get) - Retrieve health status of the server

### [lake_datasets](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md)

* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#create) - Create a Lake Dataset in the specified Lake
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#list) - List all Lake Datasets in the specified Lake
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#delete) - Delete a Lake Dataset in the specified Lake
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#get) - Retrieve a Lake Dataset in the specified Lake
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#update) - Update a Lake Dataset in the specified Lake

### [nodes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md)

* [get_count](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md#get_count) - Retrieve a count of Worker and Edge Nodes
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md#list) - Retrieve detailed metadata for Worker and Edge Nodes
* [restart](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md#restart) - Restart Worker and Edge Nodes

### [packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md)

* [install](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#install) - Install a Pack
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#list) - List all Packs
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#delete) - Uninstall a Pack
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#update) - Update a Pack

### [pipelines](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md)

* [list_pipeline](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#list_pipeline) - Get a list of Pipeline objects
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#create) - Create a Pipeline
* [get_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#get_pipeline_by_id) - Get Pipeline by ID
* [update_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#update_pipeline_by_id) - Update a Pipeline
* [delete_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#delete_pipeline_by_id) - Delete Pipeline

### [routes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#list) - Get a list of Routes objects
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#get) - Get Routes by ID
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#update) - Update Routes
* [append](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#append) - Append Routes to the end of the Routing table

### [sources](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#list) - List all Sources
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#create) - Create a Source
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#get) - Retrieve a Source
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#update) - Update a Source
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#delete) - Delete a Source
* [create_hec_token](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#create_hec_token) - Add an HEC token and optional metadata to a Splunk HEC Source
* [update_hec_token_metadata](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#update_hec_token_metadata) - Update metadata for an HEC token for a Splunk HEC Source

### [versioning](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md)

* [get_branch](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_branch) - List all branches in the Git repository used for Cribl configuration
* [create_commit](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_commit) - Create a new commit for pending changes to the Cribl configuration
* [get_file_count](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_file_count) - Retrieve a count of files that changed since a commit
* [get_branch_name](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_branch_name) - Retrieve the name of the Git branch that the Cribl configuration is checked out to
* [get_diff](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_diff) - Retrieve the diff for a commit
* [get_file_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_file_info) - Retrieve the names and statuses of files that changed since a commit
* [get_config_status](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_config_status) - Retrieve the configuration and status for the Git integration
* [push_commit](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#push_commit) - Push a commit from the local repository to the remote repository
* [revert_commit](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#revert_commit) - Revert a commit in the local repository
* [show_commit](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#show_commit) - Retrieve the diff and log message for a commit
* [get_current_status](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_current_status) - Retrieve the status of the current working tree
* [sync_local_remote](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#sync_local_remote) - Synchronize the local branch with the remote repository
* [clean_working_dir](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#clean_working_dir) - Undo the most recent commit and restore the local repository to the previous commit

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from cribl_control_plane import CriblControlPlane, models
from cribl_control_plane.utils import BackoffStrategy, RetryConfig
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
        "cache_ref": "<value>",
        "created_at": 7795.06,
        "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
        "migration_query_id": "<id>",
        "retention_in_days": 1466.58,
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
        "datatypes": [
            "<value 1>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": True,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 4334.7,
                "finished_at": 6811.22,
                "latest_scanned_time": 5303.3,
                "object_count": 9489.04,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from cribl_control_plane import CriblControlPlane, models
from cribl_control_plane.utils import BackoffStrategy, RetryConfig
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
        "cache_ref": "<value>",
        "created_at": 7795.06,
        "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
        "migration_query_id": "<id>",
        "retention_in_days": 1466.58,
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
        "datatypes": [
            "<value 1>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": True,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 4334.7,
                "finished_at": 6811.22,
                "latest_scanned_time": 5303.3,
                "object_count": 9489.04,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#error-classes). |

### Example
```python
from cribl_control_plane import CriblControlPlane, errors, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:
    res = None
    try:

        res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
            "<value 1>",
            "<value 2>",
        ], bucket_name="<value>", cache_connection={
            "accelerated_fields": [
                "<value 1>",
                "<value 2>",
            ],
            "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
            "cache_ref": "<value>",
            "created_at": 7795.06,
            "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
            "migration_query_id": "<id>",
            "retention_in_days": 1466.58,
        }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, retention_period_in_days=456.37, search_config={
            "datatypes": [
                "<value 1>",
            ],
            "metadata": {
                "earliest": "<value>",
                "enable_acceleration": True,
                "field_list": [
                    "<value 1>",
                    "<value 2>",
                ],
                "latest_run_info": {
                    "earliest_scanned_time": 4334.7,
                    "finished_at": 6811.22,
                    "latest_scanned_time": 5303.3,
                    "object_count": 9489.04,
                },
                "scan_mode": models.ScanMode.DETAILED,
            },
        }, storage_location_id="<id>", view_name="<value>")

        # Handle response
        print(res)


    except errors.CriblControlPlaneError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Error):
            print(e.data.message)  # Optional[str]
```

### Error Classes
**Primary errors:**
* [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py): The base class for HTTP error responses.
  * [`Error`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/error.py): Unexpected error. Status code `500`. *

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py)**:
* [`HealthStatusError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/healthstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 62 methods.*
* [`ResponseValidationError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from cribl_control_plane import CriblControlPlane
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CriblControlPlane(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CriblControlPlane(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CriblControlPlane` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from cribl_control_plane import CriblControlPlane, models
import os
def main():

    with CriblControlPlane(
        server_url="https://api.example.com",
        security=models.Security(
            bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
        ),
    ) as ccp_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CriblControlPlane(
        server_url="https://api.example.com",
        security=models.Security(
            bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
        ),
    ) as ccp_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from cribl_control_plane import CriblControlPlane
import logging

logging.basicConfig(level=logging.DEBUG)
s = CriblControlPlane(server_url="https://example.com", debug_logger=logging.getLogger("cribl_control_plane"))
```

You can also enable a default debug logger by setting an environment variable `CRIBLCONTROLPLANE_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
