# Destinations
(*destinations*)

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
        "id": "<id>",
        "type": models.OutputElasticCloudType.ELASTIC_CLOUD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://probable-rationale.com/",
        "index": "<value>",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.OutputElasticCloudFailedRequestLoggingMode.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": False,
            "username": "Imogene1",
            "password": "tA9DUjJtHSnXqh9",
            "auth_type": models.OutputElasticCloudAuthenticationMethod.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "response_retry_settings": [
            {
                "http_status": 7295.73,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.OutputElasticCloudBackpressureBehavior.BLOCK,
        "description": "hourly about into",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.OutputElasticCloudMode.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.OutputElasticCloudCompression.NONE,
        "pq_on_backpressure": models.OutputElasticCloudQueueFullBehavior.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Output](../../models/output.md)                             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
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
        "id": "<id>",
        "type": models.OutputSignalfxType.SIGNALFX,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "auth_type": models.OutputSignalfxAuthenticationMethod.MANUAL,
        "realm": "us0",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.OutputSignalfxFailedRequestLoggingMode.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2924.72,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.OutputSignalfxBackpressureBehavior.BLOCK,
        "description": "phooey positively a consequently meh until",
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.OutputSignalfxMode.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.OutputSignalfxCompression.NONE,
        "pq_on_backpressure": models.OutputSignalfxQueueFullBehavior.BLOCK,
        "pq_controls": {},
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