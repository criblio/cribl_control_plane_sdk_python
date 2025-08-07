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

    res = ccp_client.sources.list_source()

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

        res = await ccp_client.sources.list_source_async()

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

    res = ccp_client.sources.list_source()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [auth](docs/sdks/authsdk/README.md)

* [login](docs/sdks/authsdk/README.md#login) - Log in and obtain Auth token


### [destinations](docs/sdks/destinations/README.md)

* [list_destination](docs/sdks/destinations/README.md#list_destination) - Get a list of Destination objects
* [create_destination](docs/sdks/destinations/README.md#create_destination) - Create Destination
* [get_destination_by_id](docs/sdks/destinations/README.md#get_destination_by_id) - Get Destination by ID
* [update_destination_by_id](docs/sdks/destinations/README.md#update_destination_by_id) - Update Destination
* [delete_destination_by_id](docs/sdks/destinations/README.md#delete_destination_by_id) - Delete Destination
* [delete_destination_pq_by_id](docs/sdks/destinations/README.md#delete_destination_pq_by_id) - Clears destination persistent queue
* [get_destination_pq_by_id](docs/sdks/destinations/README.md#get_destination_pq_by_id) - Retrieves status of latest clear PQ job for a destination
* [get_destination_samples_by_id](docs/sdks/destinations/README.md#get_destination_samples_by_id) - Retrieve samples data for the specified destination. Used to get sample data for the test action.
* [create_destination_test_by_id](docs/sdks/destinations/README.md#create_destination_test_by_id) - Send sample data to a destination to validate configuration or test connectivity

### [health](docs/sdks/health/README.md)

* [get_health_info](docs/sdks/health/README.md#get_health_info) - Provides health info for REST server

### [pipelines](docs/sdks/pipelines/README.md)

* [list_pipeline](docs/sdks/pipelines/README.md#list_pipeline) - Get a list of Pipeline objects
* [create_pipeline](docs/sdks/pipelines/README.md#create_pipeline) - Create Pipeline
* [get_pipeline_by_id](docs/sdks/pipelines/README.md#get_pipeline_by_id) - Get Pipeline by ID
* [update_pipeline_by_id](docs/sdks/pipelines/README.md#update_pipeline_by_id) - Update Pipeline
* [delete_pipeline_by_id](docs/sdks/pipelines/README.md#delete_pipeline_by_id) - Delete Pipeline

### [routes](docs/sdks/routessdk/README.md)

* [list_routes](docs/sdks/routessdk/README.md#list_routes) - Get a list of Routes objects
* [get_routes_by_id](docs/sdks/routessdk/README.md#get_routes_by_id) - Get Routes by ID
* [update_routes_by_id](docs/sdks/routessdk/README.md#update_routes_by_id) - Update Routes
* [create_routes_append_by_id](docs/sdks/routessdk/README.md#create_routes_append_by_id) - Appends routes to the end of the routing table

### [sources](docs/sdks/sources/README.md)

* [list_source](docs/sdks/sources/README.md#list_source) - Get a list of Source objects
* [create_source](docs/sdks/sources/README.md#create_source) - Create Source
* [get_source_by_id](docs/sdks/sources/README.md#get_source_by_id) - Get Source by ID
* [update_source_by_id](docs/sdks/sources/README.md#update_source_by_id) - Update Source
* [delete_source_by_id](docs/sdks/sources/README.md#delete_source_by_id) - Delete Source
* [create_source_hec_token_by_id](docs/sdks/sources/README.md#create_source_hec_token_by_id) - Add token and optional metadata to an existing HEC Source
* [update_source_hec_token_by_id_and_token](docs/sdks/sources/README.md#update_source_hec_token_by_id_and_token) - Update token metadata on existing HEC Source

### [versioning](docs/sdks/versioning/README.md)

* [get_version_branch](docs/sdks/versioning/README.md#get_version_branch) - get the list of branches
* [create_version_commit](docs/sdks/versioning/README.md#create_version_commit) - create a new commit containing the current configs the given log message describing the changes.
* [get_version_count](docs/sdks/versioning/README.md#get_version_count) - get the count of files of changed
* [get_version_current_branch](docs/sdks/versioning/README.md#get_version_current_branch) - returns git branch that the config is checked out to, if any
* [get_version_diff](docs/sdks/versioning/README.md#get_version_diff) - get the textual diff for given commit
* [get_version_files](docs/sdks/versioning/README.md#get_version_files) - get the files changed
* [get_version_info](docs/sdks/versioning/README.md#get_version_info) - Get info about versioning availability
* [create_version_push](docs/sdks/versioning/README.md#create_version_push) - push the current configs to the remote repository.
* [create_version_revert](docs/sdks/versioning/README.md#create_version_revert) - revert a commit
* [get_version_show](docs/sdks/versioning/README.md#get_version_show) - get the log message and textual diff for given commit
* [get_version_status](docs/sdks/versioning/README.md#get_version_status) - get the the working tree status
* [create_version_sync](docs/sdks/versioning/README.md#create_version_sync) - syncs with remote repo via POST requests
* [create_version_undo](docs/sdks/versioning/README.md#create_version_undo) - undo the last commit

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

    res = ccp_client.sources.list_source(,
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

    res = ccp_client.sources.list_source()

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

        res = ccp_client.sources.list_source()

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
  * [`Error`](./src/cribl_control_plane/errors/error.py): Unexpected error. Status code `500`. *

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblControlPlaneError`](./src/cribl_control_plane/errors/criblcontrolplaneerror.py)**:
* [`HealthStatusError`](./src/cribl_control_plane/errors/healthstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 40 methods.*
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
