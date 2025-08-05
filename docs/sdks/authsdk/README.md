# AuthSDK
(*auth*)

## Overview

Actions related to authentication. Do not use the /auth endpoints in Cribl.Cloud deployments. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to authenticate for Cribl.Cloud.

### Available Operations

* [login](#login) - Log in and obtain Auth token

## login

This endpoint is unavailable on Cribl.Cloud. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to get an Auth token for Cribl.Cloud.

### Example Usage

<!-- UsageSnippet language="python" operationID="login" method="post" path="/auth/login" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.login(username="Nikko.Connelly", password="Ljp4BunfMR9hNyM")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuthToken](../../models/authtoken.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |