# Destinations

## Overview

Actions related to Destinations

### Available Operations

* [list](#list) - List all Destinations
* [create](#create) - Create a Destination
* [get](#get) - Get a Destination
* [update](#update) - Update a Destination
* [delete](#delete) - Delete a Destination

## list

Get a list of all Destinations.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOutput" method="get" path="/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "tcpjson-output",
        "type": models.CreateOutputTypeTcpjson.TCPJSON,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "0",
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "token_ttl_minutes": 60,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "hourly about into",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "chilly-exterior.net",
                "port": 6458.17,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateOutputRequest](../../models/createoutputrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputById" method="get" path="/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to get.                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Destination.</br></br>Provide a complete representation of the Destination that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Destination.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Destination might not function as expected.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "default-output",
        "type": models.OutputFilesystemType.FILESYSTEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dest_path": "<value>",
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 4562.74,
        "max_file_open_time_sec": 2532.09,
        "max_file_idle_time_sec": 1271.28,
        "max_open_files": 3246.22,
        "header_line": "<value>",
        "write_high_water_mark": 3612.5,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "description": "bouncy tenderly yet immediate",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 1944.46,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 1965.22,
        "directory_batch_size": 3079.24,
        "deadletter_path": "<value>",
        "max_retry_num": 7017.51,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to update.                   |
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

Delete the specified Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOutputById" method="delete" path="/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to delete.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |