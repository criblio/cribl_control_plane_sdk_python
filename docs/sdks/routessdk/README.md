# Routes

## Overview

Actions related to Routes

### Available Operations

* [list](#list) - List all Routes
* [get](#get) - Get a Routing table
* [update](#update) - Update a Route
* [append](#append) - Add a Route to the end of the Routing table

## list

Get a list of all Routes.

### Example Usage

<!-- UsageSnippet language="python" operationID="listRoutes" method="get" path="/routes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Routing table.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRoutesById" method="get" path="/routes/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Routing table to get. The supported value is <code>default</code>. |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update a Route in the specified Routing table.</br></br>Provide a complete representation of the Routing table, including the Route that you want to update, in the request body. This endpoint does not support partial updates. Cribl removes any omitted Routes and fields when updating.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the Routing table might not function as expected.

### Example Usage: RoutesUpdateExamplesBasicRoute

<!-- UsageSnippet language="python" operationID="updateRoutesById" method="patch" path="/routes/{id}" example="RoutesUpdateExamplesBasicRoute" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.update(id_param="<value>", routes=[
        models.RoutesRoute(
            id="default",
            name="my-route",
            filter_="source == \"access.log\"",
            pipeline="main",
            description="Route access logs to main pipeline",
            final=True,
        ),
    ], id="default")

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesMultipleRoutes

<!-- UsageSnippet language="python" operationID="updateRoutesById" method="patch" path="/routes/{id}" example="RoutesUpdateExamplesMultipleRoutes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.update(id_param="<value>", routes=[
        models.RoutesRoute(
            id="route-speedtest",
            name="speedtest",
            filter_="source == \"speedtest.log\"",
            pipeline="main",
            output="default",
            description="Route speedtest logs",
            final=False,
        ),
        models.RoutesRoute(
            id="route-mtr",
            name="mtr",
            filter_="source == \"mtr.log\"",
            pipeline="passthru",
            output="default",
            description="Route mtr logs",
            final=False,
        ),
        models.RoutesRoute(
            id="route-statsd",
            name="statsd",
            filter_="source == \"statsd.log\"",
            pipeline="prometheus_metrics",
            output="devnull",
            description="Route statsd metrics",
            final=False,
        ),
        models.RoutesRoute(
            id="route-default",
            name="default",
            filter_="true",
            pipeline="main",
            output="default",
            description="Catch-all Route for all other events",
            final=True,
        ),
    ], id="default")

    # Handle response
    print(res)

```
### Example Usage: RoutesUpdateExamplesRouteWithOutputExpression

<!-- UsageSnippet language="python" operationID="updateRoutesById" method="patch" path="/routes/{id}" example="RoutesUpdateExamplesRouteWithOutputExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.update(id_param="<value>", routes=[
        models.RoutesRoute(
            id="route-dynamic",
            name="dynamic-output",
            filter_="source == \"dynamic.log\"",
            pipeline="main",
            enable_output_expression=True,
            output_expression="`myDest_${C.logStreamEnv}`",
            description="Route with dynamic Destination based on environment",
            final=True,
        ),
    ], id="default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id_param`                                                                                                                 | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The <code>id</code> of the Routing table that contains the Route to update. The supported value is <code>default</code>.   |
| `routes`                                                                                                                   | List[[models.RoutesRoute](../../models/routesroute.md)]                                                                    | :heavy_check_mark:                                                                                                         | Pipeline routing rules                                                                                                     |
| `id`                                                                                                                       | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | Routes ID                                                                                                                  |
| `groups`                                                                                                                   | Dict[str, [models.AdditionalPropertiesTypePipelineConfGroups](../../models/additionalpropertiestypepipelineconfgroups.md)] | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |
| `comments`                                                                                                                 | List[[models.Comment](../../models/comment.md)]                                                                            | :heavy_minus_sign:                                                                                                         | Comments                                                                                                                   |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## append

Add a Route to the end of the specified Routing table.

### Example Usage: RoutesAppendExamplesMultipleRoutes

<!-- UsageSnippet language="python" operationID="createRoutesAppendById" method="post" path="/routes/{id}/append" example="RoutesAppendExamplesMultipleRoutes" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.append(id="<id>", request_body=[
        {
            "description": "Route audit logs",
            "filter_": "source == \"audit.log\"",
            "final": False,
            "id": "route-audit",
            "name": "audit",
            "output": "default",
            "pipeline": "main",
        },
        {
            "description": "Route security logs",
            "filter_": "source == \"security.log\"",
            "final": False,
            "id": "route-security",
            "name": "security",
            "output": "devnull",
            "pipeline": "passthru",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesAppendExamplesRouteWithOutputExpression

<!-- UsageSnippet language="python" operationID="createRoutesAppendById" method="post" path="/routes/{id}/append" example="RoutesAppendExamplesRouteWithOutputExpression" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.append(id="<id>", request_body=[
        {
            "description": "Route with dynamic Destination based on environment",
            "enable_output_expression": True,
            "filter_": "source == \"dynamic.log\"",
            "final": True,
            "id": "route-dynamic-append",
            "name": "dynamic-append",
            "output_expression": "`myDest_${C.logStreamEnv}`",
            "pipeline": "main",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: RoutesAppendExamplesSingleRoute

<!-- UsageSnippet language="python" operationID="createRoutesAppendById" method="post" path="/routes/{id}/append" example="RoutesAppendExamplesSingleRoute" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.append(id="<id>", request_body=[
        {
            "description": "Route new logs to main pipeline",
            "filter_": "source == \"new.log\"",
            "final": True,
            "id": "route-new",
            "name": "new-route",
            "pipeline": "main",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The <code>id</code> of the Routing table to add the Route to. The supported value is <code>default</code>. |
| `request_body`                                                                                             | List[[models.RouteConf](../../models/routeconf.md)]                                                        | :heavy_check_mark:                                                                                         | RouteDefinitions object                                                                                    |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.CountedRoutes](../../models/countedroutes.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |