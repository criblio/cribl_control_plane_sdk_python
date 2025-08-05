# Versioning
(*versioning*)

## Overview

Actions related to Versioning

### Available Operations

* [get_version_branch](#get_version_branch) - get the list of branches
* [create_version_commit](#create_version_commit) - create a new commit containing the current configs the given log message describing the changes.
* [get_version_count](#get_version_count) - get the count of files of changed
* [get_version_current_branch](#get_version_current_branch) - returns git branch that the config is checked out to, if any
* [get_version_diff](#get_version_diff) - get the textual diff for given commit
* [get_version_files](#get_version_files) - get the files changed
* [get_version_info](#get_version_info) - Get info about versioning availability
* [create_version_push](#create_version_push) - push the current configs to the remote repository.
* [create_version_revert](#create_version_revert) - revert a commit
* [get_version_show](#get_version_show) - get the log message and textual diff for given commit
* [get_version_status](#get_version_status) - get the the working tree status
* [create_version_sync](#create_version_sync) - syncs with remote repo via POST requests
* [create_version_undo](#create_version_undo) - undo the last commit

## get_version_branch

get the list of branches

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionBranch" method="get" path="/version/branch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versioning.get_version_branch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionBranchResponse](../../models/getversionbranchresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_version_commit

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

    res = ccp_client.versioning.create_version_commit(message="<value>", effective=False, files=[
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

## get_version_count

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

    res = ccp_client.versioning.get_version_count(group="<value>", id="<id>")

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

## get_version_current_branch

returns git branch that the config is checked out to, if any

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionCurrentBranch" method="get" path="/version/current-branch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versioning.get_version_current_branch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionCurrentBranchResponse](../../models/getversioncurrentbranchresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_version_diff

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

    res = ccp_client.versioning.get_version_diff(commit="<value>", group="<value>", filename="example.file", diff_line_limit=6362)

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

## get_version_files

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

    res = ccp_client.versioning.get_version_files(group="<value>", id="<id>")

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

## get_version_info

Get info about versioning availability

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionInfo" method="get" path="/version/info" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versioning.get_version_info()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionInfoResponse](../../models/getversioninforesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_version_push

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

    res = ccp_client.versioning.create_version_push()

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

## create_version_revert

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

    res = ccp_client.versioning.create_version_revert(commit="<value>", message="<value>", group="<value>", force=False)

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

## get_version_show

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

    res = ccp_client.versioning.get_version_show(commit="<value>", group="<value>", filename="example.file", diff_line_limit=7771.94)

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

## get_version_status

get the the working tree status

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionStatus" method="get" path="/version/status" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versioning.get_version_status(group="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Group ID                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVersionStatusResponse](../../models/getversionstatusresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_version_sync

syncs with remote repo via POST requests

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionSync" method="post" path="/version/sync" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versioning.create_version_sync()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVersionSyncResponse](../../models/createversionsyncresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_version_undo

undo the last commit

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

    res = ccp_client.versioning.create_version_undo(group="<value>")

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