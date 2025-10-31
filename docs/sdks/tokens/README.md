# Tokens
(*auth.tokens*)

## Overview

### Available Operations

* [get](#get) - Log in and fetch an authentication token

## get

This endpoint is unavailable on Cribl.Cloud.Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to get an Auth token for Cribl.Cloud.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAuthLogin" method="post" path="/auth/login" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="6j50J9421x29IhO", username="Lilly_Weissnat")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuthToken](../../models/authtoken.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |