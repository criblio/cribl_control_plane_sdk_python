# Teams
(*groups.acl.teams*)

## Overview

### Available Operations

* [get](#get) - Retrieve the Access Control List (ACL) for teams with permissions on a Worker Group or Edge Fleet for the specified Cribl product

## get

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

    res = ccp_client.groups.acl.teams.get(product=models.GetProductsGroupsACLTeamsByProductAndIDProduct.STREAM, id="<id>", type_=models.GetProductsGroupsACLTeamsByProductAndIDType.DATASETS)

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