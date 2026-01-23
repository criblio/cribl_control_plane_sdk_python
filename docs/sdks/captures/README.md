# System.Captures

## Overview

### Available Operations

* [get](#get) - Capture live incoming data

## get

Capture live incoming data

### Example Usage

<!-- UsageSnippet language="python" operationID="createSystemCapture" method="post" path="/system/capture" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.captures.get(duration=5, filter_="true", level=models.CaptureLevel.ZERO, max_events=100, step_duration=571732, worker_id="<id>", worker_threshold=609412)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `duration`                                                                             | *float*                                                                                | :heavy_check_mark:                                                                     | Amount of time to keep capture open, in seconds                                        |
| `filter_`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | Filter expression to capture events                                                    |
| `level`                                                                                | [models.CaptureLevel](../../models/capturelevel.md)                                    | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `max_events`                                                                           | *int*                                                                                  | :heavy_check_mark:                                                                     | Maximum number of events to capture                                                    |
| `step_duration`                                                                        | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | How long to wait before increasing the capture sample size. Specify 1 second or longer |
| `worker_id`                                                                            | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Worker ID                                                                              |
| `worker_threshold`                                                                     | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | Limits how many Workers will capture initially. The 0 default means unlimited.         |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[Union[jsonl.JsonLStream[Dict[str, Any]], jsonl.JsonLStreamAsync[Dict[str, Any]]]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |