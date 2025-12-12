# Versions.Commits.Files

## Overview

### Available Operations

* [count](#count) - Get a count of files that changed since a commit
* [list](#list) - Get the names and statuses of files that changed since a commit

## count

Get a count of the files that changed since a commit. Default is the latest commit (HEAD).

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

    res = ccp_client.versions.commits.files.count(group_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `group_id`                                                                  | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The <code>id</code> of the Worker Group or Edge Fleet to get the count for. |
| `id`                                                                        | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The Git commit hash to use as the starting point for the count.             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.GetVersionCountResponse](../../models/getversioncountresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get the names and statuses of files that changed since a commit. Default is the latest commit (HEAD).

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

    res = ccp_client.versions.commits.files.list(group_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `group_id`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The <code>id</code> of the Worker Group or Edge Fleet to get file names and status for. |
| `id`                                                                                    | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The Git commit hash to use as the starting point for the request.                       |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.GetVersionFilesResponse](../../models/getversionfilesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |