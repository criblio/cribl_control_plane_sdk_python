# Health
(*health*)

## Overview

Actions related to REST server health

### Available Operations

* [get](#get) - Retrieve health status of the server

## get

Retrieve health status of the server

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthInfo" method="get" path="/health" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.health.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetHealthInfoResponse](../../models/gethealthinforesponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.HealthStatusError | 420                      | application/json         |
| errors.APIError          | 4XX, 5XX                 | \*/\*                    |