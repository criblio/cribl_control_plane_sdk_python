# Nodes.Summaries

## Overview

### Available Operations

* [get](#get) - Get a summary of the Distributed deployment

## get

Get a summary of the Distributed deployment. The response includes counts of Worker Groups, Edge Fleets, Pipelines, Routes, Sources, Destinations, and Worker and Edge Nodes, as well as statistics for the Worker and Edge Nodes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSummary" method="get" path="/master/summary" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.summaries.get(mode=models.WorkerTypes.WORKER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                                                                                                                           | [Optional[models.WorkerTypes]](../../models/workertypes.md)                                                                      | :heavy_minus_sign:                                                                                                               | Filter for limiting the response by Cribl product: Cribl Stream (<code>worker</code>) or Cribl Edge (<code>managed-edge</code>). |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.CountedDistributedSummary](../../models/counteddistributedsummary.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |