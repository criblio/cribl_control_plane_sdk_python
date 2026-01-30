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

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRoutesByPackAndId" method="patch" path="/p/{pack}/routes/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.routes.update(id_param="<value>", pack="<value>", routes=[
        models.RoutesRoute(
            id="default",
            name="my-route",
            disabled=True,
            filter_="source == \"access.log\"",
            pipeline="main",
            enable_output_expression=False,
            output="<value>",
            output_expression="<value>",
            description="Route access logs to main pipeline",
            final=True,
        ),
    ], id="default", groups={
        "key": {
            "name": "<value>",
            "description": "ridge impassioned amount happily",
            "disabled": False,
        },
    }, comments=[
        models.Comment(
            comment="New ABC 13 9370, 13.3, 5th Gen CoreA5-8250U, 8GB RAM, 256GB SSD, power UHD Graphics, OS 10 Home, OS Office A & J 2016",
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id_param`                                                                                                                 | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The <code>id</code> of the Routing table that contains the Route to update. The supported value is <code>default</code>.   |
| `pack`                                                                                                                     | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The <code>id</code> of the Pack to update.                                                                                 |
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

### Example Usage

<!-- UsageSnippet language="python" operationID="createRoutesAppendByPackAndId" method="post" path="/p/{pack}/routes/{id}/append" -->
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