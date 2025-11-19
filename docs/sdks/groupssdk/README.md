# GroupsSDK
(*groups*)

## Overview

Actions related to Groups

### Available Operations

* [list](#list) - List all Worker Groups or Edge Fleets for the specified Cribl product
* [create](#create) - Create a Worker Group or Edge Fleet for the specified Cribl product
* [get](#get) - Get a Worker Group or Edge Fleet
* [update](#update) - Update a Worker Group or Edge Fleet
* [delete](#delete) - Delete a Worker Group or Edge Fleet
* [deploy](#deploy) - Deploy commits to a Worker Group or Edge Fleet

## list

Get a list of all Worker Groups or Edge Fleets for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="listConfigGroupByProduct" method="get" path="/products/{product}/groups" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.list(product=models.ProductsCore.EDGE, fields="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                                        | [models.ProductsCore](../../models/productscore.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                               | Name of the Cribl product to get the Worker Groups or Edge Fleets for.                                                                                                           |
| `fields`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | Comma-separated list of additional properties to include in the response. Available values are <code>git.commit</code>, <code>git.localChanges</code>, and <code>git.log</code>. |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Worker Group or Edge Fleet for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="createConfigGroupByProduct" method="post" path="/products/{product}/groups" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.create(product=models.ProductsCore.EDGE, id="goatCloudIanWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "us-west-2",
    }, deploying_worker_count=5631.58, description="ack resort boohoo", estimated_ingest_rate=models.GroupCreateRequestEstimatedIngestRate.RATE24_MB_PER_SEC, git={
        "commit": "<value>",
        "local_changes": 2413.01,
        "log": [
            {
                "author_email": "<value>",
                "author_name": "<value>",
                "date_": "2024-04-03",
                "hash": "<value>",
                "message": "<value>",
                "short": "<value>",
            },
        ],
    }, incompatible_worker_count=7174.43, inherits="<value>", is_fleet=False, is_search=False, lookup_deployments=[
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
    ], max_worker_age="<value>", name="goatCloudIanWg", on_prem=False, provisioned=True, source_group_id="<id>", streamtags=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], tags="<value>", type_=models.GroupCreateRequestType.LAKE_ACCESS, upgrade_version="<value>", worker_count=4980.41, worker_remote_access=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                 | [models.ProductsCore](../../models/productscore.md)                                                                                                       | :heavy_check_mark:                                                                                                                                        | required Name of the Cribl product to add the Worker Group or Edge Fleet to.                                                                              |
| `id`                                                                                                                                                      | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |
| `cloud`                                                                                                                                                   | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md)                                                                                     | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `deploying_worker_count`                                                                                                                                  | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `description`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `estimated_ingest_rate`                                                                                                                                   | [Optional[models.GroupCreateRequestEstimatedIngestRate]](../../models/groupcreaterequestestimatedingestrate.md)                                           | :heavy_minus_sign:                                                                                                                                        | Maximum expected volume of data ingested by the @{group}. (This setting is available only on @{group}s consisting of Cribl-managed Cribl.Cloud @{node}s.) |
| `git`                                                                                                                                                     | [Optional[models.GroupCreateRequestGit]](../../models/groupcreaterequestgit.md)                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `incompatible_worker_count`                                                                                                                               | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `inherits`                                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `is_fleet`                                                                                                                                                | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `is_search`                                                                                                                                               | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `lookup_deployments`                                                                                                                                      | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)]                                                                                     | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `max_worker_age`                                                                                                                                          | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `name`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `on_prem`                                                                                                                                                 | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `provisioned`                                                                                                                                             | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `source_group_id`                                                                                                                                         | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `streamtags`                                                                                                                                              | List[*str*]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `tags`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `type`                                                                                                                                                    | [Optional[models.GroupCreateRequestType]](../../models/groupcreaterequesttype.md)                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `upgrade_version`                                                                                                                                         | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `worker_count`                                                                                                                                            | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `worker_remote_access`                                                                                                                                    | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConfigGroupByProductAndId" method="get" path="/products/{product}/groups/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.get(product=models.ProductsCore.EDGE, id="<id>", fields="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                                        | [models.ProductsCore](../../models/productscore.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                               | Name of the Cribl product to get the Worker Groups or Edge Fleets for.                                                                                                           |
| `id`                                                                                                                                                                             | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The <code>id</code> of the Worker Group or Edge Fleet to get.                                                                                                                    |
| `fields`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | Comma-separated list of additional properties to include in the response. Available values are <code>git.commit</code>, <code>git.localChanges</code>, and <code>git.log</code>. |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateConfigGroupByProductAndId" method="patch" path="/products/{product}/groups/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.update(product=models.ProductsCore.STREAM, id_param="<value>", id="goatCloudIanWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "us-west-2",
    }, config_version="<value>", deploying_worker_count=7786.61, description="Scaled Worker Group with estimated ingest rate of 4096 (48 MB/s, 21 Worker Processes) for increased capacity", estimated_ingest_rate=models.ConfigGroupEstimatedIngestRate.RATE48_MB_PER_SEC, git={
        "commit": "<value>",
        "local_changes": 776.15,
        "log": [
            {
                "author_email": "<value>",
                "author_name": "<value>",
                "date_": "2024-09-29",
                "hash": "<value>",
                "message": "<value>",
                "short": "<value>",
            },
        ],
    }, incompatible_worker_count=2874.65, inherits="<value>", is_fleet=False, is_search=False, lookup_deployments=[
        {
            "context": "<value>",
            "lookups": [],
        },
    ], max_worker_age="<value>", name="goatCloudIanWg", on_prem=False, provisioned=True, streamtags=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], tags="<value>", type_=models.ConfigGroupType.LAKE_ACCESS, upgrade_version="<value>", worker_count=835.08, worker_remote_access=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                 | [models.ProductsCore](../../models/productscore.md)                                                                                                       | :heavy_check_mark:                                                                                                                                        | Name of the Cribl product to get the Worker Groups or Edge Fleets for.                                                                                    |
| `id_param`                                                                                                                                                | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The <code>id</code> of the Worker Group or Edge Fleet to update.                                                                                          |
| `id`                                                                                                                                                      | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |
| `cloud`                                                                                                                                                   | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md)                                                                                     | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `config_version`                                                                                                                                          | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `deploying_worker_count`                                                                                                                                  | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `description`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `estimated_ingest_rate`                                                                                                                                   | [Optional[models.ConfigGroupEstimatedIngestRate]](../../models/configgroupestimatedingestrate.md)                                                         | :heavy_minus_sign:                                                                                                                                        | Maximum expected volume of data ingested by the @{group}. (This setting is available only on @{group}s consisting of Cribl-managed Cribl.Cloud @{node}s.) |
| `git`                                                                                                                                                     | [Optional[models.ConfigGroupGit]](../../models/configgroupgit.md)                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `incompatible_worker_count`                                                                                                                               | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `inherits`                                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `is_fleet`                                                                                                                                                | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `is_search`                                                                                                                                               | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `lookup_deployments`                                                                                                                                      | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)]                                                                                     | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `max_worker_age`                                                                                                                                          | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `name`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `on_prem`                                                                                                                                                 | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `provisioned`                                                                                                                                             | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `streamtags`                                                                                                                                              | List[*str*]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `tags`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `type`                                                                                                                                                    | [Optional[models.ConfigGroupType]](../../models/configgrouptype.md)                                                                                       | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `upgrade_version`                                                                                                                                         | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `worker_count`                                                                                                                                            | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `worker_remote_access`                                                                                                                                    | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConfigGroupByProductAndId" method="delete" path="/products/{product}/groups/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.delete(product=models.ProductsCore.EDGE, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `product`                                                              | [models.ProductsCore](../../models/productscore.md)                    | :heavy_check_mark:                                                     | Name of the Cribl product to get the Worker Groups or Edge Fleets for. |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Worker Group or Edge Fleet to delete.       |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## deploy

Deploy commits to the specified Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateConfigGroupDeployByProductAndId" method="patch" path="/products/{product}/groups/{id}/deploy" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.deploy(product=models.ProductsCore.STREAM, id="<id>", version="<value>", lookups=[
        {
            "context": "<value>",
            "lookups": [],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `product`                                                                           | [models.ProductsCore](../../models/productscore.md)                                 | :heavy_check_mark:                                                                  | Name of the Cribl product to get the Worker Groups or Edge Fleets for.              |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The <code>id</code> of the target Worker Group or Edge Fleet for commit deployment. |
| `version`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `lookups`                                                                           | List[[models.DeployRequestLookups](../../models/deployrequestlookups.md)]           | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |