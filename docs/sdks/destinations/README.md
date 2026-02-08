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
            "<value 2>",
        ],
        "container_name": "my-container",
        "create_container": True,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "max_concurrent_file_parts": 817.98,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 7972.39,
        "max_file_open_time_sec": 8769.44,
        "max_file_idle_time_sec": 2378.15,
        "max_open_files": 6434.56,
        "header_line": "<value>",
        "write_high_water_mark": 646.16,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "auth_type": models.AuthenticationMethodOptions.CLIENT_CERT,
        "storage_class": models.CreateOutputBlobAccessTier.HOT,
        "description": "over rectangular why who instead ferociously sidetrack revoke focused futon",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 4324.82,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 5870.02,
        "directory_batch_size": 8174.56,
        "deadletter_path": "<value>",
        "max_retry_num": 9754.4,
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
            "<value 2>",
            "<value 3>",
        ],
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "validate_database_settings": False,
        "ingest_mode": models.CreateOutputIngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.AuthenticationMethodAzureDataExplorer.CLIENT_SECRET,
        "description": "complete madly simplistic",
        "client_secret": "client-secret",
        "text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 5991.99,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 3292.42,
        "directory_batch_size": 1827.67,
        "deadletter_enabled": False,
        "deadletter_path": "<value>",
        "max_retry_num": 8142.92,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://decent-chops.com/",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "stage_path": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 8975.55,
        "max_file_open_time_sec": 1446.39,
        "max_file_idle_time_sec": 5111.87,
        "max_open_files": 5440.71,
        "max_concurrent_file_parts": 9779.14,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "add_id_to_stage_path": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "timeout_sec": 2127.27,
        "flush_immediately": True,
        "retain_blob_on_success": True,
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
        "report_level": models.CreateOutputReportLevel.DO_NOT_REPORT,
        "report_method": models.CreateOutputReportMethod.QUEUE_AND_TABLE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "concurrency": 187.05,
        "max_payload_size_kb": 6017.97,
        "max_payload_events": 7576.63,
        "flush_period_sec": 5944.28,
        "reject_unauthorized": False,
        "use_round_robin_dns": False,
        "keep_alive": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8661.98,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6573.83,
        "pq_max_backpressure_sec": 94.66,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
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
        "ack": models.AcknowledgmentsOptions.ZERO,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 5899.05,
        "flush_event_count": 6638.01,
        "flush_period_sec": 8055.83,
        "connection_timeout": 9586.96,
        "request_timeout": 9695.69,
        "max_retries": 6088.68,
        "max_back_off": 6052.69,
        "initial_backoff": 6330.98,
        "backoff_rate": 623.59,
        "authentication_timeout": 8813.79,
        "reauthentication_threshold": 1016.21,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "rmAs6PwLK2nbEpz",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Rhianna_Abshire",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.MANUAL,
            "client_secret": "<value>",
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_US,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "gadzooks alive sway sans swiftly gah cemetery",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8523.95,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8483.65,
        "pq_max_backpressure_sec": 5247.04,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "log_type": "Cribl",
        "resource_id": "<id>",
        "concurrency": 9755.46,
        "max_payload_size_kb": 3239.53,
        "max_payload_events": 107.16,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 4538.64,
        "flush_period_sec": 6010.13,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "api_url": "https://bulky-printer.net",
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodAzureLogs.MANUAL,
        "description": "sour mallard ah",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1957.33,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1430.65,
        "pq_max_backpressure_sec": 8951.12,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
        "keypair_secret": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "api_version": "<value>",
        "authentication_method": models.AuthenticationMethodChronicle.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 7385.01,
        "max_payload_size_kb": 5430.66,
        "max_payload_events": 6757.95,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 6647.22,
        "flush_period_sec": 7991.92,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 680.51,
        "ingestion_method": "<value>",
        "namespace": "<value>",
        "log_type": "UNKNOWN",
        "log_text_field": "<value>",
        "gcp_project_id": "my-project",
        "gcp_instance": "customer-id",
        "custom_labels": [
            {
                "key": "<key>",
                "value": "<value>",
                "rbac_enabled": True,
            },
        ],
        "description": "think for lonely snappy council reapply onto",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6383.08,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8317.94,
        "pq_max_backpressure_sec": 8897.34,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "http://localhost:8123/",
        "auth_type": models.AuthenticationTypeClickHouse.BASIC,
        "database": "mydb",
        "table_name": "mytable",
        "format_": models.FormatClickHouse.JSON_COMPACT_EACH_ROW_WITH_NAMES,
        "mapping_type": models.CreateOutputMappingType.AUTOMATIC,
        "async_inserts": True,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 1394.89,
        "max_payload_size_kb": 5341.73,
        "max_payload_events": 8534.7,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 1388.6,
        "flush_period_sec": 1978.4,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "dump_format_errors_to_disk": True,
        "stats_destination": {
            "url": "https://rewarding-government.name",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Nikki20",
            "sql_username": "<value>",
            "password": "MBdiADt_EqwyvJ_",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "alongside blue doubtfully",
        "username": "Aaliyah.Mitchell",
        "password": "j90g4qCNUmopAcY",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://velvety-cross-contamination.biz/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 6937.57,
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
        "sql_username": "<value>",
        "wait_for_async_inserts": False,
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
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7198.36,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 552.93,
        "pq_max_backpressure_sec": 405.08,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodCloudflareR2.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V2,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "verify_permissions": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 319.61,
        "max_open_files": 3509.07,
        "header_line": "<value>",
        "write_high_water_mark": 4903.23,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 8072.1,
        "max_file_idle_time_sec": 3605.52,
        "max_concurrent_file_parts": 251.81,
        "description": "truly yippee pulse",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 3082.8,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 6773.81,
        "directory_batch_size": 9350.87,
        "deadletter_path": "<value>",
        "max_retry_num": 5305.64,
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
            "<value 3>",
        ],
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6305.14,
        "max_queue_size": 4712.6,
        "max_record_size_kb": 54.02,
        "flush_period_sec": 1950.05,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "gah sleepily or selfishly order beautifully stitcher",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5917.34,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9863.81,
        "pq_max_backpressure_sec": 5351.88,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        topic="logs",
        ack=models.AcknowledgmentsOptions1.ONE,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.NONE,
        max_record_size_kb=6128.64,
        flush_event_count=3514.77,
        flush_period_sec=5300.5,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://key-vicinity.info/",
            connection_timeout=9382.36,
            request_timeout=2250.64,
            max_retries=9302.69,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=1951.32,
            default_value_schema_id=5499.87,
        ),
        connection_timeout=7876.49,
        request_timeout=5343.71,
        max_retries=8798.66,
        max_back_off=8515.43,
        initial_backoff=791.86,
        backoff_rate=1309.17,
        authentication_timeout=5121.15,
        reauthentication_threshold=557.68,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Henry_Kilback",
            password="9FPhvPK4v3rJnwx",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://hopeful-help.info",
            client_id="<id>",
            oauth_secret_type="<value>",
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
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        description="marksman eek when pfft partridge hm terrorise",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=8549.89,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=3574.31,
        pq_max_backpressure_sec=1776.95,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.PqControlsConfluentCloud(),
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
        "load_balanced": False,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "token_ttl_minutes": 9316.53,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "compression": models.CompressionOptions1.NONE,
        "concurrency": 1734.52,
        "max_payload_size_kb": 4810.45,
        "max_payload_events": 2634.2,
        "reject_unauthorized": False,
        "timeout_sec": 8177.12,
        "flush_period_sec": 1294.36,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "throttle_rate_per_sec": "<value>",
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "sanity readjust by ah lazily scenario eek why astride er",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "capitalize oh lumbering blaring by inside conservative",
        "url": "https://married-manner.biz/",
        "use_round_robin_dns": True,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://stupendous-replacement.info/",
                "weight": 3117.53,
            },
        ],
        "dns_resolve_period_sec": 1044,
        "load_balance_stats_period_sec": 7719.42,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5564.73,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4108.73,
        "pq_max_backpressure_sec": 7654.09,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7816.2,
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.ONEZONE_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2764.14,
        "max_open_files": 9446.71,
        "header_line": "<value>",
        "write_high_water_mark": 9500.94,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 2482.69,
        "max_file_idle_time_sec": 3981.2,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 7889.42,
        "aws_authentication_method": models.MethodOptionsCredentials.AUTO,
        "format_": models.FormatOptionsCriblLakeDataset.PARQUET,
        "max_concurrent_file_parts": 4107.26,
        "description": "what thoroughly apropos nor yahoo whenever midst agreeable gray psst",
        "empty_dir_cleanup_sec": 9887.29,
        "directory_batch_size": 9452.98,
        "deadletter_path": "<value>",
        "max_retry_num": 147.99,
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
            "reject_unauthorized": False,
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
            "initial_backoff": 8934.01,
            "backoff_rate": 3173.17,
            "max_backoff": 5930.45,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "sanity readjust by ah lazily scenario eek why astride er",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "popularity till contravene secrecy ferociously likely louse afore pendant tromp",
        "url": "https://0.0.0.0:10200",
        "exclude_self": True,
        "urls": [
            {
                "url": "https://stupendous-replacement.info/",
                "weight": 3117.53,
            },
        ],
        "dns_resolve_period_sec": 1638.95,
        "load_balance_stats_period_sec": 2145.95,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5680.41,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8837.87,
        "pq_max_backpressure_sec": 3947.28,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "connection_timeout": 4118.38,
        "write_timeout": 5415.47,
        "token_ttl_minutes": 8431.21,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "overconfidently lovely flight utilized runny outlying till yahoo",
            },
        ],
        "exclude_fields": [
            "<value 1>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "where sarong that",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "proper-prohibition.com",
                "port": 7840.9,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 3441.24,
            },
        ],
        "dns_resolve_period_sec": 4237.3,
        "load_balance_stats_period_sec": 7779.99,
        "max_concurrent_senders": 6098.03,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7535.23,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 3189.59,
        "pq_max_backpressure_sec": 5212.25,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "concurrency": 7961.15,
        "max_payload_size_kb": 1751.08,
        "max_payload_events": 1418.83,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 1251.24,
        "flush_period_sec": 4180.92,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "always unless ha",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8889.52,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 8955.12,
        "pq_max_backpressure_sec": 5752.98,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dest_path": "<value>",
        "stage_path": "<value>",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 8118.95,
        "max_file_open_time_sec": 4778.49,
        "max_file_idle_time_sec": 6500.72,
        "max_open_files": 2941.77,
        "header_line": "<value>",
        "write_high_water_mark": 2897.47,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 6499.49,
        "description": "really testing editor often duh impostor",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 9741.01,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 1478.99,
        "directory_batch_size": 5007.62,
        "deadletter_path": "<value>",
        "max_retry_num": 1451.08,
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
            "<value 3>",
        ],
        "content_type": models.CreateOutputSendLogsAs.TEXT,
        "message": "<value>",
        "source": "<value>",
        "host": "devoted-hubris.org",
        "service": "<value>",
        "tags": [
            "<value 1>",
        ],
        "batch_by_tags": True,
        "allow_api_key_from_events": True,
        "severity": models.SeverityDatadog.NOTICE,
        "site": models.CreateOutputDatadogSite.AP1,
        "send_counters_as_count": True,
        "concurrency": 588.59,
        "max_payload_size_kb": 6147.82,
        "max_payload_events": 8387.71,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 9960.88,
        "flush_period_sec": 2547.26,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "total_memory_limit_kb": 8205.85,
        "description": "yowza both knottily phooey enlightened except minister uh-huh",
        "custom_url": "https://lawful-instructor.biz/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 104.73,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7937.61,
        "pq_max_backpressure_sec": 5285.84,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "message_field": "<value>",
        "exclude_fields": [
            "<value 1>",
        ],
        "server_host_field": "<value>",
        "timestamp_field": "<value>",
        "default_severity": models.SeverityDataset.FINER,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "site": models.CreateOutputDataSetSite.US,
        "concurrency": 9140.95,
        "max_payload_size_kb": 4841.21,
        "max_payload_events": 3237.75,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 6439.19,
        "flush_period_sec": 1895.3,
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
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "total_memory_limit_kb": 5843.82,
        "description": "teeming sting safe healthily spiteful",
        "custom_url": "https://merry-jungle.net",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7407.27,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6106.23,
        "pq_max_backpressure_sec": 7491.95,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
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
        ],
        "time_window": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.CompressionOptionsPersistence.GZIP,
        "partition_expr": "<value>",
        "description": "dapper adventurously brood claw fondly or incomplete",
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
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 4379.67,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions.GLACIER_IR,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9160.62,
        "max_open_files": 4664.43,
        "header_line": "<value>",
        "write_high_water_mark": 6340.06,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 7933.95,
        "max_file_idle_time_sec": 6684.23,
        "max_concurrent_file_parts": 7299.66,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 7832.01,
        "partitioning_fields": [
            "<value 1>",
        ],
        "description": "supposing and volunteer retention gee amnesty",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 4072.64,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 616.57,
        "directory_batch_size": 136.88,
        "deadletter_path": "<value>",
        "max_retry_num": 9976.52,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "method": models.MethodOptions.PATCH,
        "keep_alive": False,
        "concurrency": 4138.07,
        "max_payload_size_kb": 952.7,
        "max_payload_events": 4505.16,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 5365.06,
        "flush_period_sec": 279.61,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationTypeDynatraceHTTP.TOKEN,
        "format_": models.FormatDynatraceHTTP.JSON_ARRAY,
        "endpoint": models.CreateOutputEndpoint.CLOUD,
        "telemetry_type": models.CreateOutputTelemetryType.LOGS,
        "total_memory_limit_kb": 4777.53,
        "description": "consequently preregister transparency drat comb potable",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5892.76,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4977.18,
        "pq_max_backpressure_sec": 8460.08,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "token": "your-api-key",
        "text_secret": "<value>",
        "environment_id": "<id>",
        "active_gate_domain": "<value>",
        "url": "https://fragrant-requirement.org",
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.ProtocolDynatraceOtlp.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "compress": models.CompressionOptions4.NONE,
        "http_compress": models.CompressionOptions5.NONE,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 3795.09,
        "max_payload_size_kb": 6842.82,
        "timeout_sec": 4936.13,
        "flush_period_sec": 2905.07,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 580.05,
        "keep_alive_time": 8124.71,
        "keep_alive": False,
        "endpoint_type": models.CreateOutputEndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "when than potentially gray adult surprised bludgeon break",
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9215.6,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2893.14,
        "pq_max_backpressure_sec": 1267.79,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
        "concurrency": 1305.13,
        "max_payload_size_kb": 1967.39,
        "max_payload_events": 9276.25,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 4811.65,
        "flush_period_sec": 1565.7,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
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
            "username": "Michele_Breitenberg",
            "password": "e9CmlyugMJSf8Yp",
            "auth_type": models.AuthenticationMethodOptionsAuth.TEXT_SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.CreateOutputElasticVersion.SIX,
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "write_action": models.CreateOutputWriteAction.CREATE,
        "retry_partial_errors": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "rue from artistic till unbalance",
        "url": "https://different-guard.com/",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://crafty-loyalty.name/",
                "weight": 1891.06,
            },
        ],
        "dns_resolve_period_sec": 4086.16,
        "load_balance_stats_period_sec": 8486.79,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8212.5,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4021.19,
        "pq_max_backpressure_sec": 6425.86,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "my-cloud-id",
        "index": "logs",
        "concurrency": 1370.06,
        "max_payload_size_kb": 1887.57,
        "max_payload_events": 8629.45,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 2199.13,
        "flush_period_sec": 6328.54,
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
            "username": "Michele_Breitenberg",
            "password": "e9CmlyugMJSf8Yp",
            "auth_type": models.AuthenticationMethodOptionsAuth.TEXT_SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "baptise greedily furthermore silently labourer overcharge",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7344.96,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8050.9,
        "pq_max_backpressure_sec": 4826.17,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
            "<value 2>",
            "<value 3>",
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
        "object_acl": models.ObjectACLOptions1.BUCKET_OWNER_FULL_CONTROL,
        "storage_class": models.StorageClassOptions1.NEARLINE,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "max_file_open_time_sec": 5346.31,
        "max_file_idle_time_sec": 6694.75,
        "max_open_files": 7124.04,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_size_mb": 3929.93,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "times ouch qua chapel",
        "empty_dir_cleanup_sec": 8482.7,
        "directory_batch_size": 9688.35,
        "deadletter_path": "<value>",
        "max_retry_num": 9664.78,
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
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6295.91,
        "max_file_open_time_sec": 9272.25,
        "max_file_idle_time_sec": 8431.64,
        "max_open_files": 7740.89,
        "header_line": "<value>",
        "write_high_water_mark": 5522.82,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "description": "geez psst knowingly yum oof uh-huh rekindle",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 2499.28,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": False,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 9527.71,
        "directory_batch_size": 7326.8,
        "deadletter_path": "<value>",
        "max_retry_num": 5984.31,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "api_version": models.CreateOutputAPIVersion.V1,
        "authentication_method": models.AuthenticationMethodGoogleChronicle.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "log_format_type": models.CreateOutputSendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 8794.34,
        "max_payload_size_kb": 1682.79,
        "max_payload_events": 3320.22,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 1091.39,
        "flush_period_sec": 980.05,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "use_round_robin_dns": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 7865.63,
        "description": "immediate kindly rival whoa madly rightfully selfishly aw eternity sternly",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "until including whether whenever loosely drat excepting",
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
        "udm_type": models.CreateOutputUDMType.ENTITIES,
        "api_key": "<value>",
        "api_key_secret": "<value>",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 916.07,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1786.97,
        "pq_max_backpressure_sec": 2608.15,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
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
        "max_payload_size_kb": 132.27,
        "max_payload_events": 7232.46,
        "flush_period_sec": 4246.62,
        "concurrency": 5003.58,
        "connection_timeout": 3406.78,
        "timeout_sec": 9245.78,
        "throttle_rate_req_per_sec": 815464,
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
        "total_memory_limit_kb": 4191.17,
        "description": "rarely kielbasa unfortunate motionless service",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9958.44,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9384.34,
        "pq_max_backpressure_sec": 495.29,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.AuthenticationMethodGoogleCloudStorage.MANUAL,
        "stage_path": "/tmp/staging",
        "dest_path": "<value>",
        "verify_permissions": True,
        "object_acl": models.ObjectACLOptions1.PUBLIC_READ,
        "storage_class": models.StorageClassOptions1.NEARLINE,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2201.65,
        "max_file_open_time_sec": 2817.56,
        "max_file_idle_time_sec": 3331.7,
        "max_open_files": 7260.53,
        "header_line": "<value>",
        "write_high_water_mark": 9134.23,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "description": "before sonata opera",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 2379.27,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": False,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 2944.76,
        "directory_batch_size": 4948.28,
        "deadletter_path": "<value>",
        "max_retry_num": 6713.99,
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "aws_secret": "<value>",
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
        ],
        "topic_name": "my-topic",
        "create_topic": False,
        "ordered_delivery": False,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.SECRET,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 9392.71,
        "batch_timeout": 4367.52,
        "max_queue_size": 4966.84,
        "max_record_size_kb": 6353.7,
        "flush_period": 1345.87,
        "max_in_progress": 6886.69,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "how corrupt wherever whoa till splay gosh phew chiffonier",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 1312.67,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5116.8,
        "pq_max_backpressure_sec": 8037.49,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 2>",
        ],
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://elementary-window.com/",
        message="<value>",
        message_format=models.MessageFormatOptions.PROTOBUF,
        labels=[
            models.ItemsTypeLabels(
                name="<value>",
                value="<value>",
            ),
        ],
        metric_rename_expr="<value>",
        prometheus_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.TOKEN,
            token="<value>",
            text_secret="<value>",
            username="Bettye.Bayer10",
            password="6WzcIgopzuZrB6K",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.NONE,
            token="<value>",
            text_secret="<value>",
            username="Tremaine_Brakus",
            password="z_x0kTxamYhKAOP",
            credentials_secret="<value>",
        ),
        concurrency=8743.58,
        max_payload_size_kb=6916.2,
        max_payload_events=6975.38,
        reject_unauthorized=False,
        timeout_sec=1530.06,
        flush_period_sec=8821.56,
        extra_http_headers=[
            models.ItemsTypeExtraHTTPHeaders(
                name="<value>",
                value="<value>",
            ),
        ],
        use_round_robin_dns=False,
        failed_request_logging_mode=models.FailedRequestLoggingModeOptions.PAYLOAD,
        safe_headers=[
            "<value 1>",
            "<value 2>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=5395.85,
                initial_backoff=5493.68,
                backoff_rate=5815.97,
                max_backoff=4757.68,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=False,
            initial_backoff=483.81,
            backoff_rate=7907.59,
            max_backoff=37.91,
        ),
        response_honor_retry_after_header=True,
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        description="editor lovable confound which",
        compress=True,
        pq_strict_ordering=True,
        pq_rate_per_sec=3235.66,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=2947.95,
        pq_max_backpressure_sec=5495.79,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.CreateOutputOutputGrafanaCloudPqControls1(),
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
        "mtu": 9598.99,
        "flush_period_sec": 3418.54,
        "dns_resolve_period_sec": 3000.3,
        "description": "gift before hollow overspend overload along story",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 7954.7,
        "write_timeout": 7219.26,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9757.91,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5945.93,
        "pq_max_backpressure_sec": 8516.8,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
        ],
        "dataset": "my-dataset",
        "concurrency": 9249.02,
        "max_payload_size_kb": 8512.21,
        "max_payload_events": 1633.42,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 4547.48,
        "flush_period_sec": 3921.68,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "description": "suffice between but",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3167.42,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8550.61,
        "pq_max_backpressure_sec": 7828.93,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "concurrency": 9133.89,
        "max_payload_size_kb": 6782.11,
        "max_payload_events": 3704.43,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 6769.12,
        "flush_period_sec": 3959.36,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "aside strong promptly who youthfully pertain meh cleverly under psst",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5830.87,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6991.72,
        "pq_max_backpressure_sec": 825.98,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        "timestamp_precision": models.CreateOutputTimestampPrecision.M,
        "dynamic_value_field_name": False,
        "value_field_name": "<value>",
        "concurrency": 3866.76,
        "max_payload_size_kb": 6941.21,
        "max_payload_events": 7388.05,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 6234.27,
        "flush_period_sec": 9162.97,
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationTypeInfluxdb.BASIC,
        "description": "plus micromanage chunter",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9349.14,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3818.09,
        "pq_max_backpressure_sec": 6251.66,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Greg_Gibson46",
        "password": "icfAwtCm5h2Eklm",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://reasonable-steeple.biz/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 788.11,
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
        ack=models.AcknowledgmentsOptions1.ONE,
        format_=models.RecordDataFormatOptions1.RAW,
        compression=models.CompressionOptions3.SNAPPY,
        max_record_size_kb=8326.98,
        flush_event_count=3966.84,
        flush_period_sec=2289.98,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://key-vicinity.info/",
            connection_timeout=9382.36,
            request_timeout=2250.64,
            max_retries=9302.69,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=1951.32,
            default_value_schema_id=5499.87,
        ),
        connection_timeout=2578.59,
        request_timeout=1385.62,
        max_retries=1557.54,
        max_back_off=511.47,
        initial_backoff=3730.07,
        backoff_rate=9302.43,
        authentication_timeout=3768.04,
        reauthentication_threshold=1285.89,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Henry_Kilback",
            password="9FPhvPK4v3rJnwx",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://hopeful-help.info",
            client_id="<id>",
            oauth_secret_type="<value>",
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
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        description="realistic pale alongside",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=7938.77,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=5979.28,
        pq_max_backpressure_sec=7434.96,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.PqControlsKafka(),
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "stream_name": "my-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2865.7,
        "concurrency": 3316.35,
        "max_record_size_kb": 7875.89,
        "flush_period_sec": 730.91,
        "compression": models.CreateOutputCompression.GZIP,
        "use_list_shards": True,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "questionably freight gah tune if for lest before",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 4451.99,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 579.8,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4912.82,
        "pq_max_backpressure_sec": 2288.83,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:3100/loki/api/v1/push",
        "message": "<value>",
        "message_format": models.MessageFormatOptions.JSON,
        "labels": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
        "concurrency": 1442.96,
        "max_payload_size_kb": 3308.55,
        "max_payload_events": 3352.1,
        "reject_unauthorized": False,
        "timeout_sec": 4964.43,
        "flush_period_sec": 3137.64,
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "enable_dynamic_headers": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 4591.93,
        "description": "however valley gloomy annually belabor",
        "compress": True,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Zola.Collier",
        "password": "9kviy8fvS3TbTTq",
        "credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3850.39,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5054.27,
        "pq_max_backpressure_sec": 3645.95,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.ONE,
        "format_": models.RecordDataFormatOptions.RAW,
        "max_record_size_kb": 7982.47,
        "flush_event_count": 262.82,
        "flush_period_sec": 453.27,
        "connection_timeout": 111.17,
        "request_timeout": 5512.73,
        "max_retries": 2681.7,
        "max_back_off": 1343.6,
        "initial_backoff": 5488.51,
        "backoff_rate": 864,
        "authentication_timeout": 4128.18,
        "reauthentication_threshold": 3723.97,
        "sasl": {
            "disabled": True,
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Golden.Dare10",
            "text_secret": "<value>",
            "client_secret_auth_type": models.AuthenticationMethodMicrosoftFabric.CERTIFICATE,
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
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "hmph granny backbone outside hover huzzah provided eyeliner",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9266.94,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3373.93,
        "pq_max_backpressure_sec": 5157.19,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V2,
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3987.39,
        "max_open_files": 9617.76,
        "header_line": "<value>",
        "write_high_water_mark": 2341.4,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 5896.42,
        "max_file_idle_time_sec": 9704.79,
        "max_concurrent_file_parts": 3365.46,
        "description": "merge when fatally finally powerfully",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 5856.71,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 9288.59,
        "directory_batch_size": 1730.32,
        "deadletter_path": "<value>",
        "max_retry_num": 8687.49,
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
        ack=models.AcknowledgmentsOptions1.ZERO,
        format_=models.RecordDataFormatOptions1.PROTOBUF,
        compression=models.CompressionOptions3.SNAPPY,
        max_record_size_kb=6929.65,
        flush_event_count=526.08,
        flush_period_sec=8491.75,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://key-vicinity.info/",
            connection_timeout=9382.36,
            request_timeout=2250.64,
            max_retries=9302.69,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=1951.32,
            default_value_schema_id=5499.87,
        ),
        connection_timeout=1259.19,
        request_timeout=8147.21,
        max_retries=397.36,
        max_back_off=8757.44,
        initial_backoff=2101.9,
        backoff_rate=938.78,
        authentication_timeout=8388.4,
        reauthentication_threshold=4146.44,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V2,
        reuse_connections=False,
        reject_unauthorized=False,
        enable_assume_role=True,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=4973.23,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        description="warmly reassuringly hm shrilly freezing yet cycle",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=3594.47,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=232.42,
        pq_max_backpressure_sec=3423.62,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.PqControlsMsk(),
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
            },
        ],
        "dns_resolve_period_sec": 1950.72,
        "enable_ip_spoofing": True,
        "description": "as vamoose publication",
        "max_record_size": 8108.13,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "region": models.RegionOptions.US,
        "log_type": "<value>",
        "message_field": "<value>",
        "metadata": [
            {
                "name": models.CreateOutputFieldName.AUDIT_ID,
                "value": "<value>",
            },
        ],
        "concurrency": 7584.21,
        "max_payload_size_kb": 4367.44,
        "max_payload_events": 2339.07,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 1441.55,
        "flush_period_sec": 7102.29,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 2272.57,
        "description": "correctly blindly pfft term",
        "custom_url": "https://great-shipper.com/",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 838.73,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5066.07,
        "pq_max_backpressure_sec": 1873.12,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
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
        "region": models.RegionOptions.EU,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 1431.38,
        "max_payload_size_kb": 4941.98,
        "max_payload_events": 7424.99,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 768.04,
        "flush_period_sec": 4832.37,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "description": "straw eulogise in dandelion yowza er until state",
        "custom_url": "https://thrifty-sprinkles.biz",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1465.37,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7267.06,
        "pq_max_backpressure_sec": 2016.21,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.ProtocolOptions.HTTP,
        "endpoint": "http://localhost:4317",
        "otlp_version": models.CreateOutputOTLPVersion.ZERO_DOT_10_DOT_0,
        "compress": models.CompressionOptions4.NONE,
        "http_compress": models.CompressionOptions5.GZIP,
        "auth_type": models.AuthenticationTypeOptions.NONE,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 9299.29,
        "max_payload_size_kb": 739.01,
        "timeout_sec": 6855.16,
        "flush_period_sec": 8781.54,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 7870.65,
        "keep_alive_time": 8054.52,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "across toward sour ugh rightfully cash grown inasmuch cycle",
        "username": "Estell30",
        "password": "vbPEwCUZoqSnXXn",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://strange-farm.net/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 4520.14,
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
        "reject_unauthorized": False,
        "use_round_robin_dns": True,
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 873.64,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 296.68,
        "pq_max_backpressure_sec": 7779.3,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
        "metric_rename_expr": "<value>",
        "send_metadata": True,
        "concurrency": 1078.81,
        "max_payload_size_kb": 803.05,
        "max_payload_events": 5323.37,
        "reject_unauthorized": True,
        "timeout_sec": 6478.51,
        "flush_period_sec": 7969.18,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "description": "including hello gadzooks jubilantly over silk switch huzzah curse",
        "metrics_flush_period_sec": 5827.81,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3738.43,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 1906.14,
        "pq_max_backpressure_sec": 8575.56,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Felipa_Yundt",
        "password": "8mQZMIxN1Wp8T1b",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://complete-feather.com/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 4974.58,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "format_": models.DataFormatRing.RAW,
        "partition_expr": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.DataCompressionFormatOptionsPersistence.NONE,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "description": "rebound softly instead",
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
                "description": "pfft acidly phew selfishly premise",
                "final": True,
            },
        ],
        "description": "scare sans upon lively ick",
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
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 4729.35,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PUBLIC_READ,
        "storage_class": models.StorageClassOptions.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9278.48,
        "max_open_files": 2297.39,
        "header_line": "<value>",
        "write_high_water_mark": 8599.6,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 8481.62,
        "max_file_idle_time_sec": 9149.45,
        "max_concurrent_file_parts": 4846.03,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 8983.89,
        "description": "ultimately furthermore sauerkraut disappointment plain a considering",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 8643.32,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 6295.64,
        "directory_batch_size": 6971.16,
        "deadletter_path": "<value>",
        "max_retry_num": 7249.51,
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionSecurityLake.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1202.81,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "object_acl": models.ObjectACLOptions.BUCKET_OWNER_READ,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "base_file_name": "<value>",
        "max_file_size_mb": 5039.66,
        "max_open_files": 8178.32,
        "header_line": "<value>",
        "write_high_water_mark": 1710.78,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 8843.66,
            "backoff_multiplier": 4381.89,
            "max_backoff_ms": 7295.43,
            "jitter_percent": 1510.88,
        },
        "max_file_open_time_sec": 3271.05,
        "max_file_idle_time_sec": 3715,
        "max_concurrent_file_parts": 8180.46,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 4917.88,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": False,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 62.42,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "description": "graft huzzah huzzah next",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 7941.59,
        "directory_batch_size": 6210.2,
        "parquet_schema": "<value>",
        "deadletter_path": "<value>",
        "max_retry_num": 6171.85,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "keep_alive": False,
        "concurrency": 9907.17,
        "max_payload_size_kb": 8477.7,
        "max_payload_events": 2168.47,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 2411.96,
        "flush_period_sec": 4397.69,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.CreateOutputAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "<value>",
        "endpoint_url_configuration": models.CreateOutputEndpointConfiguration.URL,
        "total_memory_limit_kb": 2131.19,
        "description": "below opposite scramble evenly dress",
        "format_": models.FormatSentinel.JSON_ARRAY,
        "custom_source_expression": "<value>",
        "custom_drop_when_null": True,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2413.07,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7786.01,
        "pq_max_backpressure_sec": 5513.26,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "url": "https://your-workspace.ingest.monitor.azure.com",
        "dcr_id": "<id>",
        "dce_endpoint": "<value>",
        "stream_name": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "region": models.CreateOutputRegion.US,
        "endpoint": models.CreateOutputAISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
        "concurrency": 7007.43,
        "max_payload_size_kb": 6941.56,
        "max_payload_events": 9618.6,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 8044.56,
        "flush_period_sec": 7268.3,
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "couch honored likewise underplay slimy likewise sneak besides fence off",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://happy-solution.name",
        "host_expression": "<value>",
        "source_expression": "<value>",
        "source_type_expression": "<value>",
        "data_source_category_expression": "<value>",
        "data_source_name_expression": "<value>",
        "data_source_vendor_expression": "<value>",
        "event_type_expression": "<value>",
        "host": "vengeful-exasperation.name",
        "source": "<value>",
        "source_type": "<value>",
        "data_source_category": "<value>",
        "data_source_name": "<value>",
        "data_source_vendor": "<value>",
        "event_type": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6867.33,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 3761.04,
        "pq_max_backpressure_sec": 1947.27,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 1094.31,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.NONE,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 7051.95,
        "timeout_sec": 6705.96,
        "flush_period_sec": 7986.11,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "connection_timeout": 530.01,
        "keep_alive_time": 3262.39,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "iterate nifty oof understated ouch since who for down sheepishly",
        "reject_unauthorized": True,
        "use_round_robin_dns": True,
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8940.9,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7799.76,
        "pq_max_backpressure_sec": 3880.07,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "realm": "us0",
        "concurrency": 3746.6,
        "max_payload_size_kb": 6857.66,
        "max_payload_events": 8696.95,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 2650.83,
        "flush_period_sec": 3858.28,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "forceful underneath times yum partially engender digestive cafe",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8080.94,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 9607.51,
        "pq_max_backpressure_sec": 8560.98,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
            },
        ],
        "dns_resolve_period_sec": 7808.33,
        "description": "rosin before coexist but voluntarily hard-to-find gradient from gad",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "max_retries": 7254.4,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionSns.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 5491.06,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "hm godfather hexagon whispered impanel",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3592.3,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5329.21,
        "pq_max_backpressure_sec": 3899.81,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "host": "localhost",
        "port": 9997,
        "nested_fields": models.NestedFieldSerializationOptions.NONE,
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 1113.22,
        "write_timeout": 191.97,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "enable_multi_metrics": False,
        "enable_ack": True,
        "log_failed_requests": True,
        "max_s2_sversion": models.MaxS2SVersionOptions.V3,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "ouch favorite patroller neatly tenement yahoo oh unless charter",
        "max_failed_health_checks": 3081.05,
        "compress": models.CompressionOptions.DISABLED,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2872.5,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4362.89,
        "pq_max_backpressure_sec": 5381.14,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
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
        ],
        "load_balanced": True,
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 8828.22,
        "max_payload_size_kb": 187.91,
        "max_payload_events": 2994.99,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 8657.92,
        "flush_period_sec": 598.7,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "enable_multi_metrics": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "though whoa lasting granular",
        "url": "https://inexperienced-hamburger.org",
        "use_round_robin_dns": True,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://pure-rim.info/",
                "weight": 2627.65,
            },
        ],
        "dns_resolve_period_sec": 2868.7,
        "load_balance_stats_period_sec": 9466.46,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1510.16,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 210.45,
        "pq_max_backpressure_sec": 1881.8,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        dns_resolve_period_sec=8883.23,
        load_balance_stats_period_sec=803.24,
        max_concurrent_senders=2177.23,
        nested_fields=models.NestedFieldSerializationOptions.JSON,
        throttle_rate_per_sec="<value>",
        connection_timeout=6003.32,
        write_timeout=4455.31,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        enable_multi_metrics=True,
        enable_ack=True,
        log_failed_requests=False,
        max_s2_sversion=models.MaxS2SVersionOptions.V3,
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        indexer_discovery=False,
        sender_unhealthy_time_allowance=1542.82,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        description="upward pile since bowed gazebo meanwhile victoriously founder because",
        max_failed_health_checks=5051.06,
        compress=models.CompressionOptions.ALWAYS,
        indexer_discovery_configs=models.CreateOutputIndexerDiscoveryConfigs(
            site="<value>",
            master_uri="https://round-hubris.org/",
            refresh_interval_sec=2684.26,
            reject_unauthorized=False,
            auth_tokens=[
                models.CreateOutputAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                    auth_token="<value>",
                    text_secret="<value>",
                ),
            ],
            auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
            auth_token="<value>",
            text_secret="<value>",
        ),
        exclude_self=True,
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
                tls=models.TLSOptionsHostsItems.OFF,
                servername="<value>",
                weight=1026.01,
            ),
        ],
        pq_strict_ordering=True,
        pq_rate_per_sec=6241.71,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=9335.28,
        pq_max_backpressure_sec=391.14,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.PqControlsSplunkLb(),
        auth_token="<value>",
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
            "<value 2>",
            "<value 3>",
        ],
        "queue_name": "my-queue",
        "queue_type": models.CreateOutputQueueType.STANDARD,
        "aws_account_id": "<id>",
        "message_group_id": "<id>",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 190.66,
        "max_queue_size": 5269.78,
        "max_record_size_kb": 3238.61,
        "flush_period_sec": 5928.95,
        "max_in_progress": 7767.45,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "inasmuch well-worn fidget gah yippee",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 4949.29,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 1745.83,
        "pq_max_backpressure_sec": 6622.91,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        "mtu": 3093.84,
        "flush_period_sec": 532.77,
        "dns_resolve_period_sec": 2433.65,
        "description": "inasmuch deflect sternly daintily except",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 8194.81,
        "write_timeout": 1414.14,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2050.15,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5658.33,
        "pq_max_backpressure_sec": 5763.25,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 1704.38,
        "flush_period_sec": 4478.02,
        "dns_resolve_period_sec": 3892.36,
        "description": "instead towards stake follower for filter",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 7169.4,
        "write_timeout": 8487.93,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9928.78,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 9189.36,
        "pq_max_backpressure_sec": 311.77,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.DataFormatSumoLogic.RAW,
        "concurrency": 5652.68,
        "max_payload_size_kb": 3678.55,
        "max_payload_events": 3287.58,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 5510.66,
        "flush_period_sec": 1412.4,
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
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 2679.88,
        "description": "simplistic oof satirize inquisitively twist",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 339.67,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5075.58,
        "pq_max_backpressure_sec": 7425.95,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.ProtocolSyslog.TCP,
        "facility": models.CreateOutputFacility.FIFTEEN,
        "severity": models.SeveritySyslog.SEVEN,
        "app_name": "<value>",
        "message_format": models.CreateOutputMessageFormat.RFC3164,
        "timestamp_format": models.CreateOutputTimestampFormat.ISO8601,
        "throttle_rate_per_sec": "<value>",
        "octet_count_framing": False,
        "log_failed_requests": True,
        "description": "unique hence rationale",
        "load_balanced": True,
        "host": "localhost",
        "port": 514,
        "exclude_self": True,
        "hosts": [
            {
                "host": "proper-prohibition.com",
                "port": 7840.9,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 3441.24,
            },
        ],
        "dns_resolve_period_sec": 2109.55,
        "load_balance_stats_period_sec": 1344.55,
        "max_concurrent_senders": 8655.62,
        "connection_timeout": 1852.7,
        "write_timeout": 3684.02,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "max_record_size": 2177.9,
        "udp_dns_resolve_period_sec": 3317.49,
        "enable_ip_spoofing": True,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7594.37,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 9174.33,
        "pq_max_backpressure_sec": 4451.17,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        "load_balanced": False,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": True,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "connection_timeout": 861.22,
        "write_timeout": 588.22,
        "token_ttl_minutes": 3391.17,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "suckle parsnip even engage lest",
        "host": "localhost",
        "port": 10090,
        "exclude_self": True,
        "hosts": [
            {
                "host": "proper-prohibition.com",
                "port": 7840.9,
                "tls": models.TLSOptionsHostsItems.INHERIT,
                "servername": "<value>",
                "weight": 3441.24,
            },
        ],
        "dns_resolve_period_sec": 9682.2,
        "load_balance_stats_period_sec": 6468.68,
        "max_concurrent_senders": 2841.6,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5558.99,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7385.62,
        "pq_max_backpressure_sec": 5308.79,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "domain": "longboard",
        "concurrency": 2592.51,
        "max_payload_size_kb": 5525.15,
        "max_payload_events": 3598.58,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 7660.35,
        "flush_period_sec": 6545.92,
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
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "airline coal bah kissingly yippee",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7099.35,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2156.55,
        "pq_max_backpressure_sec": 741.64,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        "method": models.MethodOptions.PATCH,
        "format_": models.FormatWebhook.ADVANCED,
        "keep_alive": False,
        "concurrency": 195.61,
        "max_payload_size_kb": 6141.29,
        "max_payload_events": 2324.34,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 713.5,
        "flush_period_sec": 6612.7,
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
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationTypeWebhook.OAUTH,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "total_memory_limit_kb": 2331,
        "load_balanced": False,
        "description": "hovercraft who stoop sniveling nor etch daddy terribly boastfully for",
        "custom_source_expression": "<value>",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 296.71,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 2474.1,
        "pq_max_backpressure_sec": 2472.75,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Walter_Luettgen",
        "password": "LBwcngVN2Osqsr3",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://criminal-pillow.info",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 9310.05,
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
                "url": "https://yellowish-hunt.org",
                "weight": 6938.99,
            },
        ],
        "dns_resolve_period_sec": 3110.88,
        "load_balance_stats_period_sec": 7669.87,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 3435.49,
        "max_payload_size_kb": 3058.86,
        "max_payload_events": 2063.99,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 3533.62,
        "flush_period_sec": 373.83,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "tuber if er kindheartedly gah",
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
        ],
        "load_balanced": True,
        "concurrency": 3259.32,
        "max_payload_size_kb": 472.91,
        "max_payload_events": 4490.46,
        "reject_unauthorized": True,
        "timeout_sec": 2963.35,
        "flush_period_sec": 4715.94,
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
        "auth_type": models.AuthenticationMethodXsiam.SECRET,
        "response_retry_settings": [
            {
                "http_status": 5395.85,
                "initial_backoff": 5493.68,
                "backoff_rate": 5815.97,
                "max_backoff": 4757.68,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 483.81,
            "backoff_rate": 7907.59,
            "max_backoff": 37.91,
        },
        "response_honor_retry_after_header": False,
        "throttle_rate_req_per_sec": 438080,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 9986.17,
        "description": "term absentmindedly and fraudster generally midst",
        "url": "https://fantastic-amnesty.biz",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://staid-icebreaker.com",
                "weight": 9779.84,
            },
        ],
        "dns_resolve_period_sec": 3568.49,
        "load_balance_stats_period_sec": 3022.38,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6965.85,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6466.31,
        "pq_max_backpressure_sec": 5570.11,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
        ],
        "container_name": "my-container",
        "create_container": True,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "max_concurrent_file_parts": 4580.34,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3396.57,
        "max_file_open_time_sec": 3560.43,
        "max_file_idle_time_sec": 2760.87,
        "max_open_files": 7242.31,
        "header_line": "<value>",
        "write_high_water_mark": 8671.99,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "auth_type": models.AuthenticationMethodOptions.CLIENT_CERT,
        "storage_class": models.BlobAccessTier.COLD,
        "description": "haul that forenenst",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 584.73,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 4294.14,
        "directory_batch_size": 3913.25,
        "deadletter_path": "<value>",
        "max_retry_num": 6602.1,
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
            "<value 2>",
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
        "description": "detective nicely quickly loftily newsstand ghost close nearly intently synthesise",
        "client_secret": "client-secret",
        "text_secret": "<value>",
        "certificate": {
            "certificate_name": "<value>",
        },
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 2241.76,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": False,
        "enable_page_checksum": False,
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 2196.24,
        "directory_batch_size": 8710.85,
        "deadletter_enabled": True,
        "deadletter_path": "<value>",
        "max_retry_num": 9826.65,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://white-marimba.name",
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "stage_path": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 8620.92,
        "max_file_open_time_sec": 6337.34,
        "max_file_idle_time_sec": 7945.47,
        "max_open_files": 365.17,
        "max_concurrent_file_parts": 3276.15,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "add_id_to_stage_path": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "timeout_sec": 9666.97,
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
        "report_level": models.ReportLevel.DO_NOT_REPORT,
        "report_method": models.ReportMethod.QUEUE_AND_TABLE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "concurrency": 1570.66,
        "max_payload_size_kb": 4314.85,
        "max_payload_events": 1553.95,
        "flush_period_sec": 2872.7,
        "reject_unauthorized": True,
        "use_round_robin_dns": False,
        "keep_alive": False,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2424.13,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 958.61,
        "pq_max_backpressure_sec": 1032.28,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.MINUS_1,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 4521.66,
        "flush_event_count": 1564.36,
        "flush_period_sec": 3845.49,
        "connection_timeout": 5506.59,
        "request_timeout": 7472.87,
        "max_retries": 8467.46,
        "max_back_off": 4939.73,
        "initial_backoff": 603.91,
        "backoff_rate": 8979.21,
        "authentication_timeout": 6553.71,
        "reauthentication_threshold": 1502.47,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.SECRET,
            "password": "6ySTtkL9bJUh1Wx",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Lionel.Jakubowski",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.MANUAL,
            "client_secret": "<value>",
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_PARTNER_MICROSOFTONLINE_CN,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "sadly lyre amazing netsuke yeast",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2916.87,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8951.42,
        "pq_max_backpressure_sec": 5374.29,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        "concurrency": 1624.72,
        "max_payload_size_kb": 7964.22,
        "max_payload_events": 8601.9,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 6578.18,
        "flush_period_sec": 7805.65,
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
        ],
        "api_url": "https://straight-fog.net/",
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.OutputAzureLogsAuthenticationMethod.MANUAL,
        "description": "table brr ick following surface ha and",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8033.02,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1733.16,
        "pq_max_backpressure_sec": 6310.27,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
        "keypair_secret": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "api_version": "<value>",
        "authentication_method": models.OutputChronicleAuthenticationMethod.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 7071.07,
        "max_payload_size_kb": 3876.89,
        "max_payload_events": 8892.14,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 5148.73,
        "flush_period_sec": 9715.08,
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
        "use_round_robin_dns": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 4542.52,
        "ingestion_method": "<value>",
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
        "description": "jogging randomize yuppify ack gleefully instead pity",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5340.04,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7887.36,
        "pq_max_backpressure_sec": 3387.4,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "url": "http://localhost:8123/",
        "auth_type": models.OutputClickHouseAuthenticationType.OAUTH,
        "database": "mydb",
        "table_name": "mytable",
        "format_": models.OutputClickHouseFormat.JSON_COMPACT_EACH_ROW_WITH_NAMES,
        "mapping_type": models.MappingType.AUTOMATIC,
        "async_inserts": True,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "concurrency": 5985.05,
        "max_payload_size_kb": 3497.49,
        "max_payload_events": 6323.62,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 24.05,
        "flush_period_sec": 4113.87,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "dump_format_errors_to_disk": True,
        "stats_destination": {
            "url": "https://mealy-rust.name/",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Ubaldo6",
            "sql_username": "<value>",
            "password": "bM1DJajpgFoD_5r",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "recede how for than internalize ick ouch",
        "username": "Ethelyn98",
        "password": "33GliS58gYPjl7D",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://majestic-gastropod.biz",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 8593.96,
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
        "sql_username": "<value>",
        "wait_for_async_inserts": False,
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
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6186.07,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8015.89,
        "pq_max_backpressure_sec": 715.63,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.OutputCloudflareR2AuthenticationMethod.MANUAL,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "verify_permissions": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6944.96,
        "max_open_files": 1443.56,
        "header_line": "<value>",
        "write_high_water_mark": 8928.1,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 9960.23,
        "max_file_idle_time_sec": 2986.51,
        "max_concurrent_file_parts": 1946.7,
        "description": "excluding knowingly energetically incidentally given phooey supposing within",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 2631.54,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 596.4,
        "directory_batch_size": 9978.79,
        "deadletter_path": "<value>",
        "max_retry_num": 4725.91,
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
        ],
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3586.65,
        "max_queue_size": 8020.6,
        "max_record_size_kb": 4014.12,
        "flush_period_sec": 5779.8,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "cautiously seriously till investigate alongside obvious shakily afore",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1614.27,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 6995.82,
        "pq_max_backpressure_sec": 1566.35,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        topic="logs",
        ack=models.AcknowledgmentsOptions1.ZERO,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.SNAPPY,
        max_record_size_kb=9923.99,
        flush_event_count=6751.13,
        flush_period_sec=693.69,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://pitiful-fit.org/",
            connection_timeout=7989.51,
            request_timeout=6279.74,
            max_retries=5484.89,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
            default_key_schema_id=4850.53,
            default_value_schema_id=6240.22,
        ),
        connection_timeout=2850.7,
        request_timeout=3913.49,
        max_retries=6346.75,
        max_back_off=4195.89,
        initial_backoff=5825.56,
        backoff_rate=5390.24,
        authentication_timeout=7366.3,
        reauthentication_threshold=1755.73,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Monte13",
            password="z4xrW3jxrPrE_UR",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.KERBEROS,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://low-handful.biz",
            client_id="<id>",
            oauth_secret_type="<value>",
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
        description="cruelty well-documented poorly",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=8457.47,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=2709.96,
        pq_max_backpressure_sec=8341.2,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputConfluentCloudPqControls(),
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": True,
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "token_ttl_minutes": 6551.76,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "compression": models.CompressionOptions1.NONE,
        "concurrency": 8662.82,
        "max_payload_size_kb": 5200.55,
        "max_payload_events": 1830.87,
        "reject_unauthorized": True,
        "timeout_sec": 2363.66,
        "flush_period_sec": 743.17,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "throttle_rate_per_sec": "<value>",
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "repeatedly since ugh yippee floodlight ugh trolley",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "watery whoa amendment misguided apropos quit outset between aside",
        "url": "https://favorite-horst.net/",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://hurtful-secret.info/",
                "weight": 7112.21,
            },
        ],
        "dns_resolve_period_sec": 1383.86,
        "load_balance_stats_period_sec": 5502.37,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2826.81,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1109,
        "pq_max_backpressure_sec": 2481.88,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 433.66,
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions.GLACIER_IR,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 1372.15,
        "max_open_files": 8899.84,
        "header_line": "<value>",
        "write_high_water_mark": 35.72,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 8119.4,
        "max_file_idle_time_sec": 8688.02,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 9303.09,
        "aws_authentication_method": models.MethodOptionsCredentials.AUTO,
        "format_": models.FormatOptionsCriblLakeDataset.PARQUET,
        "max_concurrent_file_parts": 8774.65,
        "description": "swat until by phew whenever er duh",
        "empty_dir_cleanup_sec": 2310.38,
        "directory_batch_size": 4260.18,
        "deadletter_path": "<value>",
        "max_retry_num": 9036.05,
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
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
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
            "initial_backoff": 981.96,
            "backoff_rate": 7939.43,
            "max_backoff": 9594.37,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "repeatedly since ugh yippee floodlight ugh trolley",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "huzzah by purple service another gah",
        "url": "https://0.0.0.0:10200",
        "exclude_self": True,
        "urls": [
            {
                "url": "https://hurtful-secret.info/",
                "weight": 7112.21,
            },
        ],
        "dns_resolve_period_sec": 4721.64,
        "load_balance_stats_period_sec": 3084.35,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8885.13,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 1154.78,
        "pq_max_backpressure_sec": 879.62,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        "load_balanced": False,
        "compression": models.CompressionOptions1.NONE,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "connection_timeout": 9436.97,
        "write_timeout": 8454.09,
        "token_ttl_minutes": 95.16,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "save outrageous mortally than uselessly minion jittery insist when",
            },
        ],
        "exclude_fields": [
            "<value 1>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "phew beyond eternity finally saloon finally",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "wicked-bend.com",
                "port": 9502.76,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 1086.4,
            },
        ],
        "dns_resolve_period_sec": 3598.76,
        "load_balance_stats_period_sec": 9282.89,
        "max_concurrent_senders": 4950.33,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2810.66,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2806.73,
        "pq_max_backpressure_sec": 5157.3,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "concurrency": 6318.08,
        "max_payload_size_kb": 3488.18,
        "max_payload_events": 3792.45,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 6452.72,
        "flush_period_sec": 7236.96,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "rectangular opposite ew",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9833.62,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7536.74,
        "pq_max_backpressure_sec": 8262.11,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "dest_path": "<value>",
        "stage_path": "<value>",
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6413.72,
        "max_file_open_time_sec": 9372.08,
        "max_file_idle_time_sec": 2511.55,
        "max_open_files": 8005.27,
        "header_line": "<value>",
        "write_high_water_mark": 7971.94,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 5952.58,
        "description": "however taut never distorted aboard",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 4355.49,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 7943.4,
        "directory_batch_size": 6362.56,
        "deadletter_path": "<value>",
        "max_retry_num": 1324.5,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "content_type": models.SendLogsAs.JSON,
        "message": "<value>",
        "source": "<value>",
        "host": "agile-compromise.name",
        "service": "<value>",
        "tags": [
            "<value 1>",
        ],
        "batch_by_tags": True,
        "allow_api_key_from_events": False,
        "severity": models.OutputDatadogSeverity.ERROR,
        "site": models.DatadogSite.CUSTOM,
        "send_counters_as_count": False,
        "concurrency": 62.83,
        "max_payload_size_kb": 1842.84,
        "max_payload_events": 9768.16,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 2975.55,
        "flush_period_sec": 5875.99,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "total_memory_limit_kb": 9611.42,
        "description": "but yellow whereas yowza sweetly scent lobster tectonics consequently golden",
        "custom_url": "https://animated-substitution.name",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1088.03,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6744.35,
        "pq_max_backpressure_sec": 6094.02,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        "default_severity": models.OutputDatasetSeverity.FINEST,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "site": models.DataSetSite.US,
        "concurrency": 1407.28,
        "max_payload_size_kb": 9662.77,
        "max_payload_events": 5952.13,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 7255.09,
        "flush_period_sec": 7666.54,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 3254.58,
        "description": "submitter plus fatal than furthermore each meh",
        "custom_url": "https://somber-tackle.org/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 4335.03,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 9965.77,
        "pq_max_backpressure_sec": 7535.13,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "time_window": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.CompressionOptionsPersistence.GZIP,
        "partition_expr": "<value>",
        "description": "basket yuck enlist where restructure toaster",
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 5551.88,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PUBLIC_READ,
        "storage_class": models.StorageClassOptions.STANDARD_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3256.54,
        "max_open_files": 8910.59,
        "header_line": "<value>",
        "write_high_water_mark": 3829.54,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 3586.58,
        "max_file_idle_time_sec": 4251.32,
        "max_concurrent_file_parts": 436.67,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 1616.18,
        "partitioning_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "description": "personal cavernous decouple excluding",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 6177.61,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": False,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 1893.64,
        "directory_batch_size": 8819.97,
        "deadletter_path": "<value>",
        "max_retry_num": 9772.39,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "method": models.MethodOptions.PUT,
        "keep_alive": True,
        "concurrency": 7037.41,
        "max_payload_size_kb": 9651.26,
        "max_payload_events": 9258.69,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 6716.85,
        "flush_period_sec": 145.13,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputDynatraceHTTPAuthenticationType.TOKEN,
        "format_": models.OutputDynatraceHTTPFormat.JSON_ARRAY,
        "endpoint": models.Endpoint.CLOUD,
        "telemetry_type": models.TelemetryType.LOGS,
        "total_memory_limit_kb": 4591.06,
        "description": "um ouch colligate or aha abaft mmm",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7546.05,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4876.98,
        "pq_max_backpressure_sec": 289.92,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "token": "your-api-key",
        "text_secret": "<value>",
        "environment_id": "<id>",
        "active_gate_domain": "<value>",
        "url": "https://candid-knuckle.info",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.OutputDynatraceOtlpProtocol.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "compress": models.CompressionOptions4.DEFLATE,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 2993.67,
        "max_payload_size_kb": 1500.18,
        "timeout_sec": 5036.53,
        "flush_period_sec": 609.47,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "connection_timeout": 1046.56,
        "keep_alive_time": 667.85,
        "keep_alive": False,
        "endpoint_type": models.EndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "compete out beyond",
        "reject_unauthorized": False,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2172.82,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 506.93,
        "pq_max_backpressure_sec": 1743.29,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "load_balanced": True,
        "index": "logs",
        "doc_type": "<value>",
        "concurrency": 9127.73,
        "max_payload_size_kb": 3933.39,
        "max_payload_events": 2466.52,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 5952.7,
        "flush_period_sec": 5671.89,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": False,
            "username": "Claudine69",
            "password": "J3ts4hhLd7yGMlA",
            "auth_type": models.AuthenticationMethodOptionsAuth.SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.ElasticVersion.AUTO,
        "elastic_pipeline": "<value>",
        "include_doc_id": False,
        "write_action": models.WriteAction.INDEX,
        "retry_partial_errors": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "however inside knowledgeable severe eyeglasses fit ha",
        "url": "https://soft-tuba.net",
        "use_round_robin_dns": True,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://profitable-completion.biz/",
                "weight": 261.53,
            },
        ],
        "dns_resolve_period_sec": 6235.99,
        "load_balance_stats_period_sec": 4923.9,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2187.35,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1791.54,
        "pq_max_backpressure_sec": 8996.67,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
        ],
        "url": "my-cloud-id",
        "index": "logs",
        "concurrency": 8334.63,
        "max_payload_size_kb": 4489.5,
        "max_payload_events": 988.45,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 8382.89,
        "flush_period_sec": 5937.18,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": False,
            "username": "Claudine69",
            "password": "J3ts4hhLd7yGMlA",
            "auth_type": models.AuthenticationMethodOptionsAuth.SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "pish pessimistic after um disgorge within",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 122.24,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8807.85,
        "pq_max_backpressure_sec": 8400.29,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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
            "<value 2>",
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
        "signature_version": models.SignatureVersionOptions4.V2,
        "object_acl": models.ObjectACLOptions1.PUBLIC_READ,
        "storage_class": models.StorageClassOptions1.COLDLINE,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "max_file_open_time_sec": 6749.81,
        "max_file_idle_time_sec": 6990.43,
        "max_open_files": 3101.21,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_size_mb": 8701.26,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "derby once yahoo braid clavicle cross-contamination crushing clavicle swing",
        "empty_dir_cleanup_sec": 8440.38,
        "directory_batch_size": 8815.99,
        "deadletter_path": "<value>",
        "max_retry_num": 4597.15,
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
        ],
        "dest_path": "/var/log/output",
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 4579.59,
        "max_file_open_time_sec": 1591.93,
        "max_file_idle_time_sec": 1645.42,
        "max_open_files": 2710.22,
        "header_line": "<value>",
        "write_high_water_mark": 8023.17,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "description": "outside dish worth rapidly joyfully requite until",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 8841.03,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": False,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 4416.3,
        "directory_batch_size": 450.74,
        "deadletter_path": "<value>",
        "max_retry_num": 1172.59,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "api_version": models.OutputGoogleChronicleAPIVersion.V1,
        "authentication_method": models.OutputGoogleChronicleAuthenticationMethod.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "log_format_type": models.SendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 194.88,
        "max_payload_size_kb": 7780.64,
        "max_payload_events": 2256.5,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 4616.39,
        "flush_period_sec": 9309.58,
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
        "use_round_robin_dns": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 6941.09,
        "description": "insecure equatorial release until scaly around inasmuch eek",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "solder dull stay yet overcooked per debut attest",
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
        "udm_type": models.UDMType.ENTITIES,
        "api_key": "<value>",
        "api_key_secret": "<value>",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2043.78,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8903.83,
        "pq_max_backpressure_sec": 8508.98,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "log_location_type": models.LogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "sanitize_log_names": True,
        "payload_format": models.PayloadFormat.JSON,
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
        "google_auth_method": models.GoogleAuthenticationMethodOptions.AUTO,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_payload_size_kb": 2256.87,
        "max_payload_events": 2919.53,
        "flush_period_sec": 6889.61,
        "concurrency": 494.84,
        "connection_timeout": 2659.94,
        "timeout_sec": 8967.63,
        "throttle_rate_req_per_sec": 862713,
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
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 7513.2,
        "description": "save excluding ornery ameliorate",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6862.95,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4789.34,
        "pq_max_backpressure_sec": 9408.21,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
            "<value 3>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.OutputGoogleCloudStorageAuthenticationMethod.SECRET,
        "stage_path": "/tmp/staging",
        "dest_path": "<value>",
        "verify_permissions": False,
        "object_acl": models.ObjectACLOptions1.PRIVATE,
        "storage_class": models.StorageClassOptions1.ARCHIVE,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 5999.09,
        "max_file_open_time_sec": 5928.82,
        "max_file_idle_time_sec": 8950.65,
        "max_open_files": 7438.31,
        "header_line": "<value>",
        "write_high_water_mark": 2698.13,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "description": "miserably vicinity blindly moral bossy",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 467.44,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 7003.57,
        "directory_batch_size": 3127.55,
        "deadletter_path": "<value>",
        "max_retry_num": 7631.55,
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "aws_secret": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic_name": "my-topic",
        "create_topic": True,
        "ordered_delivery": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 9464.52,
        "batch_timeout": 5743.79,
        "max_queue_size": 8657.4,
        "max_record_size_kb": 7839.81,
        "flush_period": 7804.51,
        "max_in_progress": 7060.4,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "bowed jiggle acquire down bootleg",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1114.52,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 3535.93,
        "pq_max_backpressure_sec": 1129.99,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 3>",
        ],
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://deep-bidet.info",
        message="<value>",
        message_format=models.MessageFormatOptions.PROTOBUF,
        labels=[
            models.ItemsTypeLabels(
                name="<value>",
                value="<value>",
            ),
        ],
        metric_rename_expr="<value>",
        prometheus_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.TEXT_SECRET,
            token="<value>",
            text_secret="<value>",
            username="Telly34",
            password="xj5Pr1ID0oewBJ5",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.TOKEN,
            token="<value>",
            text_secret="<value>",
            username="Eduardo10",
            password="6qD_OjiWX1YoRh0",
            credentials_secret="<value>",
        ),
        concurrency=6675.42,
        max_payload_size_kb=7351.76,
        max_payload_events=1764.31,
        reject_unauthorized=False,
        timeout_sec=3221.15,
        flush_period_sec=3452.4,
        extra_http_headers=[
            models.ItemsTypeExtraHTTPHeaders(
                name="<value>",
                value="<value>",
            ),
        ],
        use_round_robin_dns=True,
        failed_request_logging_mode=models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        safe_headers=[
            "<value 1>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=3612.5,
                initial_backoff=2452.56,
                backoff_rate=1370.95,
                max_backoff=434.99,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=False,
            initial_backoff=1512.93,
            backoff_rate=7289.7,
            max_backoff=7576.49,
        ),
        response_honor_retry_after_header=False,
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        description="countess furthermore excess stable neat veto ick behind requite",
        compress=False,
        pq_strict_ordering=False,
        pq_rate_per_sec=4717.14,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=7755.43,
        pq_max_backpressure_sec=6556.99,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.OutputGrafanaCloudPqControls1(),
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
        "mtu": 60.21,
        "flush_period_sec": 7162.25,
        "dns_resolve_period_sec": 3967.84,
        "description": "silently save hope acquire reluctantly inside own outside geez segregate",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 815.93,
        "write_timeout": 4625.77,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 253.31,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5622.83,
        "pq_max_backpressure_sec": 5811.19,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "dataset": "my-dataset",
        "concurrency": 9827.16,
        "max_payload_size_kb": 4188.74,
        "max_payload_events": 3305.31,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 8127.64,
        "flush_period_sec": 1093.1,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "crooked drat readmit",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 642.3,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 732.36,
        "pq_max_backpressure_sec": 6647.84,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "concurrency": 6046.59,
        "max_payload_size_kb": 3582.01,
        "max_payload_events": 9470.26,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 6546.11,
        "flush_period_sec": 9923.35,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "writhing sizzle mechanically actually of etch quick",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6722.38,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6024.32,
        "pq_max_backpressure_sec": 6541.46,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        "url": "http://localhost:8086",
        "use_v2_api": False,
        "timestamp_precision": models.TimestampPrecision.U,
        "dynamic_value_field_name": True,
        "value_field_name": "<value>",
        "concurrency": 5996.06,
        "max_payload_size_kb": 4850.95,
        "max_payload_events": 7404.99,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 9587.3,
        "flush_period_sec": 3902.6,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputInfluxdbAuthenticationType.NONE,
        "description": "ugh trash solicit key gymnast bracelet ew sarong cumbersome um",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5201.94,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1717.22,
        "pq_max_backpressure_sec": 8317.89,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Kelvin_Schinner50",
        "password": "xOV1CyorOVG2SAG",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://muffled-venom.name/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 4728.73,
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
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        brokers=[
            "localhost:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.ZERO,
        format_=models.RecordDataFormatOptions1.RAW,
        compression=models.CompressionOptions3.ZSTD,
        max_record_size_kb=9335.5,
        flush_event_count=6847.29,
        flush_period_sec=5265.71,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://pitiful-fit.org/",
            connection_timeout=7989.51,
            request_timeout=6279.74,
            max_retries=5484.89,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
            default_key_schema_id=4850.53,
            default_value_schema_id=6240.22,
        ),
        connection_timeout=632.63,
        request_timeout=7810.04,
        max_retries=3762.8,
        max_back_off=7826.94,
        initial_backoff=1688.06,
        backoff_rate=9488.3,
        authentication_timeout=6683.04,
        reauthentication_threshold=1380.2,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Monte13",
            password="z4xrW3jxrPrE_UR",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.KERBEROS,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://low-handful.biz",
            client_id="<id>",
            oauth_secret_type="<value>",
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
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        description="indeed simple angle daddy before",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=False,
        pq_rate_per_sec=1608.03,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=7762.89,
        pq_max_backpressure_sec=5546.58,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputKafkaPqControls(),
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2327.88,
        "concurrency": 180.13,
        "max_record_size_kb": 2560.27,
        "flush_period_sec": 1305.95,
        "compression": models.OutputKinesisCompression.NONE,
        "use_list_shards": True,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "including during sundae",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 3193.11,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1415.77,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 9189.02,
        "pq_max_backpressure_sec": 8824.28,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "url": "http://localhost:3100/loki/api/v1/push",
        "message": "<value>",
        "message_format": models.MessageFormatOptions.JSON,
        "labels": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.TEXT_SECRET,
        "concurrency": 7676.41,
        "max_payload_size_kb": 8598.26,
        "max_payload_events": 9409.24,
        "reject_unauthorized": True,
        "timeout_sec": 6028.87,
        "flush_period_sec": 6526.76,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "enable_dynamic_headers": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 7686.34,
        "description": "premier healthily freight ha till furthermore excepting diver",
        "compress": True,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Matilde65",
        "password": "xqJcOYhJD96fk1o",
        "credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 794.19,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7756.87,
        "pq_max_backpressure_sec": 7578.66,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.ONE,
        "format_": models.RecordDataFormatOptions.JSON,
        "max_record_size_kb": 3515.83,
        "flush_event_count": 5133.45,
        "flush_period_sec": 9242.46,
        "connection_timeout": 4763.74,
        "request_timeout": 7816.61,
        "max_retries": 6437.59,
        "max_back_off": 3343.13,
        "initial_backoff": 1754.74,
        "backoff_rate": 1772.66,
        "authentication_timeout": 8068.63,
        "reauthentication_threshold": 9336.44,
        "sasl": {
            "disabled": False,
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Tristin_White",
            "text_secret": "<value>",
            "client_secret_auth_type": models.OutputMicrosoftFabricAuthenticationMethod.SECRET,
            "client_text_secret": "<value>",
            "certificate_name": "<value>",
            "cert_path": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_US,
            "client_id": "<id>",
            "tenant_id": "<id>",
            "scope": "<value>",
        },
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "oof doing quickly bloom scary oof worth",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5910.37,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7996.45,
        "pq_max_backpressure_sec": 721.72,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": models.ObjectACLOptions.BUCKET_OWNER_FULL_CONTROL,
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9148.78,
        "max_open_files": 8176.95,
        "header_line": "<value>",
        "write_high_water_mark": 5965.49,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 8733.54,
        "max_file_idle_time_sec": 2457.48,
        "max_concurrent_file_parts": 1224.76,
        "description": "late beep freezing about broadside defenseless ajar hmph past yuck",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 5866.7,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": False,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 734.84,
        "directory_batch_size": 8236.09,
        "deadletter_path": "<value>",
        "max_retry_num": 9685.91,
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
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.MINUS_1,
        format_=models.RecordDataFormatOptions1.PROTOBUF,
        compression=models.CompressionOptions3.SNAPPY,
        max_record_size_kb=1538.83,
        flush_event_count=8245.04,
        flush_period_sec=6192.18,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://pitiful-fit.org/",
            connection_timeout=7989.51,
            request_timeout=6279.74,
            max_retries=5484.89,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=True,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=False,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
            default_key_schema_id=4850.53,
            default_value_schema_id=6240.22,
        ),
        connection_timeout=768.28,
        request_timeout=4188.17,
        max_retries=3722.18,
        max_back_off=864.6,
        initial_backoff=1640.63,
        backoff_rate=2251,
        authentication_timeout=3509.93,
        reauthentication_threshold=1897.23,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V2,
        reuse_connections=False,
        reject_unauthorized=True,
        enable_assume_role=False,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=936.75,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        description="thankfully lest resource",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=3645.11,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=8425.35,
        pq_max_backpressure_sec=3700.97,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputMskPqControls(),
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
            },
        ],
        "dns_resolve_period_sec": 2279.48,
        "enable_ip_spoofing": True,
        "description": "hefty yawningly short successfully given tray cod",
        "max_record_size": 7657.6,
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "region": models.RegionOptions.EU,
        "log_type": "<value>",
        "message_field": "<value>",
        "metadata": [
            {
                "name": models.FieldName.SERVICE,
                "value": "<value>",
            },
        ],
        "concurrency": 7353.66,
        "max_payload_size_kb": 7927.67,
        "max_payload_events": 2106.86,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 7201.59,
        "flush_period_sec": 694.13,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 5205.55,
        "description": "bleach cautiously psst whenever",
        "custom_url": "https://serpentine-draw.net",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6481.07,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4366.65,
        "pq_max_backpressure_sec": 1664.77,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "region": models.RegionOptions.US,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 1532.27,
        "max_payload_size_kb": 9645.91,
        "max_payload_events": 4360.95,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 3897.41,
        "flush_period_sec": 4034.67,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "ill-fated down tennis crumble",
        "custom_url": "https://recent-technician.org",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2503.54,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 8623.14,
        "pq_max_backpressure_sec": 4349.61,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
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
            "<value 2>",
        ],
        "protocol": models.ProtocolOptions.HTTP,
        "endpoint": "http://localhost:4317",
        "otlp_version": models.OutputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0,
        "compress": models.CompressionOptions4.NONE,
        "http_compress": models.CompressionOptions5.GZIP,
        "auth_type": models.AuthenticationTypeOptions.OAUTH,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 7303.11,
        "max_payload_size_kb": 8230.1,
        "timeout_sec": 5107.11,
        "flush_period_sec": 8697.13,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 5372.86,
        "keep_alive_time": 2687.71,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "fray jovially brr despite even",
        "username": "Burnice.Yost26",
        "password": "xHJbfZYfEAhnjju",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://tame-lender.net/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 2153.54,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
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
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9312.71,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1752.16,
        "pq_max_backpressure_sec": 3780.65,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
        ],
        "url": "http://localhost:9091/api/v1/write",
        "metric_rename_expr": "<value>",
        "send_metadata": False,
        "concurrency": 3559.44,
        "max_payload_size_kb": 1232.43,
        "max_payload_events": 8644.71,
        "reject_unauthorized": True,
        "timeout_sec": 3599.31,
        "flush_period_sec": 8634.13,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.TOKEN,
        "description": "efface putrefy cannon whose how hard-to-find wry imaginary down",
        "metrics_flush_period_sec": 5953.83,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2175.69,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7522.56,
        "pq_max_backpressure_sec": 4247.3,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Joy.Herzog",
        "password": "a2t5_lDRX3upjqM",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://different-festival.biz/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 1717.51,
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
        ],
        "format_": models.OutputRingDataFormat.RAW,
        "partition_expr": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "description": "phooey although yowza instead irritably stark gleefully",
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
                "description": "pigpen procurement aha minus cautious density phony alliance",
                "final": True,
            },
        ],
        "description": "but midst cuddly coal eek",
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6731.29,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.BUCKET_OWNER_READ,
        "storage_class": models.StorageClassOptions.GLACIER,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9585.8,
        "max_open_files": 2297.86,
        "header_line": "<value>",
        "write_high_water_mark": 9300.56,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 8428.01,
        "max_file_idle_time_sec": 8114.35,
        "max_concurrent_file_parts": 3254.02,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 2839.27,
        "description": "failing until once sure-footed gladly loudly",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 8889.64,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": False,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": False,
        "enable_write_page_index": True,
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 5146.49,
        "directory_batch_size": 7356.99,
        "deadletter_path": "<value>",
        "max_retry_num": 3781.94,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "endpoint": "<value>",
        "signature_version": models.OutputSecurityLakeSignatureVersion.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7772.47,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "<value>",
        "max_file_size_mb": 3373.72,
        "max_open_files": 5153.34,
        "header_line": "<value>",
        "write_high_water_mark": 1755.89,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 5350.49,
            "backoff_multiplier": 7874.9,
            "max_backoff_ms": 874.88,
            "jitter_percent": 7218.41,
        },
        "max_file_open_time_sec": 7380.27,
        "max_file_idle_time_sec": 6476.19,
        "max_concurrent_file_parts": 6966.41,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 7652.27,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": True,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 2309.31,
        "parquet_page_size": "<value>",
        "should_log_invalid_rows": True,
        "key_value_metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "enable_statistics": True,
        "enable_write_page_index": True,
        "enable_page_checksum": False,
        "description": "replicate generously representation blah fully around",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 7237.78,
        "directory_batch_size": 287.34,
        "parquet_schema": "<value>",
        "deadletter_path": "<value>",
        "max_retry_num": 1915.82,
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
            "<value 2>",
            "<value 3>",
        ],
        "keep_alive": False,
        "concurrency": 4399.27,
        "max_payload_size_kb": 9319.08,
        "max_payload_events": 5469.02,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 6136.59,
        "flush_period_sec": 1433.57,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": True,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.OutputSentinelAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "<value>",
        "endpoint_url_configuration": models.EndpointConfiguration.URL,
        "total_memory_limit_kb": 6699.04,
        "description": "pleasure helpfully pulse upside-down",
        "format_": models.OutputSentinelFormat.ADVANCED,
        "custom_source_expression": "<value>",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 4904.24,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7621.74,
        "pq_max_backpressure_sec": 3266.81,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "url": "https://your-workspace.ingest.monitor.azure.com",
        "dcr_id": "<id>",
        "dce_endpoint": "<value>",
        "stream_name": "<value>",
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
        "concurrency": 1879.1,
        "max_payload_size_kb": 3366.3,
        "max_payload_events": 571.7,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 8731.16,
        "flush_period_sec": 6457.57,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "safe_headers": [
            "<value 1>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "tinted interesting however yieldingly mid unlike once er",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://grimy-noon.org/",
        "host_expression": "<value>",
        "source_expression": "<value>",
        "source_type_expression": "<value>",
        "data_source_category_expression": "<value>",
        "data_source_name_expression": "<value>",
        "data_source_vendor_expression": "<value>",
        "event_type_expression": "<value>",
        "host": "needy-tail.org",
        "source": "<value>",
        "source_type": "<value>",
        "data_source_category": "<value>",
        "data_source_name": "<value>",
        "data_source_vendor": "<value>",
        "event_type": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7517.5,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 134.42,
        "pq_max_backpressure_sec": 7333.26,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 4039.66,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.DEFLATE,
        "http_compress": models.CompressionOptions5.GZIP,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 3207.88,
        "timeout_sec": 5233.08,
        "flush_period_sec": 7948.24,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "connection_timeout": 5268.97,
        "keep_alive_time": 9870.05,
        "keep_alive": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "boastfully though verbally platter",
        "reject_unauthorized": False,
        "use_round_robin_dns": True,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "tls": {
            "disabled": True,
            "reject_unauthorized": True,
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5472.53,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3475.52,
        "pq_max_backpressure_sec": 3068.73,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "realm": "us0",
        "concurrency": 5119.86,
        "max_payload_size_kb": 5622.39,
        "max_payload_events": 5603.69,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 541.38,
        "flush_period_sec": 554.97,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "polite reopen lovingly above although into along",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8210.07,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6689.36,
        "pq_max_backpressure_sec": 3904.75,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
            },
        ],
        "dns_resolve_period_sec": 1120.23,
        "description": "whereas while meh oof behind traffic birdbath ha hm whereas",
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
            "<value 2>",
            "<value 3>",
        ],
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "max_retries": 2825.52,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.OutputSnsSignatureVersion.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 9771.63,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "bare phooey commonly instead phew consequently exasperation step",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2374.95,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 457.14,
        "pq_max_backpressure_sec": 3517.03,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "host": "localhost",
        "port": 9997,
        "nested_fields": models.NestedFieldSerializationOptions.NONE,
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 1830.9,
        "write_timeout": 6698.03,
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "enable_multi_metrics": True,
        "enable_ack": False,
        "log_failed_requests": False,
        "max_s2_sversion": models.MaxS2SVersionOptions.V3,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "after baa though zowie about scratchy unto",
        "max_failed_health_checks": 8890.04,
        "compress": models.CompressionOptions.AUTO,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6766.21,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2535.92,
        "pq_max_backpressure_sec": 6333.18,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
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
            "<value 3>",
        ],
        "load_balanced": False,
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "concurrency": 7743.2,
        "max_payload_size_kb": 8796,
        "max_payload_events": 3591.27,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 1219.61,
        "flush_period_sec": 5995.45,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "hmph separately mobilize sugary deliberately since unbearably",
        "url": "https://potable-seafood.com",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://far-off-chairperson.org/",
                "weight": 3495.92,
            },
        ],
        "dns_resolve_period_sec": 7882.73,
        "load_balance_stats_period_sec": 3036.32,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 675.99,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7321.13,
        "pq_max_backpressure_sec": 2936.9,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
        ],
        dns_resolve_period_sec=5335.2,
        load_balance_stats_period_sec=7027.9,
        max_concurrent_senders=8151.45,
        nested_fields=models.NestedFieldSerializationOptions.JSON,
        throttle_rate_per_sec="<value>",
        connection_timeout=1626.21,
        write_timeout=6511.23,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        enable_multi_metrics=False,
        enable_ack=True,
        log_failed_requests=True,
        max_s2_sversion=models.MaxS2SVersionOptions.V3,
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        indexer_discovery=False,
        sender_unhealthy_time_allowance=4137.33,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        description="hyena lest trustworthy sedately dilate as ack",
        max_failed_health_checks=8723.07,
        compress=models.CompressionOptions.ALWAYS,
        indexer_discovery_configs=models.IndexerDiscoveryConfigs(
            site="<value>",
            master_uri="https://quarrelsome-phrase.biz/",
            refresh_interval_sec=7207.13,
            reject_unauthorized=False,
            auth_tokens=[
                models.OutputSplunkLbAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                    auth_token="<value>",
                    text_secret="<value>",
                ),
            ],
            auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
            auth_token="<value>",
            text_secret="<value>",
        ),
        exclude_self=True,
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
                tls=models.TLSOptionsHostsItems.INHERIT,
                servername="<value>",
                weight=8212.15,
            ),
        ],
        pq_strict_ordering=True,
        pq_rate_per_sec=979.79,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=4046.95,
        pq_max_backpressure_sec=2626.82,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputSplunkLbPqControls(),
        auth_token="<value>",
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
        ],
        "queue_name": "my-queue",
        "queue_type": models.OutputSqsQueueType.STANDARD,
        "aws_account_id": "<id>",
        "message_group_id": "<id>",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8892.03,
        "max_queue_size": 1756.31,
        "max_record_size_kb": 6677.81,
        "flush_period_sec": 9360.69,
        "max_in_progress": 2064.65,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "submitter as intently mortally pale vainly knickers",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9077.33,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7720.51,
        "pq_max_backpressure_sec": 7048.98,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 5877.5,
        "flush_period_sec": 4783.22,
        "dns_resolve_period_sec": 920.15,
        "description": "officially independence yet nervously what yuppify futon yearningly",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 7965.79,
        "write_timeout": 4035.15,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9765.21,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 5342.07,
        "pq_max_backpressure_sec": 4943.9,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
        "mtu": 2119.13,
        "flush_period_sec": 6238.24,
        "dns_resolve_period_sec": 3006.42,
        "description": "acquaintance cannon councilman proper brr",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 9750.99,
        "write_timeout": 984.97,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9501.13,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8671.5,
        "pq_max_backpressure_sec": 1157.66,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.OutputSumoLogicDataFormat.JSON,
        "concurrency": 2454.78,
        "max_payload_size_kb": 6558.45,
        "max_payload_events": 386.08,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 6525.84,
        "flush_period_sec": 1666.15,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "use_round_robin_dns": False,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 9130.6,
        "description": "ew rally readjust",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3031.72,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7340.67,
        "pq_max_backpressure_sec": 1424.73,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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
            "<value 3>",
        ],
        "protocol": models.OutputSyslogProtocol.TCP,
        "facility": models.Facility.THREE,
        "severity": models.OutputSyslogSeverity.FIVE,
        "app_name": "<value>",
        "message_format": models.MessageFormat.RFC3164,
        "timestamp_format": models.TimestampFormat.ISO8601,
        "throttle_rate_per_sec": "<value>",
        "octet_count_framing": False,
        "log_failed_requests": False,
        "description": "sternly meaningfully next banish hypothesise obedient inside lest",
        "load_balanced": True,
        "host": "localhost",
        "port": 514,
        "exclude_self": True,
        "hosts": [
            {
                "host": "wicked-bend.com",
                "port": 9502.76,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 1086.4,
            },
        ],
        "dns_resolve_period_sec": 2481.04,
        "load_balance_stats_period_sec": 6460.17,
        "max_concurrent_senders": 4936.63,
        "connection_timeout": 4135.93,
        "write_timeout": 5785.19,
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "max_record_size": 8293.42,
        "udp_dns_resolve_period_sec": 9163.14,
        "enable_ip_spoofing": False,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 667.32,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2272.28,
        "pq_max_backpressure_sec": 3939.53,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": False,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": False,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": False,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "connection_timeout": 8617.16,
        "write_timeout": 2926.39,
        "token_ttl_minutes": 4733.74,
        "send_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "querulous bah next",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "wicked-bend.com",
                "port": 9502.76,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 1086.4,
            },
        ],
        "dns_resolve_period_sec": 1462.84,
        "load_balance_stats_period_sec": 6447.76,
        "max_concurrent_senders": 2014.57,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9647.54,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 8742.12,
        "pq_max_backpressure_sec": 8669.78,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
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
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "domain": "longboard",
        "concurrency": 3483.48,
        "max_payload_size_kb": 3129.76,
        "max_payload_events": 5185.4,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 1527.25,
        "flush_period_sec": 5851.43,
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
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "cool unlike crumble circulate materialise intermesh male incidentally celebrate",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 69.34,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7460.02,
        "pq_max_backpressure_sec": 1638.93,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "method": models.MethodOptions.POST,
        "format_": models.OutputWebhookFormat.NDJSON,
        "keep_alive": True,
        "concurrency": 2157.18,
        "max_payload_size_kb": 2167.96,
        "max_payload_events": 3492.97,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 2064.64,
        "flush_period_sec": 934.33,
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
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.OutputWebhookAuthenticationType.TOKEN,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "total_memory_limit_kb": 3175.03,
        "load_balanced": False,
        "description": "uproot pocket-watch before apricot effector mostly cruelty pro vice",
        "custom_source_expression": "<value>",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7799.85,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2604.07,
        "pq_max_backpressure_sec": 6730.04,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Leatha.Reynolds52",
        "password": "saDFsa6Z7GLu206",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://well-worn-minister.biz/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 1647.17,
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
                "url": "https://warmhearted-pigsty.name",
                "weight": 1557.06,
            },
        ],
        "dns_resolve_period_sec": 5079.2,
        "load_balance_stats_period_sec": 5978.28,
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
            "<value 2>",
            "<value 3>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": False,
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "concurrency": 7233.72,
        "max_payload_size_kb": 8699.57,
        "max_payload_events": 1501.04,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 7438.51,
        "flush_period_sec": 9385.01,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "enable_multi_metrics": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "rekindle for clear cassava overdue whoa cram incidentally",
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
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "load_balanced": False,
        "concurrency": 4531.24,
        "max_payload_size_kb": 5109.16,
        "max_payload_events": 5522.41,
        "reject_unauthorized": False,
        "timeout_sec": 5473.45,
        "flush_period_sec": 2900.95,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "safe_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.OutputXsiamAuthenticationMethod.SECRET,
        "response_retry_settings": [
            {
                "http_status": 3612.5,
                "initial_backoff": 2452.56,
                "backoff_rate": 1370.95,
                "max_backoff": 434.99,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 1512.93,
            "backoff_rate": 7289.7,
            "max_backoff": 7576.49,
        },
        "response_honor_retry_after_header": True,
        "throttle_rate_req_per_sec": 292667,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 3093.15,
        "description": "fabricate till hopelessly clamor bah icy apropos cruelly barring ick",
        "url": "https://portly-vanadyl.com/",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://wretched-willow.net/",
                "weight": 1059.02,
            },
        ],
        "dns_resolve_period_sec": 6916.46,
        "load_balance_stats_period_sec": 3358.5,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8566.53,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8234.29,
        "pq_max_backpressure_sec": 1314.61,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
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