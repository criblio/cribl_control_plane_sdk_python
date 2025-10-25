# UpdateAdminProductsMappingsByProductAndIDRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `product`                                                   | [models.ProductsCore](../models/productscore.md)            | :heavy_check_mark:                                          | Name of the Cribl product to update the Mapping Ruleset for |
| `id_param`                                                  | *str*                                                       | :heavy_check_mark:                                          | The <code>id</code> of the Mapping Ruleset to update.       |
| `mapping_ruleset`                                           | [models.MappingRuleset](../models/mappingruleset.md)        | :heavy_check_mark:                                          | MappingRuleset object                                       |