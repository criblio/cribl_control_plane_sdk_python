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

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/criblio/cribl_control_plane_sdk_python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/criblio/cribl_control_plane_sdk_python.git
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
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.diag.get_health_info()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from cribl_control_plane import CriblControlPlane

async def main():

    async with CriblControlPlane(
        server_url="https://api.example.com",
    ) as ccp_client:

        res = await ccp_client.diag.get_health_info_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable            |
| ------------- | ---- | ----------- | ------------------------------- |
| `bearer_auth` | http | HTTP Bearer | `CRIBLCONTROLPLANE_BEARER_AUTH` |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from cribl_control_plane import CriblControlPlane
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
) as ccp_client:

    res = ccp_client.diag.get_health_info()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [diag](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/diag/README.md)

* [get_health_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/diag/README.md#get_health_info) - Provides health info for REST server

### [health](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md)

* [get_health_info](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/docs/sdks/health/README.md#get_health_info) - Provides health info for REST server

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.utils import BackoffStrategy, RetryConfig


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.diag.get_health_info(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.utils import BackoffStrategy, RetryConfig


with CriblControlPlane(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as ccp_client:

    res = ccp_client.diag.get_health_info()

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
from cribl_control_plane import CriblControlPlane, errors


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:
    res = None
    try:

        res = ccp_client.diag.get_health_info()

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
        if isinstance(e, errors.HealthStatusError):
            print(e.data.role)  # Optional[models.Role]
            print(e.data.status)  # models.Status
            print(e.data.start_time)  # float
```

### Error Classes
**Primary error:**
* [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblControlPlaneError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/criblcontrolplaneerror.py)**:
* [`HealthStatusError`](https://github.com/criblio/cribl_control_plane_sdk_python/blob/master/./src/cribl_control_plane/errors/healthstatuserror.py): Healthy status. Status code `420`. Applicable to 1 of 2 methods.*
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
from cribl_control_plane import CriblControlPlane
def main():

    with CriblControlPlane(
        server_url="https://api.example.com",
    ) as ccp_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CriblControlPlane(
        server_url="https://api.example.com",
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
