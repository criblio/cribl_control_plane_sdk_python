# DeleteProductsGroupsByProductAndIDRequest


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `product`                                                                               | [models.ProductsCore](../models/productscore.md)                                        | :heavy_check_mark:                                                                      | Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The <code>id</code> of the Worker Group, Outpost Group, or Edge Fleet to delete.        |