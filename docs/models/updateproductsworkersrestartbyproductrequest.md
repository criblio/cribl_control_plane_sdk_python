# UpdateProductsWorkersRestartByProductRequest


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `product`                                                                           | [models.ProductsCore](../models/productscore.md)                                    | :heavy_check_mark:                                                                  | Name of the Cribl product whose Worker, Edge, or Outpost Nodes you want to restart. |
| `restart_request`                                                                   | [models.RestartRequest](../models/restartrequest.md)                                | :heavy_check_mark:                                                                  | RestartRequest object.                                                              |