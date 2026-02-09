# LakeDatasets

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

    res = ccp_client.lake_datasets.create(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                       | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Lake to create the Lake Dataset in.                                  |
| `id`                                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `accelerated_fields`                                                                            | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `bucket_name`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `cache_connection`                                                                              | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `deletion_started_at`                                                                           | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `description`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `format_`                                                                                       | [Optional[models.FormatOptionsCriblLakeDataset]](../../models/formatoptionscribllakedataset.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `http_da_used`                                                                                  | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `metrics`                                                                                       | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)                       | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retention_period_in_days`                                                                      | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_config`                                                                                 | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md)             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `storage_location_id`                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `view_name`                                                                                     | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

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

    res = ccp_client.lake_datasets.list(lake_id="<id>", storage_location_id="<id>", format_="<value>", exclude_ddss=True, exclude_deleted=True, exclude_internal=False, exclude_byos=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                       | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Lake that contains the Lake Datasets to list.                        |
| `storage_location_id`                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Filter datasets by storage location ID. Use <code>default</code> for default storage location.  |
| `format_`                                                                                       | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Filter datasets by format. Set to <code>ddss</code> to return only DDSS datasets.               |
| `exclude_ddss`                                                                                  | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Exclude DDSS format datasets from the response.                                                 |
| `exclude_deleted`                                                                               | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Exclude deleted datasets from the response.                                                     |
| `exclude_internal`                                                                              | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Exclude internal datasets (those with IDs starting with <code>cribl_</code>) from the response. |
| `exclude_byos`                                                                                  | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Exclude BYOS (Bring Your Own Storage) datasets from the response.                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

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

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

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

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

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

    res = ccp_client.lake_datasets.update(lake_id="<id>", id_param="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `lake_id`                                                                                       | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Lake that contains the Lake Dataset to update.                       |
| `id_param`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Lake Dataset to update.                                              |
| `accelerated_fields`                                                                            | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `bucket_name`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `cache_connection`                                                                              | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `deletion_started_at`                                                                           | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `description`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `format_`                                                                                       | [Optional[models.FormatOptionsCriblLakeDataset]](../../models/formatoptionscribllakedataset.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `http_da_used`                                                                                  | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `id`                                                                                            | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `metrics`                                                                                       | [Optional[models.LakeDatasetMetrics]](../../models/lakedatasetmetrics.md)                       | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retention_period_in_days`                                                                      | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `search_config`                                                                                 | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md)             | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `storage_location_id`                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `view_name`                                                                                     | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CountedCriblLakeDataset](../../models/countedcribllakedataset.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |