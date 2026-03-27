# GetProductsSummaryWorkersByProductRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `product`                                                                  | [models.ProductsBase](../models/productsbase.md)                           | :heavy_check_mark:                                                         | Name of the Cribl product to get the count of Worker or Edge Nodes for.    |
| `filter_exp`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter expression to evaluate against Nodes for inclusion in the response. |