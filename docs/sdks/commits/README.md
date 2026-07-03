# Versions.Commits

## Overview

### Available Operations

* [list](#list) - List the commit history
* [create](#create) - Create a new commit for pending changes to the Cribl configuration
* [diff](#diff) - Get the diff for a commit
* [push](#push) - Push local commits to the remote repository
* [revert](#revert) - Revert a commit in the local repository
* [get](#get) - Get the diff and log message for a commit
* [undo](#undo) - Discard uncommitted (staged) changes

## list

List the commit history.<br/><br/>Analogous to <code>git log</code> for the Cribl configuration, allowing you to audit and review changes over time.

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersion" method="get" path="/version" example="VersionListResponseExamplesListCommitHistory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `count`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum number of commits to return in the response for this request. |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Pagination offset                                                     |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum number of items to return                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.GetVersionResponse](../../models/getversionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new commit for pending changes to the Cribl configuration. Any merge conflicts indicated in the response must be resolved using Git.<br/><br/>To commit only a subset of configuration changes, specify the files to include in the commit in the <code>files</code> array.

### Example Usage: VersionCommitExamplesCommitAll

<!-- UsageSnippet language="python" operationID="createVersionCommit" method="post" path="/version/commit" example="VersionCommitExamplesCommitAll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.create(message="Updated pipeline configuration for syslog parsing")

    # Handle response
    print(res)

```
### Example Usage: VersionCommitExamplesCommitSpecificFiles

<!-- UsageSnippet language="python" operationID="createVersionCommit" method="post" path="/version/commit" example="VersionCommitExamplesCommitSpecificFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.create(message="Update Route and Pipeline for HTTP Sources", effective=True, files=[
        "groups/default/local/cribl/pipelines/http_input/conf.yml",
        "groups/default/local/cribl/routes.yml",
    ])

    # Handle response
    print(res)

```
### Example Usage: VersionCommitResponseExamplesCommitCreated

<!-- UsageSnippet language="python" operationID="createVersionCommit" method="post" path="/version/commit" example="VersionCommitResponseExamplesCommitCreated" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.create(message="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `message`                                                                                                                        | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | Commit message to use for the new Git commit.                                                                                    |
| `effective`                                                                                                                      | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | If <code>true</code>, apply the commit to the group's effective configuration. Otherwise, <code>false</code>.                    |
| `files`                                                                                                                          | List[*str*]                                                                                                                      | :heavy_minus_sign:                                                                                                               | Array of file paths to include in the commit, relative to the configuration root. If omitted, all pending changes are committed. |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.CountedGitCommitSummary](../../models/countedgitcommitsummary.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## diff

Get the diff for a commit. Default is the latest commit (HEAD).

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionDiff" method="get" path="/version/diff" example="VersionDiffResponseExamplesDiffResult" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.diff()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                                                  | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The Git commit hash to get the diff for.                                                                                                  |
| `filename`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The relative path of the file to get the diff for.                                                                                        |
| `diff_line_limit`                                                                                                                         | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Number of lines of the diff to return. Default is 1000. Set to <code>0</code> to return the full diff, regardless of the number of lines. |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.CountedGitDiffResult](../../models/countedgitdiffresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## push

Push all local commits from the local repository to the remote repository.<br/><br/>Requires at least one local commit that has not been pushed. Returns an error if the remote repository cannot be reached or the push is rejected.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionPush" method="post" path="/version/push" example="VersionPushResponseExamplesPushResult" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
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

**[models.CountedString](../../models/countedstring.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## revert

Revert a commit in the local repository by creating a new commit that undoes the changes introduced by the specified commit.<br/><br/>Use the <code>force</code> field to proceed even when the working directory is not clean.

### Example Usage: VersionRevertExamplesForceRevertWithMessage

<!-- UsageSnippet language="python" operationID="createVersionRevert" method="post" path="/version/revert" example="VersionRevertExamplesForceRevertWithMessage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.revert(commit="a1b2c3d4e5f6", force=True, message="Revert commit due to misconfiguration in Pipeline settings")

    # Handle response
    print(res)

```
### Example Usage: VersionRevertExamplesRevertCommit

<!-- UsageSnippet language="python" operationID="createVersionRevert" method="post" path="/version/revert" example="VersionRevertExamplesRevertCommit" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.revert(commit="a1b2c3d4e5f6")

    # Handle response
    print(res)

```
### Example Usage: VersionRevertResponseExamplesRevertResult

<!-- UsageSnippet language="python" operationID="createVersionRevert" method="post" path="/version/revert" example="VersionRevertResponseExamplesRevertResult" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.revert(commit="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                            | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | SHA-1 hash of the commit to revert.                                                                                 |
| `force`                                                                                                             | *Optional[bool]*                                                                                                    | :heavy_minus_sign:                                                                                                  | If <code>true</code>, force the revert even when the working directory is not clean. Otherwise, <code>false</code>. |
| `message`                                                                                                           | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | Custom message to use for the revert commit. If omitted, a default message is generated.                            |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.CountedGitRevertResult](../../models/countedgitrevertresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the diff and log message for a commit. Default is the latest commit (HEAD).

### Example Usage

<!-- UsageSnippet language="python" operationID="getVersionShow" method="get" path="/version/show" example="VersionShowResponseExamplesShowCommit" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `commit`                                                                                                                                  | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The Git commit hash to retrieve the diff and log message for.                                                                             |
| `filename`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | The relative path of the file to get the diff and log message for.                                                                        |
| `diff_line_limit`                                                                                                                         | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Number of lines of the diff to return. Default is 1000. Set to <code>0</code> to return the full diff, regardless of the number of lines. |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.CountedGitShowResult](../../models/countedgitshowresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## undo

Discard all uncommitted (staged) configuration changes, resetting the working directory to the last committed state. Use only if you are certain that you do not need to preserve your local changes.<br/><br/>When applied globally (no group), triggers a Cribl restart to reload the reverted configuration. Returns <code>false</code> if the working directory is already clean.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVersionUndo" method="post" path="/version/undo" example="VersionUndoResponseExamplesUndoResult" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.versions.commits.undo()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedBoolean](../../models/countedboolean.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |