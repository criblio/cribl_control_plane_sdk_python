# RoutesSDK
(*routes*)

## Overview

Actions related to Routes

### Available Operations

* [list](#list) - List all Routes
* [get](#get) - Get a Routing table
* [update](#update) - Update a Route
* [append](#append) - Append a Route to the end of the Routing table

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

**[models.ListRoutesResponse](../../models/listroutesresponse.md)**

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

**[models.GetRoutesByIDResponse](../../models/getroutesbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update a Route in the specified Routing table.</br></br>Provide a complete representation of the Routing table, including the Route that you want to update, in the request body. This endpoint does not support partial updates. Cribl removes any omitted Routes and fields when updating.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the Routing table might not function as expected.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRoutesById" method="patch" path="/routes/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.update(id_param="<value>", routes=[], id="<id>", groups={
        "key": {
            "name": "<value>",
            "description": "where internationalize yesterday woefully tank underneath",
            "disabled": True,
        },
    }, comments=[
        models.Comment(
            comment="New range of formal shirts are designed keeping you in mind. With fits and styling that will make you stand apart",
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id_param`                                                                                                               | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The <code>id</code> of the Routing table that contains the Route to update. The supported value is <code>default</code>. |
| `routes`                                                                                                                 | List[[models.RoutesRoute](../../models/routesroute.md)]                                                                  | :heavy_check_mark:                                                                                                       | Pipeline routing rules                                                                                                   |
| `id`                                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Routes ID                                                                                                                |
| `groups`                                                                                                                 | Dict[str, [models.RoutesGroups](../../models/routesgroups.md)]                                                           | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `comments`                                                                                                               | List[[models.Comment](../../models/comment.md)]                                                                          | :heavy_minus_sign:                                                                                                       | Comments                                                                                                                 |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.UpdateRoutesByIDResponse](../../models/updateroutesbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## append

Append a Route to the end of the specified Routing table.</br></br>Provide a complete representation of the Routing table, including the Route that you want to append, in the request body. Cribl removes any omitted Routes and fields in the Routing table when appending the Route.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the Routing table might not function as expected.

### Example Usage

<!-- UsageSnippet language="python" operationID="createRoutesAppendById" method="post" path="/routes/{id}/append" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.routes.append(id="<id>", request_body=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The <code>id</code> of the Routing table to append the Route to. The supported value is <code>default</code>. |
| `request_body`                                                                                                | List[[models.RouteConf](../../models/routeconf.md)]                                                           | :heavy_check_mark:                                                                                            | RouteDefinitions object                                                                                       |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CreateRoutesAppendByIDResponse](../../models/createroutesappendbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |