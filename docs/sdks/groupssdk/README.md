# Groups

## Overview

Actions related to Groups

### Available Operations

* [list](#list) - List all Worker Groups, Outpost Groups, or Edge Fleets for the specified Cribl product
* [create](#create) - Create a Worker Group, Outpost Group, or Edge Fleet for the specified Cribl product
* [get](#get) - Get a Worker Group, Outpost Group, or Edge Fleet
* [update](#update) - Update a Worker Group, Outpost Group, or Edge Fleet
* [delete](#delete) - Delete a Worker Group, Outpost Group, or Edge Fleet
* [deploy](#deploy) - Deploy commits to a Worker Group, Outpost Group, or Edge Fleet

## list

Get a list of all Worker Groups, Outpost Groups, or Edge Fleets for the specified Cribl product.

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
| `product`                                                                                                                                                                        | [models.ProductsCore](../../models/productscore.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                               | Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for.                                                                                          |
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

Create a new Worker Group, Outpost Group, or Edge Fleet for the specified Cribl product.

### Example Usage: CreateGroupExamplesCloneWg

<!-- UsageSnippet language="python" operationID="createConfigGroupByProduct" method="post" path="/products/{product}/groups" example="CreateGroupExamplesCloneWg" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.create(product=models.ProductsCore.EDGE, id="goatOnPremDollyWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "<value>",
    }, deploying_worker_count=2591.38, description="Worker Group cloned from goatOnPremIanWg with identical configuration", estimated_ingest_rate=models.EstimatedIngestRateOptionsConfigGroup.RATE48_MB_PER_SEC, git={
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
    }, incompatible_worker_count=1660.08, inherits="<value>", is_fleet=False, is_search=False, lookup_deployments=[
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
    ], max_worker_age="<value>", name="goatOnPremDollyWg", on_prem=True, provisioned=True, source_group_id="goatOnPremIanWg", streamtags=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], tags="<value>", type_=models.TypeOptionsConfigGroup.LAKE_ACCESS, upgrade_version="<value>", worker_count=5075.63, worker_remote_access=True)

    # Handle response
    print(res)

```
### Example Usage: CreateGroupExamplesCloudWg

<!-- UsageSnippet language="python" operationID="createConfigGroupByProduct" method="post" path="/products/{product}/groups" example="CreateGroupExamplesCloudWg" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.create(product=models.ProductsCore.STREAM, id="goatCloudIanWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "us-west-2",
    }, deploying_worker_count=5631.58, description="ack resort boohoo", estimated_ingest_rate=models.EstimatedIngestRateOptionsConfigGroup.RATE24_MB_PER_SEC, git={
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
    ], tags="<value>", type_=models.TypeOptionsConfigGroup.LAKE_ACCESS, upgrade_version="<value>", worker_count=4980.41, worker_remote_access=True)

    # Handle response
    print(res)

```
### Example Usage: CreateGroupExamplesEdgeFleet

<!-- UsageSnippet language="python" operationID="createConfigGroupByProduct" method="post" path="/products/{product}/groups" example="CreateGroupExamplesEdgeFleet" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.create(product=models.ProductsCore.EDGE, id="goatIanEdgeFleet", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "<value>",
    }, deploying_worker_count=9605.18, description="Create a new Edge Fleet", estimated_ingest_rate=models.EstimatedIngestRateOptionsConfigGroup.RATE48_MB_PER_SEC, git={
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
    }, incompatible_worker_count=9429.96, inherits="<value>", is_fleet=True, is_search=False, lookup_deployments=[
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
    ], max_worker_age="<value>", name="goatIanEdgeFleet", on_prem=True, provisioned=False, source_group_id="<id>", streamtags=[
        "<value 1>",
        "<value 2>",
    ], tags="<value>", type_=models.TypeOptionsConfigGroup.LAKE_ACCESS, upgrade_version="<value>", worker_count=3096.3, worker_remote_access=True)

    # Handle response
    print(res)

```
### Example Usage: CreateGroupExamplesOnPremWg

<!-- UsageSnippet language="python" operationID="createConfigGroupByProduct" method="post" path="/products/{product}/groups" example="CreateGroupExamplesOnPremWg" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.create(product=models.ProductsCore.EDGE, id="goatOnPremIanWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "<value>",
    }, deploying_worker_count=9081.3, description="Worker group in customer-managed deployment", estimated_ingest_rate=models.EstimatedIngestRateOptionsConfigGroup.RATE48_MB_PER_SEC, git={
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
    }, incompatible_worker_count=7060.3, inherits="<value>", is_fleet=False, is_search=False, lookup_deployments=[
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
    ], max_worker_age="<value>", name="goatOnPremIanWg", on_prem=True, provisioned=False, source_group_id="<id>", streamtags=[
        "<value 1>",
    ], tags="<value>", type_=models.TypeOptionsConfigGroup.LAKE_ACCESS, upgrade_version="<value>", worker_count=1230.11, worker_remote_access=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                                                                                             | [models.ProductsCore](../../models/productscore.md)                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                    | Name of the Cribl product to add the Worker Group, Outpost Group, or Edge Fleet to.                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `id`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `cloud`                                                                                                                                                                                                                               | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md)                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `deploying_worker_count`                                                                                                                                                                                                              | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `estimated_ingest_rate`                                                                                                                                                                                                               | [Optional[models.EstimatedIngestRateOptionsConfigGroup]](../../models/estimatedingestrateoptionsconfiggroup.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Estimated ingest rate for Cloud Groups, in GB/sec.                                                                                                                                                                                    | 4096                                                                                                                                                                                                                                  |
| `git`                                                                                                                                                                                                                                 | [Optional[models.GitTypeConfigGroup]](../../models/gittypeconfiggroup.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `incompatible_worker_count`                                                                                                                                                                                                           | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `inherits`                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `is_fleet`                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Indicates whether this is an Edge Fleet. This flag is deprecated — use to identify Edge Fleets.      |                                                                                                                                                                                                                                       |
| `is_search`                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Indicates whether this is an internal Search Group. This flag is deprecated — use to identify Search Groups. |                                                                                                                                                                                                                                       |
| `lookup_deployments`                                                                                                                                                                                                                  | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `max_worker_age`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `name`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `on_prem`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `provisioned`                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `source_group_id`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `streamtags`                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `tags`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `type`                                                                                                                                                                                                                                | [Optional[models.TypeOptionsConfigGroup]](../../models/typeoptionsconfiggroup.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `upgrade_version`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `worker_count`                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `worker_remote_access`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                   |                                                                                                                                                                                                                                       |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Worker Group, Outpost Group, or Edge Fleet.

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
| `product`                                                                                                                                                                        | [models.ProductsCore](../../models/productscore.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                               | Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for.                                                                                          |
| `id`                                                                                                                                                                             | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The <code>id</code> of the Worker Group, Outpost Group, or Edge Fleet to get.                                                                                                    |
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

Update the specified Worker Group, Outpost Group, or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateConfigGroupByProductAndId" method="patch" path="/products/{product}/groups/{id}" example="UpdateGroupExamplesScaleCloudWorkerGroup" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.update(product=models.ProductsCore.EDGE, id_param="<value>", id="goatCloudIanWg", cloud={
        "provider": models.CloudProvider.AWS,
        "region": "us-west-2",
    }, config_version="<value>", deploying_worker_count=7786.61, description="Scaled Worker Group with estimated ingest rate of 4096 (48 MB/s, 21 Worker Processes) for increased capacity", estimated_ingest_rate=models.EstimatedIngestRateOptionsConfigGroup.RATE48_MB_PER_SEC, git={
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
    ], tags="<value>", type_=models.TypeOptionsConfigGroup.LAKE_ACCESS, upgrade_version="<value>", worker_count=835.08, worker_remote_access=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product`                                                                                                                                                                                                                             | [models.ProductsCore](../../models/productscore.md)                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                    | Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for.                                                                                                                                               |                                                                                                                                                                                                                                       |
| `id_param`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | The <code>id</code> of the Worker Group, Outpost Group, or Edge Fleet to update.                                                                                                                                                      |                                                                                                                                                                                                                                       |
| `id`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `cloud`                                                                                                                                                                                                                               | [Optional[models.ConfigGroupCloud]](../../models/configgroupcloud.md)                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `config_version`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `deploying_worker_count`                                                                                                                                                                                                              | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `estimated_ingest_rate`                                                                                                                                                                                                               | [Optional[models.EstimatedIngestRateOptionsConfigGroup]](../../models/estimatedingestrateoptionsconfiggroup.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | Estimated ingest rate for Cloud Groups, in GB/sec.                                                                                                                                                                                    | 4096                                                                                                                                                                                                                                  |
| `git`                                                                                                                                                                                                                                 | [Optional[models.GitTypeConfigGroup]](../../models/gittypeconfiggroup.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `incompatible_worker_count`                                                                                                                                                                                                           | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `inherits`                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `is_fleet`                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Indicates whether this is an Edge Fleet. This flag is deprecated — use to identify Edge Fleets.      |                                                                                                                                                                                                                                       |
| `is_search`                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Indicates whether this is an internal Search Group. This flag is deprecated — use to identify Search Groups. |                                                                                                                                                                                                                                       |
| `lookup_deployments`                                                                                                                                                                                                                  | List[[models.ConfigGroupLookups](../../models/configgrouplookups.md)]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `max_worker_age`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `name`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `on_prem`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `provisioned`                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `streamtags`                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `tags`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `type`                                                                                                                                                                                                                                | [Optional[models.TypeOptionsConfigGroup]](../../models/typeoptionsconfiggroup.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `upgrade_version`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `worker_count`                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `worker_remote_access`                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                   |                                                                                                                                                                                                                                       |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Worker Group, Outpost Group, or Edge Fleet.

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

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `product`                                                                               | [models.ProductsCore](../../models/productscore.md)                                     | :heavy_check_mark:                                                                      | Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The <code>id</code> of the Worker Group, Outpost Group, or Edge Fleet to delete.        |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## deploy

Deploy commits to the specified Worker Group, Outpost Group, or Edge Fleet.

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

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `product`                                                                                             | [models.ProductsCore](../../models/productscore.md)                                                   | :heavy_check_mark:                                                                                    | Name of the Cribl product to deploy commits to the Worker Groups, Outpost Groups, or Edge Fleets for. |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The <code>id</code> of the target Worker Group, Outpost Group, or Edge Fleet for commit deployment.   |
| `version`                                                                                             | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `lookups`                                                                                             | List[[models.DeployRequestLookups](../../models/deployrequestlookups.md)]                             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.CountedConfigGroup](../../models/countedconfiggroup.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |