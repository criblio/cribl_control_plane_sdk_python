# Commits
(*versions.commits*)

## Overview

### Available Operations

* [create](#create) - Create a new commit for pending changes to the Cribl configuration
* [diff](#diff) - Get the diff for a commit
* [list](#list) - List the commit history
* [push](#push) - Push local commits to the remote repository
* [revert](#revert) - Revert a commit in the local repository
* [get](#get) - Get the diff and log message for a commit
* [undo](#undo) - Discard uncommitted (staged) changes

## create

Create a new commit for pending changes to the Cribl configuration. Any merge conflicts indicated in the response must be resolved using Git.</br></br>To commit only a subset of configuration changes, specify the files to include in the commit in the <code>files</code> array.

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

    res = ccp_client.versions.commits.create(message="<value>", group_id="<id>", effective=False, files=[
        "<value 1>",
    ], group="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `message`                                                                         | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `group_id`                                                                        | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The <code>id</code> of the Worker Group or Edge Fleet to create a new commit for. |
| `effective`                                                                       | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | N/A                                                                               |
| `files`                                                                           | List[*str*]                                                                       | :heavy_minus_sign:                                                                | N/A                                                                               |
| `group`                                                                           | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CountedListGitCommitSummary](../../models/countedlistgitcommitsummary.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## diff

Get the diff for a commit. Default is the latest commit (HEAD).

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

    res = ccp_client.versions.commits.diff(commit="<value>", group_id="<id>", filename="example.file", diff_line_limit=6362)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                                                  | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The Git commit hash to get the diff for.                                                                                                  |
| `group_id`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The <code>id</code> of the Worker Group or Edge Fleet to get the diff for.                                                                |
| `filename`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The relative path of the file to get the diff for.                                                                                        |
| `diff_line_limit`                                                                                                                         | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | Number of lines of the diff to return. Default is 1000. Set to <code>0</code> to return the full diff, regardless of the number of lines. |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.CountedListGitDiffResult](../../models/countedlistgitdiffresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

List the commit history.</br></br>Analogous to <code>git log</code> for the Cribl configuration, allowing you to audit and review changes over time.

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersion" method="get" path="/version" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.list(group_id="<id>", count=893.58)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `group_id`                                                                           | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The <code>id</code> of the Worker Group or Edge Fleet to get the commit history for. |
| `count`                                                                              | *Optional[float]*                                                                    | :heavy_minus_sign:                                                                   | Maximum number of commits to return in the response for this request.                |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[models.CountedListGitLogResult](../../models/countedlistgitlogresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## push

Push all local commits from the local repository to the remote repository.

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

**[models.CountedListstring](../../models/countedliststring.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## revert

Revert a commit in the local repository.

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

    res = ccp_client.versions.commits.revert(commit="<value>", group_id="<id>", force=False, message="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                                                                  | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |
| `group_id`                                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The <code>id</code> of the Worker Group or Edge Fleet to revert the commit for. Required in Distributed deployments. Omit in Single-instance deployments. |
| `force`                                                                                                                                                   | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `message`                                                                                                                                                 | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CountedListGitRevertResult](../../models/countedlistgitrevertresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the diff and log message for a commit. Default is the latest commit (HEAD).

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

    res = ccp_client.versions.commits.get(commit="<value>", group_id="<id>", filename="example.file", diff_line_limit=7771.94)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                                                  | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The Git commit hash to retrieve the diff and log message for.                                                                             |
| `group_id`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The <code>id</code> of the Worker Group or Edge Fleet to get the diff and log message for.                                                |
| `filename`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The relative path of the file to get the diff and log message for.                                                                        |
| `diff_line_limit`                                                                                                                         | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | Number of lines of the diff to return. Default is 1000. Set to <code>0</code> to return the full diff, regardless of the number of lines. |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.CountedListGitShowResult](../../models/countedlistgitshowresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## undo

Discard all uncommitted (staged) configuration changes, resetting the working directory to the last committed state. Use only if you are certain that you do not need to preserve your local changes.

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

    res = ccp_client.versions.commits.undo(group_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `group_id`                                                                                | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The <code>id</code> of the Worker Group or Edge Fleet to undo the uncommited changes for. |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.CountedListObject](../../models/countedlistobject.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |