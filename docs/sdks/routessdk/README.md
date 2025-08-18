# RoutesSDK
(*routes*)

## Overview

Actions related to Routes

### Available Operations

* [list](#list) - Get a list of Routes objects
* [get](#get) - Get Routes by ID
* [update](#update) - Update Routes
* [append](#append) - Append Routes to the end of the Routing table

## list

Get a list of Routes objects

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

Get Routes by ID

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to GET                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRoutesByIDResponse](../../models/getroutesbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update Routes

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id_param`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique ID to PATCH                                                  |
| `routes`                                                            | List[[models.RoutesRoute](../../models/routesroute.md)]             | :heavy_check_mark:                                                  | Pipeline routing rules                                              |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Routes ID                                                           |
| `groups`                                                            | Dict[str, [models.RoutesGroups](../../models/routesgroups.md)]      | :heavy_minus_sign:                                                  | N/A                                                                 |
| `comments`                                                          | List[[models.Comment](../../models/comment.md)]                     | :heavy_minus_sign:                                                  | Comments                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateRoutesByIDResponse](../../models/updateroutesbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## append

Appends routes to the end of the routing table

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

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | the route table to be appended to - currently default is the only supported value |
| `request_body`                                                                    | List[[models.RouteConf](../../models/routeconf.md)]                               | :heavy_check_mark:                                                                | RouteDefinitions object                                                           |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CreateRoutesAppendByIDResponse](../../models/createroutesappendbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |