# System.Settings

## Overview

### Available Operations

* [restart](#restart) - Restart the Cribl server

## restart

Restart the Cribl server.<br/><br/>This operation requires <code>system.restart</code> to be set to <code>api</code> in <code>cribl.yml</code>. If this setting is not configured, the request returns a <code>403</code> error.<br/><br/>Restarting the server causes a brief period of downtime while the process stops and restarts. All in-flight events are drained before the process exits. Use <code>POST /system/settings/reload</code> to apply configuration changes without a full restart.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSystemSettingsRestart" method="post" path="/system/settings/restart" example="RestartSystemExamplesDefault" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.restart()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSystemRestartResponse](../../models/countedsystemrestartresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |