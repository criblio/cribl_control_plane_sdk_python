# Lakes.Datasets

## Overview

### Available Operations

* [list](#list) - List all Lake Datasets (Cribl.Cloud only)
* [create](#create) - Create a Lake Dataset (Cribl.Cloud only)
* [get](#get) - Get a Lake Dataset (Cribl.Cloud only)
* [update](#update) - Update a Lake Dataset (Cribl.Cloud only)
* [delete](#delete) - Delete a Lake Dataset (Cribl.Cloud only)

## list

Get a list of all Lake Datasets in the specified Lake (Cribl.Cloud only).

### Example Usage

<!-- UsageSnippet language="python" operationID="getCriblLakeDatasetByLakeId" method="get" path="/products/lake/lakes/{lakeId}/datasets" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.list(lake_id="<id>", storage_location_id="<id>", exclude_ddss=True, exclude_deleted=True, exclude_internal=False, exclude_byos=False)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                                                                                  | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The <code>id</code> of the Lake that contains the Lake Datasets to list.                                                                                   |
| `storage_location_id`                                                                                                                                      | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Filter datasets by storage location ID. Use <code>default</code> for default storage location.                                                             |
| `format_`                                                                                                                                                  | [Optional[models.GetCriblLakeDatasetByLakeIDFormat]](../../models/getcribllakedatasetbylakeidformat.md)                                                    | :heavy_minus_sign:                                                                                                                                         | Filter datasets by format. Set to <code>ddss</code> to return only DDSS datasets.                                                                          |
| `exclude_ddss`                                                                                                                                             | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Exclude DDSS format datasets from the response.                                                                                                            |
| `exclude_netskope`                                                                                                                                         | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Exclude Netskope format datasets from the response.                                                                                                        |
| `exclude_deleted`                                                                                                                                          | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Exclude deleted datasets from the response.                                                                                                                |
| `exclude_internal`                                                                                                                                         | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Exclude internal datasets (those with IDs starting with <code>cribl_</code>) from the response.                                                            |
| `exclude_byos`                                                                                                                                             | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Exclude BYOS (Bring Your Own Storage) datasets from the response.                                                                                          |
| `include_metrics`                                                                                                                                          | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Set to <code>true</code> to include storage metrics for each Lake Dataset. Otherwise, <code>false</code> (default). Requires a Cribl Lake metrics license. |
| `offset`                                                                                                                                                   | *Optional[int]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Pagination offset                                                                                                                                          |
| `limit`                                                                                                                                                    | *Optional[int]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | Maximum number of items to return                                                                                                                          |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |

### Response

**[models.GetCriblLakeDatasetByLakeIDResponse](../../models/getcribllakedatasetbylakeidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Lake Dataset in the specified Lake (Cribl.Cloud only).

### Example Usage: LakeDatasetCreateExamplesJsonDataset

<!-- UsageSnippet language="python" operationID="createCriblLakeDatasetByLakeId" method="post" path="/products/lake/lakes/{lakeId}/datasets" example="LakeDatasetCreateExamplesJsonDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.create(lake_id="<id>", id="web_access_logs", accelerated_fields=[
        "host",
        "status",
    ], description="Web server access logs", format_=models.FormatOptionsCriblLakeDataset.JSON, retention_period_in_days=90, search_config={
        "metadata": {
            "earliest": "-30d",
            "enable_acceleration": False,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "scan_mode": models.ScanMode.DETAILED,
        },
    }, storage_location_id="my-storage-location")

    # Handle response
    print(res)

```
### Example Usage: LakeDatasetCreateExamplesMinimalDataset

<!-- UsageSnippet language="python" operationID="createCriblLakeDatasetByLakeId" method="post" path="/products/lake/lakes/{lakeId}/datasets" example="LakeDatasetCreateExamplesMinimalDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.create(lake_id="<id>", id="app_logs", search_config={
        "metadata": {
            "earliest": "-30d",
            "enable_acceleration": False,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "scan_mode": models.ScanMode.DETAILED,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: LakeDatasetCreateExamplesParquetDataset

<!-- UsageSnippet language="python" operationID="createCriblLakeDatasetByLakeId" method="post" path="/products/lake/lakes/{lakeId}/datasets" example="LakeDatasetCreateExamplesParquetDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.create(lake_id="<id>", id="security_events", description="Security event data in Parquet format", format_=models.FormatOptionsCriblLakeDataset.PARQUET, retention_period_in_days=365, search_config={
        "datatypes": [
            "palo_alto_firewall",
            "crowdstrike_fdr",
        ],
    }, storage_location_id="my-storage-location")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                                            | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The <code>id</code> of the Lake to create the Lake Dataset in.                                                       |
| `id`                                                                                                                 | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | Unique identifier for the Dataset.                                                                                   |
| `accelerated_fields`                                                                                                 | List[*str*]                                                                                                          | :heavy_minus_sign:                                                                                                   | Accelerated fields for the Dataset. Data is partitioned by these fields in storage to improve query performance.     |
| `bucket_name`                                                                                                        | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Name of the legacy Cribl Lake bucket that backs the Dataset. Mutually exclusive with <code>storageLocationId</code>. |
| `cache_connection`                                                                                                   | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                                                  | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `deletion_started_at`                                                                                                | *Optional[float]*                                                                                                    | :heavy_minus_sign:                                                                                                   | Timestamp (in Unix time) when Dataset deletion was initiated, in milliseconds.                                       |
| `description`                                                                                                        | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Brief description of the Dataset.                                                                                    |
| `format_`                                                                                                            | [Optional[models.FormatOptionsCriblLakeDataset]](../../models/formatoptionscribllakedataset.md)                      | :heavy_minus_sign:                                                                                                   | Storage format used for data persisted in the Dataset.                                                               |
| `http_da_used`                                                                                                       | *Optional[bool]*                                                                                                     | :heavy_minus_sign:                                                                                                   | If <code>true</code>, the Dataset is used by Direct Access HTTP. Otherwise, <code>false</code>.                      |
| `metrics`                                                                                                            | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)                                            | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `retention_period_in_days`                                                                                           | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Dataset retention period, in days.                                                                                   |
| `search_config`                                                                                                      | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md)                                  | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `storage_class`                                                                                                      | [Optional[models.StorageClassOptionsCriblLakeDataset]](../../models/storageclassoptionscribllakedataset.md)          | :heavy_minus_sign:                                                                                                   | Storage class used for objects written to the Dataset.                                                               |
| `storage_location_id`                                                                                                | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Unique identifier for the Storage Location that backs the Dataset. Mutually exclusive with <code>bucketName</code>.  |
| `view_name`                                                                                                          | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Name of the ClickHouse view for the Dataset on the Lakehouse.                                                        |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Lake Dataset in the specified Lake (Cribl.Cloud only).

### Example Usage

<!-- UsageSnippet language="python" operationID="getCriblLakeDatasetByLakeIdAndId" method="get" path="/products/lake/lakes/{lakeId}/datasets/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.get(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                                                                                  | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The <code>id</code> of the Lake that contains the Lake Dataset to get.                                                                                     |
| `id`                                                                                                                                                       | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The <code>id</code> of the Lake Dataset to get.                                                                                                            |
| `include_metrics`                                                                                                                                          | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Set to <code>true</code> to include storage metrics for each Lake Dataset. Otherwise, <code>false</code> (default). Requires a Cribl Lake metrics license. |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Lake Dataset in the specified Lake (Cribl.Cloud only).

### Example Usage: LakeDatasetUpdateExamplesUpdateDescription

<!-- UsageSnippet language="python" operationID="updateCriblLakeDatasetByLakeIdAndId" method="patch" path="/products/lake/lakes/{lakeId}/datasets/{id}" example="LakeDatasetUpdateExamplesUpdateDescription" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.update(lake_id="<id>", id_param="<value>", accelerated_fields=[
        "host",
        "status",
        "source",
    ], description="Web server access logs with accelerated fields.", search_config={
        "metadata": {
            "earliest": "-30d",
            "enable_acceleration": False,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "scan_mode": models.ScanMode.QUICK,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: LakeDatasetUpdateExamplesUpdateRetention

<!-- UsageSnippet language="python" operationID="updateCriblLakeDatasetByLakeIdAndId" method="patch" path="/products/lake/lakes/{lakeId}/datasets/{id}" example="LakeDatasetUpdateExamplesUpdateRetention" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.update(lake_id="<id>", id_param="<value>", retention_period_in_days=180, search_config={
        "metadata": {
            "earliest": "-30d",
            "enable_acceleration": False,
            "field_list": [
                "<value 1>",
                "<value 2>",
            ],
            "scan_mode": models.ScanMode.QUICK,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                                            | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The <code>id</code> of the Lake that contains the Lake Dataset to update.                                            |
| `id_param`                                                                                                           | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The <code>id</code> of the Lake Dataset to update.                                                                   |
| `accelerated_fields`                                                                                                 | List[*str*]                                                                                                          | :heavy_minus_sign:                                                                                                   | Accelerated fields for the Dataset. Data is partitioned by these fields in storage to improve query performance.     |
| `bucket_name`                                                                                                        | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Name of the legacy Cribl Lake bucket that backs the Dataset. Mutually exclusive with <code>storageLocationId</code>. |
| `cache_connection`                                                                                                   | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                                                  | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `deletion_started_at`                                                                                                | *Optional[float]*                                                                                                    | :heavy_minus_sign:                                                                                                   | Timestamp (in Unix time) when Dataset deletion was initiated, in milliseconds.                                       |
| `description`                                                                                                        | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Brief description of the Dataset.                                                                                    |
| `format_`                                                                                                            | [Optional[models.FormatOptionsCriblLakeDataset]](../../models/formatoptionscribllakedataset.md)                      | :heavy_minus_sign:                                                                                                   | Storage format used for data persisted in the Dataset.                                                               |
| `http_da_used`                                                                                                       | *Optional[bool]*                                                                                                     | :heavy_minus_sign:                                                                                                   | If <code>true</code>, the Dataset is used by Direct Access HTTP. Otherwise, <code>false</code>.                      |
| `id`                                                                                                                 | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Unique identifier for the Dataset. Optional; the path parameter <code>id</code> is authoritative.                    |
| `metrics`                                                                                                            | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)                                            | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `retention_period_in_days`                                                                                           | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Dataset retention period, in days.                                                                                   |
| `search_config`                                                                                                      | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md)                                  | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `storage_class`                                                                                                      | [Optional[models.StorageClassOptionsCriblLakeDataset]](../../models/storageclassoptionscribllakedataset.md)          | :heavy_minus_sign:                                                                                                   | Storage class used for objects written to the Dataset.                                                               |
| `storage_location_id`                                                                                                | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Unique identifier for the Storage Location that backs the Dataset. Mutually exclusive with <code>bucketName</code>.  |
| `view_name`                                                                                                          | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Name of the ClickHouse view for the Dataset on the Lakehouse.                                                        |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Lake Dataset in the specified Lake (Cribl.Cloud only).

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteCriblLakeDatasetByLakeIdAndId" method="delete" path="/products/lake/lakes/{lakeId}/datasets/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lakes.datasets.delete(lake_id="<id>", id="<id>")

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

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |