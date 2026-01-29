# Packs.Destinations

## Overview

### Available Operations

* [list](#list) - List all Destinations within a Pack
* [create](#create) - Create a Destination within a Pack
* [get](#get) - Get a Destination within a Pack
* [update](#update) - Update a Destination within a Pack
* [delete](#delete) - Delete a Destination within a Pack

## list

Get a list of all Destinations within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputSystemByPack" method="get" path="/p/{pack}/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "tcpjson-output",
        "type": models.CreateOutputSystemByPackTypeTcpjson.TCPJSON,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "connection_timeout": 4098.5,
        "write_timeout": 3807.97,
        "token_ttl_minutes": 9215.23,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "unaccountably hard-to-find same kindly deprave the moisten task",
        "host": "localhost",
        "port": 10090,
        "exclude_self": True,
        "hosts": [
            {
                "host": "adolescent-cemetery.org",
                "port": 5699.66,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 7378.74,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 1392.89,
        "load_balance_stats_period_sec": 9185.86,
        "max_concurrent_senders": 9360.71,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1119.07,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4924.47,
        "pq_max_backpressure_sec": 7420.74,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `pack`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The <code>id</code> of the Pack to create.                                                        |
| `request_body`                                                                                    | [models.CreateOutputSystemByPackRequestBody](../../models/createoutputsystembypackrequestbody.md) | :heavy_check_mark:                                                                                | Output object                                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputSystemByPackAndId" method="get" path="/p/{pack}/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to get.                      |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to get.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Destination.</br></br>Provide a complete representation of the Destination that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Destination.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Destination might not function as expected within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "default-output",
        "type": models.OutputDefaultType.DEFAULT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "default_id": "my-default-output",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to update.                   |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to update.                          |
| `output`                                                            | [models.Output](../../models/output.md)                             | :heavy_check_mark:                                                  | Output object                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOutputSystemByPackAndId" method="delete" path="/p/{pack}/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.delete(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to delete.                   |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to delete.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |