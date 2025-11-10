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

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
        "cache_ref": "<value>",
        "created_at": 7795.06,
        "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
        "migration_query_id": "<id>",
        "retention_in_days": 1466.58,
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.FormatOptions.DDSS, http_da_used=True, metrics={
        "current_size_bytes": 6170.04,
        "metrics_date": "<value>",
    }, retention_period_in_days=456.37, search_config={
        "datatypes": [
            "<value 1>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": True,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 4334.7,
                "finished_at": 6811.22,
                "latest_scanned_time": 5303.3,
                "object_count": 9489.04,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>")

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

        res = await ccp_client.lake_datasets.create_async(lake_id="<id>", id="<id>", accelerated_fields=[
            "<value 1>",
            "<value 2>",
        ], bucket_name="<value>", cache_connection={
            "accelerated_fields": [
                "<value 1>",
                "<value 2>",
            ],
            "backfill_status": models.CacheConnectionBackfillStatus.PENDING,
            "cache_ref": "<value>",
            "created_at": 7795.06,
            "lakehouse_connection_type": models.LakehouseConnectionType.CACHE,
            "migration_query_id": "<id>",
            "retention_in_days": 1466.58,
        }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.FormatOptions.DDSS, http_da_used=True, metrics={
            "current_size_bytes": 6170.04,
            "metrics_date": "<value>",
        }, retention_period_in_days=456.37, search_config={
            "datatypes": [
                "<value 1>",
            ],
            "metadata": {
                "earliest": "<value>",
                "enable_acceleration": True,
                "field_list": [
                    "<value 1>",
                    "<value 2>",
                ],
                "latest_run_info": {
                    "earliest_scanned_time": 4334.7,
                    "finished_at": 6811.22,
                    "latest_scanned_time": 5303.3,
                    "object_count": 9489.04,
                },
                "scan_mode": models.ScanMode.DETAILED,
            },
        }, storage_location_id="<id>", view_name="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->