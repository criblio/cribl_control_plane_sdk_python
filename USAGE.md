<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from cribl_control_plane import CriblControlPlane, models
import os

async def main():

    async with CriblControlPlane(
        server_url="https://api.example.com",
        security=models.Security(
            bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
        ),
    ) as ccp_client:

        res = await ccp_client.database_connections.create_async(auth_type="connectionString", database_type=models.DatabaseConnectionType.MYSQL, description="Production MySQL database for customer data", id="mysql-prod-db", config_obj="<value>", connection_string="mysql://admin:password123@mysql.example.com:3306/production?ssl=true", connection_timeout=10000, creds_secrets="<value>", password="QpvMa8DI_lUJL_b", request_timeout=4657.19, tags="production,mysql,customer-data", user="Dolores.Feil")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->