# UpdateConfigGroupDeployByProductAndIDRequest


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `product`                                                                           | [models.ProductsCore](../models/productscore.md)                                    | :heavy_check_mark:                                                                  | Name of the Cribl product to get the Worker Groups or Edge Fleets for.              |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The <code>id</code> of the target Worker Group or Edge Fleet for commit deployment. |
| `deploy_request`                                                                    | [models.DeployRequest](../models/deployrequest.md)                                  | :heavy_check_mark:                                                                  | DeployRequest object                                                                |