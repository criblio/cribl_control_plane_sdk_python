# Packs.Sources

## Overview

### Available Operations

* [list](#list) - List all Sources within a Pack
* [create](#create) - Create a Source within a Pack
* [get](#get) - Get a Source within a Pack
* [update](#update) - Update a Source within a Pack
* [delete](#delete) - Delete a Source within a Pack

## list

Get a list of all Sources within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputSystemByPack" method="get" path="/p/{pack}/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "appscope-source",
        "type": models.CreateInputSystemByPackTypeAppscope.APPSCOPE,
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 4067.15,
        "socket_idle_timeout": 1373.9,
        "socket_ending_max_wait": 5473.3,
        "socket_max_lifespan": 7426.73,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 4309.15,
        "enable_unix_path": True,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://negative-asset.info/",
        },
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "char antagonize yuck",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `pack`                                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Pack to create.                                                      |
| `request_body`                                                                                  | [models.CreateInputSystemByPackRequestBody](../../models/createinputsystembypackrequestbody.md) | :heavy_check_mark:                                                                              | Input object                                                                                    |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputSystemByPackAndId" method="get" path="/p/{pack}/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to get.                           |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to get.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Source.</br></br>Provide a complete representation of the Source that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Source.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Source might not function as expected within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "appscope-source",
        "type": models.InputAppscopeType.APPSCOPE,
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 2177.87,
        "socket_idle_timeout": 1131.76,
        "socket_ending_max_wait": 2476.4,
        "socket_max_lifespan": 8980.2,
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
        "stale_channel_flush_ms": 5201.14,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://stable-transparency.org/",
        },
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "graffiti yawningly absent when times sonata or uselessly woeful amidst",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to update.                        |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to update.                          |
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

Delete the specified Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteInputSystemByPackAndId" method="delete" path="/p/{pack}/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.delete(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to delete.                        |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to delete.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |