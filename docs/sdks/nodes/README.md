# Nodes

## Overview

### Available Operations

* [count](#count) - Get a count of Worker, Edge, or Outpost Nodes
* [list](#list) - Get detailed metadata for Worker, Edge, or Outpost Nodes
* [get](#get) - Get detailed metadata for a Worker, Edge, or Outpost Node
* [restart](#restart) - Restart Worker, Edge, or Outpost Nodes

## count

Get a count of all Worker, Edge, or Outpost Nodes for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProductsSummaryWorkersByProduct" method="get" path="/products/{product}/summary/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.count(product=models.ProductsCore.EDGE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `product`                                                                         | [models.ProductsCore](../../models/productscore.md)                               | :heavy_check_mark:                                                                | Name of the Cribl product to get the count of Worker, Edge, or Outpost Nodes for. |
| `filter_exp`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Filter expression to evaluate against Nodes for inclusion in the response.        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CountedNumber](../../models/countednumber.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get detailed metadata for Worker, Edge, or Outpost Nodes for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProductsWorkersByProduct" method="get" path="/products/{product}/workers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.list(product=models.ProductsCore.STREAM)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                          | [models.ProductsCore](../../models/productscore.md)                                                                                                | :heavy_check_mark:                                                                                                                                 | Name of the Cribl product to get Worker, Edge, or Outpost Nodes for.                                                                               |
| `filter_exp`                                                                                                                                       | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Filter expression to evaluate against Nodes for inclusion in the response.                                                                         |
| `sort_exp`                                                                                                                                         | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Sorting expression to evaluate against Nodes to specify the sort order for the response.                                                           |
| `filter_`                                                                                                                                          | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | JSON-stringified filter object to evaluate against Nodes for inclusion in the response.                                                            |
| `sort`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | JSON-stringified sorting object to evaluate against Nodes to specify the sort order for the response.                                              |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of Nodes to return in the response for this request. Use with <code>offset</code> to paginate the response into manageable batches. |
| `offset`                                                                                                                                           | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Starting point from which to retrieve results for this request. Use with <code>limit</code> to paginate the response into manageable batches.      |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.GetProductsWorkersByProductResponse](../../models/getproductsworkersbyproductresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get detailed metadata for the specified Worker, Edge, or Outpost Node for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="getProductsWorkersByProductAndId" method="get" path="/products/{product}/workers/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.get(product=models.ProductsCore.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../../models/productscore.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product that contains the Node.                   |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Node to get the metadata for.            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedMasterWorkerEntry](../../models/countedmasterworkerentry.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## restart

Restart all Worker, Edge, or Outpost Nodes for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateProductsWorkersRestartByProduct" method="patch" path="/products/{product}/workers/restart" example="RestartWorkersExamplesRestartWorkers" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.nodes.restart(product=models.ProductsCore.EDGE, guids=[
        "guid-12345678-abcd-1234-abcd-123456789abc",
        "guid-87654321-dcba-4321-dcba-cba987654321",
        "guid-11111111-2222-3333-4444-555555555555",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `product`                                                                           | [models.ProductsCore](../../models/productscore.md)                                 | :heavy_check_mark:                                                                  | Name of the Cribl product whose Worker, Edge, or Outpost Nodes you want to restart. |
| `guids`                                                                             | List[*str*]                                                                         | :heavy_check_mark:                                                                  | GUIDs of the Worker or Edge Nodes to restart.                                       |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CountedRestartResponse](../../models/countedrestartresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |