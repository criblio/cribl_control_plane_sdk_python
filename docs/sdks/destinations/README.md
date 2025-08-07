# Destinations
(*destinations*)

## Overview

### Available Operations

* [list](#list) - List all Destinations
* [create](#create) - Create a Destination
* [get](#get) - Retrieve a Destination
* [update](#update) - Update a Destination
* [delete](#delete) - Delete a Destination
* [clear_persistent_queue](#clear_persistent_queue) - Clear the persistent queue for a Destination
* [get_persistent_queue_status](#get_persistent_queue_status) - Retrieve information about the latest job to clear the persistent queue for a Destination
* [get_sample_data](#get_sample_data) - Retrieve sample event data for a Destination
* [create_sample_data](#create_sample_data) - Send sample event data to a Destination

## list

Get a list of Destination objects

### Example Usage

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

**[models.ListOutputResponse](../../models/listoutputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create Destination

### Example Usage

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
            "auth_type": models.OutputElasticCloudAuthenticationMethod.MANUAL,
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
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.OutputElasticCloudCompression.NONE,
        "pq_on_backpressure": models.OutputElasticCloudQueueFullBehavior.BLOCK,
        "pq_mode": models.OutputElasticCloudMode.ERROR,
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

**[models.CreateOutputResponse](../../models/createoutputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get Destination by ID

### Example Usage

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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to GET                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOutputByIDResponse](../../models/getoutputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update Destination

### Example Usage

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
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.OutputSignalfxCompression.NONE,
        "pq_on_backpressure": models.OutputSignalfxQueueFullBehavior.BLOCK,
        "pq_mode": models.OutputSignalfxMode.ERROR,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to PATCH                                                  |
| `output`                                                            | [models.Output](../../models/output.md)                             | :heavy_check_mark:                                                  | Output object                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateOutputByIDResponse](../../models/updateoutputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete Destination

### Example Usage

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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to DELETE                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOutputByIDResponse](../../models/deleteoutputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## clear_persistent_queue

Clears destination persistent queue

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.clear_persistent_queue(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Destination Id                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOutputPqByIDResponse](../../models/deleteoutputpqbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_persistent_queue_status

Retrieves status of latest clear PQ job for a destination

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.get_persistent_queue_status(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Destination Id                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOutputPqByIDResponse](../../models/getoutputpqbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_sample_data

Retrieve samples data for the specified destination. Used to get sample data for the test action.

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.get_sample_data(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Destination Id                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOutputSamplesByIDResponse](../../models/getoutputsamplesbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_sample_data

Send sample data to a destination to validate configuration or test connectivity

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create_sample_data(id="<id>", events=[
        {
            "raw": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Destination Id                                                      |
| `events`                                                            | List[[models.CriblEvent](../../models/criblevent.md)]               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateOutputTestByIDResponse](../../models/createoutputtestbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |