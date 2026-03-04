# Collectors

## Overview

Actions related to Collectors

### Available Operations

* [create](#create) - Create a Collector
* [list](#list) - List all Collectors
* [delete](#delete) - Delete a Collector
* [get](#get) - Get a Collector
* [update](#update) - Update a Collector

## create

Create a new Collector.

### Example Usage: CollectorExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="azure-blob-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */8 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="cribl-lake-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="database-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="filesystem-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="gcs-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */12 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="rest-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */4 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="s3-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */6 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="script-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */3 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(id="splunk-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */1 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                     | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `type`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Job type: collection, executor, or scheduledSearch.                                                                                                                                      |
| `cribl_pack`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | The <code>id</code> of the Pack to create the Collector in.                                                                                                                              |
| `environment`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere.                                                                                     |
| `group_id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Worker Group ID to run the job in. When empty, uses the default group.                                                                                                                   |
| `ignore_group_jobs_limit`                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | When enabled, this job's artifacts are not counted toward the Worker Group's finished job artifacts limit. Artifacts will be removed only after the Collector's configured time to live. |
| `resume_on_boot`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Resume the ad hoc job if a failure condition causes Stream to restart during job execution.                                                                                              |
| `schedule`                                                                                                                                                                               | [Optional[models.ScheduleOpts]](../../models/scheduleopts.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `ttl`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector.                                                          |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of all Collectors.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSavedJob" method="get" path="/lib/jobs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.list(collector_type="<value>", cribl_pack="<value>", group_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `collector_type`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by collector type                                            |
| `cribl_pack`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Pack ID                                                             |
| `group_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Worker group ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Collector.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSavedJobById" method="delete" path="/lib/jobs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.delete(id="<id>", cribl_pack="<value>", group_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The <code>id</code> of the Collector to delete.                                |
| `cribl_pack`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The <code>id</code> of the Pack that includes the Collector to delete.         |
| `group_id`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The <code>id</code> of the Worker Group that includes the Collector to delete. |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Collector.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSavedJobById" method="get" path="/lib/jobs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.get(id="<id>", cribl_pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Collector to get.                        |
| `cribl_pack`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The <code>id</code> of the Pack that includes the Collector to get. |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Collector.<br><br>Provide a complete representation of the Collector that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Collector.<br><br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Collector might not function as expected.

### Example Usage: CollectorExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="azure-blob-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */8 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="cribl-lake-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="database-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="filesystem-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */2 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="gcs-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */12 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="rest-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */4 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="s3-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */6 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="script-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */3 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id_param="<id>", id="splunk-collector", type_="collection", cribl_pack="<value>", schedule=models.ScheduleOpts(
        cron_schedule="0 */1 * * *",
        enabled=True,
        run=models.RunSettings(
            **{
                "mode": "run",
                "timeRangeType": "relative",
                "earliest": -300,
                "expression": "true",
                "logLevel": "info",
            },
        ),
        tz="UTC",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_param`                                                                                                                                                                               | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The <code>id</code> of the Collector to update.                                                                                                                                          |
| `id`                                                                                                                                                                                     | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `type`                                                                                                                                                                                   | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Job type: collection, executor, or scheduledSearch.                                                                                                                                      |
| `cribl_pack`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | The <code>id</code> of the Pack that includes the Collector to update.                                                                                                                   |
| `environment`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere.                                                                                     |
| `group_id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Worker Group ID to run the job in. When empty, uses the default group.                                                                                                                   |
| `ignore_group_jobs_limit`                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | When enabled, this job's artifacts are not counted toward the Worker Group's finished job artifacts limit. Artifacts will be removed only after the Collector's configured time to live. |
| `resume_on_boot`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Resume the ad hoc job if a failure condition causes Stream to restart during job execution.                                                                                              |
| `schedule`                                                                                                                                                                               | [Optional[models.ScheduleOpts]](../../models/scheduleopts.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `ttl`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector.                                                          |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |