# Destinations.Statuses

## Overview

### Available Operations

* [get](#get) - Get the status of a Destination
* [list](#list) - List the status of all Destinations

## get

Get the status and optional metrics for the specified Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputStatusById" method="get" path="/system/status/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.statuses.get(id="<id>", metrics=False, type_=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                   | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The <code>id</code> of the Destination to get the status for.                                                                          |
| `metrics`                                                                                                                              | *Optional[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                     | Set to true <code>true</code> to include metrics for each Destination. Otherwise, <code>false</code> (default).                        |
| `type`                                                                                                                                 | *Optional[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                     | Set to <code>true</code> to prefix the Destination <code>id</code> with the Destination type. Otherwise, <code>false</code> (default). |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.CountedOutputStatus](../../models/countedoutputstatus.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of status information and optional health metrics for all configured Destinations in the Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputStatus" method="get" path="/system/status/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.statuses.list(metrics=False, type_=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `metrics`                                                                                                                              | *Optional[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                     | Set to true <code>true</code> to include metrics for each Destination. Otherwise, <code>false</code> (default).                        |
| `type`                                                                                                                                 | *Optional[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                     | Set to <code>true</code> to prefix the Destination <code>id</code> with the Destination type. Otherwise, <code>false</code> (default). |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.CountedOutputStatus](../../models/countedoutputstatus.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |