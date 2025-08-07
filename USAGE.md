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

    res = ccp_client.sources.list_source()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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

        res = await ccp_client.sources.list_source_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->