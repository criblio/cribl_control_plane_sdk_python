# ACL
(*groups.acl*)

## Overview

### Available Operations

* [get](#get) - Retrieve the Access Control List (ACL) for a Worker Group or Edge Fleet

## get

ACL of members with permissions for resources in this Group

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.acl.get(id="<id>", type_=models.GetGroupsACLByIDType.INSIGHTS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                                                                          | *str*                                                                         | :heavy_check_mark:                                                            | Group id                                                                      |
| `type`                                                                        | [Optional[models.GetGroupsACLByIDType]](../../models/getgroupsaclbyidtype.md) | :heavy_minus_sign:                                                            | resource type by which to filter access levels                                |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.GetGroupsACLByIDResponse](../../models/getgroupsaclbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |