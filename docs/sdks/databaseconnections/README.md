# DatabaseConnections

## Overview

### Available Operations

* [create](#create) - Create Database Connection
* [delete](#delete) - Delete a Database Connection
* [get](#get) - Get a Database Connection
* [update](#update) - Update a Database Connection

## create

Create a new Database Connection.

### Example Usage: DatabaseConnectionExamplesMySQLWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesMySQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, tags="production,mysql,customer-data")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesMySQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", connection_timeout=15000, tags="analytics,mysql", text_secret="mysql-analytics-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, password="Oracle_Pass456!", tags="erp,oracle,finance", user="erp_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="secrets", database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", connection_timeout=15000, creds_secrets="oracle-secure-credentials", tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", connection_timeout=20000, password="Warehouse_Pass789!", tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="warehouse_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesPostgreSQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, tags="warehouse,postgres,reporting")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesPostgreSQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", connection_timeout=10000, tags="logs,postgres", text_secret="postgres-logs-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConfigObject

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="configObj", database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", request_timeout=60000, tags="reporting,sqlserver,analytics")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, request_timeout=30000, tags="erp,sqlserver,finance")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", connection_timeout=15000, request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection")

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
| `text_secret`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
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

### Example Usage: DatabaseConnectionExamplesMySQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesMySQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, tags="production,mysql,customer-data")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesMySQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", connection_timeout=15000, tags="analytics,mysql", text_secret="mysql-analytics-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, password="Oracle_Pass456!", tags="erp,oracle,finance", user="erp_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secrets", database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", connection_timeout=15000, creds_secrets="oracle-secure-credentials", tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", connection_timeout=20000, password="Warehouse_Pass789!", tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="warehouse_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesPostgreSQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, tags="warehouse,postgres,reporting")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesPostgreSQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", connection_timeout=10000, tags="logs,postgres", text_secret="postgres-logs-connection")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConfigObject

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="configObj", database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", request_timeout=60000, tags="reporting,sqlserver,analytics")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, request_timeout=30000, tags="erp,sqlserver,finance")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", connection_timeout=15000, request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection")

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
| `text_secret`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `user`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CountedDatabaseConnectionConfig](../../models/counteddatabaseconnectionconfig.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |