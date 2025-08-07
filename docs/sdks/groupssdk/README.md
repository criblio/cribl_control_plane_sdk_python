# GroupsSDK
(*groups*)

## Overview

Actions related to Groups

### Available Operations

* [get_config_version](#get_config_version) - Retrieve the configuration version for a Worker Group or Edge Fleet
* [create_by_product](#create_by_product) - Create a Worker Group or Edge Fleet for the specified Cribl product
* [get_by_product](#get_by_product) - List all Worker Groups or Edge Fleets for the specified Cribl product
* [delete](#delete) - Delete a Worker Group or Edge Fleet
* [get](#get) - Retrieve a Worker Group or Edge Fleet
* [update](#update) - Update a Worker Group or Edge Fleet
* [deploy_commits](#deploy_commits) - Deploy commits to a Worker Group or Edge Fleet
* [get_team_access_control_list_by_product](#get_team_access_control_list_by_product) - Retrieve the Access Control List (ACL) for teams with permissions on a Worker Group or Edge Fleet for the specified Cribl product
* [get_access_control_list](#get_access_control_list) - Retrieve the Access Control List (ACL) for a Worker Group or Edge Fleet

## get_config_version

Get effective bundle version for given Group

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

    res = ccp_client.groups.get_config_version(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group ID                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGroupsConfigVersionByIDResponse](../../models/getgroupsconfigversionbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_by_product

Create a Fleet or Worker Group

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

    res = ccp_client.groups.create_by_product(product=models.CreateProductsGroupsByProductProduct.STREAM, config_version="<value>", id="<id>", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "<value>",
    }, deploying_worker_count=1848.32, description="director um why forgery apud once er though off", estimated_ingest_rate=6663.53, git={
        "commit": "<value>",
        "local_changes": 2079.21,
        "log": [
            {
                "author_email": "<value>",
                "author_name": "<value>",
                "date_": "2024-08-24",
                "hash": "<value>",
                "message": "<value>",
                "short": "<value>",
            },
        ],
    }, incompatible_worker_count=5487.26, inherits="<value>", is_fleet=False, is_search=False, lookup_deployments=[
        {
            "context": "<value>",
            "lookups": [
                {
                    "deployed_version": "<value>",
                    "file": "<value>",
                    "version": "<value>",
                },
            ],
        },
    ], max_worker_age="<value>", name="<value>", on_prem=True, provisioned=True, streamtags=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], tags="<value>", type_=models.ConfigGroupType.LAKE_ACCESS, upgrade_version="<value>", worker_count=851.73, worker_remote_access=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `product`                                                                                           | [models.CreateProductsGroupsByProductProduct](../../models/createproductsgroupsbyproductproduct.md) | :heavy_check_mark:                                                                                  | Cribl Product                                                                                       |
| `config_version`                                                                                    | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `id`                                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `cloud`                                                                                             | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md)                               | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `deploying_worker_count`                                                                            | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `description`                                                                                       | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `estimated_ingest_rate`                                                                             | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `git`                                                                                               | [Optional[models.Git]](../../models/git.md)                                                         | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `incompatible_worker_count`                                                                         | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `inherits`                                                                                          | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `is_fleet`                                                                                          | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `is_search`                                                                                         | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `lookup_deployments`                                                                                | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)]                               | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `max_worker_age`                                                                                    | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `name`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `on_prem`                                                                                           | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `provisioned`                                                                                       | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `streamtags`                                                                                        | List[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `tags`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `type`                                                                                              | [Optional[models.ConfigGroupType]](../../models/configgrouptype.md)                                 | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `upgrade_version`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `worker_count`                                                                                      | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `worker_remote_access`                                                                              | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.CreateProductsGroupsByProductResponse](../../models/createproductsgroupsbyproductresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_by_product

Get a list of ConfigGroup objects

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

    res = ccp_client.groups.get_by_product(product=models.GetProductsGroupsByProductProduct.STREAM, fields="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `product`                                                                                     | [models.GetProductsGroupsByProductProduct](../../models/getproductsgroupsbyproductproduct.md) | :heavy_check_mark:                                                                            | Cribl Product                                                                                 |
| `fields`                                                                                      | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | fields to add to results: git.commit, git.localChanges, git.log                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.GetProductsGroupsByProductResponse](../../models/getproductsgroupsbyproductresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete a Fleet or Worker Group

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

    res = ccp_client.groups.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group ID                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteGroupsByIDResponse](../../models/deletegroupsbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get a specific ConfigGroup object

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

    res = ccp_client.groups.get(id="<id>", fields="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Group id                                                            |
| `fields`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | fields to add to results: git.commit, git.localChanges, git.log     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGroupsByIDResponse](../../models/getgroupsbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update a Fleet or Worker Group

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

    res = ccp_client.groups.update(id_param="<value>", config_version="<value>", id="<id>", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "<value>",
    }, deploying_worker_count=19.89, description="jaywalk wrathful truly indeed definitive reflecting almost massive", estimated_ingest_rate=7133.74, git={
        "commit": "<value>",
        "local_changes": 370.43,
        "log": [
            {
                "author_email": "<value>",
                "author_name": "<value>",
                "date_": "2024-08-29",
                "hash": "<value>",
                "message": "<value>",
                "short": "<value>",
            },
        ],
    }, incompatible_worker_count=7081.95, inherits="<value>", is_fleet=True, is_search=True, lookup_deployments=[
        {
            "context": "<value>",
            "lookups": [
                {
                    "deployed_version": "<value>",
                    "file": "<value>",
                    "version": "<value>",
                },
            ],
        },
    ], max_worker_age="<value>", name="<value>", on_prem=True, provisioned=True, streamtags=[
        "<value 1>",
    ], tags="<value>", type_=models.ConfigGroupType.LAKE_ACCESS, upgrade_version="<value>", worker_count=9020.63, worker_remote_access=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id_param`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | Group ID                                                              |
| `config_version`                                                      | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `cloud`                                                               | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `deploying_worker_count`                                              | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `description`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `estimated_ingest_rate`                                               | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `git`                                                                 | [Optional[models.Git]](../../models/git.md)                           | :heavy_minus_sign:                                                    | N/A                                                                   |
| `incompatible_worker_count`                                           | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `inherits`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `is_fleet`                                                            | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `is_search`                                                           | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `lookup_deployments`                                                  | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)] | :heavy_minus_sign:                                                    | N/A                                                                   |
| `max_worker_age`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `name`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `on_prem`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `provisioned`                                                         | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `streamtags`                                                          | List[*str*]                                                           | :heavy_minus_sign:                                                    | N/A                                                                   |
| `tags`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `type`                                                                | [Optional[models.ConfigGroupType]](../../models/configgrouptype.md)   | :heavy_minus_sign:                                                    | N/A                                                                   |
| `upgrade_version`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `worker_count`                                                        | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |
| `worker_remote_access`                                                | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UpdateGroupsByIDResponse](../../models/updategroupsbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## deploy_commits

Deploy commits for a Fleet or Worker Group

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

    res = ccp_client.groups.deploy_commits(id="<id>", version="<value>", lookups=[
        {
            "context": "<value>",
            "lookups": [
                {
                    "file": "<value>",
                    "version": "<value>",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | Group ID                                                                  |
| `version`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `lookups`                                                                 | List[[models.DeployRequestLookups](../../models/deployrequestlookups.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UpdateGroupsDeployByIDResponse](../../models/updategroupsdeploybyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_team_access_control_list_by_product

ACL of team with permissions for resources in this Group

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

    res = ccp_client.groups.get_team_access_control_list_by_product(product=models.GetProductsGroupsACLTeamsByProductAndIDProduct.STREAM, id="<id>", type_=models.GetProductsGroupsACLTeamsByProductAndIDType.DATASETS)

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

## get_access_control_list

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

    res = ccp_client.groups.get_access_control_list(id="<id>", type_=models.GetGroupsACLByIDType.INSIGHTS)

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