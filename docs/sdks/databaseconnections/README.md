# DatabaseConnections

## Overview

Actions related to DatabaseConnections

### Available Operations

* [list](#list) - List all Database Connections
* [create](#create) - Create a Database Connection
* [get](#get) - Get a Database Connection
* [update](#update) - Update a Database Connection
* [delete](#delete) - Delete a Database Connection

## list

Get a list of all Database Connections.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatabaseConnectionConfig" method="get" path="/lib/database-connections" example="DatabaseConnectionListResponseExamplesDatabaseConnectionList" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database_type`                                                                                                                                                   | [Optional[models.DatabaseConnectionType]](../../models/databaseconnectiontype.md)                                                                                 | :heavy_minus_sign:                                                                                                                                                | Filter results by database engine type. Use this parameter to return only Database Connections for the specified engine.                                          |
| `limit`                                                                                                                                                           | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Maximum number of Database Connections to return in the response for this request. Use with <code>offset</code> to paginate the response into manageable batches. |
| `offset`                                                                                                                                                          | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Starting point from which to retrieve results for this request. Use with <code>limit</code> to paginate the response into manageable batches.                     |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |

### Response

**[models.GetDatabaseConnectionConfigResponse](../../models/getdatabaseconnectionconfigresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Database Connection.

### Example Usage: DatabaseConnectionBadRequestResponseExamplesInvalidDatabaseConnectionRequest

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionBadRequestResponseExamplesInvalidDatabaseConnectionRequest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesMySQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesMySQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="analytics,mysql", text_secret="mysql-analytics-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,oracle,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.SECRETS, database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="yourPassword", request_timeout=30000, tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithMutualTLS

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithMutualTLS" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle database reached over TCPS with mutual TLS", id="oracle-mtls-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="tcps://oracle.example.com:2484/ORCL", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="Oracle_Pass456!", request_timeout=30000, tags="erp,oracle,mtls,production", text_secret="mysql-production-connection", tls=models.TLSClientParams(
        disabled=False,
        reject_unauthorized=True,
    ), user="erp_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesOracleWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=20000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesPostgreSQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="postgresql://yourUsername:yourPassword@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,postgres,reporting", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesPostgreSQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="logs,postgres", text_secret="postgres-logs-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConfigObject

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=60000, tags="reporting,sqlserver,analytics", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConnectionString

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=yourUsername;Password=yourPassword;Encrypt=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,sqlserver,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithSecret

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionExamplesSQLServerWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionResponseExamplesMySQLDatabaseConnection

<!-- UsageSnippet language="python" operationID="createDatabaseConnectionConfig" method="post" path="/lib/database-connections" example="DatabaseConnectionResponseExamplesMySQLDatabaseConnection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.create(auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                   | Type                                                                                                                                                                                        | Required                                                                                                                                                                                    | Description                                                                                                                                                                                 | Example                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_type`                                                                                                                                                                                 | [models.DatabaseConnectionAuthType](../../models/databaseconnectionauthtype.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                                          | N/A                                                                                                                                                                                         |                                                                                                                                                                                             |
| `database_type`                                                                                                                                                                             | [models.DatabaseConnectionType](../../models/databaseconnectiontype.md)                                                                                                                     | :heavy_check_mark:                                                                                                                                                                          | N/A                                                                                                                                                                                         |                                                                                                                                                                                             |
| `description`                                                                                                                                                                               | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | Brief description of the Database Connection.                                                                                                                                               | Production MySQL database for customer data                                                                                                                                                 |
| `id`                                                                                                                                                                                        | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | Unique identifier for the Database Connection.                                                                                                                                              | mysql-prod-db                                                                                                                                                                               |
| `config_obj`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | JSON configuration object for advanced SQL Server connection settings.                                                                                                                      | {<br/>"server": "sqlserver.example.com",<br/>"database": "Reporting",<br/>"user": "yourUsername",<br/>"password": "yourPassword",<br/>"options": {<br/>"trustServerCertificate": false,<br/>"connectTimeout": 20000<br/>}<br/>} |
| `connection_string`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database connection string with embedded credentials or server information.                                                                                                                 | mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true                                                                                                                |
| `connection_timeout`                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Maximum time (in milliseconds) to wait when establishing the database connection.                                                                                                           | 10000                                                                                                                                                                                       |
| `creds_secrets`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Name of the stored credentials secret containing username and password. Used with Oracle connections.                                                                                       | oracle-production-credentials                                                                                                                                                               |
| `password`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database password for authentication. Used with Oracle connections.                                                                                                                         | yourPassword                                                                                                                                                                                |
| `request_timeout`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Maximum time (in milliseconds) to wait for a database query to complete. Applies to SQL Server connections only.                                                                            | 30000                                                                                                                                                                                       |
| `tags`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Comma-separated list of tags for categorizing and filtering Database Connections.                                                                                                           | production,mysql,customer-data                                                                                                                                                              |
| `text_secret`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Name of the stored text secret containing the connection string.                                                                                                                            | mysql-production-connection                                                                                                                                                                 |
| `tls`                                                                                                                                                                                       | [Optional[models.TLSClientParams]](../../models/tlsclientparams.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                          | TLS client connection settings.                                                                                                                                                             |                                                                                                                                                                                             |
| `user`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database username for authentication. Used with Oracle connections.                                                                                                                         | yourUsername                                                                                                                                                                                |
| `retries`                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                         |                                                                                                                                                                                             |

### Response

**[models.DatabaseConnectionResponseEnvelope](../../models/databaseconnectionresponseenvelope.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.RestAPIJSONError | 400                     | application/json        |
| errors.Error            | 401                     | application/json        |
| errors.Error            | 500                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |

## get

Get the specified Database Connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatabaseConnectionConfigById" method="get" path="/lib/database-connections/{id}" example="DatabaseConnectionResponseExamplesMySQLDatabaseConnection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
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

**[models.DatabaseConnectionResponseEnvelope](../../models/databaseconnectionresponseenvelope.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Error            | 401                     | application/json        |
| errors.RestAPIJSONError | 404                     | application/json        |
| errors.Error            | 500                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |

## update

Update the specified Database Connection.<br/><br/>Provide a complete representation of the Database Connection that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Database Connection.<br/><br/>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Database Connection might not function as expected.

### Example Usage: DatabaseConnectionBadRequestResponseExamplesInvalidDatabaseConnectionRequest

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionBadRequestResponseExamplesInvalidDatabaseConnectionRequest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesMySQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesMySQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesMySQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="analytics,mysql", text_secret="mysql-analytics-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="Oracle_Pass456!", request_timeout=30000, tags="erp,oracle,finance", text_secret="mysql-production-connection", user="erp_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRETS, database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="yourPassword", request_timeout=30000, tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesOracleWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesOracleWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=20000, creds_secrets="oracle-production-credentials", password="Warehouse_Pass789!", request_timeout=30000, tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="warehouse_user")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesPostgreSQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,postgres,reporting", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesPostgreSQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesPostgreSQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="logs,postgres", text_secret="postgres-logs-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConfigObject

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=60000, tags="reporting,sqlserver,analytics", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,sqlserver,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionExamplesSQLServerWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionExamplesSQLServerWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: DatabaseConnectionResponseExamplesMySQLDatabaseConnection

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="DatabaseConnectionResponseExamplesMySQLDatabaseConnection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesMySQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesMySQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesMySQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesMySQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="analytics,mysql", text_secret="mysql-analytics-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesOracleWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesOracleWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="Oracle_Pass456!", request_timeout=30000, tags="erp,oracle,finance", text_secret="mysql-production-connection", user="erp_user")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesOracleWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesOracleWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRETS, database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="yourPassword", request_timeout=30000, tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesOracleWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesOracleWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=20000, creds_secrets="oracle-production-credentials", password="Warehouse_Pass789!", request_timeout=30000, tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="warehouse_user")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesPostgreSQLWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesPostgreSQLWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="postgresql://warehouse_user:SecurePass456@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,postgres,reporting", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesPostgreSQLWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesPostgreSQLWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="logs,postgres", text_secret="postgres-logs-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesSQLServerWithConfigObject

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesSQLServerWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"report_user\",\"password\":\"Report_Pass123!\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=60000, tags="reporting,sqlserver,analytics", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesSQLServerWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesSQLServerWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=erp_admin;Password=ERP_Pass789!;Encrypt=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,sqlserver,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesSQLServerWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesSQLServerWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateMySQLDatabaseConnectionWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateMySQLDatabaseConnectionWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="production,mysql,customer-data", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateMySQLDatabaseConnectionWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateMySQLDatabaseConnectionWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.MYSQL, description="Analytics MySQL database", id="mysql-analytics-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="analytics,mysql", text_secret="mysql-analytics-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle ERP database", id="oracle-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="oracle.example.com:1521/ORCL", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,oracle,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithCredentialsSecrets

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithCredentialsSecrets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRETS, database_type=models.DatabaseConnectionType.ORACLE, description="High-security Oracle database with credential secrets", id="oracle-secure-db", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-secure-credentials", password="yourPassword", request_timeout=30000, tags="secure,oracle,sensitive-data", text_secret="oracle-secure-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateOracleDatabaseConnectionWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.ORACLE, description="Oracle data warehouse", id="oracle-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=20000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,oracle,reporting", text_secret="oracle-warehouse-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdatePostgreSQLDatabaseConnectionWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdatePostgreSQLDatabaseConnectionWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.POSTGRES, description="Data warehouse PostgreSQL database", id="postgres-warehouse", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="postgresql://yourUsername:yourPassword@postgres.example.com:5432/warehouse?sslmode=require", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="warehouse,postgres,reporting", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdatePostgreSQLDatabaseConnectionWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdatePostgreSQLDatabaseConnectionWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.POSTGRES, description="Logs PostgreSQL database", id="postgres-logs", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="logs,postgres", text_secret="postgres-logs-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithConfigObject

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithConfigObject" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONFIG_OBJ, database_type=models.DatabaseConnectionType.SQLSERVER, description="Reporting SQL Server database with custom config", id="sqlserver-reporting", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"encrypt\":true,\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=60000, tags="reporting,sqlserver,analytics", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithConnectionString

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithConnectionString" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.CONNECTION_STRING, database_type=models.DatabaseConnectionType.SQLSERVER, description="ERP SQL Server database", id="sqlserver-erp", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="Server=sqlserver.example.com;Database=ERP;User Id=yourUsername;Password=yourPassword;Encrypt=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=30000, tags="erp,sqlserver,finance", text_secret="mysql-production-connection", user="yourUsername")

    # Handle response
    print(res)

```
### Example Usage: UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithSecret

<!-- UsageSnippet language="python" operationID="updateDatabaseConnectionConfigById" method="patch" path="/lib/database-connections/{id}" example="UpdateDatabaseConnectionExamplesUpdateSQLServerDatabaseConnectionWithSecret" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.database_connections.update(id_param="<value>", auth_type=models.DatabaseConnectionAuthType.SECRET, database_type=models.DatabaseConnectionType.SQLSERVER, description="CRM SQL Server database", id="sqlserver-crm", config_obj="{\"server\":\"sqlserver.example.com\",\"database\":\"Reporting\",\"user\":\"yourUsername\",\"password\":\"yourPassword\",\"options\":{\"trustServerCertificate\":false,\"connectTimeout\":20000}}", connection_string="mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true", connection_timeout=15000, creds_secrets="oracle-production-credentials", password="yourPassword", request_timeout=15000, tags="crm,sqlserver,sales", text_secret="sqlserver-crm-connection", user="yourUsername")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                   | Type                                                                                                                                                                                        | Required                                                                                                                                                                                    | Description                                                                                                                                                                                 | Example                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_param`                                                                                                                                                                                  | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | The <code>id</code> of the Database Connection to update.                                                                                                                                   |                                                                                                                                                                                             |
| `auth_type`                                                                                                                                                                                 | [models.DatabaseConnectionAuthType](../../models/databaseconnectionauthtype.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                                          | N/A                                                                                                                                                                                         |                                                                                                                                                                                             |
| `database_type`                                                                                                                                                                             | [models.DatabaseConnectionType](../../models/databaseconnectiontype.md)                                                                                                                     | :heavy_check_mark:                                                                                                                                                                          | N/A                                                                                                                                                                                         |                                                                                                                                                                                             |
| `description`                                                                                                                                                                               | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | Brief description of the Database Connection.                                                                                                                                               | Production MySQL database for customer data                                                                                                                                                 |
| `id`                                                                                                                                                                                        | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | Unique identifier for the Database Connection.                                                                                                                                              | mysql-prod-db                                                                                                                                                                               |
| `config_obj`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | JSON configuration object for advanced SQL Server connection settings.                                                                                                                      | {<br/>"server": "sqlserver.example.com",<br/>"database": "Reporting",<br/>"user": "yourUsername",<br/>"password": "yourPassword",<br/>"options": {<br/>"trustServerCertificate": false,<br/>"connectTimeout": 20000<br/>}<br/>} |
| `connection_string`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database connection string with embedded credentials or server information.                                                                                                                 | mysql://yourUsername:yourPassword@mysql.example.com:3306/production?ssl=true                                                                                                                |
| `connection_timeout`                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Maximum time (in milliseconds) to wait when establishing the database connection.                                                                                                           | 10000                                                                                                                                                                                       |
| `creds_secrets`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Name of the stored credentials secret containing username and password. Used with Oracle connections.                                                                                       | oracle-production-credentials                                                                                                                                                               |
| `password`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database password for authentication. Used with Oracle connections.                                                                                                                         | yourPassword                                                                                                                                                                                |
| `request_timeout`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Maximum time (in milliseconds) to wait for a database query to complete. Applies to SQL Server connections only.                                                                            | 30000                                                                                                                                                                                       |
| `tags`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Comma-separated list of tags for categorizing and filtering Database Connections.                                                                                                           | production,mysql,customer-data                                                                                                                                                              |
| `text_secret`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Name of the stored text secret containing the connection string.                                                                                                                            | mysql-production-connection                                                                                                                                                                 |
| `tls`                                                                                                                                                                                       | [Optional[models.TLSClientParams]](../../models/tlsclientparams.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                          | TLS client connection settings.                                                                                                                                                             |                                                                                                                                                                                             |
| `user`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                          | Database username for authentication. Used with Oracle connections.                                                                                                                         | yourUsername                                                                                                                                                                                |
| `retries`                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                         |                                                                                                                                                                                             |

### Response

**[models.DatabaseConnectionResponseEnvelope](../../models/databaseconnectionresponseenvelope.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Error            | 401                     | application/json        |
| errors.RestAPIJSONError | 400, 404                | application/json        |
| errors.Error            | 500                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |

## delete

Delete the specified Database Connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDatabaseConnectionConfigById" method="delete" path="/lib/database-connections/{id}" example="DatabaseConnectionResponseExamplesMySQLDatabaseConnection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
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

**[models.DatabaseConnectionResponseEnvelope](../../models/databaseconnectionresponseenvelope.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Error            | 401                     | application/json        |
| errors.RestAPIJSONError | 404                     | application/json        |
| errors.Error            | 500                     | application/json        |
| errors.APIError         | 4XX, 5XX                | \*/\*                   |