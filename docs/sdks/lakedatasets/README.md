# LakeDatasets
(*lake_datasets*)

## Overview

### Available Operations

* [create](#create) - Create a Lake Dataset
* [list](#list) - List all Lake Datasets
* [delete](#delete) - Delete a Lake Dataset
* [get](#get) - Get a Lake Dataset
* [update](#update) - Update a Lake Dataset

## create

Create a new Lake Dataset in the specified Lake.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCriblLakeDatasetByLakeId" method="post" path="/products/lake/lakes/{lakeId}/datasets" -->
```python
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
    }, deletion_started_at=8310.58, description="pleased toothbrush long brush smooth swiftly rightfully phooey chapel", format_=models.CriblLakeDatasetFormat.DDSS, http_da_used=True, metrics={
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

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `lake_id`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | The <code>id</code> of the Lake to create the Lake Dataset in.                      |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `accelerated_fields`                                                                | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `bucket_name`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `cache_connection`                                                                  | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                 | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `deletion_started_at`                                                               | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `format_`                                                                           | [Optional[models.CriblLakeDatasetFormat]](../../models/cribllakedatasetformat.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `http_da_used`                                                                      | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `metrics`                                                                           | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)           | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retention_period_in_days`                                                          | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `search_config`                                                                     | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `storage_location_id`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `view_name`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CountedListCriblLakeDataset](../../models/countedlistcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of all Lake Datasets in the specified Lake.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCriblLakeDatasetByLakeId" method="get" path="/products/lake/lakes/{lakeId}/datasets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.list(lake_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `lake_id`                                                                | *str*                                                                    | :heavy_check_mark:                                                       | The <code>id</code> of the Lake that contains the Lake Datasets to list. |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[models.CountedListCriblLakeDataset](../../models/countedlistcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Lake Dataset in the specified Lake

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteCriblLakeDatasetByLakeIdAndId" method="delete" path="/products/lake/lakes/{lakeId}/datasets/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.delete(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `lake_id`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake that contains the Lake Dataset to delete. |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake Dataset to delete.                        |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CountedListCriblLakeDataset](../../models/countedlistcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Lake Dataset in the specified Lake.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCriblLakeDatasetByLakeIdAndId" method="get" path="/products/lake/lakes/{lakeId}/datasets/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.get(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `lake_id`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Lake that contains the Lake Dataset to get. |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Lake Dataset to get.                        |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.CountedListCriblLakeDataset](../../models/countedlistcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Lake Dataset in the specified Lake.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCriblLakeDatasetByLakeIdAndId" method="patch" path="/products/lake/lakes/{lakeId}/datasets/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake_datasets.update(lake_id="<id>", id_param="<value>", accelerated_fields=[
        "<value 1>",
        "<value 2>",
    ], bucket_name="<value>", cache_connection={
        "accelerated_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "backfill_status": models.CacheConnectionBackfillStatus.INCOMPLETE,
        "cache_ref": "<value>",
        "created_at": 267.92,
        "lakehouse_connection_type": models.LakehouseConnectionType.ZERO_POINT,
        "migration_query_id": "<id>",
        "retention_in_days": 3769.62,
    }, deletion_started_at=836.59, description="highlight phew ponder but winding", format_=models.CriblLakeDatasetUpdateFormat.JSON, http_da_used=True, id="<id>", metrics={
        "current_size_bytes": 6237.74,
        "metrics_date": "<value>",
    }, retention_period_in_days=602.09, search_config={
        "datatypes": [
            "<value 1>",
            "<value 2>",
        ],
        "metadata": {
            "earliest": "<value>",
            "enable_acceleration": False,
            "field_list": [
                "<value 1>",
            ],
            "latest_run_info": {
                "earliest_scanned_time": 7659.78,
                "finished_at": 6404.38,
                "latest_scanned_time": 4426.77,
                "object_count": 8849.28,
            },
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="<id>", view_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                     | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Lake that contains the Lake Dataset to update.                     |
| `id_param`                                                                                    | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Lake Dataset to update.                                            |
| `accelerated_fields`                                                                          | List[*str*]                                                                                   | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `bucket_name`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `cache_connection`                                                                            | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                           | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `deletion_started_at`                                                                         | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `description`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `format_`                                                                                     | [Optional[models.CriblLakeDatasetUpdateFormat]](../../models/cribllakedatasetupdateformat.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `http_da_used`                                                                                | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `id`                                                                                          | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `metrics`                                                                                     | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)                     | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retention_period_in_days`                                                                    | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `search_config`                                                                               | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md)           | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `storage_location_id`                                                                         | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `view_name`                                                                                   | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedListCriblLakeDataset](../../models/countedlistcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |