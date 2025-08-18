# CommitsFiles
(*versions.commits.files*)

## Overview

### Available Operations

* [count](#count) - Retrieve a count of files that changed since a commit
* [list](#list) - Retrieve the names and statuses of files that changed since a commit

## count

get the count of files of changed

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionCount" method="get" path="/version/count" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.files.count(group="<value>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Commit ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionCountResponse](../../models/getversioncountresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

get the files changed

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionFiles" method="get" path="/version/files" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.files.list(group="<value>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Commit ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionFilesResponse](../../models/getversionfilesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |