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

### Example Usage

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" -->
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
        type=models.JobTypeOptionsSavedJobCollection.EXECUTOR,
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
            run=models.ScheduleTypeSavedJobCollectionRunSettings(
                type=models.ScheduleTypeSavedJobCollectionType.COLLECTION,
                reschedule_dropped_tasks=True,
                max_task_reschedule=1,
                log_level=models.ScheduleTypeSavedJobCollectionLogLevel.INFO,
                job_timeout="0",
                mode="list",
                time_range_type="relative",
                earliest=432.8,
                latest=2023.34,
                timestamp_timezone="<value>",
                time_warning=models.TimeWarning(),
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
        collector=models.CollectorTypeSavedJobCollection(
            type="<value>",
            conf=models.CollectorScript(
                type=models.CollectorScriptType.SCRIPT,
                discover_script="<value>",
                collect_script="<value>",
                shell="/bin/bash",
                env_vars=[
                    models.EnvVar(
                        name="<value>",
                        value="<value>",
                    ),
                ],
            ),
            destructive=False,
            encoding="<value>",
        ),
        input=models.InputTypeSavedJobCollection(
            type=models.TypeOptionsSavedJobCollectionInput.COLLECTION,
            breaker_rulesets=[
                "<value 1>",
            ],
            stale_channel_flush_ms=10000,
            send_to_routes=True,
            preprocess=models.PreprocessTypeSavedJobCollectionInput(
                disabled=True,
                command="<value>",
                args=[
                    "<value 1>",
                ],
            ),
            throttle_rate_per_sec="0",
            metadata=[
                models.ItemsTypeNotificationMetadata(
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

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" -->
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
        type=models.JobTypeOptionsSavedJobCollection.SCHEDULED_SEARCH,
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
            run=models.ScheduleTypeSavedJobCollectionRunSettings(
                type=models.ScheduleTypeSavedJobCollectionType.COLLECTION,
                reschedule_dropped_tasks=True,
                max_task_reschedule=1,
                log_level=models.ScheduleTypeSavedJobCollectionLogLevel.INFO,
                job_timeout="0",
                mode="list",
                time_range_type="relative",
                earliest=9142.96,
                latest=521.08,
                timestamp_timezone="<value>",
                time_warning=models.TimeWarning(),
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
        collector=models.CollectorTypeSavedJobCollection(
            type="<value>",
            conf=models.CollectorHealthCheckHealthCheck1(
                collect_method=models.HealthCheckMethod1.GET,
                collect_request_params=[
                    models.ItemsTypeCollectRequestParams(
                        name="<value>",
                        value="<value>",
                    ),
                ],
                discovery=models.CollectorHealthCheckDiscovery1(
                    discover_type=models.CollectorHealthCheckDiscoverType1.NONE,
                ),
                collect_url="https://shameful-vicinity.com/",
                collect_body="`{ }`",
                collect_request_headers=[
                    models.CollectorHealthCheckCollectRequestHeader1(
                        name="<value>",
                        value="<value>",
                    ),
                ],
                authenticate_collect=False,
                authentication=models.CollectorHealthCheckAuthentication1.NONE,
                timeout=30,
                reject_unauthorized=False,
                default_breakers=models.HiddenDefaultBreakersOptions.CRIBL,
                safe_headers=[
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                retry_rules=models.CollectorHealthCheckRetryRules1(
                    type=models.RetryTypeOptionsRetryRules.BACKOFF,
                    interval="<value>",
                    limit="<value>",
                    multiplier="<value>",
                    codes="<value>",
                    enable_header="<value>",
                ),
                username="Daphnee_Schimmel-Wolf26",
                password="qwZ927mZOVqnV8W",
                credentials_secret="<value>",
                login_url="",
                login_body="`{ \"username\": \"${username}\", \"password\": \"${password}\" }`",
                token_resp_attribute="<value>",
                auth_header_expr="`Bearer ${token}`",
                auth_request_headers=[
                    models.ItemsTypeAuthRequestHeaders(
                        name="<value>",
                        value="<value>",
                    ),
                ],
                client_secret_param_name="client_secret",
                client_secret_param_value="<value>",
                auth_request_params=[
                    models.ItemsTypeAuthRequestParams(
                        name="<value>",
                        value="<value>",
                    ),
                ],
                text_secret="<value>",
                type=models.CollectorHealthCheckType1.HEALTH_CHECK,
            ),
            destructive=False,
            encoding="<value>",
        ),
        input=models.InputTypeSavedJobCollection(
            type=models.TypeOptionsSavedJobCollectionInput.COLLECTION,
            breaker_rulesets=[
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            stale_channel_flush_ms=10000,
            send_to_routes=True,
            preprocess=models.PreprocessTypeSavedJobCollectionInput(
                disabled=True,
                command="<value>",
                args=[
                    "<value 1>",
                    "<value 2>",
                ],
            ),
            throttle_rate_per_sec="0",
            metadata=[
                models.ItemsTypeNotificationMetadata(
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