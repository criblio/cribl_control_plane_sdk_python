# Packs.Sources.Statuses

## Overview

### Available Operations

* [get](#get) - Get the status of a Source within a Pack
* [list](#list) - List the status of all Sources within a Pack

## get

Get the status and optional metrics for the specified Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputStatusSystemInputsByPackAndId" method="get" path="/p/{pack}/system/status/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.statuses.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                         | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The <code>id</code> of the Source to get the status for.                                                                     |
| `pack`                                                                                                                       | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The <code>id</code> of the Pack to get.                                                                                      |
| `metrics`                                                                                                                    | *Optional[bool]*                                                                                                             | :heavy_minus_sign:                                                                                                           | Set to <code>true</code> to include metrics for each Source. Otherwise, <code>false</code> (default).                        |
| `type`                                                                                                                       | *Optional[bool]*                                                                                                             | :heavy_minus_sign:                                                                                                           | Set to <code>true</code> to prefix the Source <code>id</code> with the Source type. Otherwise, <code>false</code> (default). |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.CountedInputStatus](../../models/countedinputstatus.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

List status information and optional metrics for all configured Sources in the Worker Group or Edge Fleet within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputStatusSystemInputsByPack" method="get" path="/p/{pack}/system/status/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.statuses.list(pack="<value>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pack`                                                                                                                                             | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | The <code>id</code> of the Pack to list.                                                                                                           |
| `metrics`                                                                                                                                          | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | Set to <code>true</code> to include metrics for each Source. Otherwise, <code>false</code> (default).                                              |
| `type`                                                                                                                                             | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | Set to <code>true</code> to prefix the Source <code>id</code> with the Source type. Otherwise, <code>false</code> (default).                       |
| `offset`                                                                                                                                           | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Starting point from which to retrieve results for this request. Use with <code>limit</code> to paginate the response into manageable batches.      |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of items to return in the response for this request. Use with <code>offset</code> to paginate the response into manageable batches. |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.GetInputStatusSystemInputsByPackResponse](../../models/getinputstatussysteminputsbypackresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |