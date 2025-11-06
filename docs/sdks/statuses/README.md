# Statuses
(*versions.statuses*)

## Overview

### Available Operations

* [get](#get) - Get the status of the current working tree

## get

Get the status of the current working tree of the Git repository used for Cribl configuration. The response includes details about modified, staged, untracked, and conflicted files, as well as branch and remote tracking information.

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

    res = ccp_client.versions.statuses.get(group_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `group_id`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The <code>id</code> of the Worker Group or Edge Fleet to get the status for. |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.CountedListGitStatusResult](../../models/countedlistgitstatusresult.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |