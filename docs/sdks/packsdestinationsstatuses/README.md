# Packs.Destinations.Statuses

## Overview

### Available Operations

* [get](#get) - Get the status of a Destination within a Pack
* [list](#list) - List the status of all Destinations within a Pack

## get

Get the status and optional metrics for the specified Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputStatusSystemOutputsByPackAndId" method="get" path="/p/{pack}/system/status/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.statuses.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                   | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The <code>id</code> of the Destination to get the status for.                                                                          |
| `pack`                                                                                                                                 | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The <code>id</code> of the Pack to get.                                                                                                |
| `metrics`                                                                                                                              | *Optional[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                     | Set to <code>true</code> to include metrics for each Destination. Otherwise, <code>false</code> (default).                             |
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

List status information and optional metrics for all configured Destinations in the Worker Group or Edge Fleet within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputStatusSystemOutputsByPack" method="get" path="/p/{pack}/system/status/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.statuses.list(pack="<value>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pack`                                                                                                                                             | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | The <code>id</code> of the Pack to list.                                                                                                           |
| `metrics`                                                                                                                                          | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | Set to <code>true</code> to include metrics for each Destination. Otherwise, <code>false</code> (default).                                         |
| `type`                                                                                                                                             | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | Set to <code>true</code> to prefix the Destination <code>id</code> with the Destination type. Otherwise, <code>false</code> (default).             |
| `offset`                                                                                                                                           | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Starting point from which to retrieve results for this request. Use with <code>limit</code> to paginate the response into manageable batches.      |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of items to return in the response for this request. Use with <code>offset</code> to paginate the response into manageable batches. |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.GetOutputStatusSystemOutputsByPackResponse](../../models/getoutputstatussystemoutputsbypackresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |