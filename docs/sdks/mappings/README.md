# Groups.Mappings

## Overview

### Available Operations

* [activate](#activate) - Set a Mapping Ruleset as the active configuration for the specified Cribl product
* [create](#create) - Create a new Mapping Ruleset for the specified Cribl product
* [list](#list) - List all Mapping Rulesets for the specified Cribl product
* [delete](#delete) - Delete the specified Mapping Ruleset from the Worker Group or Edge Fleet
* [get](#get) - Retrieve a Specific Mapping Ruleset
* [update](#update) - Update an existing Mapping Ruleset for a Worker Group or Edge Fleet

## activate

Set a specific Mapping Ruleset as the currently active configuration for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsActivateByProduct" method="post" path="/admin/products/{product}/mappings/activate" example="MappingRulesetActivateExamplesActivate" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.activate(product=models.ProductsBase.STREAM, id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsBase](../../models/productsbase.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to activate the Mapping Ruleset for       |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedRulesetID](../../models/countedrulesetid.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create and save a new Mapping Ruleset for the specified Cribl product.<br><br>Note: This functionality is not supported for Cribl Stream Workers on Cribl.Cloud.

### Example Usage: MappingRulesetCreateExamplesAWSEC2InstanceMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesAWSEC2InstanceMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.EDGE, id="aws-ec2-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'aws_prod_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "aws?.tags?.Environment === \"Production\"",
                    "description": "Map Production EC2 instances",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'devops_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "aws?.tags?.Team === \"DevOps\"",
                    "description": "Map DevOps team EC2 instances",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesComplexMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesComplexMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.EDGE, id="complex-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'high_perf_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "(conn_ip.startsWith(\"10.10.42.\") && cpus > 6) || env.CRIBL_HOME.match(\"DMZ\")",
                    "description": "Map high-performance nodes in specific network or DMZ",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'database_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "platform === \"linux\" && memory > 16000 && cribl.tags.includes(\"Database\")",
                    "description": "Map Linux nodes with high memory for database workloads",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesContainerBasedMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesContainerBasedMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.STREAM, id="container-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'container_high_cpu_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "hostOs?.platform === \"linux\" && hostOs?.cpu_count > 4",
                    "description": "Map containerized nodes on high-CPU Linux hosts",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'container_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "hostOs?.id",
                    "description": "Map all containerized Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping for non-containerized nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesDefaultRuleset

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesDefaultRuleset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.EDGE, id="simple-default-mappings", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Simple default Mapping Ruleset",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesOSBasedMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesOSBasedMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.STREAM, id="os-based-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'linux_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "platform === \"linux\"",
                    "description": "Map Linux Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'windows_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "platform === \"win32\"",
                    "description": "Map Windows Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'macos_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "platform === \"darwin\"",
                    "description": "Map macOS Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping for unmapped nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesOutpostBasedMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesOutpostBasedMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.EDGE, id="outpost-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'outpost_a_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "outpost.host === \"5ab6c676be6a\"",
                    "description": "Map Edge Nodes from Outpost A",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'outpost_b_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "outpost.guid === \"550e8400-e29b-41d4-a716-446655440000\"",
                    "description": "Map Edge Nodes from Outpost B by GUID",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetCreateExamplesTagBasedMapping

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" example="MappingRulesetCreateExamplesTagBasedMapping" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsBase.STREAM, id="tag-based-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'laptop_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "cribl.tags.includes(\"WinLaptop\")",
                    "description": "Map Windows Laptop Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'production_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "cribl.tags.includes(\"Production\")",
                    "description": "Map Production Edge Nodes",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `product`                                                                 | [models.ProductsBase](../../models/productsbase.md)                       | :heavy_check_mark:                                                        | Name of the Cribl product to create the Mapping Ruleset for               |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `conf`                                                                    | [Optional[models.MappingRulesetConf]](../../models/mappingrulesetconf.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `active`                                                                  | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CountedMappingRuleset](../../models/countedmappingruleset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Retrieve a list of all existing Mapping Rulesets for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdminProductsMappingsByProduct" method="get" path="/admin/products/{product}/mappings" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.list(product=models.ProductsBase.EDGE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsBase](../../models/productsbase.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to list the Mapping Rulesets for          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedMappingRuleset](../../models/countedmappingruleset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Permanently remove the specified Mapping Ruleset from the Worker Group or Edge Fleet.<br><br>Note: This functionality is not supported for Cribl Stream Workers on Cribl.Cloud.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAdminProductsMappingsByProductAndId" method="delete" path="/admin/products/{product}/mappings/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.delete(product=models.ProductsBase.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsBase](../../models/productsbase.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to delete the Mapping Ruleset for         |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Mapping Ruleset to delete.               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedMappingRuleset](../../models/countedmappingruleset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the details for a single Mapping Ruleset, identified by its id, for a Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdminProductsMappingsByProductAndId" method="get" path="/admin/products/{product}/mappings/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.get(product=models.ProductsBase.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `product`                                                                    | [models.ProductsBase](../../models/productsbase.md)                          | :heavy_check_mark:                                                           | Name of the Cribl product to get the Mappings for                            |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The <code>id</code> of the Worker Group or Edge Fleet Mapping Ruleset to get |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.CountedMappingRuleset](../../models/countedmappingruleset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Modify the configuration of the specified Mapping Ruleset for a Worker Group or Edge Fleet.

### Example Usage: MappingRulesetUpdateExamplesEnableDisabledRule

<!-- UsageSnippet language="python" operationID="updateAdminProductsMappingsByProductAndId" method="patch" path="/admin/products/{product}/mappings/{id}" example="MappingRulesetUpdateExamplesEnableDisabledRule" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.update(product=models.ProductsBase.EDGE, id_param="<value>", id="default", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default Mappings",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    }, active=True)

    # Handle response
    print(res)

```
### Example Usage: MappingRulesetUpdateExamplesUpdateComplexRule

<!-- UsageSnippet language="python" operationID="updateAdminProductsMappingsByProductAndId" method="patch" path="/admin/products/{product}/mappings/{id}" example="MappingRulesetUpdateExamplesUpdateComplexRule" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.update(product=models.ProductsBase.STREAM, id_param="<value>", id="complex-mapping", conf={
        "functions": [
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'high_perf_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "(conn_ip.startsWith(\"10.10.42.\") && cpus > 6) || env.CRIBL_HOME.match(\"DMZ\")",
                    "description": "Map high-performance nodes in specific network or DMZ",
                    "disabled": False,
                    "final": True,
                },
            ),
            models.Function(
                id=models.MappingRulesetID.EVAL,
                conf=models.FunctionConf(
                    add=[
                        models.MappingRulesetAdd(
                            name=models.Name.GROUP_ID,
                            value="'default_fleet'",
                        ),
                    ],
                ),
                **{
                    "filter": "!cribl.group",
                    "description": "Default mapping",
                    "disabled": False,
                    "final": True,
                },
            ),
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `product`                                                                 | [models.ProductsBase](../../models/productsbase.md)                       | :heavy_check_mark:                                                        | Name of the Cribl product to update the Mapping Ruleset for               |
| `id_param`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Mapping Ruleset to update.                     |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `conf`                                                                    | [Optional[models.MappingRulesetConf]](../../models/mappingrulesetconf.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `active`                                                                  | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CountedMappingRuleset](../../models/countedmappingruleset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |