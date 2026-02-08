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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "which um whenever pro chase video uh-huh atop baritone yum",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 7324.19,
                "latest": 6945.52,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "cautiously annual worth before cleaner parsnip nimble onset once burgeon",
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 2728.52,
                "latest": 4162.9,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "pomelo outside offensively ew",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 432.8,
                "latest": 2023.34,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "pomelo outside offensively ew",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 432.8,
                "latest": 2023.34,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "cautiously annual worth before cleaner parsnip nimble onset once burgeon",
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 2728.52,
                "latest": 4162.9,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job=models.SavedJobCollection(
        id="<id>",
        description="pomelo outside offensively ew",
        type=models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        ttl="4h",
        ignore_group_jobs_limit=False,
        remove_fields=[
            "<value 1>",
            "<value 2>",
        ],
        resume_on_boot=False,
        environment="<value>",
        schedule=models.ScheduleTypeSavedJobCollection(
            enabled=True,
            skippable=True,
            resume_missed=False,
            cron_schedule="*/5 * * * *",
            max_concurrent_runs=1,
            run=models.RunSettingsTypeSavedJobCollectionSchedule(
                type=models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                reschedule_dropped_tasks=True,
                max_task_reschedule=1,
                log_level=models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                job_timeout="0",
                mode="list",
                time_range_type="relative",
                earliest=432.8,
                latest=2023.34,
                timestamp_timezone="<value>",
                time_warning=models.MetricsStore(),
                expression="true",
                min_task_size="1MB",
                max_task_size="10MB",
            ),
        ),
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        worker_affinity=False,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
                query_validation_enabled=True,
                default_breakers=models.HiddenDefaultBreakersOptionsDatabaseCollectorConf.CRIBL,
                scheduling=models.DatabaseCollectorConfScheduling(
                    state_tracking=models.DatabaseCollectorConfStateTracking(
                        enabled=True,
                    ),
                ),
            ),
            destructive=True,
            encoding="<value>",
        ),
        input=models.TypeCollectionWithBreakerRulesetsConstraint(
            type=models.TypeCollectionWithBreakerRulesetsConstraintType.COLLECTION,
            breaker_rulesets=[
                "<value 1>",
            ],
            stale_channel_flush_ms=10000,
            send_to_routes=True,
            preprocess=models.PreprocessType(
                disabled=True,
                command="<value>",
                args=[
                    "<value 1>",
                ],
            ),
            throttle_rate_per_sec="0",
            metadata=[
                models.ItemsTypeMetadata(
                    name="<value>",
                    value="<value>",
                ),
            ],
            pipeline="<value>",
            output="<value>",
        ),
    ), cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "pomelo outside offensively ew",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 432.8,
                "latest": 2023.34,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "cautiously annual worth before cleaner parsnip nimble onset once burgeon",
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 2728.52,
                "latest": 4162.9,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(saved_job={
        "id": "<id>",
        "description": "cautiously annual worth before cleaner parsnip nimble onset once burgeon",
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 2728.52,
                "latest": 4162.9,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `saved_job`                                                         | [models.SavedJob](../../models/savedjob.md)                         | :heavy_check_mark:                                                  | SavedJob object                                                     |
| `cribl_pack`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The <code>id</code> of the Pack to create the Collector in.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
    server_url="https://api.example.com",
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
    server_url="https://api.example.com",
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
    server_url="https://api.example.com",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "wee supposing blaring spectate dark",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": False,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 4891.8,
                "latest": 5936.75,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        id="<id>",
        description="unabashedly notwithstanding ugh digestive",
        type=models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        ttl="4h",
        ignore_group_jobs_limit=False,
        remove_fields=[
            "<value 1>",
            "<value 2>",
        ],
        resume_on_boot=False,
        environment="<value>",
        schedule=models.ScheduleTypeSavedJobCollection(
            enabled=True,
            skippable=True,
            resume_missed=False,
            cron_schedule="*/5 * * * *",
            max_concurrent_runs=1,
            run=models.RunSettingsTypeSavedJobCollectionSchedule(
                type=models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                reschedule_dropped_tasks=True,
                max_task_reschedule=1,
                log_level=models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                job_timeout="0",
                mode="list",
                time_range_type="relative",
                earliest=9142.96,
                latest=521.08,
                timestamp_timezone="<value>",
                time_warning=models.MetricsStore(),
                expression="true",
                min_task_size="1MB",
                max_task_size="10MB",
            ),
        ),
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        worker_affinity=False,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
                query_validation_enabled=True,
                default_breakers=models.HiddenDefaultBreakersOptionsDatabaseCollectorConf.CRIBL,
                scheduling=models.DatabaseCollectorConfScheduling(
                    state_tracking=models.DatabaseCollectorConfStateTracking(
                        enabled=False,
                    ),
                ),
            ),
            destructive=True,
            encoding="<value>",
        ),
        input=models.TypeCollectionWithBreakerRulesetsConstraint(
            type=models.TypeCollectionWithBreakerRulesetsConstraintType.COLLECTION,
            breaker_rulesets=[
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            stale_channel_flush_ms=10000,
            send_to_routes=True,
            preprocess=models.PreprocessType(
                disabled=True,
                command="<value>",
                args=[
                    "<value 1>",
                    "<value 2>",
                ],
            ),
            throttle_rate_per_sec="0",
            metadata=[
                models.ItemsTypeMetadata(
                    name="<value>",
                    value="<value>",
                ),
            ],
            pipeline="<value>",
            output="<value>",
        ),
    ), cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "unabashedly notwithstanding ugh digestive",
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 9142.96,
                "latest": 521.08,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "wee supposing blaring spectate dark",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": False,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 4891.8,
                "latest": 5936.75,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "horde before huzzah apud ha even murky favorite",
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": False,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 6033.18,
                "latest": 6852.51,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        id="<id>",
        description="unabashedly notwithstanding ugh digestive",
        type=models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        ttl="4h",
        ignore_group_jobs_limit=False,
        remove_fields=[
            "<value 1>",
            "<value 2>",
        ],
        resume_on_boot=False,
        environment="<value>",
        schedule=models.ScheduleTypeSavedJobCollection(
            enabled=True,
            skippable=True,
            resume_missed=False,
            cron_schedule="*/5 * * * *",
            max_concurrent_runs=1,
            run=models.RunSettingsTypeSavedJobCollectionSchedule(
                type=models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                reschedule_dropped_tasks=True,
                max_task_reschedule=1,
                log_level=models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                job_timeout="0",
                mode="list",
                time_range_type="relative",
                earliest=9142.96,
                latest=521.08,
                timestamp_timezone="<value>",
                time_warning=models.MetricsStore(),
                expression="true",
                min_task_size="1MB",
                max_task_size="10MB",
            ),
        ),
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        worker_affinity=False,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
                query_validation_enabled=True,
                default_breakers=models.HiddenDefaultBreakersOptionsDatabaseCollectorConf.CRIBL,
                scheduling=models.DatabaseCollectorConfScheduling(
                    state_tracking=models.DatabaseCollectorConfStateTracking(
                        enabled=False,
                    ),
                ),
            ),
            destructive=True,
            encoding="<value>",
        ),
        input=models.TypeCollectionWithBreakerRulesetsConstraint(
            type=models.TypeCollectionWithBreakerRulesetsConstraintType.COLLECTION,
            breaker_rulesets=[
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            stale_channel_flush_ms=10000,
            send_to_routes=True,
            preprocess=models.PreprocessType(
                disabled=True,
                command="<value>",
                args=[
                    "<value 1>",
                    "<value 2>",
                ],
            ),
            throttle_rate_per_sec="0",
            metadata=[
                models.ItemsTypeMetadata(
                    name="<value>",
                    value="<value>",
                ),
            ],
            pipeline="<value>",
            output="<value>",
        ),
    ), cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "unabashedly notwithstanding ugh digestive",
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 9142.96,
                "latest": 521.08,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "saved_query_id": "<id>",
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "wee supposing blaring spectate dark",
        "type": models.JobTypeOptionsRunnableJobCollection.EXECUTOR,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": False,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 4891.8,
                "latest": 5936.75,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "id": "<id>",
        "description": "unabashedly notwithstanding ugh digestive",
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "remove_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "resume_on_boot": False,
        "environment": "<value>",
        "schedule": {
            "enabled": True,
            "skippable": True,
            "resume_missed": False,
            "cron_schedule": "*/5 * * * *",
            "max_concurrent_runs": 1,
            "run": {
                "type": models.RunSettingsTypeSavedJobCollectionScheduleType.COLLECTION,
                "reschedule_dropped_tasks": True,
                "max_task_reschedule": 1,
                "log_level": models.LogLevelOptionsRunnableJobCollectionScheduleRun.INFO,
                "job_timeout": "0",
                "mode": "list",
                "time_range_type": "relative",
                "earliest": 9142.96,
                "latest": 521.08,
                "timestamp_timezone": "<value>",
                "time_warning": {},
                "expression": "true",
                "min_task_size": "1MB",
                "max_task_size": "10MB",
            },
        },
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "executor": {
            "type": "<value>",
            "store_task_results": True,
            "conf": {},
        },
    }, cribl_pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Collector to update.                        |
| `saved_job`                                                            | [models.SavedJob](../../models/savedjob.md)                            | :heavy_check_mark:                                                     | SavedJob object                                                        |
| `cribl_pack`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The <code>id</code> of the Pack that includes the Collector to update. |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.CountedSavedJob](../../models/countedsavedjob.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |