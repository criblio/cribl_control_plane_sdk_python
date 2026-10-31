<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    "https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="yourPassword", username="yourUsername")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from cribl_control_plane import CriblControlPlane

async def main():

    async with CriblControlPlane(
        "https://api.example.com",
    ) as ccp_client:

        res = await ccp_client.auth.tokens.get_async(password="yourPassword", username="yourUsername")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->