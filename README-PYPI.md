# cribl_control_plane_sdk_python

The Cribl Python SDK for the control plane provides operational control over Cribl resources and helps streamline the process of integrating with Cribl.

In addition to the usage examples in this repository, the Cribl documentation includes [code examples for common use cases](https://docs.cribl.io/cribl-as-code/code-examples).

Complementary API reference documentation is available at https://docs.cribl.io/cribl-as-code/api-reference. Product documentation is available at https://docs.cribl.io.

> [!IMPORTANT]
> **Preview Feature**
> The Cribl SDKs are Preview features that are still being developed. We do not recommend using them in a production environment, because the features might not be fully tested or optimized for performance, and related documentation could be incomplete.
>
> Please continue to submit feedback through normal Cribl support channels, but assistance might be limited while the features remain in Preview.

<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [cribl_control_plane_sdk_python](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#criblcontrolplanesdkpython)
  * [SDK Installation](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#available-resources-and-operations)
  * [File uploads](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#file-uploads)
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

## Authentication

Except for the `health.get` and `auth.tokens.get` methods, all Cribl SDK requests require you to authenticate with a Bearer token. You must include a valid Bearer token in the configuration when initializing your SDK client. The Bearer token verifies your identity and ensures secure access to the requested resources. The SDK automatically manages the `Authorization` header for subsequent requests once properly authenticated.

For information about Bearer token expiration, see [Token Management](https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-token-mgmt) in the Cribl as Code documentation.

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name           | Type   | Scheme       | Environment Variable             |
| -------------- | ------ | ------------ | -------------------------------- |
| `bearer_auth`  | http   | HTTP Bearer  | `CRIBLCONTROLPLANE_BEARER_AUTH`  |
| `client_oauth` | oauth2 | OAuth2 token | `CRIBLCONTROLPLANE_CLIENT_OAUTH` |

To configure authentication on Cribl.Cloud and in hybrid deployments, use the `client_oauth` security scheme. The SDK uses the OAuth credentials that you provide to obtain a Bearer token and refresh the token within its expiration window using the standard OAuth2 flow.

In on-prem deployments, use the `bearer_auth` security scheme. The SDK uses the username/password credentials that you provide to obtain a Bearer token. Automatically refreshing the Bearer token within its expiration window requires a callback function as shown in the authentication example.

Set the security scheme through the `security` optional parameter when initializing the SDK client instance. The SDK uses the selected scheme by default to authenticate with the API for all operations that support it, as shown in the [SDK Example Usage](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/#sdk-example-usage) code example.

### Authentication Examples

The [Cribl.Cloud and Hybrid Authentication Example](https://github.com/criblio/cribl_control_plane_sdk_python/blob/main/examples/example_cloud_auth.py) demonstrates how to configure authentication on Cribl.Cloud and in hybrid deployments. To obtain the Client ID and Client Secret you'll need to initialize using the `client_oauth` security schema, follow the [instructions for creating an API Credential](https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud) in the Cribl as Code documentation.

The [On-Prem Authentication Example](https://github.com/criblio/cribl_control_plane_sdk_python/blob/main/examples/example_onprem_auth.py) demonstrates how to configure authentication in on-prem deployments using your username and password.

<!-- No Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

#### [auth.tokens](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/tokens/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/tokens/README.md#get) - Log in and fetch an authentication token

### [destinations](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#list) - List all Destinations
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#create) - Create a Destination
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get) - Get a Destination
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#update) - Update a Destination
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#delete) - Delete a Destination

#### [destinations.pq](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinationspq/README.md)

* [clear](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinationspq/README.md#clear) - Clear the persistent queue for a Destination
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinationspq/README.md#get) - Get information about the latest job to clear the persistent queue for a Destination

#### [destinations.samples](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/samples/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/samples/README.md#get) - Get sample event data for a Destination
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/samples/README.md#create) - Send sample event data to a Destination

### [groups](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#list) - List all Worker Groups or Edge Fleets for the specified Cribl product
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#create) - Create a Worker Group or Edge Fleet for the specified Cribl product
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get) - Get a Worker Group or Edge Fleet
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#update) - Update a Worker Group or Edge Fleet
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#delete) - Delete a Worker Group or Edge Fleet
* [deploy](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#deploy) - Deploy commits to a Worker Group or Edge Fleet

#### [groups.acl](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/acl/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/acl/README.md#get) - Get the Access Control List for a Worker Group or Edge Fleet

#### [groups.acl.teams](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/teams/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/teams/README.md#get) - Get the Access Control List for teams with permissions on a Worker Group or Edge Fleet for the specified Cribl product

#### [groups.configs.versions](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/configsversions/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/configsversions/README.md#get) - Get the configuration version for a Worker Group or Edge Fleet

### [health](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md#get) - Retrieve health status of the server

### [lake_datasets](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md)

* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#create) - Create a Lake Dataset
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#list) - List all Lake Datasets
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#delete) - Delete a Lake Dataset
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#get) - Get a Lake Dataset
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lakedatasets/README.md#update) - Update a Lake Dataset

### [nodes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md#list) - Get detailed metadata for Worker and Edge Nodes
* [count](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/nodes/README.md#count) - Get a count of Worker and Edge Nodes

#### [nodes.summaries](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/summaries/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/summaries/README.md#get) - Get a summary of the Distributed deployment

### [packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md)

* [install](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#install) - Install a Pack
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#list) - List all Packs
* [upload](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#upload) - Upload a Pack file
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#delete) - Uninstall a Pack
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#get) - Get a Pack
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#update) - Upgrade a Pack

### [pipelines](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#list) - List all Pipelines
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#create) - Create a Pipeline
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#get) - Get a Pipeline
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#update) - Update a Pipeline
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#delete) - Delete a Pipeline

### [routes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#list) - List all Routes
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#get) - Get a Routing table
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#update) - Update a Route
* [append](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#append) - Add a Route to the end of the Routing table

### [sources](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#list) - List all Sources
* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#create) - Create a Source
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#get) - Get a Source
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#update) - Update a Source
* [delete](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#delete) - Delete a Source

#### [sources.hec_tokens](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/hectokens/README.md)

* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/hectokens/README.md#create) - Add an HEC token and optional metadata to a Splunk HEC Source
* [update](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/hectokens/README.md#update) - Update metadata for an HEC token for a Splunk HEC Source

#### [versions.branches](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/branches/README.md)

* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/branches/README.md#list) - List all branches in the Git repository used for Cribl configuration
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/branches/README.md#get) - Get the name of the Git branch that the Cribl configuration is checked out to

#### [versions.commits](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md)

* [create](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#create) - Create a new commit for pending changes to the Cribl configuration
* [diff](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#diff) - Get the diff for a commit
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#list) - List the commit history
* [push](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#push) - Push local commits to the remote repository
* [revert](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#revert) - Revert a commit in the local repository
* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#get) - Get the diff and log message for a commit
* [undo](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commits/README.md#undo) - Discard uncommitted (staged) changes

#### [versions.commits.files](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commitsfiles/README.md)

* [count](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commitsfiles/README.md#count) - Get a count of files that changed since a commit
* [list](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/commitsfiles/README.md#list) - Get the names and statuses of files that changed since a commit

#### [versions.configs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versionsconfigs/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versionsconfigs/README.md#get) - Get the configuration and status for the Git integration

#### [versions.statuses](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/statuses/README.md)

* [get](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/statuses/README.md#get) - Get the status of the current working tree

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
* [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py): The base class for HTTP error responses.
  * [`Error`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/error.py): Unexpected error. Status code `500`.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py)**:
* [`HealthServerStatusError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/healthserverstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 63 methods.*
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
