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
                filter_="aws?.tags?.Environment === \"Production\"",
                disabled=False,
                description="Map Production EC2 instances",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'aws_prod_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="aws?.tags?.Team === \"DevOps\"",
                disabled=False,
                description="Map DevOps team EC2 instances",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'devops_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="(conn_ip.startsWith(\"10.10.42.\") && cpus > 6) || env.CRIBL_HOME.match(\"DMZ\")",
                disabled=False,
                description="Map high-performance nodes in specific network or DMZ",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'high_perf_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="platform === \"linux\" && memory > 16000 && cribl.tags.includes(\"Database\")",
                disabled=False,
                description="Map Linux nodes with high memory for database workloads",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'database_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="hostOs?.platform === \"linux\" && hostOs?.cpu_count > 4",
                disabled=False,
                description="Map containerized nodes on high-CPU Linux hosts",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'container_high_cpu_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="hostOs?.id",
                disabled=False,
                description="Map all containerized Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'container_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping for non-containerized nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="!cribl.group",
                disabled=False,
                description="Simple default Mapping Ruleset",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="platform === \"linux\"",
                disabled=False,
                description="Map Linux Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'linux_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="platform === \"win32\"",
                disabled=False,
                description="Map Windows Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'windows_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="platform === \"darwin\"",
                disabled=False,
                description="Map macOS Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'macos_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping for unmapped nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="outpost.host === \"5ab6c676be6a\"",
                disabled=False,
                description="Map Edge Nodes from Outpost A",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'outpost_a_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="outpost.guid === \"550e8400-e29b-41d4-a716-446655440000\"",
                disabled=False,
                description="Map Edge Nodes from Outpost B by GUID",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'outpost_b_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="cribl.tags.includes(\"WinLaptop\")",
                disabled=False,
                description="Map Windows Laptop Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'laptop_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="cribl.tags.includes(\"Production\")",
                disabled=False,
                description="Map Production Edge Nodes",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'production_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="!cribl.group",
                disabled=False,
                description="Default Mappings",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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
                filter_="(conn_ip.startsWith(\"10.10.42.\") && cpus > 6) || env.CRIBL_HOME.match(\"DMZ\")",
                disabled=False,
                description="Map high-performance nodes in specific network or DMZ",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'high_perf_fleet'",
                        ),
                    ],
                ),
            ),
            models.Function(
                filter_="!cribl.group",
                disabled=False,
                description="Default mapping",
                conf=models.ConfEval(
                    add=[
                        models.MappingRulesetAdd(
                            value="'default_fleet'",
                        ),
                    ],
                ),
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