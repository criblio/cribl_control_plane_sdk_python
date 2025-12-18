# Groups.Acl

## Overview

### Available Operations

* [get](#get) - Get the Access Control List for a Worker Group or Edge Fleet

## get

Get the Access Control List (ACL) for the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConfigGroupAclByProductAndId" method="get" path="/products/{product}/groups/{id}/acl" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.acl.get(product=models.ProductsCore.EDGE, id="<id>", type_=models.RbacResource.MACROS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `product`                                                                             | [models.ProductsCore](../../models/productscore.md)                                   | :heavy_check_mark:                                                                    | Name of the Cribl product to get the Worker Groups or Edge Fleets for.                |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The <code>id</code> of the Worker Group or Edge Fleet to get the ACL for.             |
| `type`                                                                                | [Optional[models.RbacResource]](../../models/rbacresource.md)                         | :heavy_minus_sign:                                                                    | Filter for limiting the response to ACL entries for the specified RBAC resource type. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CountedUserAccessControlList](../../models/counteduseraccesscontrollist.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |