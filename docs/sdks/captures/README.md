# System.Captures

## Overview

### Available Operations

* [create](#create) - Capture live incoming data

## create

Initiate a live data capture from Cribl Workers.Returns a stream of captured events in NDJSON format that match the parameters specified in the request body.

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

    res = ccp_client.system.captures.create(duration=5, filter_="sourcetype===\"pan:traffic\"", level=models.CaptureLevel.BEFORE_PRE_PROCESSING_PIPELINE, max_events=100, step_duration=571732, worker_id="<id>", worker_threshold=609412)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `duration`                                                                                                                                                                                                                          | *float*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                  | Amount of time to keep capture open, in seconds.                                                                                                                                                                                    |
| `filter_`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                  | JavaScript expression evaluated against each event to determine whether an event is included in the capture output. Expressions can reference any event field and use logical operators.                                            |
| `level`                                                                                                                                                                                                                             | [models.CaptureLevel](../../models/capturelevel.md)                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                  | Stage at which events are captured. <br><code>0</code> == Before pre-processing Pipeline <br><code>1</code> == Before the Routes <br><code>2</code> == Before post-processing Pipeline <br><code>3</code> == Before the Destination |
| `max_events`                                                                                                                                                                                                                        | *int*                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                  | Maximum number of events to capture.                                                                                                                                                                                                |
| `step_duration`                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | How long to wait before increasing the capture sample size. Specify <code>1</code> second or longer.                                                                                                                                |
| `worker_id`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Unique ID of the Worker.                                                                                                                                                                                                            |
| `worker_threshold`                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Maximum number of Workers that can capture initially. A value of <code>0</code> means unlimited (all available Workers can capture).                                                                                                |
| `retries`                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                 |

### Response

**[Union[jsonl.JsonLStream[Dict[str, Any]], jsonl.JsonLStreamAsync[Dict[str, Any]]]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |