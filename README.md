# cribl_control_plane_sdk_python
<!-- Start Summary [summary] -->
## Summary

Cribl API Reference: This API Reference lists available REST endpoints, along with their supported operations for accessing, creating, updating, or deleting resources. See our complementary product documentation at [docs.cribl.io](http://docs.cribl.io).
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [cribl_control_plane_sdk_python](#criblcontrolplanesdkpython)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add cribl-control-plane
```

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
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
        "current_size_bytes": 6170.04,
        "metrics_date": "<value>",
    }, retention_period_in_days=456.37, search_config={
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

The same SDK client can also be used to make asynchronous requests by importing asyncio.

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
        }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
            "current_size_bytes": 6170.04,
            "metrics_date": "<value>",
        }, retention_period_in_days=456.37, search_config={
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
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
        "current_size_bytes": 6170.04,
        "metrics_date": "<value>",
    }, retention_period_in_days=456.37, search_config={
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

#### [auth.tokens](docs/sdks/tokens/README.md)

* [get](docs/sdks/tokens/README.md#get) - Log in and fetch an authentication token

### [destinations](docs/sdks/destinations/README.md)

* [list](docs/sdks/destinations/README.md#list) - List all Destinations
* [create](docs/sdks/destinations/README.md#create) - Create a Destination
* [get](docs/sdks/destinations/README.md#get) - Get a Destination
* [update](docs/sdks/destinations/README.md#update) - Update a Destination
* [delete](docs/sdks/destinations/README.md#delete) - Delete a Destination

#### [destinations.pq](docs/sdks/destinationspq/README.md)

* [clear](docs/sdks/destinationspq/README.md#clear) - Clear the persistent queue for a Destination
* [get](docs/sdks/destinationspq/README.md#get) - Get information about the latest job to clear the persistent queue for a Destination

#### [destinations.samples](docs/sdks/samples/README.md)

* [get](docs/sdks/samples/README.md#get) - Get sample event data for a Destination
* [create](docs/sdks/samples/README.md#create) - Send sample event data to a Destination

### [groups](docs/sdks/groupssdk/README.md)

* [list](docs/sdks/groupssdk/README.md#list) - List all Worker Groups or Edge Fleets for the specified Cribl product
* [create](docs/sdks/groupssdk/README.md#create) - Create a Worker Group or Edge Fleet for the specified Cribl product
* [get](docs/sdks/groupssdk/README.md#get) - Get a Worker Group or Edge Fleet
* [update](docs/sdks/groupssdk/README.md#update) - Update a Worker Group or Edge Fleet
* [delete](docs/sdks/groupssdk/README.md#delete) - Delete a Worker Group or Edge Fleet
* [deploy](docs/sdks/groupssdk/README.md#deploy) - Deploy commits to a Worker Group or Edge Fleet

#### [groups.acl](docs/sdks/acl/README.md)

* [get](docs/sdks/acl/README.md#get) - Get the Access Control List for a Worker Group or Edge Fleet

#### [groups.acl.teams](docs/sdks/teams/README.md)

* [get](docs/sdks/teams/README.md#get) - Get the Access Control List for teams with permissions on a Worker Group or Edge Fleet for the specified Cribl product

#### [groups.configs.versions](docs/sdks/configsversions/README.md)

* [get](docs/sdks/configsversions/README.md#get) - Get the configuration version for a Worker Group or Edge Fleet

### [health](docs/sdks/health/README.md)

* [get](docs/sdks/health/README.md#get) - Retrieve health status of the server

### [lake_datasets](docs/sdks/lakedatasets/README.md)

* [create](docs/sdks/lakedatasets/README.md#create) - Create a Lake Dataset
* [list](docs/sdks/lakedatasets/README.md#list) - List all Lake Datasets
* [delete](docs/sdks/lakedatasets/README.md#delete) - Delete a Lake Dataset
* [get](docs/sdks/lakedatasets/README.md#get) - Get a Lake Dataset
* [update](docs/sdks/lakedatasets/README.md#update) - Update a Lake Dataset

### [nodes](docs/sdks/nodes/README.md)

* [list](docs/sdks/nodes/README.md#list) - Get detailed metadata for Worker and Edge Nodes
* [count](docs/sdks/nodes/README.md#count) - Get a count of Worker and Edge Nodes

#### [nodes.summaries](docs/sdks/summaries/README.md)

* [get](docs/sdks/summaries/README.md#get) - Get a summary of the Distributed deployment

### [packs](docs/sdks/packs/README.md)

* [install](docs/sdks/packs/README.md#install) - Install a Pack
* [list](docs/sdks/packs/README.md#list) - List all Packs
* [upload](docs/sdks/packs/README.md#upload) - Upload a Pack file
* [delete](docs/sdks/packs/README.md#delete) - Uninstall a Pack
* [get](docs/sdks/packs/README.md#get) - Get a Pack
* [update](docs/sdks/packs/README.md#update) - Upgrade a Pack

### [pipelines](docs/sdks/pipelines/README.md)

* [list](docs/sdks/pipelines/README.md#list) - List all Pipelines
* [create](docs/sdks/pipelines/README.md#create) - Create a Pipeline
* [get](docs/sdks/pipelines/README.md#get) - Get a Pipeline
* [update](docs/sdks/pipelines/README.md#update) - Update a Pipeline
* [delete](docs/sdks/pipelines/README.md#delete) - Delete a Pipeline

### [routes](docs/sdks/routessdk/README.md)

* [list](docs/sdks/routessdk/README.md#list) - List all Routes
* [get](docs/sdks/routessdk/README.md#get) - Get a Routing table
* [update](docs/sdks/routessdk/README.md#update) - Update a Route
* [append](docs/sdks/routessdk/README.md#append) - Add a Route to the end of the Routing table

### [sources](docs/sdks/sources/README.md)

* [list](docs/sdks/sources/README.md#list) - List all Sources
* [create](docs/sdks/sources/README.md#create) - Create a Source
* [get](docs/sdks/sources/README.md#get) - Get a Source
* [update](docs/sdks/sources/README.md#update) - Update a Source
* [delete](docs/sdks/sources/README.md#delete) - Delete a Source

#### [sources.hec_tokens](docs/sdks/hectokens/README.md)

* [create](docs/sdks/hectokens/README.md#create) - Add an HEC token and optional metadata to a Splunk HEC Source
* [update](docs/sdks/hectokens/README.md#update) - Update metadata for an HEC token for a Splunk HEC Source

#### [versions.branches](docs/sdks/branches/README.md)

* [list](docs/sdks/branches/README.md#list) - List all branches in the Git repository used for Cribl configuration
* [get](docs/sdks/branches/README.md#get) - Get the name of the Git branch that the Cribl configuration is checked out to

#### [versions.commits](docs/sdks/commits/README.md)

* [create](docs/sdks/commits/README.md#create) - Create a new commit for pending changes to the Cribl configuration
* [diff](docs/sdks/commits/README.md#diff) - Get the diff for a commit
* [list](docs/sdks/commits/README.md#list) - List the commit history
* [push](docs/sdks/commits/README.md#push) - Push local commits to the remote repository
* [revert](docs/sdks/commits/README.md#revert) - Revert a commit in the local repository
* [get](docs/sdks/commits/README.md#get) - Get the diff and log message for a commit
* [undo](docs/sdks/commits/README.md#undo) - Discard uncommitted (staged) changes

#### [versions.commits.files](docs/sdks/commitsfiles/README.md)

* [count](docs/sdks/commitsfiles/README.md#count) - Get a count of files that changed since a commit
* [list](docs/sdks/commitsfiles/README.md#list) - Get the names and statuses of files that changed since a commit

#### [versions.configs](docs/sdks/versionsconfigs/README.md)

* [get](docs/sdks/versionsconfigs/README.md#get) - Get the configuration and status for the Git integration

#### [versions.statuses](docs/sdks/statuses/README.md)

* [get](docs/sdks/statuses/README.md#get) - Get the status of the current working tree

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.upload(filename="example.file", request_body=open("example.file", "rb"))

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

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
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
        "current_size_bytes": 6170.04,
        "metrics_date": "<value>",
    }, retention_period_in_days=456.37, search_config={
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
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
        "current_size_bytes": 6170.04,
        "metrics_date": "<value>",
    }, retention_period_in_days=456.37, search_config={
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

[`CriblControlPlaneError`](./src/cribl_control_plane/errors/criblcontrolplaneerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

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
        }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
            "current_size_bytes": 6170.04,
            "metrics_date": "<value>",
        }, retention_period_in_days=456.37, search_config={
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
* [`CriblControlPlaneError`](./src/cribl_control_plane/errors/criblcontrolplaneerror.py): The base class for HTTP error responses.
  * [`Error`](./src/cribl_control_plane/errors/error.py): Unexpected error. Status code `500`.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblControlPlaneError`](./src/cribl_control_plane/errors/criblcontrolplaneerror.py)**:
* [`HealthServerStatusError`](./src/cribl_control_plane/errors/healthserverstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 63 methods.*
* [`ResponseValidationError`](./src/cribl_control_plane/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
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
