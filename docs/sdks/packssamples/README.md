# Packs.Destinations.Samples

## Overview

### Available Operations

* [get](#get) - Get sample event data for a Destination within a Pack
* [create](#create) - Send sample event data to a Destination within a Pack

## get

Get sample event data for the specified Destination to validate the configuration or test connectivity within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputSystemSamplesByPackAndId" method="get" path="/p/{pack}/system/outputs/{id}/samples" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.samples.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Destination to get sample event data for. |
| `pack`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Pack to get.                              |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.CountedOutputSamplesResponse](../../models/countedoutputsamplesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Send sample event data to the specified Destination to validate the configuration or test connectivity within the specified Pack.

### Example Usage: OutputTestExamplesMultipleEvents

<!-- UsageSnippet language="python" operationID="createOutputSystemTestByPackAndId" method="post" path="/p/{pack}/system/outputs/{id}/test" example="OutputTestExamplesMultipleEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.samples.create(id="<id>", pack="<value>", events=[
        {
            "_raw": "Test event 1",
            "source": "test",
            "sourcetype": "manual",
        },
        {
            "_raw": "Test event 2",
            "source": "test",
            "sourcetype": "manual",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: OutputTestExamplesSingleEvent

<!-- UsageSnippet language="python" operationID="createOutputSystemTestByPackAndId" method="post" path="/p/{pack}/system/outputs/{id}/test" example="OutputTestExamplesSingleEvent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.samples.create(id="<id>", pack="<value>", events=[
        {
            "_raw": "This is a test event",
            "source": "test",
            "sourcetype": "manual",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Destination to send sample event data to. |
| `pack`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Pack to create.                           |
| `events`                                                             | List[Dict[str, *Any*]]                                               | :heavy_check_mark:                                                   | Array of event objects to send to the Destination for testing.       |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.CountedOutputTestResponse](../../models/countedoutputtestresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |