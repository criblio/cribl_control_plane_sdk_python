# System.Previews

## Overview

### Available Operations

* [create](#create) - Send sample events through a Pipeline and review results

## create

Send sample events through the specified Pipeline.The response contains an array of objects, each showing the transformations,additions, and removals for an event after it passes through the pipeline.Useful for testing Pipeline logic with sample data before deploying changes.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPreview" method="post" path="/preview" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.previews.create(mode=models.PreviewDataParamsMode.PIPE, pipeline_id="<id>", sample_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `mode`                                                                | [models.PreviewDataParamsMode](../../models/previewdataparamsmode.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `pipeline_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `sample_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `cpu_profile`                                                         | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `dropped`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `enhance_metrics_output`                                              | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `events`                                                              | List[Dict[str, *Any*]]                                                | :heavy_minus_sign:                                                    | N/A                                                                   |
| `input_id`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `level`                                                               | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `memory`                                                              | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `sample_pipeline_id`                                                  | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `timeout`                                                             | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.PreviewResponse](../../models/previewresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |