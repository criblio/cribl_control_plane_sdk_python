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

    res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>")

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

        res = await ccp_client.lake.create_cribl_lake_dataset_by_lake_id_async(lake_id="<id>", id="<id>")

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

    res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [auth](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/authsdk/README.md)

* [login](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/authsdk/README.md#login) - Log in and obtain Auth token


### [destinations](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md)

* [list_destination](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#list_destination) - Get a list of Destination objects
* [create_destination](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#create_destination) - Create Destination
* [get_destination_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get_destination_by_id) - Get Destination by ID
* [update_destination_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#update_destination_by_id) - Update Destination
* [delete_destination_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#delete_destination_by_id) - Delete Destination
* [delete_destination_pq_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#delete_destination_pq_by_id) - Clears destination persistent queue
* [get_destination_pq_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get_destination_pq_by_id) - Retrieves status of latest clear PQ job for a destination
* [get_destination_samples_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#get_destination_samples_by_id) - Retrieve samples data for the specified destination. Used to get sample data for the test action.
* [create_destination_test_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/destinations/README.md#create_destination_test_by_id) - Send sample data to a destination to validate configuration or test connectivity

### [distributed](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/distributed/README.md)

* [get_summary](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/distributed/README.md#get_summary) - Get summary of Distributed deployment

### [groups](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md)

* [get_groups_config_version_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_groups_config_version_by_id) - Get effective bundle version for given Group
* [create_products_groups_by_product](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#create_products_groups_by_product) - Create a Fleet or Worker Group
* [get_products_groups_by_product](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_products_groups_by_product) - Get a list of ConfigGroup objects
* [update_groups_deploy_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#update_groups_deploy_by_id) - Deploy commits for a Fleet or Worker Group
* [get_groups_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_groups_by_id) - Get a specific ConfigGroup object
* [get_groups_acl_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/groupssdk/README.md#get_groups_acl_by_id) - ACL of members with permissions for resources in this Group

### [health](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md)

* [get_health_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md#get_health_info) - Provides health info for REST server

### [lake](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md)

* [create_cribl_lake_dataset_by_lake_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md#create_cribl_lake_dataset_by_lake_id) - Create a Dataset in the specified Lake
* [get_cribl_lake_dataset_by_lake_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md#get_cribl_lake_dataset_by_lake_id) - Get the list of Dataset contained in the specified Lake
* [delete_cribl_lake_dataset_by_lake_id_and_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md#delete_cribl_lake_dataset_by_lake_id_and_id) - Delete a Dataset in the specified Lake
* [get_cribl_lake_dataset_by_lake_id_and_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md#get_cribl_lake_dataset_by_lake_id_and_id) - Get a Dataset in the specified Lake
* [update_cribl_lake_dataset_by_lake_id_and_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/lake/README.md#update_cribl_lake_dataset_by_lake_id_and_id) - Update a Dataset in the specified Lake

### [packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md)

* [create_packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#create_packs) - Install Pack
* [get_packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#get_packs) - Get info on packs
* [update_packs](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#update_packs) - Upload Pack
* [delete_packs_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#delete_packs_by_id) - Uninstall Pack from the system
* [update_packs_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/packs/README.md#update_packs_by_id) - Upgrade Pack

### [pipelines](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md)

* [list_pipeline](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#list_pipeline) - Get a list of Pipeline objects
* [create_pipeline](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#create_pipeline) - Create Pipeline
* [get_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#get_pipeline_by_id) - Get Pipeline by ID
* [update_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#update_pipeline_by_id) - Update Pipeline
* [delete_pipeline_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/pipelines/README.md#delete_pipeline_by_id) - Delete Pipeline

### [routes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md)

* [list_routes](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#list_routes) - Get a list of Routes objects
* [get_routes_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#get_routes_by_id) - Get Routes by ID
* [update_routes_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#update_routes_by_id) - Update Routes
* [create_routes_append_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/routessdk/README.md#create_routes_append_by_id) - Appends routes to the end of the routing table

### [sources](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md)

* [list_source](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#list_source) - Get a list of Source objects
* [create_source](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#create_source) - Create Source
* [get_source_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#get_source_by_id) - Get Source by ID
* [update_source_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#update_source_by_id) - Update Source
* [delete_source_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#delete_source_by_id) - Delete Source
* [create_source_hec_token_by_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#create_source_hec_token_by_id) - Add token and optional metadata to an existing HEC Source
* [update_source_hec_token_by_id_and_token](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/sources/README.md#update_source_hec_token_by_id_and_token) - Update token metadata on existing HEC Source

### [teams](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/teams/README.md)

* [get_products_groups_acl_teams_by_product_and_id](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/teams/README.md#get_products_groups_acl_teams_by_product_and_id) - ACL of team with permissions for resources in this Group

### [versioning](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md)

* [get_version_branch](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_branch) - get the list of branches
* [create_version_commit](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_version_commit) - create a new commit containing the current configs the given log message describing the changes.
* [get_version_count](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_count) - get the count of files of changed
* [get_version_current_branch](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_current_branch) - returns git branch that the config is checked out to, if any
* [get_version_diff](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_diff) - get the textual diff for given commit
* [get_version_files](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_files) - get the files changed
* [get_version_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_info) - Get info about versioning availability
* [create_version_push](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_version_push) - push the current configs to the remote repository.
* [create_version_revert](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_version_revert) - revert a commit
* [get_version_show](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_show) - get the log message and textual diff for given commit
* [get_version_status](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#get_version_status) - get the the working tree status
* [create_version_sync](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_version_sync) - syncs with remote repo via POST requests
* [create_version_undo](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/versioning/README.md#create_version_undo) - undo the last commit

### [workers](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/workerssdk/README.md)

* [get_summary_workers](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/workerssdk/README.md#get_summary_workers) - get worker and edge nodes count
* [get_workers](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/workerssdk/README.md#get_workers) - get worker and edge nodes
* [update_workers_restart](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/workerssdk/README.md#update_workers_restart) - restarts worker nodes

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

    res = ccp_client.packs.update_packs(size=779474, request_body=open("example.file", "rb"))

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

    res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>",
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

    res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>")

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

        res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>")

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
* [`HealthStatusError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/healthstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 61 methods.*
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
