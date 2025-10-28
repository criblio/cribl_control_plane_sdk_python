# CreateConfigGroupByProductRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../models/productscore.md)                    | :heavy_check_mark:                                                  | Name of the Cribl product to add the Worker Group or Edge Fleet to. |
| `group_create_request`                                              | [models.GroupCreateRequest](../models/groupcreaterequest.md)        | :heavy_check_mark:                                                  | GroupCreateRequest object                                           |