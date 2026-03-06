# UpdateProductsWorkersRestartByProductRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `product`                                                                 | [models.ProductsBase](../models/productsbase.md)                          | :heavy_check_mark:                                                        | Name of the Cribl product whose Worker or Edge Nodes you want to restart. |
| `restart_request`                                                         | [models.RestartRequest](../models/restartrequest.md)                      | :heavy_check_mark:                                                        | RestartRequest object                                                     |