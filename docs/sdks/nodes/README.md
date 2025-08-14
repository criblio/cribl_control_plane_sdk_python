# Nodes
(*nodes*)

## Overview

### Available Operations

* [count](#count) - Retrieve a count of Worker and Edge Nodes
* [list](#list) - Retrieve detailed metadata for Worker and Edge Nodes

## count

get worker and edge nodes count

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

    res = ccp_client.nodes.count(filter_exp="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filter_exp`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter expression evaluated against nodes                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSummaryWorkersResponse](../../models/getsummaryworkersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

get worker and edge nodes

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

    res = ccp_client.nodes.list(filter_exp="<value>", sort="<value>", sort_exp="<value>", limit=402753, offset=848752, filter_="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `filter_exp`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter expression evaluated against nodes                            |
| `sort`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Sorting object (JSON stringified) expression evaluated against nodes |
| `sort_exp`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Sorting expression evaluated against nodes                           |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Maximum number of nodes to return                                    |
| `offset`                                                             | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Pagination offset                                                    |
| `filter_`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter object (JSON stringified) to select nodes                     |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.GetWorkersResponse](../../models/getworkersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |