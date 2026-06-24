# Packs.Routes

## Overview

### Available Operations

* [list](#list) - List all Routes within a Pack
* [get](#get) - Get a Routing table within a Pack
* [update](#update) - Update a Route within a Pack
* [append](#append) - Add a Route to the end of the Routing table within a Pack

## list

Get a list of all Routes within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRoutesByPack" method="get" path="/p/{pack}/routes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
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
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack.                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Routing table within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRoutesByPackAndId" method="get" path="/p/{pack}/routes/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
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
| `pack`                                                                                        | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Pack.                                                              |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Route within the specified Pack.<br/><br/>Provide a complete representation of the Routing table, including the Route that you want to update, in the request body.<br/><br/>This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Routing table.<br/><br/>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Routing table might not function as expected.<br/><br/>Cribl also removes any omitted Routes when updating the Routing table.

### Example Usage: RoutesUpdateExamplesBasicRoute

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesBasicRoute" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "description": "Route access logs to main Pipeline",
            "filter_": "source == \"access.log\"",
            "name": "my-route",
            "pipeline": "main",
            "final": True,
            "id": "default",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesMultipleRoutes

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesMultipleRoutes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "description": "Route speedtest logs",
            "filter_": "source == \"speedtest.log\"",
            "name": "speedtest",
            "output": "default",
            "pipeline": "main",
            "final": False,
            "id": "route-speedtest",
        },
        {
            "description": "Route mtr logs",
            "filter_": "source == \"mtr.log\"",
            "name": "mtr",
            "output": "default",
            "pipeline": "passthru",
            "final": False,
            "id": "route-mtr",
        },
        {
            "description": "Route statsd metrics",
            "filter_": "source == \"statsd.log\"",
            "name": "statsd",
            "output": "devnull",
            "pipeline": "prometheus_metrics",
            "final": False,
            "id": "route-statsd",
        },
        {
            "description": "Catch-all Route for all other events",
            "filter_": "true",
            "name": "default",
            "output": "default",
            "pipeline": "main",
            "final": True,
            "id": "route-default",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesRouteWithDefaults

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesRouteWithDefaults" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "description": "Route access logs to main Pipeline",
            "filter_": "source == \"access.log\"",
            "name": "my-route",
            "pipeline": "main",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesRouteWithOutputExpression

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" example="RoutesUpdateExamplesRouteWithOutputExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", id="default", routes=[
        {
            "description": "Route with dynamic Destination based on environment",
            "enable_output_expression": True,
            "filter_": "source == \"dynamic.log\"",
            "name": "dynamic-output",
            "output_expression": "`myDest_${C.logStreamEnv}`",
            "pipeline": "main",
            "final": True,
            "id": "route-dynamic",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id_param`                                                                                                               | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The <code>id</code> of the Routing table that contains the Route to update. The supported value is <code>default</code>. |
| `pack`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The <code>id</code> of the Pack.                                                                                         |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Unique identifier for the Routing table. The supported value is <code>default</code>.                                    |
| `routes`                                                                                                                 | List[[models.RouteConfInput](../../models/routeconfinput.md)]                                                            | :heavy_check_mark:                                                                                                       | Array of Route configurations that define how events are processed and routed.                                           |
| `comments`                                                                                                               | List[[models.RouteComment](../../models/routecomment.md)]                                                                | :heavy_minus_sign:                                                                                                       | Array of user-provided comments that describe or annotate Routes.                                                        |
| `groups`                                                                                                                 | Dict[str, [models.AdditionalPropertiesTypeRoutesGroups](../../models/additionalpropertiestyperoutesgroups.md)]           | :heavy_minus_sign:                                                                                                       | Information about the Route Groups that the Route is associated with.                                                    |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

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
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "description": "Route audit logs",
            "filter_": "source == \"audit.log\"",
            "name": "audit",
            "output": "default",
            "pipeline": "main",
            "final": False,
            "id": "route-audit",
        },
        {
            "description": "Route security logs",
            "filter_": "source == \"security.log\"",
            "name": "security",
            "output": "devnull",
            "pipeline": "passthru",
            "final": False,
            "id": "route-security",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesAppendExamplesRouteWithDefaults

<!-- UsageSnippet language="python" operationID="createRoutesAppendByPackAndId" method="post" path="/p/{pack}/routes/{id}/append" example="RoutesAppendExamplesRouteWithDefaults" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "description": "Route with server-generated id and default final value",
            "filter_": "source == \"new.log\"",
            "name": "new-route",
            "pipeline": "main",
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
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "description": "Route with dynamic Destination based on environment",
            "enable_output_expression": True,
            "filter_": "source == \"dynamic.log\"",
            "name": "dynamic-append",
            "output_expression": "`myDest_${C.logStreamEnv}`",
            "pipeline": "main",
            "final": True,
            "id": "route-dynamic-append",
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
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.append(id="<id>", pack="<value>", request_body=[
        {
            "description": "Route new logs to main pipeline",
            "filter_": "source == \"new.log\"",
            "name": "new-route",
            "pipeline": "main",
            "final": True,
            "id": "route-new",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The <code>id</code> of the Routing table to add the Route to. The supported value is <code>default</code>. |
| `pack`                                                                                                     | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The <code>id</code> of the Pack.                                                                           |
| `request_body`                                                                                             | List[[models.RouteConfInput](../../models/routeconfinput.md)]                                              | :heavy_check_mark:                                                                                         | RouteDefinitions object.                                                                                   |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |