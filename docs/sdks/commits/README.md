# Commits
(*versions.commits*)

## Overview

### Available Operations

* [create](#create) - Create a new commit for pending changes to the Cribl configuration
* [diff](#diff) - Retrieve the diff for a commit
* [push](#push) - Push a commit from the local repository to the remote repository
* [revert](#revert) - Revert a commit in the local repository
* [get](#get) - Retrieve the diff and log message for a commit
* [undo](#undo) - Discard uncommitted (staged) changes

## create

create a new commit containing the current configs the given log message describing the changes.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionCommit" method="post" path="/version/commit" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.create(message="<value>", effective=False, files=[
        "<value 1>",
    ], group="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `message`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `effective`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `files`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVersionCommitResponse](../../models/createversioncommitresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## diff

get the textual diff for given commit

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionDiff" method="get" path="/version/diff" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.diff(commit="<value>", group="<value>", filename="example.file", diff_line_limit=6362)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `commit`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Commit hash (default is HEAD)                                       |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `filename`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filename                                                            |
| `diff_line_limit`                                                   | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Limit maximum lines in the diff                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionDiffResponse](../../models/getversiondiffresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## push

push the current configs to the remote repository.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionPush" method="post" path="/version/push" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.push()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVersionPushResponse](../../models/createversionpushresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## revert

revert a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionRevert" method="post" path="/version/revert" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.revert(commit="<value>", message="<value>", group="<value>", force=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `commit`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `message`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `force`                                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVersionRevertResponse](../../models/createversionrevertresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

get the log message and textual diff for given commit

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionShow" method="get" path="/version/show" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.get(commit="<value>", group="<value>", filename="example.file", diff_line_limit=7771.94)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `commit`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Commit hash (default is HEAD)                                       |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `filename`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filename                                                            |
| `diff_line_limit`                                                   | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Limit maximum lines in the diff                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionShowResponse](../../models/getversionshowresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## undo

Discards all uncommitted (staged) configuration changes, resetting the working directory to the last committed state.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionUndo" method="post" path="/version/undo" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.undo(group="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVersionUndoResponse](../../models/createversionundoresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |