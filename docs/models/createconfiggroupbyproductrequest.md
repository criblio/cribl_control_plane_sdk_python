# CreateConfigGroupByProductRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../models/productscore.md)                    | :heavy_check_mark:                                                  | Name of the Cribl product to add the Worker Group or Edge Fleet to. |
| `config_group`                                                      | [models.ConfigGroup](../models/configgroup.md)                      | :heavy_check_mark:                                                  | ConfigGroup object                                                  |