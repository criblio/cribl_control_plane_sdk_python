# Packs.Routes

## Overview

### Available Operations

* [get](#get) - Get a Routing table within a Pack
* [update](#update) - Update a Route within a Pack
* [list](#list) - List all Routes within a Pack
* [append](#append) - Add a Route to the end of the Routing table within a Pack

## get

Get the specified Routing table within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRoutesByPackAndId" method="get" path="/p/{pack}/routes/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Routing table to get. The supported value is <code>default</code>. |
| `pack`                                                                                        | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Pack to get.                                                       |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Route within the specified Pack.</br></br>Provide a complete representation of the Routing table, including the Route that you want to update, in the request body. This endpoint does not support partial updates. Cribl removes any omitted Routes and fields when updating.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the Routing table might not function as expected.

### Example Usage: RoutesUpdateExamplesBasicRoute

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesBasicRoute" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "clones": [
                {
                    "key": "<value>",
                    "key1": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route access logs to main pipeline",
            "disabled": True,
            "enable_output_expression": False,
            "filter_": "source == \"access.log\"",
            "final": True,
            "group_id": "<id>",
            "id": "default",
            "name": "my-route",
            "output": "<value>",
            "output_expression": "<value>",
            "pipeline": "main",
            "target_context": models.TargetContext.GROUP,
        },
    ], comments=[
        {
            "comment": "New ABC 13 9370, 13.3, 5th Gen CoreA5-8250U, 8GB RAM, 256GB SSD, power UHD Graphics, OS 10 Home, OS Office A & J 2016",
            "group_id": "<id>",
            "id": "<id>",
            "index": 4999.72,
        },
    ], groups={
        "key": {
            "description": "ridge impassioned amount happily",
            "index": 8485.39,
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesMultipleRoutes

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesMultipleRoutes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "clones": [
                {
                    "key": "<value>",
                },
                {
                    "key": "<value>",
                    "key1": "<value>",
                },
                {
                    "key": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route speedtest logs",
            "disabled": True,
            "enable_output_expression": False,
            "filter_": "source == \"speedtest.log\"",
            "final": False,
            "group_id": "<id>",
            "id": "route-speedtest",
            "name": "speedtest",
            "output": "default",
            "output_expression": "<value>",
            "pipeline": "main",
            "target_context": models.TargetContext.PACK,
        },
        {
            "clones": [
                {

                },
            ],
            "context": "<value>",
            "description": "Route mtr logs",
            "disabled": False,
            "enable_output_expression": False,
            "filter_": "source == \"mtr.log\"",
            "final": False,
            "group_id": "<id>",
            "id": "route-mtr",
            "name": "mtr",
            "output": "default",
            "output_expression": "<value>",
            "pipeline": "passthru",
            "target_context": models.TargetContext.GROUP,
        },
        {
            "clones": [
                {

                },
            ],
            "context": "<value>",
            "description": "Route statsd metrics",
            "disabled": True,
            "enable_output_expression": False,
            "filter_": "source == \"statsd.log\"",
            "final": False,
            "group_id": "<id>",
            "id": "route-statsd",
            "name": "statsd",
            "output": "devnull",
            "output_expression": "<value>",
            "pipeline": "prometheus_metrics",
            "target_context": models.TargetContext.GROUP,
        },
        {
            "clones": [
                {

                },
                {
                    "key": "<value>",
                    "key1": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Catch-all Route for all other events",
            "disabled": False,
            "enable_output_expression": False,
            "filter_": "true",
            "final": True,
            "group_id": "<id>",
            "id": "route-default",
            "name": "default",
            "output": "default",
            "output_expression": "<value>",
            "pipeline": "main",
            "target_context": models.TargetContext.GROUP,
        },
    ], comments=[
        {
            "comment": "New ABC 13 9370, 13.3, 5th Gen CoreA5-8250U, 8GB RAM, 256GB SSD, power UHD Graphics, OS 10 Home, OS Office A & J 2016",
            "group_id": "<id>",
            "id": "<id>",
            "index": 2877.94,
        },
    ], groups={
        "key": {
            "description": "ridge impassioned amount happily",
            "index": 7418.21,
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesRouteWithOutputExpression

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesRouteWithOutputExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "clones": [
                {
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route with dynamic Destination based on environment",
            "disabled": True,
            "enable_output_expression": True,
            "filter_": "source == \"dynamic.log\"",
            "final": True,
            "group_id": "<id>",
            "id": "route-dynamic",
            "name": "dynamic-output",
            "output": "<value>",
            "output_expression": "`myDest_${C.logStreamEnv}`",
            "pipeline": "main",
            "target_context": models.TargetContext.GROUP,
        },
    ], comments=[
        {
            "comment": "New ABC 13 9370, 13.3, 5th Gen CoreA5-8250U, 8GB RAM, 256GB SSD, power UHD Graphics, OS 10 Home, OS Office A & J 2016",
            "group_id": "<id>",
            "id": "<id>",
            "index": 7514.98,
        },
    ], groups={
        "key": {
            "description": "ridge impassioned amount happily",
            "index": 3321.41,
            "name": "<value>",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id_param`                                                                                                               | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The <code>id</code> of the Routing table that contains the Route to update. The supported value is <code>default</code>. |
| `pack`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The <code>id</code> of the Pack to update.                                                                               |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Unique identifier for the Routing table. The supported value is <code>default</code>.                                    |
| `routes`                                                                                                                 | List[[models.RouteConf](../../models/routeconf.md)]                                                                      | :heavy_check_mark:                                                                                                       | Array of Route configurations that define how events are processed and routed.                                           |
| `comments`                                                                                                               | List[[models.RouteComment](../../models/routecomment.md)]                                                                | :heavy_minus_sign:                                                                                                       | Array of user-provided comments that describe or annotate Routes.                                                        |
| `groups`                                                                                                                 | Dict[str, [models.RoutesGroups](../../models/routesgroups.md)]                                                           | :heavy_minus_sign:                                                                                                       | Information about the Route Groups that the Route is associated with.                                                    |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of all Routes within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRoutesByPack" method="get" path="/p/{pack}/routes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## append

Add a Route to the end of the specified Routing table within the specified Pack.

### Example Usage: RoutesAppendExamplesMultipleRoutes

<!-- UsageSnippet language="python" operationID="createRoutesAppendByPackAndId" method="post" path="/p/{pack}/routes/{id}/append" example="RoutesAppendExamplesMultipleRoutes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "clones": [
                {
                    "key": "<value>",
                    "key1": "<value>",
                },
                {
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
                {
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route audit logs",
            "disabled": False,
            "enable_output_expression": False,
            "filter_": "source == \"audit.log\"",
            "final": False,
            "group_id": "<id>",
            "id": "route-audit",
            "name": "audit",
            "output": "default",
            "output_expression": "<value>",
            "pipeline": "main",
            "target_context": models.TargetContext.GROUP,
        },
        {
            "clones": [
                {
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route security logs",
            "disabled": False,
            "enable_output_expression": False,
            "filter_": "source == \"security.log\"",
            "final": False,
            "group_id": "<id>",
            "id": "route-security",
            "name": "security",
            "output": "devnull",
            "output_expression": "<value>",
            "pipeline": "passthru",
            "target_context": models.TargetContext.PACK,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesAppendExamplesRouteWithOutputExpression

<!-- UsageSnippet language="python" operationID="createRoutesAppendByPackAndId" method="post" path="/p/{pack}/routes/{id}/append" example="RoutesAppendExamplesRouteWithOutputExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "clones": [
                {
                    "key": "<value>",
                },
                {
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route with dynamic Destination based on environment",
            "disabled": True,
            "enable_output_expression": True,
            "filter_": "source == \"dynamic.log\"",
            "final": True,
            "group_id": "<id>",
            "id": "route-dynamic-append",
            "name": "dynamic-append",
            "output": "<value>",
            "output_expression": "`myDest_${C.logStreamEnv}`",
            "pipeline": "main",
            "target_context": models.TargetContext.PACK,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesAppendExamplesSingleRoute

<!-- UsageSnippet language="python" operationID="createRoutesAppendByPackAndId" method="post" path="/p/{pack}/routes/{id}/append" example="RoutesAppendExamplesSingleRoute" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "clones": [
                {

                },
                {
                    "key": "<value>",
                },
            ],
            "context": "<value>",
            "description": "Route new logs to main pipeline",
            "disabled": False,
            "enable_output_expression": True,
            "filter_": "source == \"new.log\"",
            "final": True,
            "group_id": "<id>",
            "id": "route-new",
            "name": "new-route",
            "output": "<value>",
            "output_expression": "<value>",
            "pipeline": "main",
            "target_context": models.TargetContext.PACK,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The <code>id</code> of the Routing table to add the Route to. The supported value is <code>default</code>. |
| `pack`                                                                                                     | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The <code>id</code> of the Pack to append.                                                                 |
| `request_body`                                                                                             | List[[models.RouteConf](../../models/routeconf.md)]                                                        | :heavy_check_mark:                                                                                         | RouteDefinitions object                                                                                    |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |