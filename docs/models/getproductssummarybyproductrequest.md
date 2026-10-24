# GetProductsSummaryByProductRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `product`                                         | [models.ProductsBase](../models/productsbase.md)  | :heavy_check_mark:                                | Name of the Cribl product to get the summary for. |
| `offset`                                          | *Optional[int]*                                   | :heavy_minus_sign:                                | Pagination offset                                 |
| `limit`                                           | *Optional[int]*                                   | :heavy_minus_sign:                                | Maximum number of items to return                 |