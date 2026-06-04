<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    "https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.tokens.get(password="6j50J9421x29IhO", username="Lilly_Weissnat")

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

        res = await ccp_client.auth.tokens.get_async(password="6j50J9421x29IhO", username="Lilly_Weissnat")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->