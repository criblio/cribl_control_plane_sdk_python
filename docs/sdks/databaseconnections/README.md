# DatabaseConnections

## Overview

### Available Operations

* [create](#create) - Create Database Connection
* [delete](#delete) - Delete a Database Connection
* [get](#get) - Get a Database Connection
* [update](#update) - Update a Database Connection

## create

Create a new Database Connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="<value>", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="<value>", password="QpvMa8DI_lUJL_b", request_timeout=4657.19, tags="production,mysql,customer-data", user="Dolores.Feil")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `auth_type`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `database_type`                                                         | [models.DatabaseConnectionType](../../models/databaseconnectiontype.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `description`                                                           | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `config_obj`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connection_string`                                                     | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connection_timeout`                                                    | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | N/A                                                                     |
| `creds_secrets`                                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `password`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `request_timeout`                                                       | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | N/A                                                                     |
| `tags`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `user`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CountedDatabaseConnectionConfig](../../models/counteddatabaseconnectionconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Database Connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDatabaseConnectionConfigById" method="delete" path="/lib/database-connections/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Database Connection to delete.           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedDatabaseConnectionConfig](../../models/counteddatabaseconnectionconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Database Connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatabaseConnectionConfigById" method="get" path="/lib/database-connections/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Database Connection to get.              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedDatabaseConnectionConfig](../../models/counteddatabaseconnectionconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Database Connection.</br></br>Provide a complete representation of the Database Connection that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Database Connection.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Database Connection might not function as expected.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="<value>", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="<value>", password="Fu8u0O8uNNPcA9S", request_timeout=7946.16, tags="production,mysql,customer-data", user="Rubie93")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id_param`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | The <code>id</code> of the Database Connection to update.               |
| `auth_type`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `database_type`                                                         | [models.DatabaseConnectionType](../../models/databaseconnectiontype.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `description`                                                           | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `config_obj`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connection_string`                                                     | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connection_timeout`                                                    | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | N/A                                                                     |
| `creds_secrets`                                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `password`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `request_timeout`                                                       | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | N/A                                                                     |
| `tags`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `user`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CountedDatabaseConnectionConfig](../../models/counteddatabaseconnectionconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |