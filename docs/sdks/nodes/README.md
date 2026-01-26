# Nodes

## Overview

### Available Operations

* [list](#list) - Get detailed metadata for Worker and Edge Nodes
* [count](#count) - Get a count of Worker and Edge Nodes

## list

Get detailed metadata for Worker and Edge Nodes.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMasterWorkerEntry" method="get" path="/master/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.list(filter_exp="<value>", sort_exp="<value>", filter_="<value>", sort="<value>", limit=554169, offset=426660)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_exp`                                                                                                                                       | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Filter expression to evaluate against Nodes for inclusion in the response.                                                                         |
| `sort_exp`                                                                                                                                         | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Sorting expression to evaluate against Nodes to specify the sort order for the response.                                                           |
| `filter_`                                                                                                                                          | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | JSON-stringified filter object to evaluate against Nodes for inclusion in the response.                                                            |
| `sort`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | JSON-stringified sorting object to evaluate against Nodes to specify the sort order for the response.                                              |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of Nodes to return in the response for this request. Use with <code>offset</code> to paginate the response into manageable batches. |
| `offset`                                                                                                                                           | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Starting point from which to retrieve results for this request. Use with <code>limit</code> to paginate the response into manageable batches.      |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.CountedMasterWorkerEntry](../../models/countedmasterworkerentry.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## count

Get a count of all Worker and Edge Nodes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMasterWorkerEntry" method="get" path="/master/summary/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.count(filter_exp="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `filter_exp`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter expression to evaluate against Nodes for inclusion in the response. |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.CountedNumber](../../models/countednumber.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |