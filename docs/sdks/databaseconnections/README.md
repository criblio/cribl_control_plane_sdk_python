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

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="<value>", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="<value>", password="QpvMa8DI_lUJL_b", request_timeout=4657.19, tags="production,mysql,customer-data", user="Dolores.Feil")

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

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="<value>", password="QdEG1YZma4X6Q0d", request_timeout=8016.38, tags="analytics,mysql", user="Deon.Zulauf40")

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

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="<value>", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="<value>", password="Oracle_Pass456!", request_timeout=8432.44, tags="erp,oracle,finance", user="erp_user")

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

    res = ccp_client.database_connections.create(auth_type="secrets", database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="O0ma5h_gwqFSiXO", request_timeout=5552.27, tags="secure,oracle,sensitive-data", user="Alek_Dibbert")

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

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="<value>", connection_string="<value>", connection_timeout=20000, creds_secrets="<value>", password="Warehouse_Pass789!", request_timeout=1474.54, tags="warehouse,oracle,reporting", user="warehouse_user")

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

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="<value>", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="<value>", password="iRpyPXc98_8DDCo", request_timeout=6489.43, tags="warehouse,postgres,reporting", user="Ashlynn_Cassin")

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

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="<value>", connection_string="<value>", connection_timeout=10000, creds_secrets="<value>", password="S_R5PzDp3_vEzJr", request_timeout=3972.05, tags="logs,postgres", user="Eldon53")

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

    res = ccp_client.database_connections.create(auth_type="configObj", database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="<value>", connection_timeout=4499.78, creds_secrets="<value>", password="g9Dv7PtDzLx0pmQ", request_timeout=60000, tags="reporting,sqlserver,analytics", user="Aubree_Herman32")

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

    res = ccp_client.database_connections.create(auth_type="connectionString", database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="<value>", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, creds_secrets="<value>", password="KdnOen49IaSDMY2", request_timeout=30000, tags="erp,sqlserver,finance", user="Jessika_Smitham")

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

    res = ccp_client.database_connections.create(auth_type="secret", database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="<value>", password="Ua8rfhO1uYnrBPC", request_timeout=15000, tags="crm,sqlserver,sales", user="Genevieve.Douglas13")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="<value>", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="<value>", password="Fu8u0O8uNNPcA9S", request_timeout=7946.16, tags="production,mysql,customer-data", user="Rubie93")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="<value>", password="I4rBabWGYRpCqjN", request_timeout=3077.93, tags="analytics,mysql", user="Gunnar_Hickle-Davis")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="<value>", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="<value>", password="Oracle_Pass456!", request_timeout=4812.37, tags="erp,oracle,finance", user="erp_user")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secrets", database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="h2R8xU7uFdKI0S6", request_timeout=9629.77, tags="secure,oracle,sensitive-data", user="Kay83")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="<value>", connection_string="<value>", connection_timeout=20000, creds_secrets="<value>", password="Warehouse_Pass789!", request_timeout=2147.18, tags="warehouse,oracle,reporting", user="warehouse_user")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="<value>", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="<value>", password="SJ185mzGNnaospV", request_timeout=4073.17, tags="warehouse,postgres,reporting", user="Charlene27")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="<value>", connection_string="<value>", connection_timeout=10000, creds_secrets="<value>", password="bJaM8xGlX7QHy5k", request_timeout=145.27, tags="logs,postgres", user="Ulices_Morar85")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="configObj", database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="<value>", connection_timeout=1192.73, creds_secrets="<value>", password="uj_P5dL_oZDsm0P", request_timeout=60000, tags="reporting,sqlserver,analytics", user="Retta_Welch")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="connectionString", database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="<value>", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, creds_secrets="<value>", password="gAICi7pHE7tEZAQ", request_timeout=30000, tags="erp,sqlserver,finance", user="Jennifer60")

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

    res = ccp_client.database_connections.update(id_param="<value>", auth_type="secret", database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="<value>", connection_string="<value>", connection_timeout=15000, creds_secrets="<value>", password="uplhN8ZaDm8LRt_", request_timeout=15000, tags="crm,sqlserver,sales", user="Millie.Dickens93")

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