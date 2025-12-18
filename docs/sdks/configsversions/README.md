# Groups.Configs.Versions

## Overview

### Available Operations

* [get](#get) - Get the configuration version for a Worker Group or Edge Fleet

## get

Get the configuration version for the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConfigGroupConfigVersionByProductAndId" method="get" path="/products/{product}/groups/{id}/configVersion" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.configs.versions.get(product=models.ProductsCore.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `product`                                                                                   | [models.ProductsCore](../../models/productscore.md)                                         | :heavy_check_mark:                                                                          | Name of the Cribl product to get the Worker Groups or Edge Fleets for.                      |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | The <code>id</code> of the Worker Group or Edge Fleet to get the configuration version for. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.CountedString](../../models/countedstring.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |