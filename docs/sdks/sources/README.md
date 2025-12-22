# Sources

## Overview

Actions related to Sources

### Available Operations

* [list](#list) - List all Sources
* [create](#create) - Create a Source
* [get](#get) - Get a Source
* [update](#update) - Update a Source
* [delete](#delete) - Delete a Source

## list

Get a list of all Sources.

### Example Usage

<!-- UsageSnippet language="python" operationID="listInput" method="get" path="/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "appscope-source",
        "type": models.CreateInputTypeAppscope.APPSCOPE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeAppscope.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionAppscope.NONE,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://drab-scrap.info/",
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatAppscope.GZIP,
            "dest_path": "$CRIBL_HOME/state/appscope",
        },
        "auth_type": models.AuthenticationMethodAppscope.MANUAL,
        "description": "if deserted boohoo red chops excepting know stay bah",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionAppscope.TL_SV1_1,
            "max_version": models.MaximumTLSVersionAppscope.TL_SV1,
        },
        "unix_socket_path": "$CRIBL_HOME/state/appscope.sock",
        "unix_socket_perms": "<value>",
        "auth_token": "",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateInputRequest](../../models/createinputrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputById" method="get" path="/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to get.                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Source.</br></br>Provide a complete representation of the Source that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Source.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Source might not function as expected.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "appscope-source",
        "type": models.InputAppscopeType.APPSCOPE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.InputAppscopeMode.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.InputAppscopeCompression.NONE,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://youthful-hammock.net/",
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.InputAppscopeDataCompressionFormat.GZIP,
            "dest_path": "$CRIBL_HOME/state/appscope",
        },
        "auth_type": models.InputAppscopeAuthenticationMethod.MANUAL,
        "description": "beyond hidden supposing ghost fictionalize disarm geez",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.InputAppscopeMinimumTLSVersion.TL_SV1_1,
            "max_version": models.InputAppscopeMaximumTLSVersion.TL_SV1_2,
        },
        "unix_socket_path": "$CRIBL_HOME/state/appscope.sock",
        "unix_socket_perms": "<value>",
        "auth_token": "",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to update.                        |
| `input`                                                             | [models.Input](../../models/input.md)                               | :heavy_check_mark:                                                  | Input object                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteInputById" method="delete" path="/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to delete.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |