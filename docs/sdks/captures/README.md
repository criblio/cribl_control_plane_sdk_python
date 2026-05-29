# System.Captures

## Overview

### Available Operations

* [create](#create) - Capture live data

## create

Initiate a live data capture from Cribl Workers. Returns a stream of captured events in NDJSON format that match the parameters specified in the request body.

### Example Usage: CaptureExamplesComplexFilter

<!-- UsageSnippet language="python" operationID="createSystemCapture" method="post" path="/system/capture" example="CaptureExamplesComplexFilter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.captures.create(duration=15, filter_="__inputId.startsWith(\"http:\") && status >= 400 && status < 500", level=models.CaptureLevel.BEFORE_ROUTES, max_events=500)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```
### Example Usage: CaptureExamplesCompoundAndExpression

<!-- UsageSnippet language="python" operationID="createSystemCapture" method="post" path="/system/capture" example="CaptureExamplesCompoundAndExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.captures.create(duration=5, filter_="sourcetype===\"pan:traffic\" && src_zone===\"trusted\"", level=models.CaptureLevel.BEFORE_PRE_PROCESSING_PIPELINE, max_events=100)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```
### Example Usage: CaptureExamplesNestedFieldAccess

<!-- UsageSnippet language="python" operationID="createSystemCapture" method="post" path="/system/capture" example="CaptureExamplesNestedFieldAccess" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.captures.create(duration=5, filter_="sourcetype===\"pan:traffic\" && dest_geoip.country.iso_code === \"US\"", level=models.CaptureLevel.BEFORE_PRE_PROCESSING_PIPELINE, max_events=100)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```
### Example Usage: CaptureExamplesSimpleExpression

<!-- UsageSnippet language="python" operationID="createSystemCapture" method="post" path="/system/capture" example="CaptureExamplesSimpleExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.captures.create(duration=5, filter_="sourcetype===\"pan:traffic\"", level=models.CaptureLevel.BEFORE_PRE_PROCESSING_PIPELINE, max_events=100)

    with res as jsonl_stream:
        for event in jsonl_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `duration`                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | Amount of time to keep capture open, in seconds. If not provided, the default is 5 seconds.                                                                                                                                          |
| `filter_`                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | JavaScript expression evaluated against each event to determine whether an event is included in the capture output. Expressions can reference any event field and use logical operators. If not provided, all events are captured.   |
| `level`                                                                                                                                                                                                                              | [Optional[models.CaptureLevel]](../../models/capturelevel.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                   | Stage at which events are captured. <br><code>0</code> == Before pre-processing Pipeline <br><code>1</code> == Before the Routes <br><code>2</code> == Before post-processing Pipeline <br><code>3</code> == Before the Destination. |
| `max_events`                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | Maximum number of events to capture. If not provided, the default is 100.                                                                                                                                                            |
| `step_duration`                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | How long to wait before increasing the capture sample size. Specify <code>1</code> second or longer. If not provided, the default is 5 seconds.                                                                                      |
| `worker_id`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | Unique ID of the Worker.                                                                                                                                                                                                             |
| `worker_threshold`                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | Maximum number of Workers that can capture initially. A value of <code>0</code> means unlimited (all available Workers can capture). If not provided, the default is 50.                                                             |
| `retries`                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                  |

### Response

**[Union[jsonl.JsonLStream[Dict[str, Any]], jsonl.JsonLStreamAsync[Dict[str, Any]]]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |