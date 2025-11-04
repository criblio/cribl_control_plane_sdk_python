# Mappings
(*groups.mappings*)

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

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsActivateByProduct" method="post" path="/admin/products/{product}/mappings/activate" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.activate(product=models.ProductsCore.STREAM, id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../../models/productscore.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to activate the Mapping Ruleset for       |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAdminProductsMappingsActivateByProductResponse](../../models/createadminproductsmappingsactivatebyproductresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create and save a new Mapping Ruleset for the specified Cribl product.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdminProductsMappingsByProduct" method="post" path="/admin/products/{product}/mappings" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.create(product=models.ProductsCore.EDGE, id="os-based-mapping", conf={
        "functions": [
            {
                "filter_": "platform === \"linux\"",
                "id": models.ID.EVAL,
                "description": "Map Linux Edge Nodes",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                    ],
                },
            },
            {
                "filter_": "platform === \"win32\"",
                "id": models.ID.EVAL,
                "description": "Map Windows Edge Nodes",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                    ],
                },
            },
            {
                "filter_": "platform === \"darwin\"",
                "id": models.ID.EVAL,
                "description": "Map macOS Edge Nodes",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                    ],
                },
            },
            {
                "filter_": "!cribl.group",
                "id": models.ID.EVAL,
                "description": "Default mapping for unmapped nodes",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                    ],
                },
            },
        ],
    }, active=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `product`                                                                 | [models.ProductsCore](../../models/productscore.md)                       | :heavy_check_mark:                                                        | Name of the Cribl product to create the Mapping Ruleset for               |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `conf`                                                                    | [Optional[models.MappingRulesetConf]](../../models/mappingrulesetconf.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `active`                                                                  | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateAdminProductsMappingsByProductResponse](../../models/createadminproductsmappingsbyproductresponse.md)**

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

    res = ccp_client.groups.mappings.list(product=models.ProductsCore.EDGE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../../models/productscore.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to list the Mapping Rulesets for          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAdminProductsMappingsByProductResponse](../../models/getadminproductsmappingsbyproductresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Permanently remove the specified Mapping Ruleset from the Worker Group or Edge Fleet.

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

    res = ccp_client.groups.mappings.delete(product=models.ProductsCore.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `product`                                                           | [models.ProductsCore](../../models/productscore.md)                 | :heavy_check_mark:                                                  | Name of the Cribl product to delete the Mapping Ruleset for         |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Mapping Ruleset to delete.               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAdminProductsMappingsByProductAndIDResponse](../../models/deleteadminproductsmappingsbyproductandidresponse.md)**

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

    res = ccp_client.groups.mappings.get(product=models.ProductsCore.STREAM, id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `product`                                                                    | [models.ProductsCore](../../models/productscore.md)                          | :heavy_check_mark:                                                           | Name of the Cribl product to get the Mappings for                            |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The <code>id</code> of the Worker Group or Edge Fleet Mapping Ruleset to get |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.GetAdminProductsMappingsByProductAndIDResponse](../../models/getadminproductsmappingsbyproductandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Modify the configuration of the specified Mapping Ruleset for a Worker Group or Edge Fleet.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdminProductsMappingsByProductAndId" method="patch" path="/admin/products/{product}/mappings/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.groups.mappings.update(product=models.ProductsCore.STREAM, id_param="<value>", id="complex-mapping", conf={
        "functions": [
            {
                "filter_": "(conn_ip.startsWith(\"10.10.42.\") && cpus > 6) || env.CRIBL_HOME.match(\"DMZ\")",
                "id": models.ID.EVAL,
                "description": "Map high-performance nodes in specific network or DMZ",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                        "<value 2>",
                    ],
                },
            },
            {
                "filter_": "!cribl.group",
                "id": models.ID.EVAL,
                "description": "Default mapping",
                "disabled": False,
                "final": True,
                "conf": {},
                "group_id": "<id>",
                "name": models.Name.EVAL,
                "group": models.Group.STANDARD,
                "schema_": {
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "keep": [
                        "<value 1>",
                    ],
                    "remove": [
                        "<value 1>",
                        "<value 2>",
                    ],
                },
            },
        ],
    }, active=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `product`                                                                 | [models.ProductsCore](../../models/productscore.md)                       | :heavy_check_mark:                                                        | Name of the Cribl product to update the Mapping Ruleset for               |
| `id_param`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Mapping Ruleset to update.                     |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `conf`                                                                    | [Optional[models.MappingRulesetConf]](../../models/mappingrulesetconf.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `active`                                                                  | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UpdateAdminProductsMappingsByProductAndIDResponse](../../models/updateadminproductsmappingsbyproductandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |