# Auth.Tokens

## Overview

### Available Operations

* [get](#get) - Log in and fetch an authentication token

## get

This endpoint is unavailable on Cribl.Cloud. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to get an Auth token for Cribl.Cloud.

### Example Usage: LoginExamplesLocalLogin

<!-- UsageSnippet language="python" operationID="createAuthLogin" method="post" path="/auth/login" example="LoginExamplesLocalLogin" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    "https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="yourPassword", username="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: LoginResponseExamplesLocalLogin

<!-- UsageSnippet language="python" operationID="createAuthLogin" method="post" path="/auth/login" example="LoginResponseExamplesLocalLogin" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    "https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="j50J9421x29IhO_", username="Turner.Kuhn")

    # Handle response
    print(res)

```
### Example Usage: authenticationFailed

<!-- UsageSnippet language="python" operationID="createAuthLogin" method="post" path="/auth/login" example="authenticationFailed" -->
```python
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    "https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="j50J9421x29IhO_", username="Turner.Kuhn")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Password for the account.                                           |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Username of the account to authenticate.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAuthLoginResponse](../../models/createauthloginresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |