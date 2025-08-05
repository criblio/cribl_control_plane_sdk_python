# WorkersSDK
(*workers*)

## Overview

Actions related to Workers

### Available Operations

* [get_summary_workers](#get_summary_workers) - get worker and edge nodes count
* [get_workers](#get_workers) - get worker and edge nodes
* [update_workers_restart](#update_workers_restart) - restarts worker nodes

## get_summary_workers

get worker and edge nodes count

### Example Usage

<!-- UsageSnippet language="python" operationID="getSummaryWorkers" method="get" path="/master/summary/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.workers.get_summary_workers(filter_exp="<value>")

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

## get_workers

get worker and edge nodes

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkers" method="get" path="/master/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.workers.get_workers(filter_exp="<value>", sort="<value>", sort_exp="<value>", limit=402753, offset=848752, filter_="<value>")

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

## update_workers_restart

restarts worker nodes

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWorkersRestart" method="patch" path="/master/workers/restart" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.workers.update_workers_restart()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateWorkersRestartResponse](../../models/updateworkersrestartresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |