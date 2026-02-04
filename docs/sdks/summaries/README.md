# Nodes.Summaries

## Overview

### Available Operations

* [get](#get) - Get a summary of the Distributed deployment for a specific product

## get

Get a summary of the Distributed deployment for a specific Cribl product (Stream or Edge). The response includes counts of Worker Groups or Edge Fleets, Pipelines, Routes, Sources, Destinations, and Worker or Edge Nodes, as well as statistics for the nodes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProductsSummaryByProduct" method="get" path="/products/{product}/summary" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.summaries.get(product=models.ProductsBase.STREAM)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsBase](../../models/productsbase.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to get the summary for.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedDistributedSummary](../../models/counteddistributedsummary.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |