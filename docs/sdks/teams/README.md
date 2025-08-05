# Teams
(*teams*)

## Overview

Actions related to Teams

### Available Operations

* [get_products_groups_acl_teams_by_product_and_id](#get_products_groups_acl_teams_by_product_and_id) - ACL of team with permissions for resources in this Group

## get_products_groups_acl_teams_by_product_and_id

ACL of team with permissions for resources in this Group

### Example Usage

<!-- UsageSnippet language="python" operationID="getProductsGroupsAclTeamsByProductAndId" method="get" path="/products/{product}/groups/{id}/acl/teams" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.teams.get_products_groups_acl_teams_by_product_and_id(product=models.GetProductsGroupsACLTeamsByProductAndIDProduct.STREAM, id="<id>", type_=models.GetProductsGroupsACLTeamsByProductAndIDType.DATASETS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                   | [models.GetProductsGroupsACLTeamsByProductAndIDProduct](../../models/getproductsgroupsaclteamsbyproductandidproduct.md)     | :heavy_check_mark:                                                                                                          | Cribl Product                                                                                                               |
| `id`                                                                                                                        | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Group ID                                                                                                                    |
| `type`                                                                                                                      | [Optional[models.GetProductsGroupsACLTeamsByProductAndIDType]](../../models/getproductsgroupsaclteamsbyproductandidtype.md) | :heavy_minus_sign:                                                                                                          | resource type by which to filter access levels                                                                              |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.GetProductsGroupsACLTeamsByProductAndIDResponse](../../models/getproductsgroupsaclteamsbyproductandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |