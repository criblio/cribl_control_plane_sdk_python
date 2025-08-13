# Sources
(*sources*)

## Overview

Actions related to Sources

### Available Operations

* [list](#list) - List all Sources
* [create](#create) - Create a Source
* [get](#get) - Retrieve a Source
* [update](#update) - Update a Source
* [delete](#delete) - Delete a Source
* [create_hec_token](#create_hec_token) - Add an HEC token and optional metadata to a Splunk HEC Source
* [update_hec_token_metadata](#update_hec_token_metadata) - Update metadata for an HEC token for a Splunk HEC Source

## list

Get a list of Source objects

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

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListInputResponse](../../models/listinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create Source

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

    res = ccp_client.sources.create(request={
        "id": "<id>",
        "type": models.InputTCPType.TCP,
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
            "mode": models.InputTCPMode.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.InputTCPCompression.NONE,
        },
        "host": "0.0.0.0",
        "port": 301.76,
        "tls": {
            "disabled": True,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "request_cert": False,
            "reject_unauthorized": "<value>",
            "common_name_regex": "<value>",
            "min_version": models.InputTCPMinimumTLSVersion.TL_SV1,
            "max_version": models.InputTCPMaximumTLSVersion.TL_SV1_1,
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
        "enable_header": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "description": "classic pish supposing misguided carefully fen",
        "auth_type": models.InputTCPAuthenticationMethod.MANUAL,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Input](../../models/input.md)                               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateInputResponse](../../models/createinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get Source by ID

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

    res = ccp_client.sources.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to GET                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInputByIDResponse](../../models/getinputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update Source

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

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "<id>",
        "type": models.InputKubeEventsType.KUBE_EVENTS,
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
            "mode": models.InputKubeEventsMode.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.InputKubeEventsCompression.NONE,
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "invite meh corny incidentally down",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "gown deployment portray gah mindless carp stabilise",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to PATCH                                                  |
| `input`                                                             | [models.Input](../../models/input.md)                               | :heavy_check_mark:                                                  | Input object                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateInputByIDResponse](../../models/updateinputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete Source

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

    res = ccp_client.sources.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to DELETE                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteInputByIDResponse](../../models/deleteinputbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_hec_token

Add token and optional metadata to an existing HEC Source

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

    res = ccp_client.sources.create_hec_token(id="<id>", token="<value>", description="bah ick stingy", enabled=False, metadata=[
        {
            "name": "<value>",
            "value": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | HEC Source id                                                                           |
| `token`                                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `description`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `enabled`                                                                               | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `metadata`                                                                              | List[[models.AddHecTokenRequestMetadatum](../../models/addhectokenrequestmetadatum.md)] | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.CreateInputHecTokenByIDResponse](../../models/createinputhectokenbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update_hec_token_metadata

Update token metadata on existing HEC Source

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

    res = ccp_client.sources.update_hec_token_metadata(id="<id>", token="<value>", description="by bleakly fortunately phew barring", enabled=False, metadata=[
        {
            "name": "<value>",
            "value": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | HEC Source id                                                                                 |
| `token`                                                                                       | *str*                                                                                         | :heavy_check_mark:                                                                            | token to update                                                                               |
| `description`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `enabled`                                                                                     | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `metadata`                                                                                    | List[[models.UpdateHecTokenRequestMetadatum](../../models/updatehectokenrequestmetadatum.md)] | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.UpdateInputHecTokenByIDAndTokenResponse](../../models/updateinputhectokenbyidandtokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |