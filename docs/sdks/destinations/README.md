# Destinations

## Overview

Actions related to Destinations

### Available Operations

* [list](#list) - List all Destinations
* [create](#create) - Create a Destination
* [get](#get) - Get a Destination
* [update](#update) - Update a Destination
* [delete](#delete) - Delete a Destination

## list

Get a list of all Destinations.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOutput" method="get" path="/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Destination.

### Example Usage: OutputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "azure-blob-output",
        "type": models.CreateOutputTypeAzureBlob.AZURE_BLOB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "container_name": "my-container",
        "create_container": False,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "max_concurrent_file_parts": 1,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "storage_class": models.CreateOutputBlobAccessTier.INFERRED,
        "description": "each before down ouch inexperienced below vaguely celebrated past quizzically",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "connection_string": "<value>",
        "text_secret": "<value>",
        "storage_account_name": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "azure_cloud": "<value>",
        "endpoint_suffix": "<value>",
        "client_text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "template_container_name": "<value>",
        "template_format": "<value>",
        "template_connection_string": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureDataExplorer

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesAzureDataExplorer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "azure-data-explorer-output",
        "type": models.CreateOutputTypeAzureDataExplorer.AZURE_DATA_EXPLORER,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "validate_database_settings": True,
        "ingest_mode": models.CreateOutputIngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.CreateOutputAuthenticationMethodAzureDataExplorer.CLIENT_SECRET,
        "description": "rationale fundraising er muffled",
        "client_secret": "client-secret",
        "text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_enabled": False,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://precious-transparency.org/",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "max_concurrent_file_parts": 1,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "add_id_to_stage_path": True,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "timeout_sec": 30,
        "flush_immediately": False,
        "retain_blob_on_success": False,
        "extent_tags": [
            {
                "prefix": models.CreateOutputPrefixOptional.INGEST_BY,
                "value": "<value>",
            },
        ],
        "ingest_if_not_exists": [
            {
                "value": "<value>",
            },
        ],
        "report_level": models.CreateOutputReportLevel.FAILURES_ONLY,
        "report_method": models.CreateOutputReportMethod.QUEUE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 5522.82,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "flush_period_sec": 1,
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "keep_alive": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_cluster_url": "https://breakable-backburn.info",
        "template_database": "<value>",
        "template_table": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_client_secret": "<value>",
        "template_format": "<value>",
        "template_ingest_url": "https://animated-discourse.info/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureEventhub

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesAzureEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "azure-eventhub-output",
        "type": models.CreateOutputTypeAzureEventhub.AZURE_EVENTHUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.LEADER,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 768,
        "flush_event_count": 1000,
        "flush_period_sec": 1,
        "connection_timeout": 10000,
        "request_timeout": 60000,
        "max_retries": 5,
        "max_back_off": 30000,
        "initial_backoff": 300,
        "backoff_rate": 2,
        "authentication_timeout": 10000,
        "reauthentication_threshold": 10000,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "7VJ9TjHGl3iVy2A",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "$ConnectionString",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.MANUAL,
            "client_secret": "<value>",
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "monthly although strident replacement boo phrase after",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureLogs

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesAzureLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "azure-logs-output",
        "type": models.CreateOutputTypeAzureLogs.AZURE_LOGS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "log_type": "Cribl",
        "resource_id": "<id>",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "api_url": ".ods.opinsights.azure.com",
        "response_retry_settings": [
            {
                "http_status": 2572.31,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputAuthenticationMethodAzureLogs.MANUAL,
        "description": "rival consign pressure",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
        "keypair_secret": "<value>",
        "template_workspace_id": "<id>",
        "template_workspace_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesChronicle

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "chronicle-output",
        "type": models.CreateOutputTypeChronicle.CHRONICLE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "api_version": "v1alpha",
        "authentication_method": models.CreateOutputAuthenticationMethodChronicle.SERVICE_ACCOUNT,
        "response_retry_settings": [
            {
                "http_status": 3484.86,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 90,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 1733.6,
        "ingestion_method": "ImportLogs",
        "namespace": "<value>",
        "log_type": "UNKNOWN",
        "log_text_field": "<value>",
        "gcp_project_id": "my-project",
        "gcp_instance": "customer-id",
        "custom_labels": [
            {
                "key": "<key>",
                "value": "<value>",
                "rbac_enabled": False,
            },
        ],
        "description": "loyally glider till hunger but ouch gosh geez ick warmly",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesClickHouse

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesClickHouse" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "clickhouse-output",
        "type": models.CreateOutputTypeClickHouse.CLICK_HOUSE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "http://localhost:8123/",
        "auth_type": models.CreateOutputAuthenticationTypeClickHouse.NONE,
        "database": "mydb",
        "table_name": "mytable",
        "format_": models.CreateOutputFormatClickHouse.JSON_COMPACT_EACH_ROW_WITH_NAMES,
        "mapping_type": models.CreateOutputMappingType.AUTOMATIC,
        "async_inserts": False,
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 4759.15,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "dump_format_errors_to_disk": False,
        "stats_destination": {
            "url": "https://torn-fuel.name/",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Shaniya77",
            "sql_username": "<value>",
            "password": "98PkMUDqunaXk0y",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "so sans bah rear once throughout outrageous following birth",
        "username": "Marshall2",
        "password": "bE8HycltTILd6LR",
        "credentials_secret": "<value>",
        "sql_username": "<value>",
        "wait_for_async_inserts": True,
        "exclude_mapping_fields": [
            "<value 1>",
        ],
        "describe_table": "<value>",
        "column_mappings": [
            {
                "column_name": "<value>",
                "column_type": "<value>",
                "column_value_expression": "<value>",
            },
        ],
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://sticky-granny.net/",
        "template_database": "<value>",
        "template_table_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudflareR2

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCloudflareR2" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cloudflare-r2-output",
        "type": models.CreateOutputTypeCloudflareR2.CLOUDFLARE_R2,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.CreateOutputAuthenticationMethodCloudflareR2.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "description": "kiddingly lively provided neatly importance instantly effector",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudwatch

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCloudwatch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cloudwatch-output",
        "type": models.CreateOutputTypeCloudwatch.CLOUDWATCH,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "max_queue_size": 5,
        "max_record_size_kb": 1024,
        "flush_period_sec": 1,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "often configuration why breastplate ick beside amidst sauerkraut aw",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request=models.CreateOutputOutputConfluentCloud(
        id="confluent-cloud-output",
        type=models.CreateOutputTypeConfluentCloud.CONFLUENT_CLOUD,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=98.58,
            default_value_schema_id=7633.9,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Kim_Fadel",
            password="2TjsMJ6T9VV12ax",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://gloomy-metal.org/",
            client_id="<id>",
            oauth_secret_type="secret",
            client_text_secret="<value>",
            oauth_params=[
                models.ItemsTypeSaslOauthParams(
                    name="<value>",
                    value="<value>",
                ),
            ],
            sasl_extensions=[
                models.ItemsTypeSaslSaslExtensions(
                    name="<value>",
                    value="<value>",
                ),
            ],
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="quiet hopelessly outrank blacken reclassify sunbathe institute memorise",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputPqControlsConfluentCloud(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cribl-http-output",
        "type": models.CreateOutputTypeCriblHTTP.CRIBL_HTTP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "token_ttl_minutes": 60,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "throttle_rate_per_sec": "0",
        "response_retry_settings": [
            {
                "http_status": 7159.8,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "wherever whoa till splay",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "castanet lender godparent seldom beyond courageously thankfully easy aha",
        "url": "https://zesty-remark.net/",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://worldly-pocket-watch.com/",
                "weight": 1,
                "template_url": "https://clueless-jellyfish.net/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://low-pacemaker.biz",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblLake

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cribl-lake-output",
        "type": models.CreateOutputTypeCriblLake.CRIBL_LAKE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.STANDARD_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 64,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 300,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "aws_authentication_method": models.AwsAuthenticationMethodOptions.AUTO,
        "format_": models.FormatOptions.JSON,
        "max_concurrent_file_parts": 1,
        "description": "amongst round huzzah while direct abaft powerfully",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_dest_path": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblSearchEngine

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCriblSearchEngine" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cribl-search-engine-output",
        "type": models.CreateOutputTypeCriblSearchEngine.CRIBL_SEARCH_ENGINE,
        "pipeline": "<value>",
        "system_fields": [
            "cribl_pipe",
        ],
        "environment": "<value>",
        "streamtags": [],
        "load_balanced": False,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "token_ttl_minutes": 60,
        "exclude_fields": [
            "__kube_*",
            "__metadata",
            "__winEvent",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [],
        "throttle_rate_per_sec": "0",
        "response_retry_settings": [
            {
                "http_status": 401,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 20000,
            },
            {
                "http_status": 403,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 20000,
            },
            {
                "http_status": 408,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 429,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 500,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 502,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 503,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 504,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 509,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "bob often heating mixture incidentally rewrite cow why",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "flickering equally defensive worth miserably unexpectedly yuck ample",
        "url": "https://0.0.0.0:10200",
        "exclude_self": False,
        "urls": [
            {
                "url": "https://unkempt-travel.net/",
                "weight": 1,
                "template_url": "https://timely-sand.org/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://muted-backbone.org",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "cribl-tcp-output",
        "type": models.CreateOutputTypeCriblTCP.CRIBL_TCP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "0",
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "token_ttl_minutes": 60,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "uh-huh silver vicinity",
            },
        ],
        "exclude_fields": [
            "<value 1>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "until sashay woot keenly traffic bright lounge information",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "tough-issue.info",
                "port": 10300,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCrowdstrikeNextGenSiem

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesCrowdstrikeNextGenSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "crowdstrike-next-gen-siem-output",
        "type": models.CreateOutputTypeCrowdstrikeNextGenSiem.CROWDSTRIKE_NEXT_GEN_SIEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 5055.78,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "boohoo near knife soybean besides pish gah alongside",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://squeaky-academics.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatabricks

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDatabricks" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "databricks-output",
        "type": models.CreateOutputTypeDatabricks.DATABRICKS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dest_path": "",
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 60,
        "description": "brr recklessly why so",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatadog

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDatadog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "datadog-output",
        "type": models.CreateOutputTypeDatadog.DATADOG,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "content_type": models.CreateOutputSendLogsAs.JSON,
        "message": "<value>",
        "source": "<value>",
        "host": "woeful-ad.net",
        "service": "<value>",
        "tags": [
            "<value 1>",
            "<value 2>",
        ],
        "batch_by_tags": True,
        "allow_api_key_from_events": False,
        "severity": models.CreateOutputSeverityDatadog.WARNING,
        "site": models.CreateOutputDatadogSite.US,
        "send_counters_as_count": False,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 6276.58,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 3573.66,
        "description": "to midst phooey",
        "custom_url": "https://quick-godfather.biz",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDataset

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "dataset-output",
        "type": models.CreateOutputTypeDataset.DATASET,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "message_field": "<value>",
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "server_host_field": "<value>",
        "timestamp_field": "<value>",
        "default_severity": models.CreateOutputSeverityDataset.INFO,
        "response_retry_settings": [
            {
                "http_status": 8426.7,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "site": models.CreateOutputDataSetSite.US,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 8747.36,
        "description": "out furthermore ew bludgeon unbearably nocturnal jaggedly midst knight",
        "custom_url": "https://educated-turret.net/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
        "template_custom_url": "https://apt-knight.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDiskSpool

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDiskSpool" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "disk-spool-output",
        "type": models.CreateOutputTypeDiskSpool.DISK_SPOOL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "time_window": "10m",
        "max_data_size": "1GB",
        "max_data_time": "24h",
        "compress": models.CompressionOptionsPersistence.GZIP,
        "partition_expr": "<value>",
        "description": "blah daintily ah",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDlS3

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDlS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "dl-s3-output",
        "type": models.CreateOutputTypeDlS3.DL_S3,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "partitioning_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "description": "segregate helplessly clinking",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceHttp

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDynatraceHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "dynatrace-http-output",
        "type": models.CreateOutputTypeDynatraceHTTP.DYNATRACE_HTTP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "method": models.MethodOptions.POST,
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 9584.62,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputAuthenticationTypeDynatraceHTTP.TOKEN,
        "format_": models.CreateOutputFormatDynatraceHTTP.JSON_ARRAY,
        "endpoint": models.CreateOutputEndpoint.CLOUD,
        "telemetry_type": models.CreateOutputTelemetryType.LOGS,
        "total_memory_limit_kb": 5849.2,
        "description": "across yowza coarse notwithstanding ham",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "token": "your-api-key",
        "text_secret": "<value>",
        "environment_id": "<id>",
        "active_gate_domain": "<value>",
        "url": "https://dapper-gripper.info",
        "template_url": "https://cheap-premise.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceOtlp

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesDynatraceOtlp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "dynatrace-otlp-output",
        "type": models.CreateOutputTypeDynatraceOtlp.DYNATRACE_OTLP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.CreateOutputProtocolDynatraceOtlp.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 2048,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "endpoint_type": models.CreateOutputEndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "Authorization",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "yippee fabricate drat wherever so",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 8446.48,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElastic

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "elastic-output",
        "type": models.CreateOutputTypeElastic.ELASTIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": True,
        "index": "logs",
        "doc_type": "<value>",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3353.65,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Maddison_Willms",
            "password": "YjRP4IarMDm7WjU",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.CreateOutputElasticVersion.AUTO,
        "elastic_pipeline": "<value>",
        "include_doc_id": False,
        "write_action": models.CreateOutputWriteAction.CREATE,
        "retry_partial_errors": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "thoughtfully scope queasily indelible",
        "url": "https://bruised-yeast.info/",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://needy-hawk.com",
                "weight": 1,
                "template_url": "https://multicolored-cannon.biz/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://punctual-mixture.org",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElasticCloud

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesElasticCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "elastic-cloud-output",
        "type": models.CreateOutputTypeElasticCloud.ELASTIC_CLOUD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "my-cloud-id",
        "index": "logs",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Maddison_Willms",
            "password": "YjRP4IarMDm7WjU",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "response_retry_settings": [
            {
                "http_status": 3400.37,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "upon moor mysteriously incidentally",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesExabeam

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesExabeam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "exabeam-output",
        "type": models.CreateOutputTypeExabeam.EXABEAM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "stage_path": "/tmp/staging",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "object_acl": models.ObjectACLOptions1.PRIVATE,
        "storage_class": models.StorageClassOptions1.STANDARD,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_size_mb": 10,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "likewise chapel phooey mount nor",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesFilesystem

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "filesystem-output",
        "type": models.CreateOutputTypeFilesystem.FILESYSTEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "dest_path": "/var/log/output",
        "stage_path": "<value>",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "description": "meanwhile victoriously founder because before",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleChronicle

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGoogleChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "google-chronicle-output",
        "type": models.CreateOutputTypeGoogleChronicle.GOOGLE_CHRONICLE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "api_version": models.CreateOutputAPIVersion.V1,
        "authentication_method": models.CreateOutputAuthenticationMethodGoogleChronicle.SERVICE_ACCOUNT,
        "response_retry_settings": [
            {
                "http_status": 379.55,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "log_format_type": models.CreateOutputSendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 90,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 3260.96,
        "description": "incidentally testify but heartache fooey of",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "jealously qua before obnoxiously",
            },
        ],
        "log_type": "<value>",
        "log_text_field": "<value>",
        "customer_id": "customer-id",
        "namespace": "<value>",
        "custom_labels": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "udm_type": models.CreateOutputUDMType.LOGS,
        "api_key": "<value>",
        "api_key_secret": "<value>",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_api_version": "<value>",
        "template_region": "<value>",
        "template_customer_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleCloudLogging

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGoogleCloudLogging" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "google-cloud-logging-output",
        "type": models.CreateOutputTypeGoogleCloudLogging.GOOGLE_CLOUD_LOGGING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "log_location_type": models.CreateOutputLogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "sanitize_log_names": False,
        "payload_format": models.CreateOutputPayloadFormat.TEXT,
        "log_labels": [
            {
                "label": "<value>",
                "value_expression": "<value>",
            },
        ],
        "resource_type_expression": "<value>",
        "resource_type_labels": [
            {
                "label": "<value>",
                "value_expression": "<value>",
            },
        ],
        "severity_expression": "<value>",
        "insert_id_expression": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "flush_period_sec": 1,
        "concurrency": 5,
        "connection_timeout": 10000,
        "timeout_sec": 30,
        "throttle_rate_req_per_sec": 208589,
        "request_method_expression": "<value>",
        "request_url_expression": "<value>",
        "request_size_expression": "<value>",
        "status_expression": "<value>",
        "response_size_expression": "<value>",
        "user_agent_expression": "<value>",
        "remote_ip_expression": "<value>",
        "server_ip_expression": "<value>",
        "referer_expression": "<value>",
        "latency_expression": "<value>",
        "cache_lookup_expression": "<value>",
        "cache_hit_expression": "<value>",
        "cache_validated_expression": "<value>",
        "cache_fill_bytes_expression": "<value>",
        "protocol_expression": "<value>",
        "id_expression": "<value>",
        "producer_expression": "<value>",
        "first_expression": "<value>",
        "last_expression": "<value>",
        "file_expression": "<value>",
        "line_expression": "<value>",
        "function_expression": "<value>",
        "uid_expression": "<value>",
        "index_expression": "<value>",
        "total_splits_expression": "<value>",
        "trace_expression": "<value>",
        "span_id_expression": "<value>",
        "trace_sampled_expression": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 3307.75,
        "description": "apropos amidst steep gee think for lonely snappy council",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "google-cloud-storage-output",
        "type": models.CreateOutputTypeGoogleCloudStorage.GOOGLE_CLOUD_STORAGE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.CreateOutputAuthenticationMethodGoogleCloudStorage.MANUAL,
        "stage_path": "/tmp/staging",
        "dest_path": "",
        "verify_permissions": True,
        "object_acl": models.ObjectACLOptions1.PRIVATE,
        "storage_class": models.StorageClassOptions1.ARCHIVE,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "description": "dutiful parsnip likewise guard warmhearted lucky spattering despite above",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "aws_secret": "<value>",
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "google-pubsub-output",
        "type": models.CreateOutputTypeGooglePubsub.GOOGLE_PUBSUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "topic_name": "my-topic",
        "create_topic": False,
        "ordered_delivery": False,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 1000,
        "batch_timeout": 100,
        "max_queue_size": 100,
        "max_record_size_kb": 256,
        "flush_period": 1,
        "max_in_progress": 10,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "gee freezing with beside defrag lieu devastation",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic_name": "<value>",
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGrafanaCloud

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGrafanaCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request=models.CreateOutputOutputGrafanaCloudGrafanaCloud1(
        id="grafana-cloud-output",
        type=models.CreateOutputOutputGrafanaCloudType1.GRAFANA_CLOUD,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
        ],
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://smoggy-tomb.org/",
        message="<value>",
        message_format=models.MessageFormatOptions.PROTOBUF,
        labels=[
            models.ItemsTypeLabels(
                name="",
                value="<value>",
            ),
        ],
        metric_rename_expr="name.replace(/[^a-zA-Z0-9_]/g, '_')",
        prometheus_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
            token="<value>",
            text_secret="<value>",
            username="Pete.Cormier97",
            password="YqqU_9UCy3i_Jit",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
            token="<value>",
            text_secret="<value>",
            username="Dayton.Kunde",
            password="tn2vY0ufsrH9vj_",
            credentials_secret="<value>",
        ),
        concurrency=1,
        max_payload_size_kb=4096,
        max_payload_events=0,
        reject_unauthorized=True,
        timeout_sec=30,
        flush_period_sec=15,
        extra_http_headers=[
            models.ItemsTypeExtraHTTPHeaders(
                name="<value>",
                value="<value>",
            ),
        ],
        use_round_robin_dns=False,
        failed_request_logging_mode=models.FailedRequestLoggingModeOptions.NONE,
        safe_headers=[
            "<value 1>",
            "<value 2>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=8105.6,
                initial_backoff=1000,
                backoff_rate=2,
                max_backoff=10000,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=False,
            initial_backoff=1000,
            backoff_rate=2,
            max_backoff=10000,
        ),
        response_honor_retry_after_header=True,
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="lace frantically ha forceful underneath times yum partially",
        compress=True,
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputOutputGrafanaCloudPqControls1(),
        template_loki_url="https://deadly-sundae.biz/",
        template_prometheus_url="https://distorted-outset.biz/",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGraphite

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesGraphite" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "graphite-output",
        "type": models.CreateOutputTypeGraphite.GRAPHITE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "pfft term towards",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesHoneycomb

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesHoneycomb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "honeycomb-output",
        "type": models.CreateOutputTypeHoneycomb.HONEYCOMB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "dataset": "my-dataset",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 7702.22,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "between yum than lawful morning thoroughly compromise lost negligible",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "team": "<value>",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesHumioHec

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesHumioHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "humio-hec-output",
        "type": models.CreateOutputTypeHumioHec.HUMIO_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9520.58,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "gadzooks jubilantly over silk switch huzzah",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://other-interchange.org",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesInfluxdb

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesInfluxdb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "influxdb-output",
        "type": models.CreateOutputTypeInfluxdb.INFLUXDB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "http://localhost:8086",
        "use_v2_api": False,
        "timestamp_precision": models.CreateOutputTimestampPrecision.MS,
        "dynamic_value_field_name": True,
        "value_field_name": "value",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 786.03,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputAuthenticationTypeInfluxdb.NONE,
        "description": "terrorise spook meh towards mysteriously",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Mariane_Schneider28",
        "password": "z3FVqSY2GquoGXg",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://growing-declaration.net/",
        "template_database": "<value>",
        "template_bucket": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request=models.CreateOutputOutputKafka(
        id="kafka-output",
        type=models.CreateOutputTypeKafka.KAFKA,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        brokers=[
            "localhost:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=98.58,
            default_value_schema_id=7633.9,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Kim_Fadel",
            password="2TjsMJ6T9VV12ax",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://gloomy-metal.org/",
            client_id="<id>",
            oauth_secret_type="secret",
            client_text_secret="<value>",
            oauth_params=[
                models.ItemsTypeSaslOauthParams(
                    name="<value>",
                    value="<value>",
                ),
            ],
            sasl_extensions=[
                models.ItemsTypeSaslSaslExtensions(
                    name="<value>",
                    value="<value>",
                ),
            ],
        ),
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="unimpressively firm late under shirk loftily till",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputPqControlsKafka(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "kinesis-output",
        "type": models.CreateOutputTypeKinesis.KINESIS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stream_name": "my-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "concurrency": 5,
        "max_record_size_kb": 1024,
        "flush_period_sec": 1,
        "compression": models.CreateOutputCompression.GZIP,
        "use_list_shards": False,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "negotiation ad to eek about phew",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 500,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_stream_name": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "loki-output",
        "type": models.CreateOutputTypeLoki.LOKI,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:3100/loki/api/v1/push",
        "message": "<value>",
        "message_format": models.MessageFormatOptions.PROTOBUF,
        "labels": [
            {
                "name": "",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.NONE,
        "concurrency": 1,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 15,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3434.64,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "enable_dynamic_headers": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 9877.1,
        "description": "hospitable hence adjudge",
        "compress": True,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Magdalena_Zulauf-Kuhlman8",
        "password": "IqSYjCmovUFcOZH",
        "credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMicrosoftFabric

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesMicrosoftFabric" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "microsoft-fabric-output",
        "type": models.CreateOutputTypeMicrosoftFabric.MICROSOFT_FABRIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.LEADER,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 768,
        "flush_event_count": 1000,
        "flush_period_sec": 1,
        "connection_timeout": 10000,
        "request_timeout": 60000,
        "max_retries": 5,
        "max_back_off": 30000,
        "initial_backoff": 300,
        "backoff_rate": 2,
        "authentication_timeout": 10000,
        "reauthentication_threshold": 10000,
        "sasl": {
            "disabled": False,
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "$ConnectionString",
            "text_secret": "<value>",
            "client_secret_auth_type": models.CreateOutputAuthenticationMethodMicrosoftFabric.SECRET,
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "testimonial woot ingratiate clearly",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
        "template_bootstrap_server": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMinio

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesMinio" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "minio-output",
        "type": models.CreateOutputTypeMinio.MINIO,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "description": "supposing instead elegantly explode slope tasty direct what",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request=models.CreateOutputOutputMsk(
        id="msk-output",
        type=models.CreateOutputTypeMsk.MSK,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
        ],
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=98.58,
            default_value_schema_id=7633.9,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V4,
        reuse_connections=True,
        reject_unauthorized=True,
        enable_assume_role=False,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=3600,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="redevelop consequently for",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputPqControlsMsk(),
        template_topic="<value>",
        template_aws_secret_key="<value>",
        template_region="<value>",
        template_assume_role_arn="<value>",
        template_assume_role_external_id="<id>",
        template_aws_api_key="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNetflow

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "netflow-output",
        "type": models.CreateOutputTypeNetflow.NETFLOW,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 0,
        "enable_ip_spoofing": False,
        "description": "unfortunately if scuffle",
        "max_record_size": 1500,
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelic

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesNewrelic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "newrelic-output",
        "type": models.CreateOutputTypeNewrelic.NEWRELIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "region": models.RegionOptions.US,
        "log_type": "",
        "message_field": "",
        "metadata": [
            {
                "name": models.CreateOutputFieldName.AUDIT_ID,
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 1966.78,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 6526.58,
        "description": "whoa cycle furthermore but",
        "custom_url": "https://puny-governance.biz/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_log_type": "<value>",
        "template_message_field": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelicEvents

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesNewrelicEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "newrelic-events-output",
        "type": models.CreateOutputTypeNewrelicEvents.NEWRELIC_EVENTS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "region": models.RegionOptions.US,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3594.47,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "utilization sensitize whose hydrocarbon within innocently ouch er officially appertain",
        "custom_url": "https://appropriate-dependency.name",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_account_id": "<id>",
        "template_event_type": "<value>",
        "template_custom_url": "https://fluffy-diver.name",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "opentelemetry-output",
        "type": models.CreateOutputTypeOpenTelemetry.OPEN_TELEMETRY,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "protocol": models.ProtocolOptions.GRPC,
        "endpoint": "http://localhost:4317",
        "otlp_version": models.CreateOutputOTLPVersion.ZERO_DOT_10_DOT_0,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "auth_type": models.AuthenticationTypeOptions.NONE,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "next sermon whenever",
        "username": "Jerod7",
        "password": "HeFGuNo6pe5ewNs",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 1858.11,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "prometheus-output",
        "type": models.CreateOutputTypePrometheus.PROMETHEUS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "http://localhost:9091/api/v1/write",
        "metric_rename_expr": "name.replace(/[^a-zA-Z0-9_]/g, '_')",
        "send_metadata": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 516.48,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "description": "forenenst without which brief fuzzy gah",
        "metrics_flush_period_sec": 60,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Isac38",
        "password": "zMoVVLUWpStIVEr",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://gloomy-marten.net/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRing

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesRing" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "ring-output",
        "type": models.CreateOutputTypeRing.RING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "format_": models.CreateOutputDataFormatRing.JSON,
        "partition_expr": "<value>",
        "max_data_size": "1GB",
        "max_data_time": "24h",
        "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "description": "bolster woot athwart",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRouter

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesRouter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "router-output",
        "type": models.CreateOutputTypeRouter.ROUTER,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
                "description": "lasting uh-huh weatherize consequently joyous beloved",
                "final": True,
            },
        ],
        "description": "boom kiddingly moral",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "s3-output",
        "type": models.CreateOutputTypeS3.S3,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "description": "cross-contamination upside-down above",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "security-lake-output",
        "type": models.CreateOutputTypeSecurityLake.SECURITY_LAKE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.CreateOutputSignatureVersionSecurityLake.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.INTELLIGENT_TIERING,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "`CriblOut`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": False,
            "initial_backoff_ms": 861.22,
            "backoff_multiplier": 588.22,
            "max_backoff_ms": 3391.17,
            "jitter_percent": 650.52,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": False,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "description": "crowded furthermore editor lovable confound which",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "parquet_schema": "<value>",
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinel

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSentinel" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "sentinel-output",
        "type": models.CreateOutputTypeSentinel.SENTINEL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 1000,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 4485.56,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "https://monitor.azure.com/.default",
        "endpoint_url_configuration": models.CreateOutputEndpointConfiguration.URL,
        "total_memory_limit_kb": 4955.04,
        "description": "instantly yuck hmph yet uh-huh outfit whistle given though yum",
        "format_": models.CreateOutputFormatSentinel.NDJSON,
        "custom_source_expression": "__httpOut",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "\\n",
        "custom_content_type": "application/x-ndjson",
        "custom_payload_expression": "`${events}`",
        "advanced_content_type": "application/json",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "url": "https://your-workspace.ingest.monitor.azure.com",
        "dcr_id": "<id>",
        "dce_endpoint": "<value>",
        "stream_name": "<value>",
        "template_login_url": "https://sophisticated-alert.com",
        "template_secret": "<value>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_url": "https://reasonable-swine.info/",
        "template_dcr_id": "<id>",
        "template_dce_endpoint": "<value>",
        "template_stream_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinelOneAiSiem

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSentinelOneAiSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "sentinel-one-ai-siem-output",
        "type": models.CreateOutputTypeSentinelOneAiSiem.SENTINEL_ONE_AI_SIEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "region": models.CreateOutputRegion.US,
        "endpoint": models.CreateOutputAISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
        "concurrency": 5,
        "max_payload_size_kb": 5120,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 5,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9304.93,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "towards joyfully woot with basket pace cassava for mobilize",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://<Your-S1-Tenant>.sentinelone.net",
        "host_expression": "__e.host || C.os.hostname()",
        "source_expression": "__e.source || (__e.__criblMetrics ? 'metrics' : 'cribl')",
        "source_type_expression": "__e.sourcetype || 'dottedJson'",
        "data_source_category_expression": "'security'",
        "data_source_name_expression": "__e.__dataSourceName || 'cribl'",
        "data_source_vendor_expression": "__e.__dataSourceVendor || 'cribl'",
        "event_type_expression": "",
        "host": "C.os.hostname()",
        "source": "cribl",
        "source_type": "hecRawParser",
        "data_source_category": "security",
        "data_source_name": "cribl",
        "data_source_vendor": "cribl",
        "event_type": "",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesServiceNow

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesServiceNow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "servicenow-output",
        "type": models.CreateOutputTypeServiceNow.SERVICE_NOW,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "auth_token_name": "lightstep-access-token",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 2048,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "carefully almost per midst fleck daintily gruesome once bleach",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 781.29,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSignalfx

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSignalfx" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "signalfx-output",
        "type": models.CreateOutputTypeSignalfx.SIGNALFX,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "realm": "us0",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 7111.85,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "cautious fairly needily guzzle",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "snmp-output",
        "type": models.CreateOutputTypeSnmp.SNMP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 0,
        "description": "um but pfft mmm an qua",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSns

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSns" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "sns-output",
        "type": models.CreateOutputTypeSns.SNS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "max_retries": 7880.99,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.CreateOutputSignatureVersionSns.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "switchboard smuggle decision and whose truthfully clueless",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunk

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "splunk-output",
        "type": models.CreateOutputTypeSplunk.SPLUNK,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "host": "localhost",
        "port": 9997,
        "nested_fields": models.NestedFieldSerializationOptions.NONE,
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "enable_multi_metrics": False,
        "enable_ack": True,
        "log_failed_requests": False,
        "max_s2_sversion": models.MaxS2SVersionOptions.V3,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "arrange authentic phew scramble tenderly highlight pleasure lest",
        "max_failed_health_checks": 1,
        "compress": models.CompressionOptions.DISABLED,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "splunk-hec-output",
        "type": models.CreateOutputTypeSplunkHec.SPLUNK_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "next_queue": "indexQueue",
        "tcp_routing": "nowhere",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 1179.71,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "stuff fluctuate grim meanwhile",
        "url": "http://localhost:8088/services/collector/event",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "http://localhost:8088/services/collector/event",
                "weight": 1,
                "template_url": "https://fat-packaging.net/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://simple-circumference.org/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkLb

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSplunkLb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request=models.CreateOutputOutputSplunkLb(
        id="splunk-lb-output",
        type=models.CreateOutputTypeSplunkLb.SPLUNK_LB,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        dns_resolve_period_sec=600,
        load_balance_stats_period_sec=300,
        max_concurrent_senders=0,
        nested_fields=models.NestedFieldSerializationOptions.NONE,
        throttle_rate_per_sec="0",
        connection_timeout=10000,
        write_timeout=60000,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        enable_multi_metrics=False,
        enable_ack=True,
        log_failed_requests=False,
        max_s2_sversion=models.MaxS2SVersionOptions.V3,
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        indexer_discovery=False,
        sender_unhealthy_time_allowance=100,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        description="besides spice questionable how",
        max_failed_health_checks=1,
        compress=models.CompressionOptions.DISABLED,
        indexer_discovery_configs=models.CreateOutputIndexerDiscoveryConfigs(
            site="default",
            master_uri="https://slimy-supplier.info/",
            refresh_interval_sec=300,
            reject_unauthorized=False,
            auth_tokens=[
                models.CreateOutputAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                    auth_token="",
                    text_secret="<value>",
                ),
            ],
            auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
            auth_token="",
            text_secret="<value>",
        ),
        exclude_self=False,
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
                tls=models.TLSOptionsHostsItems.INHERIT,
                servername="<value>",
                weight=1,
                template_host="<value>",
                template_port="<value>",
            ),
        ],
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputPqControlsSplunkLb(),
        auth_token="",
        text_secret="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "sqs-output",
        "type": models.CreateOutputTypeSqs.SQS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "queue_name": "my-queue",
        "queue_type": models.CreateOutputQueueType.STANDARD,
        "aws_account_id": "<id>",
        "message_group_id": "cribl",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "max_queue_size": 100,
        "max_record_size_kb": 256,
        "flush_period_sec": 1,
        "max_in_progress": 10,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "abaft consequently upon shinny yowza why slake",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_queue_name": "<value>",
        "template_aws_account_id": "<id>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesStatsd

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesStatsd" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "statsd-output",
        "type": models.CreateOutputTypeStatsd.STATSD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "browse longingly tame regarding pendant playfully orchestrate",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesStatsdExt

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesStatsdExt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "statsd-ext-output",
        "type": models.CreateOutputTypeStatsdExt.STATSD_EXT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "after with wafer collaboration",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSumoLogic

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSumoLogic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "sumo-logic-output",
        "type": models.CreateOutputTypeSumoLogic.SUMO_LOGIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.CreateOutputDataFormatSumoLogic.JSON,
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 8295.69,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 7368.99,
        "description": "jovially mmm but zebra phew deform",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://profuse-decryption.biz",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "syslog-output",
        "type": models.CreateOutputTypeSyslog.SYSLOG,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.CreateOutputProtocolSyslog.TCP,
        "facility": models.CreateOutputFacility.ONE,
        "severity": models.CreateOutputSeveritySyslog.NOTICE,
        "app_name": "Cribl",
        "message_format": models.CreateOutputMessageFormat.RFC3164,
        "timestamp_format": models.CreateOutputTimestampFormat.SYSLOG,
        "throttle_rate_per_sec": "0",
        "octet_count_framing": True,
        "log_failed_requests": False,
        "description": "drat consequently restfully distorted phooey overconfidently",
        "load_balanced": True,
        "host": "localhost",
        "port": 514,
        "exclude_self": False,
        "hosts": [
            {
                "host": "separate-blossom.biz",
                "port": 8854.36,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "max_record_size": 1500,
        "udp_dns_resolve_period_sec": 0,
        "enable_ip_spoofing": False,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "tcpjson-output",
        "type": models.CreateOutputTypeTcpjson.TCPJSON,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "0",
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "token_ttl_minutes": 60,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "hourly about into",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "chilly-exterior.net",
                "port": 6458.17,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWavefront

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesWavefront" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "wavefront-output",
        "type": models.CreateOutputTypeWavefront.WAVEFRONT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "domain": "longboard",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 6928.76,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "excepting fooey solace spear",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWebhook

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "webhook-output",
        "type": models.CreateOutputTypeWebhook.WEBHOOK,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "method": models.MethodOptions.POST,
        "format_": models.CreateOutputFormatWebhook.NDJSON,
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 4167.91,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputAuthenticationTypeWebhook.NONE,
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "total_memory_limit_kb": 1305.29,
        "load_balanced": False,
        "description": "breakable hospitable override hmph presell",
        "custom_source_expression": "__httpOut",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "\\n",
        "custom_content_type": "application/x-ndjson",
        "custom_payload_expression": "`${events}`",
        "advanced_content_type": "application/json",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Janiya_Dietrich",
        "password": "QSmMfe0g6BQ_7dP",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://neglected-suspension.net/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "`Bearer ${token}`",
        "token_timeout_secs": 3600,
        "oauth_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "oauth_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "url": "https://example.com/webhook",
        "exclude_self": False,
        "urls": [
            {
                "url": "https://second-hand-apparatus.info",
                "weight": 1,
                "template_url": "https://unfit-grandson.biz/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "template_login_url": "https://scented-chiffonier.net",
        "template_secret": "<value>",
        "template_url": "https://grown-video.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWizHec

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesWizHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "wiz-hec-output",
        "type": models.CreateOutputTypeWizHec.WIZ_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "next_queue": "indexQueue",
        "tcp_routing": "nowhere",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 7295.73,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "hourly about into",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2614.76,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7295.73,
        "pq_max_backpressure_sec": 166.54,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "token": "<value>",
        "text_secret": "<value>",
        "template_wiz_environment": "<value>",
        "template_data_center": "<value>",
        "template_wiz_sourcetype": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesXsiam

<!-- UsageSnippet language="python" operationID="createOutput" method="post" path="/system/outputs" example="OutputCreateExamplesXsiam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.create(request={
        "id": "xsiam-output",
        "type": models.CreateOutputTypeXsiam.XSIAM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": False,
        "concurrency": 5,
        "max_payload_size_kb": 9500,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "auth_type": models.CreateOutputAuthenticationMethodXsiam.TOKEN,
        "response_retry_settings": [
            {
                "http_status": 4836.34,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "throttle_rate_req_per_sec": 400,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 9568.13,
        "description": "competent hospitalization zowie blah",
        "url": "http://localhost:8088/logs/v1/event",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://slimy-castanet.com/",
                "weight": 1,
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://unkempt-travel.net/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateOutputRequest](../../models/createoutputrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputById" method="get" path="/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to get.                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Destination.</br></br>Provide a complete representation of the Destination that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Destination.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Destination might not function as expected.

### Example Usage: OutputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "azure-blob-output",
        "type": models.OutputAzureBlobType.AZURE_BLOB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "container_name": "my-container",
        "create_container": False,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "max_concurrent_file_parts": 1,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "storage_class": models.BlobAccessTier.INFERRED,
        "description": "practical adumbrate by",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "connection_string": "<value>",
        "text_secret": "<value>",
        "storage_account_name": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "azure_cloud": "<value>",
        "endpoint_suffix": "<value>",
        "client_text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "template_container_name": "<value>",
        "template_format": "<value>",
        "template_connection_string": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureDataExplorer

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesAzureDataExplorer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "azure-data-explorer-output",
        "type": models.OutputAzureDataExplorerType.AZURE_DATA_EXPLORER,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "validate_database_settings": True,
        "ingest_mode": models.IngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.OutputAzureDataExplorerAuthenticationMethod.CLIENT_SECRET,
        "description": "oof pace once",
        "client_secret": "client-secret",
        "text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_enabled": False,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://competent-nephew.name",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "max_concurrent_file_parts": 1,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "add_id_to_stage_path": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "timeout_sec": 30,
        "flush_immediately": False,
        "retain_blob_on_success": False,
        "extent_tags": [
            {
                "prefix": models.PrefixOptional.DROP_BY,
                "value": "<value>",
            },
        ],
        "ingest_if_not_exists": [
            {
                "value": "<value>",
            },
        ],
        "report_level": models.ReportLevel.FAILURES_ONLY,
        "report_method": models.ReportMethod.QUEUE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 4119.46,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "flush_period_sec": 1,
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "keep_alive": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_cluster_url": "https://exotic-championship.com/",
        "template_database": "<value>",
        "template_table": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_client_secret": "<value>",
        "template_format": "<value>",
        "template_ingest_url": "https://critical-range.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureEventhub

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesAzureEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "azure-eventhub-output",
        "type": models.OutputAzureEventhubType.AZURE_EVENTHUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.LEADER,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 768,
        "flush_event_count": 1000,
        "flush_period_sec": 1,
        "connection_timeout": 10000,
        "request_timeout": 60000,
        "max_retries": 5,
        "max_back_off": 30000,
        "initial_backoff": 300,
        "backoff_rate": 2,
        "authentication_timeout": 10000,
        "reauthentication_threshold": 10000,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "l4UiMzAymhgS2bu",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "$ConnectionString",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.MANUAL,
            "client_secret": "<value>",
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "over excluding knowingly energetically incidentally given",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureLogs

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesAzureLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "azure-logs-output",
        "type": models.OutputAzureLogsType.AZURE_LOGS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "log_type": "Cribl",
        "resource_id": "<id>",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "api_url": ".ods.opinsights.azure.com",
        "response_retry_settings": [
            {
                "http_status": 6460.17,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputAzureLogsAuthenticationMethod.MANUAL,
        "description": "critical under even beyond condense diligently",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
        "keypair_secret": "<value>",
        "template_workspace_id": "<id>",
        "template_workspace_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesChronicle

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "chronicle-output",
        "type": models.OutputChronicleType.CHRONICLE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "api_version": "v1alpha",
        "authentication_method": models.OutputChronicleAuthenticationMethod.SERVICE_ACCOUNT,
        "response_retry_settings": [
            {
                "http_status": 4457.03,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 90,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 1999.04,
        "ingestion_method": "ImportLogs",
        "namespace": "<value>",
        "log_type": "UNKNOWN",
        "log_text_field": "<value>",
        "gcp_project_id": "my-project",
        "gcp_instance": "customer-id",
        "custom_labels": [
            {
                "key": "<key>",
                "value": "<value>",
                "rbac_enabled": False,
            },
        ],
        "description": "pleasant waist cease aha because switchboard phew keenly arrogantly husky",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesClickHouse

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesClickHouse" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "clickhouse-output",
        "type": models.OutputClickHouseType.CLICK_HOUSE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:8123/",
        "auth_type": models.OutputClickHouseAuthenticationType.NONE,
        "database": "mydb",
        "table_name": "mytable",
        "format_": models.OutputClickHouseFormat.JSON_COMPACT_EACH_ROW_WITH_NAMES,
        "mapping_type": models.MappingType.AUTOMATIC,
        "async_inserts": False,
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5472.53,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "dump_format_errors_to_disk": False,
        "stats_destination": {
            "url": "https://grumpy-executor.net/",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Marco.Halvorson77",
            "sql_username": "<value>",
            "password": "PIYToV3IkVuO_AI",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "amidst oh till section soup thyme able sad",
        "username": "Aylin5",
        "password": "UNEGv2BtuPwBqwA",
        "credentials_secret": "<value>",
        "sql_username": "<value>",
        "wait_for_async_inserts": True,
        "exclude_mapping_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "describe_table": "<value>",
        "column_mappings": [
            {
                "column_name": "<value>",
                "column_type": "<value>",
                "column_value_expression": "<value>",
            },
        ],
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://quarrelsome-slime.name",
        "template_database": "<value>",
        "template_table_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudflareR2

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCloudflareR2" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cloudflare-r2-output",
        "type": models.OutputCloudflareR2Type.CLOUDFLARE_R2,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.OutputCloudflareR2AuthenticationMethod.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "description": "whenever beret quirkily certainly cruelty well-documented poorly inject throughout",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudwatch

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCloudwatch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cloudwatch-output",
        "type": models.OutputCloudwatchType.CLOUDWATCH,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "max_queue_size": 5,
        "max_record_size_kb": 1024,
        "flush_period_sec": 1,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "hubris gray materialise aboard content ick self-assured cleaner imagineer",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output=models.OutputConfluentCloud(
        id="confluent-cloud-output",
        type=models.OutputConfluentCloudType.CONFLUENT_CLOUD,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=2571.24,
            default_value_schema_id=4603.74,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Beverly93",
            password="iNd6FlpDEbKPe_d",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://smooth-conservative.com",
            client_id="<id>",
            oauth_secret_type="secret",
            client_text_secret="<value>",
            oauth_params=[
                models.ItemsTypeSaslOauthParams(
                    name="<value>",
                    value="<value>",
                ),
            ],
            sasl_extensions=[
                models.ItemsTypeSaslSaslExtensions(
                    name="<value>",
                    value="<value>",
                ),
            ],
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="until scientific since properly massage and",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputConfluentCloudPqControls(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cribl-http-output",
        "type": models.OutputCriblHTTPType.CRIBL_HTTP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "token_ttl_minutes": 60,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "throttle_rate_per_sec": "0",
        "response_retry_settings": [
            {
                "http_status": 3673.51,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "fabricate focalise calmly per outside aside astride known lumpy",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "unique filthy irresponsible wherever lawful an settle unlike",
        "url": "https://tidy-beret.biz",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://weird-finer.net",
                "weight": 1,
                "template_url": "https://adolescent-sprinkles.biz/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://focused-quinoa.info",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cribl-lake-output",
        "type": models.OutputCriblLakeType.CRIBL_LAKE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 64,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 300,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "aws_authentication_method": models.AwsAuthenticationMethodOptions.AUTO,
        "format_": models.FormatOptions.DDSS,
        "max_concurrent_file_parts": 1,
        "description": "mad mmm bitterly ah overwork mysterious instead miskey",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_dest_path": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblSearchEngine

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCriblSearchEngine" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cribl-search-engine-output",
        "type": models.OutputCriblSearchEngineType.CRIBL_SEARCH_ENGINE,
        "pipeline": "<value>",
        "system_fields": [
            "cribl_pipe",
        ],
        "environment": "<value>",
        "streamtags": [],
        "load_balanced": False,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "token_ttl_minutes": 60,
        "exclude_fields": [
            "__kube_*",
            "__metadata",
            "__winEvent",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [],
        "throttle_rate_per_sec": "0",
        "response_retry_settings": [
            {
                "http_status": 401,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 20000,
            },
            {
                "http_status": 403,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 20000,
            },
            {
                "http_status": 408,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 429,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 500,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 502,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 503,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 504,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
            {
                "http_status": 509,
                "initial_backoff": 250,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "developmental yum tomatillo",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "contradict unless busy for concerned buck grandiose dreamily what solder",
        "url": "https://0.0.0.0:10200",
        "exclude_self": False,
        "urls": [
            {
                "url": "https://short-term-ectoderm.net/",
                "weight": 1,
                "template_url": "https://dull-mainstream.org",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://burdensome-discourse.com/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "cribl-tcp-output",
        "type": models.OutputCriblTCPType.CRIBL_TCP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "0",
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "token_ttl_minutes": 60,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "unless zowie unbearably throughout oh brr solemnly",
            },
        ],
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "pace primary nor tomography once",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "tough-colonialism.info",
                "port": 10300,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCrowdstrikeNextGenSiem

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesCrowdstrikeNextGenSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "crowdstrike-next-gen-siem-output",
        "type": models.OutputCrowdstrikeNextGenSiemType.CROWDSTRIKE_NEXT_GEN_SIEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 1023.69,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "yesterday connect whose",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://quiet-riser.org/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatabricks

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDatabricks" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "databricks-output",
        "type": models.OutputDatabricksType.DATABRICKS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "dest_path": "",
        "stage_path": "$CRIBL_HOME/state/outputs/staging",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 60,
        "description": "procurement aha minus cautious density phony alliance despite",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatadog

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDatadog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "datadog-output",
        "type": models.OutputDatadogType.DATADOG,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "content_type": models.SendLogsAs.JSON,
        "message": "<value>",
        "source": "<value>",
        "host": "weighty-release.net",
        "service": "<value>",
        "tags": [
            "<value 1>",
        ],
        "batch_by_tags": True,
        "allow_api_key_from_events": False,
        "severity": models.OutputDatadogSeverity.INFO,
        "site": models.DatadogSite.US,
        "send_counters_as_count": False,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3412.47,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 230.7,
        "description": "yippee what during put that pish uselessly although wherever declaration",
        "custom_url": "https://stingy-guide.name/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDataset

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "dataset-output",
        "type": models.OutputDatasetType.DATASET,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "message_field": "<value>",
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "server_host_field": "<value>",
        "timestamp_field": "<value>",
        "default_severity": models.OutputDatasetSeverity.INFO,
        "response_retry_settings": [
            {
                "http_status": 5952.63,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "site": models.DataSetSite.US,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 1088.03,
        "description": "apropos gosh overvalue than handful fully leading yuck portray",
        "custom_url": "https://blue-forage.info",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
        "template_custom_url": "https://sleepy-cassava.org/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDiskSpool

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDiskSpool" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "disk-spool-output",
        "type": models.OutputDiskSpoolType.DISK_SPOOL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "time_window": "10m",
        "max_data_size": "1GB",
        "max_data_time": "24h",
        "compress": models.CompressionOptionsPersistence.GZIP,
        "partition_expr": "<value>",
        "description": "along between embed into declaration boastfully though verbally platter",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDlS3

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDlS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "dl-s3-output",
        "type": models.OutputDlS3Type.DL_S3,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "partitioning_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "description": "whenever mash ugh reasoning premier healthily",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceHttp

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDynatraceHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "dynatrace-http-output",
        "type": models.OutputDynatraceHTTPType.DYNATRACE_HTTP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "method": models.MethodOptions.POST,
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 994.29,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputDynatraceHTTPAuthenticationType.TOKEN,
        "format_": models.OutputDynatraceHTTPFormat.JSON_ARRAY,
        "endpoint": models.Endpoint.CLOUD,
        "telemetry_type": models.TelemetryType.LOGS,
        "total_memory_limit_kb": 9576.28,
        "description": "yowza instead zowie under foodstuffs massive reproach",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "token": "your-api-key",
        "text_secret": "<value>",
        "environment_id": "<id>",
        "active_gate_domain": "<value>",
        "url": "https://mad-guidance.info/",
        "template_url": "https://timely-mountain.info",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceOtlp

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesDynatraceOtlp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "dynatrace-otlp-output",
        "type": models.OutputDynatraceOtlpType.DYNATRACE_OTLP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.OutputDynatraceOtlpProtocol.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 2048,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "endpoint_type": models.EndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "Authorization",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "tinderbox now until than appreciate nervously aching seafood",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 7970.31,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElastic

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "elastic-output",
        "type": models.OutputElasticType.ELASTIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "index": "logs",
        "doc_type": "<value>",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5469.02,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Timmothy.Morar",
            "password": "lCK4OFBNamsTS5U",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.ElasticVersion.AUTO,
        "elastic_pipeline": "<value>",
        "include_doc_id": False,
        "write_action": models.WriteAction.CREATE,
        "retry_partial_errors": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "save along larva quantify forearm drat physically",
        "url": "https://alert-fort.info/",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://first-bourgeoisie.biz",
                "weight": 1,
                "template_url": "https://accomplished-cuckoo.net",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://thin-other.biz",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElasticCloud

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesElasticCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "elastic-cloud-output",
        "type": models.OutputElasticCloudType.ELASTIC_CLOUD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "my-cloud-id",
        "index": "logs",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Timmothy.Morar",
            "password": "lCK4OFBNamsTS5U",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "response_retry_settings": [
            {
                "http_status": 6701.64,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "gadzooks quaintly jet unearth",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesExabeam

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesExabeam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "exabeam-output",
        "type": models.OutputExabeamType.EXABEAM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "stage_path": "/tmp/staging",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "object_acl": models.ObjectACLOptions1.PRIVATE,
        "storage_class": models.StorageClassOptions1.STANDARD,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_size_mb": 10,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "brr despite even er woefully regarding",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "filesystem-output",
        "type": models.OutputFilesystemType.FILESYSTEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dest_path": "/var/log/output",
        "stage_path": "<value>",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "description": "luck ah ski",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleChronicle

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGoogleChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "google-chronicle-output",
        "type": models.OutputGoogleChronicleType.GOOGLE_CHRONICLE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "api_version": models.OutputGoogleChronicleAPIVersion.V1,
        "authentication_method": models.OutputGoogleChronicleAuthenticationMethod.SERVICE_ACCOUNT,
        "response_retry_settings": [
            {
                "http_status": 1271.28,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "log_format_type": models.SendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 90,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 304.57,
        "description": "fooey safely ah tuba nervous sans whoever at invite",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "busy for concerned buck grandiose dreamily what solder",
            },
        ],
        "log_type": "<value>",
        "log_text_field": "<value>",
        "customer_id": "customer-id",
        "namespace": "<value>",
        "custom_labels": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "udm_type": models.UDMType.LOGS,
        "api_key": "<value>",
        "api_key_secret": "<value>",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_api_version": "<value>",
        "template_region": "<value>",
        "template_customer_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleCloudLogging

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGoogleCloudLogging" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "google-cloud-logging-output",
        "type": models.OutputGoogleCloudLoggingType.GOOGLE_CLOUD_LOGGING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "log_location_type": models.LogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "sanitize_log_names": False,
        "payload_format": models.PayloadFormat.TEXT,
        "log_labels": [
            {
                "label": "<value>",
                "value_expression": "<value>",
            },
        ],
        "resource_type_expression": "<value>",
        "resource_type_labels": [
            {
                "label": "<value>",
                "value_expression": "<value>",
            },
        ],
        "severity_expression": "<value>",
        "insert_id_expression": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "flush_period_sec": 1,
        "concurrency": 5,
        "connection_timeout": 10000,
        "timeout_sec": 30,
        "throttle_rate_req_per_sec": 829528,
        "request_method_expression": "<value>",
        "request_url_expression": "<value>",
        "request_size_expression": "<value>",
        "status_expression": "<value>",
        "response_size_expression": "<value>",
        "user_agent_expression": "<value>",
        "remote_ip_expression": "<value>",
        "server_ip_expression": "<value>",
        "referer_expression": "<value>",
        "latency_expression": "<value>",
        "cache_lookup_expression": "<value>",
        "cache_hit_expression": "<value>",
        "cache_validated_expression": "<value>",
        "cache_fill_bytes_expression": "<value>",
        "protocol_expression": "<value>",
        "id_expression": "<value>",
        "producer_expression": "<value>",
        "first_expression": "<value>",
        "last_expression": "<value>",
        "file_expression": "<value>",
        "line_expression": "<value>",
        "function_expression": "<value>",
        "uid_expression": "<value>",
        "index_expression": "<value>",
        "total_splits_expression": "<value>",
        "trace_expression": "<value>",
        "span_id_expression": "<value>",
        "trace_sampled_expression": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 527.61,
        "description": "meanwhile boo beneficial below positively huzzah fully anxiously",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "google-cloud-storage-output",
        "type": models.OutputGoogleCloudStorageType.GOOGLE_CLOUD_STORAGE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.OutputGoogleCloudStorageAuthenticationMethod.MANUAL,
        "stage_path": "/tmp/staging",
        "dest_path": "",
        "verify_permissions": True,
        "object_acl": models.ObjectACLOptions1.PRIVATE,
        "storage_class": models.StorageClassOptions1.ARCHIVE,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "description": "ew sarong cumbersome",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "aws_secret": "<value>",
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "google-pubsub-output",
        "type": models.OutputGooglePubsubType.GOOGLE_PUBSUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "topic_name": "my-topic",
        "create_topic": False,
        "ordered_delivery": False,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 1000,
        "batch_timeout": 100,
        "max_queue_size": 100,
        "max_record_size_kb": 256,
        "flush_period": 1,
        "max_in_progress": 10,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "although worth reckon",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic_name": "<value>",
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGrafanaCloud

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGrafanaCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output=models.OutputGrafanaCloudGrafanaCloud1(
        id="grafana-cloud-output",
        type=models.OutputGrafanaCloudType1.GRAFANA_CLOUD,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://jubilant-disclosure.org",
        message="<value>",
        message_format=models.MessageFormatOptions.PROTOBUF,
        labels=[
            models.ItemsTypeLabels(
                name="",
                value="<value>",
            ),
        ],
        metric_rename_expr="name.replace(/[^a-zA-Z0-9_]/g, '_')",
        prometheus_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
            token="<value>",
            text_secret="<value>",
            username="Flo.Koelpin",
            password="WalxTm654qjkLiW",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
            token="<value>",
            text_secret="<value>",
            username="Alda_MacGyver88",
            password="s0xBReXekhrDqCh",
            credentials_secret="<value>",
        ),
        concurrency=1,
        max_payload_size_kb=4096,
        max_payload_events=0,
        reject_unauthorized=True,
        timeout_sec=30,
        flush_period_sec=15,
        extra_http_headers=[
            models.ItemsTypeExtraHTTPHeaders(
                name="<value>",
                value="<value>",
            ),
        ],
        use_round_robin_dns=False,
        failed_request_logging_mode=models.FailedRequestLoggingModeOptions.NONE,
        safe_headers=[
            "<value 1>",
            "<value 2>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=8961.65,
                initial_backoff=1000,
                backoff_rate=2,
                max_backoff=10000,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=False,
            initial_backoff=1000,
            backoff_rate=2,
            max_backoff=10000,
        ),
        response_honor_retry_after_header=True,
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="unlike crumble circulate materialise",
        compress=True,
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputGrafanaCloudPqControls1(),
        template_loki_url="https://firsthand-straw.name",
        template_prometheus_url="https://grandiose-technologist.com",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGraphite

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesGraphite" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "graphite-output",
        "type": models.OutputGraphiteType.GRAPHITE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "whopping fine whose meanwhile finally off plump",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesHoneycomb

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesHoneycomb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "honeycomb-output",
        "type": models.OutputHoneycombType.HONEYCOMB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dataset": "my-dataset",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 864.6,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "scope castanet pfft creature",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "team": "<value>",
        "text_secret": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesHumioHec

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesHumioHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "humio-hec-output",
        "type": models.OutputHumioHecType.HUMIO_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 8378.07,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "nippy impressionable ouch concerning upside-down after",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://heartfelt-deed.net/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesInfluxdb

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesInfluxdb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "influxdb-output",
        "type": models.OutputInfluxdbType.INFLUXDB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "http://localhost:8086",
        "use_v2_api": False,
        "timestamp_precision": models.TimestampPrecision.MS,
        "dynamic_value_field_name": True,
        "value_field_name": "value",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2224.46,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputInfluxdbAuthenticationType.NONE,
        "description": "once till aw forgery",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Hector.Kshlerin29",
        "password": "uj1bSnZx1GRBoIy",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://warmhearted-premise.info/",
        "template_database": "<value>",
        "template_bucket": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output=models.OutputKafka(
        id="kafka-output",
        type=models.OutputKafkaType.KAFKA,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
        ],
        brokers=[
            "localhost:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=2571.24,
            default_value_schema_id=4603.74,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Beverly93",
            password="iNd6FlpDEbKPe_d",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://smooth-conservative.com",
            client_id="<id>",
            oauth_secret_type="secret",
            client_text_secret="<value>",
            oauth_params=[
                models.ItemsTypeSaslOauthParams(
                    name="<value>",
                    value="<value>",
                ),
            ],
            sasl_extensions=[
                models.ItemsTypeSaslSaslExtensions(
                    name="<value>",
                    value="<value>",
                ),
            ],
        ),
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="forenenst red which solicit where rejigger uncommon scoop",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputKafkaPqControls(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "kinesis-output",
        "type": models.OutputKinesisType.KINESIS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stream_name": "my-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "concurrency": 5,
        "max_record_size_kb": 1024,
        "flush_period_sec": 1,
        "compression": models.OutputKinesisCompression.GZIP,
        "use_list_shards": False,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "obediently or pricey why hose detective scout",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 500,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_stream_name": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "loki-output",
        "type": models.OutputLokiType.LOKI,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:3100/loki/api/v1/push",
        "message": "<value>",
        "message_format": models.MessageFormatOptions.PROTOBUF,
        "labels": [
            {
                "name": "",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.NONE,
        "concurrency": 1,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 15,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 259.76,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "enable_dynamic_headers": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 3553.75,
        "description": "perfectly youthfully often usefully midst once shameless out for",
        "compress": True,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Virginie.Kohler",
        "password": "oxajD3Wd8pLSEnh",
        "credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMicrosoftFabric

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesMicrosoftFabric" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "microsoft-fabric-output",
        "type": models.OutputMicrosoftFabricType.MICROSOFT_FABRIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.LEADER,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 768,
        "flush_event_count": 1000,
        "flush_period_sec": 1,
        "connection_timeout": 10000,
        "request_timeout": 60000,
        "max_retries": 5,
        "max_back_off": 30000,
        "initial_backoff": 300,
        "backoff_rate": 2,
        "authentication_timeout": 10000,
        "reauthentication_threshold": 10000,
        "sasl": {
            "disabled": False,
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "$ConnectionString",
            "text_secret": "<value>",
            "client_secret_auth_type": models.OutputMicrosoftFabricAuthenticationMethod.SECRET,
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "while so squirm surprise circa indeed simple angle daddy",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
        "template_bootstrap_server": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMinio

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesMinio" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "minio-output",
        "type": models.OutputMinioType.MINIO,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions2.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "description": "gosh footrest complication",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output=models.OutputMsk(
        id="msk-output",
        type=models.OutputMskType.MSK,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
        ],
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.GZIP,
        max_record_size_kb=768,
        flush_event_count=1000,
        flush_period_sec=1,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="http://localhost:8081",
            connection_timeout=30000,
            request_timeout=30000,
            max_retries=1,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
            default_key_schema_id=2571.24,
            default_value_schema_id=4603.74,
        ),
        connection_timeout=10000,
        request_timeout=60000,
        max_retries=5,
        max_back_off=30000,
        initial_backoff=300,
        backoff_rate=2,
        authentication_timeout=10000,
        reauthentication_threshold=10000,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V4,
        reuse_connections=True,
        reject_unauthorized=True,
        enable_assume_role=False,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=3600,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="kick adrenalin above airbus oil or smart babushka ethyl dash",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputMskPqControls(),
        template_topic="<value>",
        template_aws_secret_key="<value>",
        template_region="<value>",
        template_assume_role_arn="<value>",
        template_assume_role_external_id="<id>",
        template_aws_api_key="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNetflow

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "netflow-output",
        "type": models.OutputNetflowType.NETFLOW,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 0,
        "enable_ip_spoofing": False,
        "description": "each meh glisten zowie",
        "max_record_size": 1500,
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelic

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesNewrelic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "newrelic-output",
        "type": models.OutputNewrelicType.NEWRELIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "region": models.RegionOptions.US,
        "log_type": "",
        "message_field": "",
        "metadata": [
            {
                "name": models.FieldName.AUDIT_ID,
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3645.11,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 2690.34,
        "description": "abaft among madly kielbasa despite strictly solemnly whether digital",
        "custom_url": "https://well-worn-casket.net",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_log_type": "<value>",
        "template_message_field": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelicEvents

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesNewrelicEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "newrelic-events-output",
        "type": models.OutputNewrelicEventsType.NEWRELIC_EVENTS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "region": models.RegionOptions.US,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 1898.39,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "for upon healthily distorted as",
        "custom_url": "https://squeaky-mathematics.org/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_account_id": "<id>",
        "template_event_type": "<value>",
        "template_custom_url": "https://old-yak.info/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "opentelemetry-output",
        "type": models.OutputOpenTelemetryType.OPEN_TELEMETRY,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.ProtocolOptions.GRPC,
        "endpoint": "http://localhost:4317",
        "otlp_version": models.OutputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "auth_type": models.AuthenticationTypeOptions.NONE,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "playfully lounge fooey vet overwork acknowledge above drat",
        "username": "Eve11",
        "password": "6wNRRvPHwjcljoo",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 7232.05,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "prometheus-output",
        "type": models.OutputPrometheusType.PROMETHEUS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "http://localhost:9091/api/v1/write",
        "metric_rename_expr": "name.replace(/[^a-zA-Z0-9_]/g, '_')",
        "send_metadata": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2064.65,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "description": "instead though litter fortunately perfectly unless vary",
        "metrics_flush_period_sec": 60,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Tracey68",
        "password": "kTcECZfBZpBWuvT",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://unlawful-duster.name",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRing

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesRing" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "ring-output",
        "type": models.OutputRingType.RING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "format_": models.OutputRingDataFormat.JSON,
        "partition_expr": "<value>",
        "max_data_size": "1GB",
        "max_data_time": "24h",
        "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "description": "safely swerve sparkling print um equal coop astride crushing",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRouter

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesRouter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "router-output",
        "type": models.OutputRouterType.ROUTER,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
                "description": "fort supposing bleakly recede hmph",
                "final": True,
            },
        ],
        "description": "whose how hard-to-find",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "s3-output",
        "type": models.OutputS3Type.S3,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.ONEZONE_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "partition_expr": "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "`CriblOut`",
        "file_name_suffix": "`.${C.env[\"CRIBL_WORKER_ID\"]}.${__format}${__compression === \"gzip\" ? \".gz\" : \"\"}`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "description": "starch nephew including hmph separately mobilize sugary deliberately",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "security-lake-output",
        "type": models.OutputSecurityLakeType.SECURITY_LAKE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.OutputSecurityLakeSignatureVersion.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "`CriblOut`",
        "max_file_size_mb": 32,
        "max_open_files": 100,
        "header_line": "",
        "write_high_water_mark": 64,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 2452.56,
            "backoff_multiplier": 1370.95,
            "max_backoff_ms": 434.99,
            "jitter_percent": 9632.75,
        },
        "max_file_open_time_sec": 300,
        "max_file_idle_time_sec": 30,
        "max_concurrent_file_parts": 4,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 100,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": False,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 10000,
        "parquet_page_size": "1MB",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "description": "ha till furthermore excepting diver",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 300,
        "directory_batch_size": 1000,
        "parquet_schema": "<value>",
        "deadletter_path": "$CRIBL_HOME/state/outputs/dead-letter",
        "max_retry_num": 20,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_aws_secret_key": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinel

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSentinel" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "sentinel-output",
        "type": models.OutputSentinelType.SENTINEL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 1000,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2382.67,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputSentinelAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "https://monitor.azure.com/.default",
        "endpoint_url_configuration": models.EndpointConfiguration.URL,
        "total_memory_limit_kb": 933.62,
        "description": "exhausted against respectful editor majestically",
        "format_": models.OutputSentinelFormat.NDJSON,
        "custom_source_expression": "__httpOut",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "\\n",
        "custom_content_type": "application/x-ndjson",
        "custom_payload_expression": "`${events}`",
        "advanced_content_type": "application/json",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "url": "https://your-workspace.ingest.monitor.azure.com",
        "dcr_id": "<id>",
        "dce_endpoint": "<value>",
        "stream_name": "<value>",
        "template_login_url": "https://lumpy-muscat.name/",
        "template_secret": "<value>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_url": "https://long-honesty.org/",
        "template_dcr_id": "<id>",
        "template_dce_endpoint": "<value>",
        "template_stream_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinelOneAiSiem

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSentinelOneAiSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "sentinel-one-ai-siem-output",
        "type": models.OutputSentinelOneAiSiemType.SENTINEL_ONE_AI_SIEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "region": models.Region.US,
        "endpoint": models.AISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
        "concurrency": 5,
        "max_payload_size_kb": 5120,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 5,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9611.42,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "but yellow whereas yowza sweetly scent lobster tectonics consequently golden",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://<Your-S1-Tenant>.sentinelone.net",
        "host_expression": "__e.host || C.os.hostname()",
        "source_expression": "__e.source || (__e.__criblMetrics ? 'metrics' : 'cribl')",
        "source_type_expression": "__e.sourcetype || 'dottedJson'",
        "data_source_category_expression": "'security'",
        "data_source_name_expression": "__e.__dataSourceName || 'cribl'",
        "data_source_vendor_expression": "__e.__dataSourceVendor || 'cribl'",
        "event_type_expression": "",
        "host": "C.os.hostname()",
        "source": "cribl",
        "source_type": "hecRawParser",
        "data_source_category": "security",
        "data_source_name": "cribl",
        "data_source_vendor": "cribl",
        "event_type": "",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesServiceNow

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesServiceNow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "servicenow-output",
        "type": models.OutputServiceNowType.SERVICE_NOW,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "auth_token_name": "lightstep-access-token",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 2048,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "",
                "value": "<value>",
            },
        ],
        "concurrency": 5,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 10000,
        "keep_alive_time": 30,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "pinion among beyond behind thorough helplessly sadly anti",
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2454.78,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSignalfx

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSignalfx" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "signalfx-output",
        "type": models.OutputSignalfxType.SIGNALFX,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "realm": "us0",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 2401.56,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "hawk next gnash sympathetically numb spork discrete whereas",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "snmp-output",
        "type": models.OutputSnmpType.SNMP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 0,
        "description": "executor caring kiddingly violently into",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSns

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSns" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "sns-output",
        "type": models.OutputSnsType.SNS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "max_retries": 9109,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.OutputSnsSignatureVersion.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "where duh via numb as abaft pfft",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "splunk-output",
        "type": models.OutputSplunkType.SPLUNK,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "host": "localhost",
        "port": 9997,
        "nested_fields": models.NestedFieldSerializationOptions.NONE,
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "enable_multi_metrics": False,
        "enable_ack": True,
        "log_failed_requests": False,
        "max_s2_sversion": models.MaxS2SVersionOptions.V3,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "wrathful upright guest excepting",
        "max_failed_health_checks": 1,
        "compress": models.CompressionOptions.DISABLED,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "splunk-hec-output",
        "type": models.OutputSplunkHecType.SPLUNK_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "next_queue": "indexQueue",
        "tcp_routing": "nowhere",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 6617.86,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "bus majestically absent once opposite brr enroll",
        "url": "http://localhost:8088/services/collector/event",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "http://localhost:8088/services/collector/event",
                "weight": 1,
                "template_url": "https://proud-blowgun.biz/",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://fair-cauliflower.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkLb

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSplunkLb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output=models.OutputSplunkLb(
        id="splunk-lb-output",
        type=models.OutputSplunkLbType.SPLUNK_LB,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        dns_resolve_period_sec=600,
        load_balance_stats_period_sec=300,
        max_concurrent_senders=0,
        nested_fields=models.NestedFieldSerializationOptions.NONE,
        throttle_rate_per_sec="0",
        connection_timeout=10000,
        write_timeout=60000,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        enable_multi_metrics=False,
        enable_ack=True,
        log_failed_requests=False,
        max_s2_sversion=models.MaxS2SVersionOptions.V3,
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        indexer_discovery=False,
        sender_unhealthy_time_allowance=100,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        description="veto rarely yahoo and",
        max_failed_health_checks=1,
        compress=models.CompressionOptions.DISABLED,
        indexer_discovery_configs=models.IndexerDiscoveryConfigs(
            site="default",
            master_uri="https://simple-gym.biz",
            refresh_interval_sec=300,
            reject_unauthorized=False,
            auth_tokens=[
                models.OutputSplunkLbAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                    auth_token="",
                    text_secret="<value>",
                ),
            ],
            auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
            auth_token="",
            text_secret="<value>",
        ),
        exclude_self=False,
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
                tls=models.TLSOptionsHostsItems.INHERIT,
                servername="<value>",
                weight=1,
                template_host="<value>",
                template_port="<value>",
            ),
        ],
        pq_strict_ordering=True,
        pq_rate_per_sec=0,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=42,
        pq_max_backpressure_sec=30,
        pq_max_file_size="1 MB",
        pq_max_size="5GB",
        pq_path="$CRIBL_HOME/state/queues",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputSplunkLbPqControls(),
        auth_token="",
        text_secret="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "sqs-output",
        "type": models.OutputSqsType.SQS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "queue_name": "my-queue",
        "queue_type": models.OutputSqsQueueType.STANDARD,
        "aws_account_id": "<id>",
        "message_group_id": "cribl",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "max_queue_size": 100,
        "max_record_size_kb": 256,
        "flush_period_sec": 1,
        "max_in_progress": 10,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "meatloaf um what contrast acknowledge helpfully however shy nor bah",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_queue_name": "<value>",
        "template_aws_account_id": "<id>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesStatsd

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesStatsd" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "statsd-output",
        "type": models.OutputStatsdType.STATSD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "bah reflate however accompanist hunt gut hello",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesStatsdExt

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesStatsdExt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "statsd-ext-output",
        "type": models.OutputStatsdExtType.STATSD_EXT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 512,
        "flush_period_sec": 1,
        "dns_resolve_period_sec": 0,
        "description": "gosh trusty though reword overstay conclude bleach cautiously",
        "throttle_rate_per_sec": "0",
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSumoLogic

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSumoLogic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "sumo-logic-output",
        "type": models.OutputSumoLogicType.SUMO_LOGIC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.OutputSumoLogicDataFormat.JSON,
        "concurrency": 5,
        "max_payload_size_kb": 1024,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 1298.59,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 6460.48,
        "description": "subsidy translation carp impractical woot mozzarella beyond however underneath aboard",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://busy-thigh.biz",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "syslog-output",
        "type": models.OutputSyslogType.SYSLOG,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.OutputSyslogProtocol.TCP,
        "facility": models.Facility.ONE,
        "severity": models.OutputSyslogSeverity.NOTICE,
        "app_name": "Cribl",
        "message_format": models.MessageFormat.RFC3164,
        "timestamp_format": models.TimestampFormat.SYSLOG,
        "throttle_rate_per_sec": "0",
        "octet_count_framing": True,
        "log_failed_requests": False,
        "description": "deeply recount ack satirise typewriter consequently acquaintance",
        "load_balanced": True,
        "host": "localhost",
        "port": 514,
        "exclude_self": False,
        "hosts": [
            {
                "host": "meager-stock.biz",
                "port": 2033.08,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "max_record_size": 1500,
        "udp_dns_resolve_period_sec": 0,
        "enable_ip_spoofing": False,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "tcpjson-output",
        "type": models.OutputTcpjsonType.TCPJSON,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "0",
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "connection_timeout": 10000,
        "write_timeout": 60000,
        "token_ttl_minutes": 60,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "barring astonishing swine creamy but gosh",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "flawless-archaeology.net",
                "port": 2419.51,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 1,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "max_concurrent_senders": 0,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWavefront

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesWavefront" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "wavefront-output",
        "type": models.OutputWavefrontType.WAVEFRONT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "domain": "longboard",
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3992.8,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "onto speedily hmph",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWebhook

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "webhook-output",
        "type": models.OutputWebhookType.WEBHOOK,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "method": models.MethodOptions.POST,
        "format_": models.OutputWebhookFormat.NDJSON,
        "keep_alive": True,
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 8283.06,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputWebhookAuthenticationType.NONE,
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "total_memory_limit_kb": 7404.48,
        "load_balanced": False,
        "description": "fisherman physically besides",
        "custom_source_expression": "__httpOut",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "\\n",
        "custom_content_type": "application/x-ndjson",
        "custom_payload_expression": "`${events}`",
        "advanced_content_type": "application/json",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Jackeline5",
        "password": "tI4tGhpVEwbYMeW",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://honored-yogurt.info/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "`Bearer ${token}`",
        "token_timeout_secs": 3600,
        "oauth_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "oauth_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "url": "https://example.com/webhook",
        "exclude_self": False,
        "urls": [
            {
                "url": "https://blind-mentor.com/",
                "weight": 1,
                "template_url": "https://agreeable-dulcimer.net",
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "template_login_url": "https://funny-premise.biz/",
        "template_secret": "<value>",
        "template_url": "https://shady-zebra.com/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWizHec

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesWizHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "wiz-hec-output",
        "type": models.OutputWizHecType.WIZ_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "load_balanced": True,
        "next_queue": "indexQueue",
        "tcp_routing": "nowhere",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "concurrency": 5,
        "max_payload_size_kb": 4096,
        "max_payload_events": 0,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 2924.72,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "phooey positively a consequently meh until",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6434.77,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2924.72,
        "pq_max_backpressure_sec": 4562.74,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "token": "<value>",
        "text_secret": "<value>",
        "template_wiz_environment": "<value>",
        "template_data_center": "<value>",
        "template_wiz_sourcetype": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesXsiam

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputCreateExamplesXsiam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "xsiam-output",
        "type": models.OutputXsiamType.XSIAM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": False,
        "concurrency": 5,
        "max_payload_size_kb": 9500,
        "max_payload_events": 0,
        "reject_unauthorized": True,
        "timeout_sec": 30,
        "flush_period_sec": 1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "safe_headers": [
            "<value 1>",
        ],
        "auth_type": models.OutputXsiamAuthenticationMethod.TOKEN,
        "response_retry_settings": [
            {
                "http_status": 134.42,
                "initial_backoff": 1000,
                "backoff_rate": 2,
                "max_backoff": 10000,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1000,
            "backoff_rate": 2,
            "max_backoff": 10000,
        },
        "response_honor_retry_after_header": True,
        "throttle_rate_req_per_sec": 400,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 7333.26,
        "description": "cap schlep promptly submitter plus fatal than",
        "url": "http://localhost:8088/logs/v1/event",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://potable-captain.org",
                "weight": 1,
            },
        ],
        "dns_resolve_period_sec": 600,
        "load_balance_stats_period_sec": 300,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 0,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 42,
        "pq_max_backpressure_sec": 30,
        "pq_max_file_size": "1 MB",
        "pq_max_size": "5GB",
        "pq_path": "$CRIBL_HOME/state/queues",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://worthwhile-polarisation.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputExamplesDefault

<!-- UsageSnippet language="python" operationID="updateOutputById" method="patch" path="/system/outputs/{id}" example="OutputExamplesDefault" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.update(id="<id>", output={
        "id": "default-output",
        "type": models.OutputDefaultType.DEFAULT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "default_id": "my-default-output",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to update.                   |
| `output`                                                            | [models.Output](../../models/output.md)                             | :heavy_check_mark:                                                  | Output object                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOutputById" method="delete" path="/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.destinations.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to delete.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |