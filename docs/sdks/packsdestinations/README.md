# Packs.Destinations

## Overview

### Available Operations

* [list](#list) - List all Destinations within a Pack
* [create](#create) - Create a Destination within a Pack
* [get](#get) - Get a Destination within a Pack
* [update](#update) - Update a Destination within a Pack
* [delete](#delete) - Delete a Destination within a Pack

## list

Get a list of all Destinations within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputSystemByPack" method="get" path="/p/{pack}/system/outputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Destination within the specified Pack.

### Example Usage: OutputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "azure-blob-output",
        "type": models.CreateOutputSystemByPackTypeAzureBlob.AZURE_BLOB,
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
        "container_name": "my-container",
        "create_container": True,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "max_concurrent_file_parts": 1789.95,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 5235.4,
        "max_file_open_time_sec": 373.78,
        "max_file_idle_time_sec": 2011.77,
        "max_open_files": 9670.5,
        "header_line": "<value>",
        "write_high_water_mark": 3614.52,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "auth_type": models.AuthenticationMethodOptions.CLIENT_CERT,
        "storage_class": models.CreateOutputSystemByPackBlobAccessTier.HOT,
        "description": "concentration writhing defiantly shrill unfortunately recklessly when",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 1367.63,
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
        "empty_dir_cleanup_sec": 9688.12,
        "directory_batch_size": 5926.86,
        "deadletter_path": "<value>",
        "max_retry_num": 7443.01,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesAzureDataExplorer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "azure-data-explorer-output",
        "type": models.CreateOutputSystemByPackTypeAzureDataExplorer.AZURE_DATA_EXPLORER,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "validate_database_settings": True,
        "ingest_mode": models.CreateOutputSystemByPackIngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.CreateOutputSystemByPackAuthenticationMethodAzureDataExplorer.CLIENT_SECRET,
        "description": "allegation pleasure orient anti rout forecast absent hence unto",
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
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 8673.65,
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
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 2046.39,
        "directory_batch_size": 6195.79,
        "deadletter_enabled": False,
        "deadletter_path": "<value>",
        "max_retry_num": 49.27,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://talkative-edge.biz/",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "stage_path": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3693.13,
        "max_file_open_time_sec": 369.97,
        "max_file_idle_time_sec": 9166.41,
        "max_open_files": 6949.39,
        "max_concurrent_file_parts": 1551.41,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "add_id_to_stage_path": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "timeout_sec": 7481.82,
        "flush_immediately": False,
        "retain_blob_on_success": False,
        "extent_tags": [
            {
                "prefix": models.CreateOutputSystemByPackPrefixOptional.INGEST_BY,
                "value": "<value>",
            },
        ],
        "ingest_if_not_exists": [
            {
                "value": "<value>",
            },
        ],
        "report_level": models.CreateOutputSystemByPackReportLevel.FAILURES_AND_SUCCESSES,
        "report_method": models.CreateOutputSystemByPackReportMethod.QUEUE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "concurrency": 6050.98,
        "max_payload_size_kb": 9743.06,
        "max_payload_events": 4864.39,
        "flush_period_sec": 9238.64,
        "reject_unauthorized": False,
        "use_round_robin_dns": False,
        "keep_alive": True,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8217.74,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 2192.23,
        "pq_max_backpressure_sec": 342.7,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_cluster_url": "https://slow-airline.name",
        "template_database": "<value>",
        "template_table": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_client_secret": "<value>",
        "template_format": "<value>",
        "template_ingest_url": "https://imaginative-contractor.com/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureEventhub

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesAzureEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "azure-eventhub-output",
        "type": models.CreateOutputSystemByPackTypeAzureEventhub.AZURE_EVENTHUB,
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
        "ack": models.AcknowledgmentsOptions.LEADER,
        "format_": models.RecordDataFormatOptions.RAW,
        "max_record_size_kb": 8675.97,
        "flush_event_count": 8556.87,
        "flush_period_sec": 8039.59,
        "connection_timeout": 8255,
        "request_timeout": 2433.39,
        "max_retries": 5930.87,
        "max_back_off": 2311.35,
        "initial_backoff": 2640.47,
        "backoff_rate": 6022.68,
        "authentication_timeout": 8625.98,
        "reauthentication_threshold": 9613.74,
        "sasl": {
            "disabled": True,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "AuRj3AcLPI0x9Ju",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Annetta33",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.CERTIFICATE,
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
            "disabled": True,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "academics where queasily woot nervously weird oh after pecan",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6690.26,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 802.2,
        "pq_max_backpressure_sec": 8801.27,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureLogs

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesAzureLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "azure-logs-output",
        "type": models.CreateOutputSystemByPackTypeAzureLogs.AZURE_LOGS,
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
        "concurrency": 9102.79,
        "max_payload_size_kb": 4801.03,
        "max_payload_events": 8307.36,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 1571.25,
        "flush_period_sec": 5174.17,
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
        "api_url": "https://ample-pliers.net",
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.CreateOutputSystemByPackAuthenticationMethodAzureLogs.MANUAL,
        "description": "eek testing boo that",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8407,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2910.6,
        "pq_max_backpressure_sec": 4740.31,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "chronicle-output",
        "type": models.CreateOutputSystemByPackTypeChronicle.CHRONICLE,
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
        "api_version": "<value>",
        "authentication_method": models.CreateOutputSystemByPackAuthenticationMethodChronicle.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 6953.73,
        "max_payload_size_kb": 2955.01,
        "max_payload_events": 5676.03,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 4660,
        "flush_period_sec": 7930.45,
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
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 2639.28,
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
        "description": "testimonial conceal ah whose wetly except resource",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1950.82,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7546.11,
        "pq_max_backpressure_sec": 1188.64,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesClickHouse

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesClickHouse" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "clickhouse-output",
        "type": models.CreateOutputSystemByPackTypeClickHouse.CLICK_HOUSE,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:8123/",
        "auth_type": models.CreateOutputSystemByPackAuthenticationTypeClickHouse.SSL_USER_CERTIFICATE,
        "database": "mydb",
        "table_name": "mytable",
        "format_": models.CreateOutputSystemByPackFormatClickHouse.JSON_COMPACT_EACH_ROW_WITH_NAMES,
        "mapping_type": models.CreateOutputSystemByPackMappingType.CUSTOM,
        "async_inserts": True,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 3199.11,
        "max_payload_size_kb": 392.9,
        "max_payload_events": 5643.64,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 294.98,
        "flush_period_sec": 7689.72,
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
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "dump_format_errors_to_disk": True,
        "stats_destination": {
            "url": "https://supportive-veto.com/",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Earline4",
            "sql_username": "<value>",
            "password": "fn_ubMAFMtOwBpx",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "instead afterwards chunter exalted oh as",
        "username": "Bethel26",
        "password": "dN33b8ZkjXUCnHP",
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
        "pq_rate_per_sec": 1442.22,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 6319.08,
        "pq_max_backpressure_sec": 6685.88,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://early-finer.info/",
        "template_database": "<value>",
        "template_table_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudflareR2

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCloudflareR2" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cloudflare-r2-output",
        "type": models.CreateOutputSystemByPackTypeCloudflareR2.CLOUDFLARE_R2,
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
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.CreateOutputSystemByPackAuthenticationMethodCloudflareR2.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "verify_permissions": True,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 8892.26,
        "max_open_files": 525.29,
        "header_line": "<value>",
        "write_high_water_mark": 7938.95,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 1135.53,
        "max_file_idle_time_sec": 4195.99,
        "max_concurrent_file_parts": 3062.39,
        "description": "opera catalyze absentmindedly shudder lyre nor familiar what notwithstanding considering",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 3900.48,
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
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 2838.89,
        "directory_batch_size": 8968.38,
        "deadletter_path": "<value>",
        "max_retry_num": 5274.03,
        "template_bucket": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudwatch

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCloudwatch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cloudwatch-output",
        "type": models.CreateOutputSystemByPackTypeCloudwatch.CLOUDWATCH,
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7012.18,
        "max_queue_size": 3270.64,
        "max_record_size_kb": 3913.32,
        "flush_period_sec": 4120.36,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "qua ugly hypothesise direct er vivaciously",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 4860.51,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7884.96,
        "pq_max_backpressure_sec": 1997.19,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body=models.CreateOutputSystemByPackOutputConfluentCloud(
        id="confluent-cloud-output",
        type=models.CreateOutputSystemByPackTypeConfluentCloud.CONFLUENT_CLOUD,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
        ],
        environment="<value>",
        streamtags=[
            "<value 1>",
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
        ack=models.AcknowledgmentsOptions1.LEADER,
        format_=models.RecordDataFormatOptions1.RAW,
        compression=models.CompressionOptions3.ZSTD,
        max_record_size_kb=6366.62,
        flush_event_count=5374.13,
        flush_period_sec=5869.76,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://orderly-knitting.info/",
            connection_timeout=65.04,
            request_timeout=7620.77,
            max_retries=1627.05,
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
            default_key_schema_id=3110.3,
            default_value_schema_id=4216.12,
        ),
        connection_timeout=5394.03,
        request_timeout=2190.11,
        max_retries=1441.82,
        max_back_off=8482.93,
        initial_backoff=1824.83,
        backoff_rate=7880.22,
        authentication_timeout=5479.88,
        reauthentication_threshold=9839.91,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Jeromy34",
            password="mkbiANI3XTLISi6",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://definitive-kielbasa.com",
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
        description="possible configuration headline sparse outside forgo",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=1939.48,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=3342.59,
        pq_max_backpressure_sec=6520.74,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputSystemByPackPqControlsConfluentCloud(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cribl-http-output",
        "type": models.CreateOutputSystemByPackTypeCriblHTTP.CRIBL_HTTP,
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
        "token_ttl_minutes": 1134.2,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 1653.74,
        "max_payload_size_kb": 9494.28,
        "max_payload_events": 8070.97,
        "reject_unauthorized": False,
        "timeout_sec": 6216.85,
        "flush_period_sec": 5963.98,
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
        "throttle_rate_per_sec": "<value>",
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "as patiently incidentally favorite failing festival blah upwardly modulo embed",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "around status liquid",
        "url": "https://circular-disconnection.com",
        "use_round_robin_dns": True,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://serene-challenge.name/",
                "weight": 50.28,
                "template_url": "https://hefty-hawk.name",
            },
        ],
        "dns_resolve_period_sec": 5021.98,
        "load_balance_stats_period_sec": 4608.29,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 145.09,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7044.3,
        "pq_max_backpressure_sec": 4123.65,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://awesome-availability.info",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblLake

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cribl-lake-output",
        "type": models.CreateOutputSystemByPackTypeCriblLake.CRIBL_LAKE,
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
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 5759.58,
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.BUCKET_OWNER_READ,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3018.8,
        "max_open_files": 3645.7,
        "header_line": "<value>",
        "write_high_water_mark": 8651.05,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 9215.57,
        "max_file_idle_time_sec": 8392.15,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 5089.57,
        "aws_authentication_method": models.AwsAuthenticationMethodOptions.AUTO_RPC,
        "format_": models.FormatOptions.JSON,
        "max_concurrent_file_parts": 9776.75,
        "description": "immediately sham given quirkily since lean",
        "empty_dir_cleanup_sec": 6637.62,
        "directory_batch_size": 7553.43,
        "deadletter_path": "<value>",
        "max_retry_num": 3491.79,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCriblSearchEngine" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cribl-search-engine-output",
        "type": models.CreateOutputSystemByPackTypeCriblSearchEngine.CRIBL_SEARCH_ENGINE,
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
            "initial_backoff": 5510.34,
            "backoff_rate": 6720.13,
            "max_backoff": 214.03,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "as patiently incidentally favorite failing festival blah upwardly modulo embed",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "lest lest oof",
        "url": "https://0.0.0.0:10200",
        "exclude_self": True,
        "urls": [
            {
                "url": "https://serene-challenge.name/",
                "weight": 50.28,
                "template_url": "https://hefty-hawk.name",
            },
        ],
        "dns_resolve_period_sec": 9867.26,
        "load_balance_stats_period_sec": 562.01,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 918.86,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 1938.18,
        "pq_max_backpressure_sec": 7222.85,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://bossy-vestment.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "cribl-tcp-output",
        "type": models.CreateOutputSystemByPackTypeCriblTCP.CRIBL_TCP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
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
        "connection_timeout": 9223.46,
        "write_timeout": 3115.03,
        "token_ttl_minutes": 5115.16,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "tuba while yuck ah boastfully",
            },
        ],
        "exclude_fields": [
            "<value 1>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "ashamed voluminous mmm",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "adolescent-cemetery.org",
                "port": 5699.66,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 7378.74,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 3954.84,
        "load_balance_stats_period_sec": 1051.16,
        "max_concurrent_senders": 7291.71,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 569.47,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 6128.38,
        "pq_max_backpressure_sec": 5664.51,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCrowdstrikeNextGenSiem

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesCrowdstrikeNextGenSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "crowdstrike-next-gen-siem-output",
        "type": models.CreateOutputSystemByPackTypeCrowdstrikeNextGenSiem.CROWDSTRIKE_NEXT_GEN_SIEM,
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
        "concurrency": 6085.06,
        "max_payload_size_kb": 7765.33,
        "max_payload_events": 596.15,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 2515.16,
        "flush_period_sec": 1760.23,
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
        ],
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "apropos instead masquerade gray numeric polarisation",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8044.56,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2332.3,
        "pq_max_backpressure_sec": 2926.21,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://impressive-vista.com",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatabricks

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDatabricks" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "databricks-output",
        "type": models.CreateOutputSystemByPackTypeDatabricks.DATABRICKS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "dest_path": "<value>",
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2478.02,
        "max_file_open_time_sec": 7056.55,
        "max_file_idle_time_sec": 7694.51,
        "max_open_files": 6708.36,
        "header_line": "<value>",
        "write_high_water_mark": 3215.06,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 7590.35,
        "description": "where pish what astride underpants upright veg solemnly",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 673.74,
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
        "empty_dir_cleanup_sec": 7208.74,
        "directory_batch_size": 1011.97,
        "deadletter_path": "<value>",
        "max_retry_num": 3748.53,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatadog

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDatadog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "datadog-output",
        "type": models.CreateOutputSystemByPackTypeDatadog.DATADOG,
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
        "content_type": models.CreateOutputSystemByPackSendLogsAs.JSON,
        "message": "<value>",
        "source": "<value>",
        "host": "primary-casement.name",
        "service": "<value>",
        "tags": [
            "<value 1>",
            "<value 2>",
        ],
        "batch_by_tags": False,
        "allow_api_key_from_events": False,
        "severity": models.CreateOutputSystemByPackSeverityDatadog.ERROR,
        "site": models.CreateOutputSystemByPackDatadogSite.CUSTOM,
        "send_counters_as_count": False,
        "concurrency": 4996.19,
        "max_payload_size_kb": 783.8,
        "max_payload_events": 3498.58,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 6306.6,
        "flush_period_sec": 3548.4,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "total_memory_limit_kb": 2050.93,
        "description": "well-worn sternly silk",
        "custom_url": "https://tall-mouser.net",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8870.68,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3588.47,
        "pq_max_backpressure_sec": 2596.94,
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
### Example Usage: OutputCreateExamplesDataset

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "dataset-output",
        "type": models.CreateOutputSystemByPackTypeDataset.DATASET,
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
        "message_field": "<value>",
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "server_host_field": "<value>",
        "timestamp_field": "<value>",
        "default_severity": models.CreateOutputSystemByPackSeverityDataset.FINEST,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "site": models.CreateOutputSystemByPackDataSetSite.EU,
        "concurrency": 975.15,
        "max_payload_size_kb": 7090.23,
        "max_payload_events": 6642.59,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 6897.1,
        "flush_period_sec": 7457.7,
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
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "total_memory_limit_kb": 7282.67,
        "description": "of pfft gladly",
        "custom_url": "https://harmful-intellect.info/",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 3554,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 6448.6,
        "pq_max_backpressure_sec": 3676.42,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
        "template_custom_url": "https://acceptable-compromise.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDiskSpool

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDiskSpool" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "disk-spool-output",
        "type": models.CreateOutputSystemByPackTypeDiskSpool.DISK_SPOOL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "time_window": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.CompressionOptionsPersistence.NONE,
        "partition_expr": "<value>",
        "description": "sorrowful excepting tattered",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDlS3

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDlS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "dl-s3-output",
        "type": models.CreateOutputSystemByPackTypeDlS3.DL_S3,
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2701.53,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.AUTHENTICATED_READ,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2614.56,
        "max_open_files": 8785.34,
        "header_line": "<value>",
        "write_high_water_mark": 5785.31,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 8096.65,
        "max_file_idle_time_sec": 3785.78,
        "max_concurrent_file_parts": 4826.39,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 913.63,
        "partitioning_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "description": "beside furthermore merry rightfully boldly gadzooks lumpy inborn",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 6089.28,
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
        "empty_dir_cleanup_sec": 6278.92,
        "directory_batch_size": 6525.85,
        "deadletter_path": "<value>",
        "max_retry_num": 9619.17,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDynatraceHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "dynatrace-http-output",
        "type": models.CreateOutputSystemByPackTypeDynatraceHTTP.DYNATRACE_HTTP,
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
        "method": models.MethodOptions.PUT,
        "keep_alive": True,
        "concurrency": 630.09,
        "max_payload_size_kb": 6057.03,
        "max_payload_events": 5392.66,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 6660.13,
        "flush_period_sec": 8150.62,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.CreateOutputSystemByPackAuthenticationTypeDynatraceHTTP.TOKEN,
        "format_": models.CreateOutputSystemByPackFormatDynatraceHTTP.JSON_ARRAY,
        "endpoint": models.CreateOutputSystemByPackEndpoint.CLOUD,
        "telemetry_type": models.CreateOutputSystemByPackTelemetryType.LOGS,
        "total_memory_limit_kb": 6491.32,
        "description": "aw beyond than so",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2384.36,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 6495.59,
        "pq_max_backpressure_sec": 8006.32,
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
        "url": "https://frail-doorpost.biz/",
        "template_url": "https://altruistic-inspection.com",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceOtlp

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesDynatraceOtlp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "dynatrace-otlp-output",
        "type": models.CreateOutputSystemByPackTypeDynatraceOtlp.DYNATRACE_OTLP,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.CreateOutputSystemByPackProtocolDynatraceOtlp.HTTP,
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
        "concurrency": 5411.14,
        "max_payload_size_kb": 678.56,
        "timeout_sec": 3256.42,
        "flush_period_sec": 2512.28,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 8923.37,
        "keep_alive_time": 612.86,
        "keep_alive": False,
        "endpoint_type": models.CreateOutputSystemByPackEndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "petticoat toward ack weight breakable until",
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
        ],
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8121.78,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5538.56,
        "pq_max_backpressure_sec": 6321.23,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "elastic-output",
        "type": models.CreateOutputSystemByPackTypeElastic.ELASTIC,
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
        "index": "logs",
        "doc_type": "<value>",
        "concurrency": 1502.29,
        "max_payload_size_kb": 3134.83,
        "max_payload_events": 137.38,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 4867.48,
        "flush_period_sec": 5125.77,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Lou_Pfeffer24",
            "password": "tuLWEvVJ7xoDNhs",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.CreateOutputSystemByPackElasticVersion.SIX,
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "write_action": models.CreateOutputSystemByPackWriteAction.INDEX,
        "retry_partial_errors": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "hm irritably traditionalism amazing",
        "url": "https://intelligent-management.org",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://legal-traditionalism.biz/",
                "weight": 4899.28,
                "template_url": "https://hard-to-find-kinase.info",
            },
        ],
        "dns_resolve_period_sec": 3663.2,
        "load_balance_stats_period_sec": 6869.14,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9533.05,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 5259.8,
        "pq_max_backpressure_sec": 7333.84,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://orange-legging.info",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElasticCloud

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesElasticCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "elastic-cloud-output",
        "type": models.CreateOutputSystemByPackTypeElasticCloud.ELASTIC_CLOUD,
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
        "concurrency": 1121.92,
        "max_payload_size_kb": 9781.82,
        "max_payload_events": 791.89,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 8807.42,
        "flush_period_sec": 326.05,
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
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": True,
            "username": "Lou_Pfeffer24",
            "password": "tuLWEvVJ7xoDNhs",
            "auth_type": models.AuthenticationMethodOptionsAuth.MANUAL,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": False,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "sans rationalize object sniveling towards persecute jubilantly kindly",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8354.98,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7384.07,
        "pq_max_backpressure_sec": 3294.09,
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
### Example Usage: OutputCreateExamplesExabeam

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesExabeam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "exabeam-output",
        "type": models.CreateOutputSystemByPackTypeExabeam.EXABEAM,
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
        "signature_version": models.SignatureVersionOptions4.V2,
        "object_acl": models.ObjectACLOptions1.PROJECT_PRIVATE,
        "storage_class": models.StorageClassOptions1.ARCHIVE,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": False,
        "max_file_open_time_sec": 9154.74,
        "max_file_idle_time_sec": 2771.71,
        "max_open_files": 7467.87,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_size_mb": 5791.63,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "likewise home ick",
        "empty_dir_cleanup_sec": 1922.62,
        "directory_batch_size": 8157.19,
        "deadletter_path": "<value>",
        "max_retry_num": 5052.55,
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesFilesystem

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "filesystem-output",
        "type": models.CreateOutputSystemByPackTypeFilesystem.FILESYSTEM,
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
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2839.52,
        "max_file_open_time_sec": 9635.12,
        "max_file_idle_time_sec": 3867.38,
        "max_open_files": 7228.29,
        "header_line": "<value>",
        "write_high_water_mark": 3951.73,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "description": "huddle solemnly divert information",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 9998.38,
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
        "empty_dir_cleanup_sec": 1168.77,
        "directory_batch_size": 7818.69,
        "deadletter_path": "<value>",
        "max_retry_num": 9073.02,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleChronicle

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGoogleChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "google-chronicle-output",
        "type": models.CreateOutputSystemByPackTypeGoogleChronicle.GOOGLE_CHRONICLE,
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
        "api_version": models.CreateOutputSystemByPackAPIVersion.V2,
        "authentication_method": models.CreateOutputSystemByPackAuthenticationMethodGoogleChronicle.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "log_format_type": models.CreateOutputSystemByPackSendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 6836.19,
        "max_payload_size_kb": 4752.71,
        "max_payload_events": 3157.86,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 4825.55,
        "flush_period_sec": 3633.7,
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
        "use_round_robin_dns": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 8409.11,
        "description": "juggernaut instead sympathetically",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "surface respectful when popularize",
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
        "udm_type": models.CreateOutputSystemByPackUDMType.ENTITIES,
        "api_key": "<value>",
        "api_key_secret": "<value>",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3416.4,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 635.3,
        "pq_max_backpressure_sec": 8140.42,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGoogleCloudLogging" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "google-cloud-logging-output",
        "type": models.CreateOutputSystemByPackTypeGoogleCloudLogging.GOOGLE_CLOUD_LOGGING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "log_location_type": models.CreateOutputSystemByPackLogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "sanitize_log_names": True,
        "payload_format": models.CreateOutputSystemByPackPayloadFormat.JSON,
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
        "max_payload_size_kb": 1744.96,
        "max_payload_events": 3426.33,
        "flush_period_sec": 5934.82,
        "concurrency": 2939.76,
        "connection_timeout": 7127.91,
        "timeout_sec": 1175.45,
        "throttle_rate_req_per_sec": 625818,
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
        "total_memory_limit_kb": 2579.72,
        "description": "ack instead at whether aw frizzy inasmuch husk motionless",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9650.84,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 3600.26,
        "pq_max_backpressure_sec": 8654.63,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "google-cloud-storage-output",
        "type": models.CreateOutputSystemByPackTypeGoogleCloudStorage.GOOGLE_CLOUD_STORAGE,
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
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.CreateOutputSystemByPackAuthenticationMethodGoogleCloudStorage.MANUAL,
        "stage_path": "/tmp/staging",
        "dest_path": "<value>",
        "verify_permissions": True,
        "object_acl": models.ObjectACLOptions1.BUCKET_OWNER_READ,
        "storage_class": models.StorageClassOptions1.NEARLINE,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 1542.83,
        "max_file_open_time_sec": 83.66,
        "max_file_idle_time_sec": 2030.04,
        "max_open_files": 4148.44,
        "header_line": "<value>",
        "write_high_water_mark": 5005.38,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "description": "chase untrue maintainer searchingly athwart bootleg",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 5409.47,
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
        "empty_dir_cleanup_sec": 5064.36,
        "directory_batch_size": 7802.24,
        "deadletter_path": "<value>",
        "max_retry_num": 8400.2,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "google-pubsub-output",
        "type": models.CreateOutputSystemByPackTypeGooglePubsub.GOOGLE_PUBSUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "topic_name": "my-topic",
        "create_topic": True,
        "ordered_delivery": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.AUTO,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 5376.75,
        "batch_timeout": 8928.52,
        "max_queue_size": 2707.47,
        "max_record_size_kb": 1466.77,
        "flush_period": 9515.96,
        "max_in_progress": 3285.97,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "scarcely bathhouse notwithstanding unless gadzooks across wound in-joke infinite",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9743.6,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4533.61,
        "pq_max_backpressure_sec": 230.29,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_topic_name": "<value>",
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGrafanaCloud

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGrafanaCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body=models.CreateOutputSystemByPackOutputGrafanaCloudGrafanaCloud1(
        id="grafana-cloud-output",
        type=models.CreateOutputSystemByPackOutputGrafanaCloudType1.GRAFANA_CLOUD,
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
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://steep-amendment.name",
        message="<value>",
        message_format=models.MessageFormatOptions.JSON,
        labels=[
            models.ItemsTypeLabels(
                name="<value>",
                value="<value>",
            ),
        ],
        metric_rename_expr="<value>",
        prometheus_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.CREDENTIALS_SECRET,
            token="<value>",
            text_secret="<value>",
            username="Jamey_Pagac",
            password="FunP8vUHMJ7SCJw",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.CREDENTIALS_SECRET,
            token="<value>",
            text_secret="<value>",
            username="Ford_Funk55",
            password="Qsq6QXVCZ8Kn7zO",
            credentials_secret="<value>",
        ),
        concurrency=957.76,
        max_payload_size_kb=7013.67,
        max_payload_events=1661.58,
        reject_unauthorized=False,
        timeout_sec=6284.86,
        flush_period_sec=8783.91,
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
            "<value 2>",
            "<value 3>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=8177.04,
                initial_backoff=7866.98,
                backoff_rate=6178.16,
                max_backoff=3348.05,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=True,
            initial_backoff=9325.54,
            backoff_rate=3205.55,
            max_backoff=1352.21,
        ),
        response_honor_retry_after_header=True,
        on_backpressure=models.BackpressureBehaviorOptions.QUEUE,
        description="glisten but apropos label solder meanwhile",
        compress=True,
        pq_strict_ordering=False,
        pq_rate_per_sec=2106.95,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=3413.11,
        pq_max_backpressure_sec=7713.97,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.CreateOutputSystemByPackOutputGrafanaCloudPqControls1(),
        template_loki_url="https://excellent-grass.name",
        template_prometheus_url="https://nocturnal-programme.com",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGraphite

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesGraphite" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "graphite-output",
        "type": models.CreateOutputSystemByPackTypeGraphite.GRAPHITE,
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
        "mtu": 7866.83,
        "flush_period_sec": 1426.35,
        "dns_resolve_period_sec": 8899.18,
        "description": "incidentally inwardly boohoo absent license fibre yet aha",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 6999.86,
        "write_timeout": 6874.71,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 468.36,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8559.24,
        "pq_max_backpressure_sec": 238.67,
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
### Example Usage: OutputCreateExamplesHoneycomb

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesHoneycomb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "honeycomb-output",
        "type": models.CreateOutputSystemByPackTypeHoneycomb.HONEYCOMB,
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
        "concurrency": 3521.46,
        "max_payload_size_kb": 2922.05,
        "max_payload_events": 160.1,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 4128.27,
        "flush_period_sec": 1304.16,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "description": "clonk consequently newsletter that excepting although unlearn",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7952.29,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 2340.96,
        "pq_max_backpressure_sec": 8250.64,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesHumioHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "humio-hec-output",
        "type": models.CreateOutputSystemByPackTypeHumioHec.HUMIO_HEC,
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
        "concurrency": 4843.25,
        "max_payload_size_kb": 5786.95,
        "max_payload_events": 1997.07,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 7504.67,
        "flush_period_sec": 9338.27,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "gum inasmuch promptly legislature deer caring near operating",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8938.16,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 1435,
        "pq_max_backpressure_sec": 5502.93,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://worst-forager.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesInfluxdb

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesInfluxdb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "influxdb-output",
        "type": models.CreateOutputSystemByPackTypeInfluxdb.INFLUXDB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "url": "http://localhost:8086",
        "use_v2_api": True,
        "timestamp_precision": models.CreateOutputSystemByPackTimestampPrecision.S,
        "dynamic_value_field_name": False,
        "value_field_name": "<value>",
        "concurrency": 4865.38,
        "max_payload_size_kb": 7713.92,
        "max_payload_events": 1654.04,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 9548.5,
        "flush_period_sec": 9122.06,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputSystemByPackAuthenticationTypeInfluxdb.TOKEN,
        "description": "even after reporter",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 644.64,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4345.91,
        "pq_max_backpressure_sec": 8044.48,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Graham_Cummerata",
        "password": "QoazYQzuIXrYLgy",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://astonishing-disconnection.name",
        "template_database": "<value>",
        "template_bucket": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body=models.CreateOutputSystemByPackOutputKafka(
        id="kafka-output",
        type=models.CreateOutputSystemByPackTypeKafka.KAFKA,
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
        format_=models.RecordDataFormatOptions1.RAW,
        compression=models.CompressionOptions3.ZSTD,
        max_record_size_kb=7314.96,
        flush_event_count=2019.51,
        flush_period_sec=3377.23,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://orderly-knitting.info/",
            connection_timeout=65.04,
            request_timeout=7620.77,
            max_retries=1627.05,
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
            default_key_schema_id=3110.3,
            default_value_schema_id=4216.12,
        ),
        connection_timeout=7181.04,
        request_timeout=3724.78,
        max_retries=4755.27,
        max_back_off=7144.48,
        initial_backoff=6810.09,
        backoff_rate=4556.71,
        authentication_timeout=6671.44,
        reauthentication_threshold=5906.1,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Jeromy34",
            password="mkbiANI3XTLISi6",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://definitive-kielbasa.com",
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
        description="than never yum shoddy finger",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=False,
        pq_rate_per_sec=5957.13,
        pq_mode=models.ModeOptions.ALWAYS,
        pq_max_buffer_size=3159,
        pq_max_backpressure_sec=1778.58,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.CreateOutputSystemByPackPqControlsKafka(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "kinesis-output",
        "type": models.CreateOutputSystemByPackTypeKinesis.KINESIS,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
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
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2206.96,
        "concurrency": 578.15,
        "max_record_size_kb": 1353.1,
        "flush_period_sec": 7828.01,
        "compression": models.CreateOutputSystemByPackCompression.GZIP,
        "use_list_shards": True,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "never quizzically ecliptic",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 7848.06,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6095.42,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8419.65,
        "pq_max_backpressure_sec": 4700.16,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "loki-output",
        "type": models.CreateOutputSystemByPackTypeLoki.LOKI,
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
        "url": "http://localhost:3100/loki/api/v1/push",
        "message": "<value>",
        "message_format": models.MessageFormatOptions.PROTOBUF,
        "labels": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.TOKEN,
        "concurrency": 200.1,
        "max_payload_size_kb": 1452.29,
        "max_payload_events": 8898.77,
        "reject_unauthorized": False,
        "timeout_sec": 917.42,
        "flush_period_sec": 4481.48,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "enable_dynamic_headers": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 5475.99,
        "description": "pfft chapel swat save phew aside dress",
        "compress": False,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Aliza.Schiller7",
        "password": "llUzXbfL955jZKg",
        "credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1961.13,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 726.31,
        "pq_max_backpressure_sec": 6710.87,
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
### Example Usage: OutputCreateExamplesMicrosoftFabric

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesMicrosoftFabric" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "microsoft-fabric-output",
        "type": models.CreateOutputSystemByPackTypeMicrosoftFabric.MICROSOFT_FABRIC,
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
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.ALL,
        "format_": models.RecordDataFormatOptions.RAW,
        "max_record_size_kb": 4124.7,
        "flush_event_count": 5573.22,
        "flush_period_sec": 1504.21,
        "connection_timeout": 4318.81,
        "request_timeout": 2670.54,
        "max_retries": 7669.88,
        "max_back_off": 3448.63,
        "initial_backoff": 2514.2,
        "backoff_rate": 9653.92,
        "authentication_timeout": 5832.31,
        "reauthentication_threshold": 8601.04,
        "sasl": {
            "disabled": True,
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Arthur_Pfeffer",
            "text_secret": "<value>",
            "client_secret_auth_type": models.CreateOutputSystemByPackAuthenticationMethodMicrosoftFabric.SECRET,
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
            "disabled": True,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "violent incomparable yahoo pendant diligently square innocently",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 154.96,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9316.56,
        "pq_max_backpressure_sec": 7819.76,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
        "template_bootstrap_server": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMinio

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesMinio" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "minio-output",
        "type": models.CreateOutputSystemByPackTypeMinio.MINIO,
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
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V2,
        "object_acl": models.ObjectACLOptions.PUBLIC_READ,
        "storage_class": models.StorageClassOptions2.REDUCED_REDUNDANCY,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "verify_permissions": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 2618.15,
        "max_open_files": 6371.52,
        "header_line": "<value>",
        "write_high_water_mark": 193.27,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 2803.98,
        "max_file_idle_time_sec": 3019.56,
        "max_concurrent_file_parts": 519.06,
        "description": "flat phew abaft junior hunt eyebrow disposer robust",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 587.46,
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
        "empty_dir_cleanup_sec": 5832.98,
        "directory_batch_size": 6279.33,
        "deadletter_path": "<value>",
        "max_retry_num": 1198.46,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body=models.CreateOutputSystemByPackOutputMsk(
        id="msk-output",
        type=models.CreateOutputSystemByPackTypeMsk.MSK,
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
        ack=models.AcknowledgmentsOptions1.NONE,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.LZ4,
        max_record_size_kb=6028.8,
        flush_event_count=5526.35,
        flush_period_sec=3412.48,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=False,
            schema_registry_url="https://orderly-knitting.info/",
            connection_timeout=65.04,
            request_timeout=7620.77,
            max_retries=1627.05,
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
            default_key_schema_id=3110.3,
            default_value_schema_id=4216.12,
        ),
        connection_timeout=593.31,
        request_timeout=175.51,
        max_retries=4501.98,
        max_back_off=9120.57,
        initial_backoff=1617.95,
        backoff_rate=651.48,
        authentication_timeout=1474.54,
        reauthentication_threshold=3357.1,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V2,
        reuse_connections=True,
        reject_unauthorized=False,
        enable_assume_role=True,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=699.67,
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
        description="slake about intend innocently resource",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=4002.99,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=9919.57,
        pq_max_backpressure_sec=5946.41,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.CreateOutputSystemByPackPqControlsMsk(),
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "netflow-output",
        "type": models.CreateOutputSystemByPackTypeNetflow.NETFLOW,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
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
        "dns_resolve_period_sec": 5309.41,
        "enable_ip_spoofing": False,
        "description": "making sneak store lyre rough like",
        "max_record_size": 9396.95,
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelic

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesNewrelic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "newrelic-output",
        "type": models.CreateOutputSystemByPackTypeNewrelic.NEWRELIC,
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
        "region": models.RegionOptions.CUSTOM,
        "log_type": "<value>",
        "message_field": "<value>",
        "metadata": [
            {
                "name": models.CreateOutputSystemByPackFieldName.HOSTNAME,
                "value": "<value>",
            },
        ],
        "concurrency": 4757.96,
        "max_payload_size_kb": 6250.48,
        "max_payload_events": 4654.17,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 3745.63,
        "flush_period_sec": 3355.24,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 4813.25,
        "description": "notwithstanding by interchange reservation that downright so cruelly",
        "custom_url": "https://fluffy-bump.biz/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6694.11,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2562.6,
        "pq_max_backpressure_sec": 1412.75,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesNewrelicEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "newrelic-events-output",
        "type": models.CreateOutputSystemByPackTypeNewrelicEvents.NEWRELIC_EVENTS,
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
        "region": models.RegionOptions.US,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 83.93,
        "max_payload_size_kb": 4622.8,
        "max_payload_events": 6007.1,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 9181.26,
        "flush_period_sec": 8180.04,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.SECRET,
        "description": "yowza ick claw fussy singe swing dirty",
        "custom_url": "https://concrete-possession.org",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 4362.97,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 955.1,
        "pq_max_backpressure_sec": 2757.81,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_account_id": "<id>",
        "template_event_type": "<value>",
        "template_custom_url": "https://leading-palate.name",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "opentelemetry-output",
        "type": models.CreateOutputSystemByPackTypeOpenTelemetry.OPEN_TELEMETRY,
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
        "otlp_version": models.CreateOutputSystemByPackOTLPVersion.ONE_DOT_3_DOT_1,
        "compress": models.CompressionOptions4.DEFLATE,
        "http_compress": models.CompressionOptions5.NONE,
        "auth_type": models.AuthenticationTypeOptions.TEXT_SECRET,
        "http_traces_endpoint_override": "<value>",
        "http_metrics_endpoint_override": "<value>",
        "http_logs_endpoint_override": "<value>",
        "metadata": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "concurrency": 5277.69,
        "max_payload_size_kb": 8479.36,
        "timeout_sec": 1500.56,
        "flush_period_sec": 7118.59,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "connection_timeout": 236.26,
        "keep_alive_time": 1152.01,
        "keep_alive": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "lightly merit consequently impossible",
        "username": "Annamae_Ondricka",
        "password": "F_ZED65h2bmasxD",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1156.32,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5935.54,
        "pq_max_backpressure_sec": 5842.73,
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
### Example Usage: OutputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "prometheus-output",
        "type": models.CreateOutputSystemByPackTypePrometheus.PROMETHEUS,
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
        "url": "http://localhost:9091/api/v1/write",
        "metric_rename_expr": "<value>",
        "send_metadata": False,
        "concurrency": 8539.58,
        "max_payload_size_kb": 5457.42,
        "max_payload_events": 6165.24,
        "reject_unauthorized": False,
        "timeout_sec": 131.09,
        "flush_period_sec": 7914.63,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "description": "official free brr pish wherever drat awkwardly yet",
        "metrics_flush_period_sec": 1546.38,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 3024.12,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4777.5,
        "pq_max_backpressure_sec": 1256.83,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Dina_Dooley",
        "password": "jWIvX2o_9GpWhf7",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://athletic-zen.com",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRing

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesRing" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "ring-output",
        "type": models.CreateOutputSystemByPackTypeRing.RING,
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
        "format_": models.CreateOutputSystemByPackDataFormatRing.JSON,
        "partition_expr": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "description": "interesting well-documented casket pfft cassava joyously",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRouter

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesRouter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "router-output",
        "type": models.CreateOutputSystemByPackTypeRouter.ROUTER,
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
                "description": "testify morning secret and rigidly diligently emulsify",
                "final": False,
            },
        ],
        "description": "platter yum across",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "s3-output",
        "type": models.CreateOutputSystemByPackTypeS3.S3,
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
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1137.22,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions.INTELLIGENT_TIERING,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 4861.56,
        "max_open_files": 979.15,
        "header_line": "<value>",
        "write_high_water_mark": 5009.3,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 7299.34,
        "max_file_idle_time_sec": 7678.19,
        "max_concurrent_file_parts": 4461.04,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 5681.16,
        "description": "acquire unless phooey furthermore blah pish of limply via even",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 5602.83,
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
        "enable_page_checksum": True,
        "empty_dir_cleanup_sec": 4474.24,
        "directory_batch_size": 8131.76,
        "deadletter_path": "<value>",
        "max_retry_num": 4149.04,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "security-lake-output",
        "type": models.CreateOutputSystemByPackTypeSecurityLake.SECURITY_LAKE,
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
        "signature_version": models.CreateOutputSystemByPackSignatureVersionSecurityLake.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7869.73,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "object_acl": models.ObjectACLOptions.AUTHENTICATED_READ,
        "storage_class": models.StorageClassOptions.STANDARD_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "base_file_name": "<value>",
        "max_file_size_mb": 4079.53,
        "max_open_files": 2520.16,
        "header_line": "<value>",
        "write_high_water_mark": 7042.03,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 27.11,
            "backoff_multiplier": 4258.54,
            "max_backoff_ms": 1146.47,
            "jitter_percent": 1403.61,
        },
        "max_file_open_time_sec": 161.23,
        "max_file_idle_time_sec": 9675.63,
        "max_concurrent_file_parts": 1500.74,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 2660.43,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": True,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 608.83,
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
        "description": "unlike brisk license",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 6857.05,
        "directory_batch_size": 1431.06,
        "parquet_schema": "<value>",
        "deadletter_path": "<value>",
        "max_retry_num": 8351.21,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSentinel" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "sentinel-output",
        "type": models.CreateOutputSystemByPackTypeSentinel.SENTINEL,
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
        "concurrency": 1449.12,
        "max_payload_size_kb": 4077.75,
        "max_payload_events": 4029.17,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 2469.04,
        "flush_period_sec": 8583.42,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.CreateOutputSystemByPackAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "<value>",
        "endpoint_url_configuration": models.CreateOutputSystemByPackEndpointConfiguration.URL,
        "total_memory_limit_kb": 9753.03,
        "description": "holster oh ha next forecast sheepishly",
        "format_": models.CreateOutputSystemByPackFormatSentinel.CUSTOM,
        "custom_source_expression": "<value>",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6973.94,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 9191.66,
        "pq_max_backpressure_sec": 6570.19,
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
        "template_login_url": "https://grave-amendment.org",
        "template_secret": "<value>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_url": "https://talkative-legislature.info/",
        "template_dcr_id": "<id>",
        "template_dce_endpoint": "<value>",
        "template_stream_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinelOneAiSiem

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSentinelOneAiSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "sentinel-one-ai-siem-output",
        "type": models.CreateOutputSystemByPackTypeSentinelOneAiSiem.SENTINEL_ONE_AI_SIEM,
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
        "region": models.CreateOutputSystemByPackRegion.US,
        "endpoint": models.CreateOutputSystemByPackAISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
        "concurrency": 246.07,
        "max_payload_size_kb": 8345.77,
        "max_payload_events": 6926.81,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 8657.49,
        "flush_period_sec": 9009.46,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "decent gosh hotfoot focalise jet",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://golden-guidance.biz/",
        "host_expression": "<value>",
        "source_expression": "<value>",
        "source_type_expression": "<value>",
        "data_source_category_expression": "<value>",
        "data_source_name_expression": "<value>",
        "data_source_vendor_expression": "<value>",
        "event_type_expression": "<value>",
        "host": "humble-scrap.net",
        "source": "<value>",
        "source_type": "<value>",
        "data_source_category": "<value>",
        "data_source_name": "<value>",
        "data_source_vendor": "<value>",
        "event_type": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 4392.85,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2026.56,
        "pq_max_backpressure_sec": 6084.94,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesServiceNow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "servicenow-output",
        "type": models.CreateOutputSystemByPackTypeServiceNow.SERVICE_NOW,
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
        "auth_token_name": "<value>",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 503.77,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.GZIP,
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
        "concurrency": 2154.24,
        "timeout_sec": 4368.66,
        "flush_period_sec": 1760.74,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD_AND_HEADERS,
        "connection_timeout": 4443.02,
        "keep_alive_time": 5437.31,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "woefully ick marathon mostly oof amid if inwardly commemorate",
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9783.22,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 3299.29,
        "pq_max_backpressure_sec": 8193.24,
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
### Example Usage: OutputCreateExamplesSignalfx

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSignalfx" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "signalfx-output",
        "type": models.CreateOutputSystemByPackTypeSignalfx.SIGNALFX,
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "realm": "us0",
        "concurrency": 6645.7,
        "max_payload_size_kb": 9487.59,
        "max_payload_events": 7248.16,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 9800.19,
        "flush_period_sec": 3414.66,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "inwardly milestone reopen meanwhile leading radiant hole mature drive cheerfully",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8643.23,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 1709.64,
        "pq_max_backpressure_sec": 5809.61,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "snmp-output",
        "type": models.CreateOutputSystemByPackTypeSnmp.SNMP,
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
        "dns_resolve_period_sec": 4878.98,
        "description": "exactly representation officially yuck easily absent jacket",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSns

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSns" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "sns-output",
        "type": models.CreateOutputSystemByPackTypeSns.SNS,
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
        "max_retries": 9220.51,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.CreateOutputSystemByPackSignatureVersionSns.V4,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6435.8,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "supposing oh hastily give fortunately hammock",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2030.75,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4614.55,
        "pq_max_backpressure_sec": 874.72,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "splunk-output",
        "type": models.CreateOutputSystemByPackTypeSplunk.SPLUNK,
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
        "nested_fields": models.NestedFieldSerializationOptions.JSON,
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 5454.45,
        "write_timeout": 2267.18,
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
        "enable_multi_metrics": True,
        "enable_ack": True,
        "log_failed_requests": False,
        "max_s2_sversion": models.MaxS2SVersionOptions.V3,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "certification yum likely throughout seriously stupendous jellyfish certification lazily better",
        "max_failed_health_checks": 8593.9,
        "compress": models.CompressionOptions.AUTO,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5137.13,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3578.55,
        "pq_max_backpressure_sec": 626.61,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "splunk-hec-output",
        "type": models.CreateOutputSystemByPackTypeSplunkHec.SPLUNK_HEC,
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 3689.15,
        "max_payload_size_kb": 6879.41,
        "max_payload_events": 4653.04,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 8311.1,
        "flush_period_sec": 6170.31,
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
        "enable_multi_metrics": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "querulous painfully what beside while unlucky gee overstay",
        "url": "https://orderly-cruelty.net/",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://illustrious-permafrost.net",
                "weight": 6169.06,
                "template_url": "https://careless-casement.com",
            },
        ],
        "dns_resolve_period_sec": 7364.12,
        "load_balance_stats_period_sec": 4627.82,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 1872.69,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9087.95,
        "pq_max_backpressure_sec": 5363.05,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://breakable-championship.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkLb

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSplunkLb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body=models.CreateOutputSystemByPackOutputSplunkLb(
        id="splunk-lb-output",
        type=models.CreateOutputSystemByPackTypeSplunkLb.SPLUNK_LB,
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
        dns_resolve_period_sec=7056.71,
        load_balance_stats_period_sec=7257.28,
        max_concurrent_senders=8308.87,
        nested_fields=models.NestedFieldSerializationOptions.JSON,
        throttle_rate_per_sec="<value>",
        connection_timeout=4504.9,
        write_timeout=3216.79,
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
        enable_multi_metrics=False,
        enable_ack=False,
        log_failed_requests=True,
        max_s2_sversion=models.MaxS2SVersionOptions.V3,
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        indexer_discovery=False,
        sender_unhealthy_time_allowance=9874.35,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        description="impractical powerfully pulverize round zowie",
        max_failed_health_checks=7299.56,
        compress=models.CompressionOptions.DISABLED,
        indexer_discovery_configs=models.CreateOutputSystemByPackIndexerDiscoveryConfigs(
            site="<value>",
            master_uri="https://mild-bonfire.biz",
            refresh_interval_sec=481.47,
            reject_unauthorized=True,
            auth_tokens=[
                models.CreateOutputSystemByPackAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
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
                tls=models.TLSOptionsHostsItems.INHERIT,
                servername="<value>",
                weight=7243.49,
                template_host="<value>",
                template_port="<value>",
            ),
        ],
        pq_strict_ordering=True,
        pq_rate_per_sec=3109.58,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=3899.85,
        pq_max_backpressure_sec=4967.6,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.CreateOutputSystemByPackPqControlsSplunkLb(),
        auth_token="<value>",
        text_secret="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "sqs-output",
        "type": models.CreateOutputSystemByPackTypeSqs.SQS,
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
        "queue_type": models.CreateOutputSystemByPackQueueType.STANDARD,
        "aws_account_id": "<id>",
        "message_group_id": "<id>",
        "create_queue": False,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7240.49,
        "max_queue_size": 7569.17,
        "max_record_size_kb": 7532.91,
        "flush_period_sec": 9657.12,
        "max_in_progress": 6097.73,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "ecstatic opposite or around phew ouch whether whose consequently versus",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 41.51,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4240.87,
        "pq_max_backpressure_sec": 9550.59,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesStatsd" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "statsd-output",
        "type": models.CreateOutputSystemByPackTypeStatsd.STATSD,
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
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 8881.31,
        "flush_period_sec": 1139.86,
        "dns_resolve_period_sec": 2858.69,
        "description": "scuttle upright well-off weary zowie procurement after debit",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 2682.71,
        "write_timeout": 1267.8,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2479.41,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7900.85,
        "pq_max_backpressure_sec": 2414,
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
### Example Usage: OutputCreateExamplesStatsdExt

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesStatsdExt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "statsd-ext-output",
        "type": models.CreateOutputSystemByPackTypeStatsdExt.STATSD_EXT,
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
        "mtu": 1819.2,
        "flush_period_sec": 4621.8,
        "dns_resolve_period_sec": 5593.14,
        "description": "consequently playfully hoick realistic",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 2291.64,
        "write_timeout": 1484.48,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6506.07,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 5507.17,
        "pq_max_backpressure_sec": 2725.91,
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
### Example Usage: OutputCreateExamplesSumoLogic

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSumoLogic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "sumo-logic-output",
        "type": models.CreateOutputSystemByPackTypeSumoLogic.SUMO_LOGIC,
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
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.CreateOutputSystemByPackDataFormatSumoLogic.JSON,
        "concurrency": 1424.31,
        "max_payload_size_kb": 922.32,
        "max_payload_events": 5993.15,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 1717.56,
        "flush_period_sec": 2003.39,
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
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 5961.13,
        "description": "down worriedly at around easily or inasmuch outbid",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3481.25,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2319.77,
        "pq_max_backpressure_sec": 4362.24,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://understated-sediment.info",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "syslog-output",
        "type": models.CreateOutputSystemByPackTypeSyslog.SYSLOG,
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
        "protocol": models.CreateOutputSystemByPackProtocolSyslog.TCP,
        "facility": models.CreateOutputSystemByPackFacility.SIX,
        "severity": models.CreateOutputSystemByPackSeveritySyslog.DEBUG,
        "app_name": "<value>",
        "message_format": models.CreateOutputSystemByPackMessageFormat.RFC5424,
        "timestamp_format": models.CreateOutputSystemByPackTimestampFormat.SYSLOG,
        "throttle_rate_per_sec": "<value>",
        "octet_count_framing": True,
        "log_failed_requests": False,
        "description": "fairly pleasure jiggle",
        "load_balanced": True,
        "host": "localhost",
        "port": 514,
        "exclude_self": True,
        "hosts": [
            {
                "host": "adolescent-cemetery.org",
                "port": 5699.66,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 7378.74,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 6656.86,
        "load_balance_stats_period_sec": 4768.36,
        "max_concurrent_senders": 748.42,
        "connection_timeout": 9832.65,
        "write_timeout": 1279.92,
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
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "max_record_size": 6152.25,
        "udp_dns_resolve_period_sec": 3762.93,
        "enable_ip_spoofing": True,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5395.19,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 7289.32,
        "pq_max_backpressure_sec": 4600.99,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "tcpjson-output",
        "type": models.CreateOutputSystemByPackTypeTcpjson.TCPJSON,
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
        "connection_timeout": 4098.5,
        "write_timeout": 3807.97,
        "token_ttl_minutes": 9215.23,
        "send_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "unaccountably hard-to-find same kindly deprave the moisten task",
        "host": "localhost",
        "port": 10090,
        "exclude_self": True,
        "hosts": [
            {
                "host": "adolescent-cemetery.org",
                "port": 5699.66,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 7378.74,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 1392.89,
        "load_balance_stats_period_sec": 9185.86,
        "max_concurrent_senders": 9360.71,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1119.07,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4924.47,
        "pq_max_backpressure_sec": 7420.74,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWavefront

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesWavefront" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "wavefront-output",
        "type": models.CreateOutputSystemByPackTypeWavefront.WAVEFRONT,
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
        "concurrency": 8786.17,
        "max_payload_size_kb": 2965.79,
        "max_payload_events": 3712.73,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 3372.05,
        "flush_period_sec": 2182.98,
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
        ],
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "through yieldingly inquisitively pfft readies whenever minus louse alliance",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1288.03,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2799.01,
        "pq_max_backpressure_sec": 2440.55,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "webhook-output",
        "type": models.CreateOutputSystemByPackTypeWebhook.WEBHOOK,
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
        "method": models.MethodOptions.PUT,
        "format_": models.CreateOutputSystemByPackFormatWebhook.ADVANCED,
        "keep_alive": False,
        "concurrency": 9520.49,
        "max_payload_size_kb": 5120.47,
        "max_payload_events": 1110.11,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 9465.68,
        "flush_period_sec": 1261.02,
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
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.CreateOutputSystemByPackAuthenticationTypeWebhook.TEXT_SECRET,
        "tls": {
            "disabled": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "total_memory_limit_kb": 8639.61,
        "load_balanced": False,
        "description": "gosh lobotomise weakly contravene print",
        "custom_source_expression": "<value>",
        "custom_drop_when_null": False,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6552.81,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 2560.36,
        "pq_max_backpressure_sec": 4650.34,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Icie69",
        "password": "9AbOW9tqERCfhMp",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://unaware-fowl.info",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 3789.51,
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
                "url": "https://gloomy-publication.com/",
                "weight": 1833.76,
                "template_url": "https://courageous-saloon.net/",
            },
        ],
        "dns_resolve_period_sec": 2546.17,
        "load_balance_stats_period_sec": 2294.07,
        "template_login_url": "https://fake-louse.biz/",
        "template_secret": "<value>",
        "template_url": "https://submissive-heartache.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWizHec

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesWizHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "wiz-hec-output",
        "type": models.CreateOutputSystemByPackTypeWizHec.WIZ_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": "<value>",
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 4222.91,
        "max_payload_size_kb": 2163.92,
        "max_payload_events": 5534.34,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 1901,
        "flush_period_sec": 5774.63,
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
        "enable_multi_metrics": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "excluding hydrolyze eyeglasses ha kookily zowie home blah during battle",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 8687.97,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 5698.85,
        "pq_max_backpressure_sec": 465.8,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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

<!-- UsageSnippet language="python" operationID="createOutputSystemByPack" method="post" path="/p/{pack}/system/outputs" example="OutputCreateExamplesXsiam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.create(pack="<value>", request_body={
        "id": "xsiam-output",
        "type": models.CreateOutputSystemByPackTypeXsiam.XSIAM,
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
        "load_balanced": False,
        "concurrency": 5763.61,
        "max_payload_size_kb": 6925.51,
        "max_payload_events": 4318.09,
        "reject_unauthorized": True,
        "timeout_sec": 9888.04,
        "flush_period_sec": 6723.71,
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
        "auth_type": models.CreateOutputSystemByPackAuthenticationMethodXsiam.SECRET,
        "response_retry_settings": [
            {
                "http_status": 8177.04,
                "initial_backoff": 7866.98,
                "backoff_rate": 6178.16,
                "max_backoff": 3348.05,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": True,
            "initial_backoff": 9325.54,
            "backoff_rate": 3205.55,
            "max_backoff": 1352.21,
        },
        "response_honor_retry_after_header": False,
        "throttle_rate_req_per_sec": 188000,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 664.63,
        "description": "soliloquy abnegate numb",
        "url": "https://fatal-typewriter.net",
        "use_round_robin_dns": False,
        "exclude_self": True,
        "urls": [
            {
                "url": "https://sour-willow.net",
                "weight": 2247.73,
            },
        ],
        "dns_resolve_period_sec": 4453.39,
        "load_balance_stats_period_sec": 2927.5,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5713.34,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7532.3,
        "pq_max_backpressure_sec": 6857.66,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://acceptable-napkin.biz/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `pack`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The <code>id</code> of the Pack to create.                                                        |
| `request_body`                                                                                    | [models.CreateOutputSystemByPackRequestBody](../../models/createoutputsystembypackrequestbody.md) | :heavy_check_mark:                                                                                | Output object                                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOutputSystemByPackAndId" method="get" path="/p/{pack}/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to get.                      |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to get.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Destination.</br></br>Provide a complete representation of the Destination that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Destination.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Destination might not function as expected within the specified Pack.

### Example Usage: OutputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "create_container": False,
        "dest_path": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "max_concurrent_file_parts": 9626.81,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 1190.21,
        "max_file_open_time_sec": 5799.8,
        "max_file_idle_time_sec": 2643.71,
        "max_open_files": 4914.27,
        "header_line": "<value>",
        "write_high_water_mark": 460.88,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "auth_type": models.AuthenticationMethodOptions.CLIENT_CERT,
        "storage_class": models.BlobAccessTier.HOT,
        "description": "outside duh publicize neatly unto nun",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 8090.72,
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
        "empty_dir_cleanup_sec": 3115.77,
        "directory_batch_size": 5180.41,
        "deadletter_path": "<value>",
        "max_retry_num": 7908.54,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesAzureDataExplorer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "validate_database_settings": False,
        "ingest_mode": models.IngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.OutputAzureDataExplorerAuthenticationMethod.CLIENT_SECRET,
        "description": "judgementally gee now phooey",
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
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 4890.71,
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
        "enable_page_checksum": False,
        "remove_empty_dirs": True,
        "empty_dir_cleanup_sec": 7222.75,
        "directory_batch_size": 6416.36,
        "deadletter_enabled": False,
        "deadletter_path": "<value>",
        "max_retry_num": 2049.99,
        "is_mapping_obj": False,
        "mapping_obj": "<value>",
        "mapping_ref": "<value>",
        "ingest_url": "https://scornful-premier.info",
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "stage_path": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 4304.04,
        "max_file_open_time_sec": 5478.64,
        "max_file_idle_time_sec": 5753.43,
        "max_open_files": 4384.79,
        "max_concurrent_file_parts": 1628.67,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "add_id_to_stage_path": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "timeout_sec": 5395.45,
        "flush_immediately": True,
        "retain_blob_on_success": False,
        "extent_tags": [
            {
                "prefix": models.PrefixOptional.INGEST_BY,
                "value": "<value>",
            },
        ],
        "ingest_if_not_exists": [
            {
                "value": "<value>",
            },
        ],
        "report_level": models.ReportLevel.FAILURES_ONLY,
        "report_method": models.ReportMethod.TABLE,
        "additional_properties": [
            {
                "key": "<key>",
                "value": "<value>",
            },
        ],
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "concurrency": 8457.32,
        "max_payload_size_kb": 6553.47,
        "max_payload_events": 1458.55,
        "flush_period_sec": 6284.6,
        "reject_unauthorized": True,
        "use_round_robin_dns": True,
        "keep_alive": True,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5229.32,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 3774.4,
        "pq_max_backpressure_sec": 9855.68,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_cluster_url": "https://yellowish-trick.net/",
        "template_database": "<value>",
        "template_table": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_client_secret": "<value>",
        "template_format": "<value>",
        "template_ingest_url": "https://blushing-colonialism.name",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureEventhub

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesAzureEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "azure-eventhub-output",
        "type": models.OutputAzureEventhubType.AZURE_EVENTHUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.NONE,
        "format_": models.RecordDataFormatOptions.RAW,
        "max_record_size_kb": 7301.52,
        "flush_event_count": 5790.81,
        "flush_period_sec": 6221.86,
        "connection_timeout": 6833.13,
        "request_timeout": 2611.24,
        "max_retries": 7039.15,
        "max_back_off": 4527.16,
        "initial_backoff": 4140.17,
        "backoff_rate": 5925.09,
        "authentication_timeout": 3354.64,
        "reauthentication_threshold": 8673.22,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.SECRET,
            "password": "7UquuWKnI4T8yEp",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Otha.Wolf36",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.CERTIFICATE,
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
            "disabled": True,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "bind unethically behind velocity",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9002.1,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4029.74,
        "pq_max_backpressure_sec": 5403.8,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_topic": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesAzureLogs

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesAzureLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "azure-logs-output",
        "type": models.OutputAzureLogsType.AZURE_LOGS,
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
        "concurrency": 7445.48,
        "max_payload_size_kb": 9222.37,
        "max_payload_events": 9758.33,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 9069.11,
        "flush_period_sec": 8626.46,
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
        "api_url": "https://delicious-assist.org/",
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.OutputAzureLogsAuthenticationMethod.MANUAL,
        "description": "while sleet yahoo subsidy drat ripe moralise meh clonk",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9055.24,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 3094.09,
        "pq_max_backpressure_sec": 8231.22,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "chronicle-output",
        "type": models.OutputChronicleType.CHRONICLE,
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
        "api_version": "<value>",
        "authentication_method": models.OutputChronicleAuthenticationMethod.SERVICE_ACCOUNT_SECRET,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "region": "us",
        "concurrency": 1591.96,
        "max_payload_size_kb": 360.82,
        "max_payload_events": 669.48,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 917.86,
        "flush_period_sec": 3344.53,
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
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 5872.26,
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
        "description": "quit regulate deliberately if far oh a",
        "service_account_credentials": "<value>",
        "service_account_credentials_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6992.05,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 9241.54,
        "pq_max_backpressure_sec": 7581.91,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesClickHouse

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesClickHouse" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 6496.06,
        "max_payload_size_kb": 6754.34,
        "max_payload_events": 2144.97,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 8229.2,
        "flush_period_sec": 5763.32,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "dump_format_errors_to_disk": True,
        "stats_destination": {
            "url": "https://apprehensive-exasperation.name",
            "database": "<value>",
            "table_name": "<value>",
            "auth_type": "<value>",
            "username": "Jett.Waelchi4",
            "sql_username": "<value>",
            "password": "w2NGyozKB5spoFh",
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "yet impish keenly insecure instructor dead perfectly",
        "username": "Lulu.Spinka46",
        "password": "NZUA9GkXcdy50id",
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
        "pq_rate_per_sec": 4194.7,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3660.82,
        "pq_max_backpressure_sec": 6559.7,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://standard-pine.info/",
        "template_database": "<value>",
        "template_table_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudflareR2

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCloudflareR2" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "cloudflare-r2-output",
        "type": models.OutputCloudflareR2Type.CLOUDFLARE_R2,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "aws_authentication_method": models.OutputCloudflareR2AuthenticationMethod.AUTO,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": False,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V4,
        "object_acl": "<value>",
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "verify_permissions": True,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 1251.74,
        "max_open_files": 2969.43,
        "header_line": "<value>",
        "write_high_water_mark": 8826.77,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 8446.52,
        "max_file_idle_time_sec": 2426.05,
        "max_concurrent_file_parts": 5933.43,
        "description": "amid loosely linear",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 6645.34,
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
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 3135.25,
        "directory_batch_size": 1154.61,
        "deadletter_path": "<value>",
        "max_retry_num": 185.03,
        "template_bucket": "<value>",
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCloudwatch

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCloudwatch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "cloudwatch-output",
        "type": models.OutputCloudwatchType.CLOUDWATCH,
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 4520.57,
        "max_queue_size": 4309.43,
        "max_record_size_kb": 9350.28,
        "flush_period_sec": 6984.69,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "birdcage fooey sternly whether majestically excluding",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5109.17,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 1085.97,
        "pq_max_backpressure_sec": 9827,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output=models.OutputConfluentCloud(
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
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        topic="logs",
        ack=models.AcknowledgmentsOptions1.ALL,
        format_=models.RecordDataFormatOptions1.JSON,
        compression=models.CompressionOptions3.SNAPPY,
        max_record_size_kb=5407.63,
        flush_event_count=715.33,
        flush_period_sec=5546.59,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://lighthearted-dredger.org",
            connection_timeout=7210.32,
            request_timeout=7627.12,
            max_retries=7494.42,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=5091.61,
            default_value_schema_id=2259.59,
        ),
        connection_timeout=6448.17,
        request_timeout=7558.24,
        max_retries=3448.64,
        max_back_off=2938.63,
        initial_backoff=5846.5,
        backoff_rate=4656.1,
        authentication_timeout=9684.87,
        reauthentication_threshold=4341.07,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Vaughn_Botsford",
            password="J3to4z1Pba3wD7B",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_256,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://runny-saw.name",
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
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        description="astride impressionable trial for stake godfather gosh aside kindly supposing",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=False,
        pq_rate_per_sec=6978.04,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=7228.5,
        pq_max_backpressure_sec=3343.79,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.OutputConfluentCloudPqControls(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "load_balanced": True,
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "token_ttl_minutes": 3197.79,
        "exclude_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "compression": models.CompressionOptions1.GZIP,
        "concurrency": 3056.71,
        "max_payload_size_kb": 3747.12,
        "max_payload_events": 7787.01,
        "reject_unauthorized": True,
        "timeout_sec": 3082.83,
        "flush_period_sec": 8834.82,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "tenement until where pfft anti closely quarterly",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "modulo firsthand appropriate impressionable unnaturally label",
        "url": "https://shrill-cake.net/",
        "use_round_robin_dns": True,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://unkempt-charlatan.net/",
                "weight": 7027.74,
                "template_url": "https://married-chiffonier.net",
            },
        ],
        "dns_resolve_period_sec": 2705.77,
        "load_balance_stats_period_sec": 2439.7,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9095.75,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 4144.65,
        "pq_max_backpressure_sec": 543.85,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://silky-councilman.com/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "cribl-lake-output",
        "type": models.OutputCriblLakeType.CRIBL_LAKE,
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
        "bucket": "<value>",
        "region": "<value>",
        "aws_secret_key": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8301.38,
        "stage_path": "<value>",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.AUTHENTICATED_READ,
        "storage_class": models.StorageClassOptions.DEEP_ARCHIVE,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6872.45,
        "max_open_files": 922.06,
        "header_line": "<value>",
        "write_high_water_mark": 2405.54,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 8321.52,
        "max_file_idle_time_sec": 3354.55,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 8402.1,
        "aws_authentication_method": models.AwsAuthenticationMethodOptions.AUTO,
        "format_": models.FormatOptions.DDSS,
        "max_concurrent_file_parts": 5969.66,
        "description": "excluding now mallard reorganisation grok busily",
        "empty_dir_cleanup_sec": 1546.23,
        "directory_batch_size": 9248.69,
        "deadletter_path": "<value>",
        "max_retry_num": 3518.28,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCriblSearchEngine" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "initial_backoff": 9897.86,
            "backoff_rate": 5067.51,
            "max_backoff": 90.87,
        },
        "response_honor_retry_after_header": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "tenement until where pfft anti closely quarterly",
            },
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "description": "boohoo beneath scamper",
        "url": "https://0.0.0.0:10200",
        "exclude_self": False,
        "urls": [
            {
                "url": "https://unkempt-charlatan.net/",
                "weight": 7027.74,
                "template_url": "https://married-chiffonier.net",
            },
        ],
        "dns_resolve_period_sec": 494.5,
        "load_balance_stats_period_sec": 1392.24,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5384.36,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 9654.22,
        "pq_max_backpressure_sec": 38.09,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://puzzled-cope.org/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "cribl-tcp-output",
        "type": models.OutputCriblTCPType.CRIBL_TCP,
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
        "compression": models.CompressionOptions1.NONE,
        "log_failed_requests": True,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "connection_timeout": 4499.75,
        "write_timeout": 9083.6,
        "token_ttl_minutes": 3194.42,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "by hence why step-mother bleakly thankfully whose prohibition whisper",
            },
        ],
        "exclude_fields": [
            "<value 1>",
        ],
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "into enormously mmm uh-huh rudely mispronounce pigpen ew huzzah",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "webbed-import.com",
                "port": 5669.2,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 8579.92,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 4679.8,
        "load_balance_stats_period_sec": 4291.78,
        "max_concurrent_senders": 1845.71,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5642.93,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 50.68,
        "pq_max_backpressure_sec": 6764.87,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesCrowdstrikeNextGenSiem

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesCrowdstrikeNextGenSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 1332.31,
        "max_payload_size_kb": 8421.11,
        "max_payload_events": 4372.03,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 9653.19,
        "flush_period_sec": 6146.45,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "huzzah eek enfold",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9665.01,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8335.23,
        "pq_max_backpressure_sec": 4317.26,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://well-worn-finer.net/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatabricks

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDatabricks" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "dest_path": "<value>",
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "remove_empty_dirs": False,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 970.54,
        "max_file_open_time_sec": 9610.63,
        "max_file_idle_time_sec": 7268.2,
        "max_open_files": 7514.57,
        "header_line": "<value>",
        "write_high_water_mark": 9064.92,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
        "timeout_sec": 371.07,
        "description": "hubris eulogise react finer clamour pigpen fervently",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 8628.52,
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
        "empty_dir_cleanup_sec": 9170.98,
        "directory_batch_size": 4426.15,
        "deadletter_path": "<value>",
        "max_retry_num": 8094.33,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDatadog

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDatadog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "content_type": models.SendLogsAs.JSON,
        "message": "<value>",
        "source": "<value>",
        "host": "animated-tentacle.biz",
        "service": "<value>",
        "tags": [
            "<value 1>",
            "<value 2>",
        ],
        "batch_by_tags": False,
        "allow_api_key_from_events": True,
        "severity": models.OutputDatadogSeverity.EMERGENCY,
        "site": models.DatadogSite.US5,
        "send_counters_as_count": True,
        "concurrency": 7305.28,
        "max_payload_size_kb": 8510.77,
        "max_payload_events": 6981.39,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 9822.43,
        "flush_period_sec": 9155.3,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 8670.83,
        "description": "subtract duh general almost",
        "custom_url": "https://glaring-membership.name/",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 511.66,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 2626.58,
        "pq_max_backpressure_sec": 8406.46,
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
### Example Usage: OutputCreateExamplesDataset

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDataset" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "server_host_field": "<value>",
        "timestamp_field": "<value>",
        "default_severity": models.OutputDatasetSeverity.FINEST,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "site": models.DataSetSite.US,
        "concurrency": 9193.77,
        "max_payload_size_kb": 9808.87,
        "max_payload_events": 253.36,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 2723.58,
        "flush_period_sec": 3591.85,
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
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 7404.58,
        "description": "unlike by belabor waist barracks superficial vol",
        "custom_url": "https://wavy-mainstream.com",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6272.47,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 8207.74,
        "pq_max_backpressure_sec": 9156.37,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "api_key": "<value>",
        "text_secret": "<value>",
        "template_custom_url": "https://short-validity.org/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDiskSpool

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDiskSpool" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "time_window": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.CompressionOptionsPersistence.NONE,
        "partition_expr": "<value>",
        "description": "sunny what likewise vivaciously rarely",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDlS3

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDlS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6863.47,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PRIVATE,
        "storage_class": models.StorageClassOptions.ONEZONE_IA,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AES256,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9099.5,
        "max_open_files": 3454.84,
        "header_line": "<value>",
        "write_high_water_mark": 8359.92,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 1612.93,
        "max_file_idle_time_sec": 1991.26,
        "max_concurrent_file_parts": 8183.89,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 9401.43,
        "partitioning_fields": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "description": "before across seemingly courageously yuck providence underneath",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 6793.06,
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
        "empty_dir_cleanup_sec": 5188.13,
        "directory_batch_size": 8658.32,
        "deadletter_path": "<value>",
        "max_retry_num": 2633.72,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDynatraceHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 3097.84,
        "max_payload_size_kb": 6714.87,
        "max_payload_events": 1141.45,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 7758.15,
        "flush_period_sec": 6285.52,
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
        ],
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.OutputDynatraceHTTPAuthenticationType.TOKEN,
        "format_": models.OutputDynatraceHTTPFormat.JSON_ARRAY,
        "endpoint": models.Endpoint.CLOUD,
        "telemetry_type": models.TelemetryType.LOGS,
        "total_memory_limit_kb": 3794.77,
        "description": "round affectionate likely whether tooth",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1551.62,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6826.29,
        "pq_max_backpressure_sec": 5720.73,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "token": "your-api-key",
        "text_secret": "<value>",
        "environment_id": "<id>",
        "active_gate_domain": "<value>",
        "url": "https://gullible-attraction.info/",
        "template_url": "https://well-lit-costume.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesDynatraceOtlp

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesDynatraceOtlp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 2>",
        ],
        "protocol": models.OutputDynatraceOtlpProtocol.HTTP,
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
        "concurrency": 210.47,
        "max_payload_size_kb": 9413.88,
        "timeout_sec": 4820.34,
        "flush_period_sec": 86.91,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.PAYLOAD,
        "connection_timeout": 5704.41,
        "keep_alive_time": 5789.58,
        "keep_alive": True,
        "endpoint_type": models.EndpointType.SAAS,
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "quick-witted while phew fooey helplessly pfft",
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 242.91,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4385.39,
        "pq_max_backpressure_sec": 5538.13,
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
### Example Usage: OutputCreateExamplesElastic

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 733.26,
        "max_payload_size_kb": 5746.62,
        "max_payload_events": 9728.73,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 9678.92,
        "flush_period_sec": 3467.47,
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
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": False,
            "username": "Odie.Skiles",
            "password": "RyWsR_yFaKceblE",
            "auth_type": models.AuthenticationMethodOptionsAuth.TEXT_SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_version": models.ElasticVersion.SEVEN,
        "elastic_pipeline": "<value>",
        "include_doc_id": True,
        "write_action": models.WriteAction.INDEX,
        "retry_partial_errors": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "whereas oof modulo impossible mmm till",
        "url": "https://cuddly-printer.info",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://easy-dandelion.info/",
                "weight": 9314.75,
                "template_url": "https://proud-footrest.info",
            },
        ],
        "dns_resolve_period_sec": 5398,
        "load_balance_stats_period_sec": 14.64,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 3077.68,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 3308.34,
        "pq_max_backpressure_sec": 1449.39,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://whirlwind-tennis.org",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesElasticCloud

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesElasticCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "elastic-cloud-output",
        "type": models.OutputElasticCloudType.ELASTIC_CLOUD,
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
        "concurrency": 4319.98,
        "max_payload_size_kb": 9163.36,
        "max_payload_events": 2697.78,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 2028.06,
        "flush_period_sec": 8449.21,
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
        "extra_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth": {
            "disabled": False,
            "username": "Odie.Skiles",
            "password": "RyWsR_yFaKceblE",
            "auth_type": models.AuthenticationMethodOptionsAuth.TEXT_SECRET,
            "credentials_secret": "<value>",
            "manual_api_key": "<value>",
            "text_secret": "<value>",
        },
        "elastic_pipeline": "<value>",
        "include_doc_id": False,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "or well-to-do diligently joyfully negotiation greatly bewail gadzooks considering",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9392.65,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 556.12,
        "pq_max_backpressure_sec": 2451.19,
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
### Example Usage: OutputCreateExamplesExabeam

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesExabeam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "exabeam-output",
        "type": models.OutputExabeamType.EXABEAM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "bucket": "my-bucket",
        "region": "us-east1",
        "stage_path": "/tmp/staging",
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V2,
        "object_acl": models.ObjectACLOptions1.BUCKET_OWNER_FULL_CONTROL,
        "storage_class": models.StorageClassOptions1.NEARLINE,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "max_file_open_time_sec": 8587.19,
        "max_file_idle_time_sec": 5462.55,
        "max_open_files": 2343.76,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_size_mb": 1337.73,
        "encoded_configuration": "<value>",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
        "site_name": "<value>",
        "site_id": "<id>",
        "timezone_offset": "<value>",
        "aws_api_key": "<value>",
        "aws_secret_key": "<value>",
        "description": "seldom gadzooks snarling forecast",
        "empty_dir_cleanup_sec": 9206.29,
        "directory_batch_size": 3791.32,
        "deadletter_path": "<value>",
        "max_retry_num": 1606.45,
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "filesystem-output",
        "type": models.OutputFilesystemType.FILESYSTEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "dest_path": "/var/log/output",
        "stage_path": "<value>",
        "add_id_to_stage_path": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 9141.81,
        "max_file_open_time_sec": 6269.67,
        "max_file_idle_time_sec": 4900.17,
        "max_open_files": 3178.13,
        "header_line": "<value>",
        "write_high_water_mark": 5888.68,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "description": "dicker unto scrap young exotic unless drat joyfully",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.NORMAL,
        "automatic_schema": False,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 3704.88,
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
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 5667.47,
        "directory_batch_size": 9357.47,
        "deadletter_path": "<value>",
        "max_retry_num": 6117.35,
        "template_format": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleChronicle

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGoogleChronicle" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "google-chronicle-output",
        "type": models.OutputGoogleChronicleType.GOOGLE_CHRONICLE,
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
        "api_version": models.OutputGoogleChronicleAPIVersion.V1,
        "authentication_method": models.OutputGoogleChronicleAuthenticationMethod.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "log_format_type": models.SendEventsAs.UNSTRUCTURED,
        "region": "us",
        "concurrency": 8784.21,
        "max_payload_size_kb": 8397.4,
        "max_payload_events": 6095.89,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 6957.39,
        "flush_period_sec": 8927.22,
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
            "<value 3>",
        ],
        "use_round_robin_dns": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "total_memory_limit_kb": 6657.33,
        "description": "despite ouch yum duh",
        "extra_log_types": [
            {
                "log_type": "<value>",
                "description": "incidentally amid if vicinity ribbon including whether toward",
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
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 1368.71,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 1168.56,
        "pq_max_backpressure_sec": 5538.69,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_api_version": "<value>",
        "template_region": "<value>",
        "template_customer_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGoogleCloudLogging

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGoogleCloudLogging" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 3>",
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
        "google_auth_method": models.GoogleAuthenticationMethodOptions.SECRET,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_payload_size_kb": 5491.4,
        "max_payload_events": 8655.58,
        "flush_period_sec": 4379.89,
        "concurrency": 6997,
        "connection_timeout": 9702.69,
        "timeout_sec": 1224.89,
        "throttle_rate_req_per_sec": 306923,
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
        "total_memory_limit_kb": 7152.99,
        "description": "correctly whirlwind consequently that um nucleotidase nor round independence",
        "log_location_expression": "my-project",
        "payload_expression": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2278.08,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 1187.19,
        "pq_max_backpressure_sec": 1895.52,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "google-cloud-storage-output",
        "type": models.OutputGoogleCloudStorageType.GOOGLE_CLOUD_STORAGE,
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
        "endpoint": "https://storage.googleapis.com",
        "signature_version": models.SignatureVersionOptions4.V4,
        "aws_authentication_method": models.OutputGoogleCloudStorageAuthenticationMethod.AUTO,
        "stage_path": "/tmp/staging",
        "dest_path": "<value>",
        "verify_permissions": True,
        "object_acl": models.ObjectACLOptions1.AUTHENTICATED_READ,
        "storage_class": models.StorageClassOptions1.COLDLINE,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "add_id_to_stage_path": True,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.PARQUET,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 3344.08,
        "max_file_open_time_sec": 3310.81,
        "max_file_idle_time_sec": 1124.18,
        "max_open_files": 5414.81,
        "header_line": "<value>",
        "write_high_water_mark": 216.54,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "description": "slow actually readily",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_1_0,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 4167.75,
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
        "empty_dir_cleanup_sec": 9443.56,
        "directory_batch_size": 318.2,
        "deadletter_path": "<value>",
        "max_retry_num": 8876.52,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "google-pubsub-output",
        "type": models.OutputGooglePubsubType.GOOGLE_PUBSUB,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "topic_name": "my-topic",
        "create_topic": True,
        "ordered_delivery": False,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.SECRET,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "batch_size": 9482.92,
        "batch_timeout": 7263.98,
        "max_queue_size": 5971.61,
        "max_record_size_kb": 3431.33,
        "flush_period": 288.76,
        "max_in_progress": 1946.73,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "maroon deduct truly",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7475.46,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 8048.15,
        "pq_max_backpressure_sec": 6977.08,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_topic_name": "<value>",
        "template_region": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGrafanaCloud

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGrafanaCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output=models.OutputGrafanaCloudGrafanaCloud1(
        id="grafana-cloud-output",
        type=models.OutputGrafanaCloudType1.GRAFANA_CLOUD,
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
        loki_url="https://logs-prod-us-central1.grafana.net",
        prometheus_url="https://difficult-mentor.info",
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
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.CREDENTIALS_SECRET,
            token="<value>",
            text_secret="<value>",
            username="Jedidiah.Hammes",
            password="vldG5B7AGD7DT_h",
            credentials_secret="<value>",
        ),
        loki_auth=models.PrometheusAuthType(
            auth_type=models.AuthenticationTypeOptionsPrometheusAuth1.BASIC,
            token="<value>",
            text_secret="<value>",
            username="Berry.Lowe",
            password="pUBpjkjynnpVdwt",
            credentials_secret="<value>",
        ),
        concurrency=2881.29,
        max_payload_size_kb=4737.16,
        max_payload_events=5944.74,
        reject_unauthorized=True,
        timeout_sec=1009.95,
        flush_period_sec=9956.31,
        extra_http_headers=[
            models.ItemsTypeExtraHTTPHeaders(
                name="<value>",
                value="<value>",
            ),
        ],
        use_round_robin_dns=True,
        failed_request_logging_mode=models.FailedRequestLoggingModeOptions.PAYLOAD,
        safe_headers=[
            "<value 1>",
            "<value 2>",
        ],
        response_retry_settings=[
            models.ItemsTypeResponseRetrySettings(
                http_status=9145.72,
                initial_backoff=8049.35,
                backoff_rate=7506.18,
                max_backoff=8392.23,
            ),
        ],
        timeout_retry_settings=models.TimeoutRetrySettingsType(
            timeout_retry=False,
            initial_backoff=9705.48,
            backoff_rate=8513.57,
            max_backoff=3688.43,
        ),
        response_honor_retry_after_header=True,
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        description="stir-fry inquisitively developing coaxingly icy gee",
        compress=False,
        pq_strict_ordering=True,
        pq_rate_per_sec=6236.79,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=2055.87,
        pq_max_backpressure_sec=5302.97,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.NONE,
        pq_on_backpressure=models.QueueFullBehaviorOptions.BLOCK,
        pq_controls=models.OutputGrafanaCloudPqControls1(),
        template_loki_url="https://wasteful-summary.org",
        template_prometheus_url="https://zesty-hyphenation.net",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesGraphite

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesGraphite" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "mtu": 1108.13,
        "flush_period_sec": 3328.06,
        "dns_resolve_period_sec": 2083.11,
        "description": "affectionate about clear save dwell",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 2176.12,
        "write_timeout": 1709.73,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9742.96,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 6208.93,
        "pq_max_backpressure_sec": 3617.53,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesHoneycomb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 1911.92,
        "max_payload_size_kb": 6791.12,
        "max_payload_events": 2263.49,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 4717.56,
        "flush_period_sec": 6241.91,
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
        ],
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "singing pacemaker abaft finger help meh um and",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5731.2,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4952.91,
        "pq_max_backpressure_sec": 2623.72,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesHumioHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 8748.35,
        "max_payload_size_kb": 5912.04,
        "max_payload_events": 1669.79,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 3955.5,
        "flush_period_sec": 8784.08,
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
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "on humble that provided",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 1560.43,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 7920.24,
        "pq_max_backpressure_sec": 77.53,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://free-in-joke.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesInfluxdb

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesInfluxdb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "influxdb-output",
        "type": models.OutputInfluxdbType.INFLUXDB,
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
        "use_v2_api": True,
        "timestamp_precision": models.TimestampPrecision.M,
        "dynamic_value_field_name": False,
        "value_field_name": "<value>",
        "concurrency": 3829.03,
        "max_payload_size_kb": 6069.71,
        "max_payload_events": 5528.1,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 33.06,
        "flush_period_sec": 9775.28,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.OutputInfluxdbAuthenticationType.TEXT_SECRET,
        "description": "unsteady famously however",
        "database": "mydb",
        "bucket": "<value>",
        "org": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6508.18,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 5310.59,
        "pq_max_backpressure_sec": 9488.72,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "username": "Jackson_Hettinger40",
        "password": "cNBgRT46DROEKDU",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://utter-nectarine.com/",
        "template_database": "<value>",
        "template_bucket": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output=models.OutputKafka(
        id="kafka-output",
        type=models.OutputKafkaType.KAFKA,
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
            "localhost:9092",
        ],
        topic="logs",
        ack=models.AcknowledgmentsOptions1.NONE,
        format_=models.RecordDataFormatOptions1.RAW,
        compression=models.CompressionOptions3.LZ4,
        max_record_size_kb=2385.96,
        flush_event_count=4905.03,
        flush_period_sec=7310,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://lighthearted-dredger.org",
            connection_timeout=7210.32,
            request_timeout=7627.12,
            max_retries=7494.42,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=5091.61,
            default_value_schema_id=2259.59,
        ),
        connection_timeout=6414.38,
        request_timeout=6220.17,
        max_retries=9336.12,
        max_back_off=1613.32,
        initial_backoff=6542.35,
        backoff_rate=4920.44,
        authentication_timeout=2234.31,
        reauthentication_threshold=1737.55,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Vaughn_Botsford",
            password="J3to4z1Pba3wD7B",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_256,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://runny-saw.name",
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
            disabled=True,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="meanwhile aching in ecliptic than through",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=True,
        pq_rate_per_sec=558.33,
        pq_mode=models.ModeOptions.ERROR,
        pq_max_buffer_size=5057.63,
        pq_max_backpressure_sec=5220.97,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
        pq_on_backpressure=models.QueueFullBehaviorOptions.DROP,
        pq_controls=models.OutputKafkaPqControls(),
        template_topic="<value>",
    ))

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "kinesis-output",
        "type": models.OutputKinesisType.KINESIS,
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
        "stream_name": "my-stream",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1103.42,
        "concurrency": 3976.04,
        "max_record_size_kb": 2294.33,
        "flush_period_sec": 209.99,
        "compression": models.OutputKinesisCompression.NONE,
        "use_list_shards": True,
        "as_ndjson": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "oddly through gadzooks whoa",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "max_events_per_flush": 4963.5,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5757.02,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 5915.4,
        "pq_max_backpressure_sec": 9169.27,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "loki-output",
        "type": models.OutputLokiType.LOKI,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
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
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth1.TOKEN,
        "concurrency": 5209.75,
        "max_payload_size_kb": 4899.83,
        "max_payload_events": 866.12,
        "reject_unauthorized": True,
        "timeout_sec": 661.18,
        "flush_period_sec": 8113.72,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "enable_dynamic_headers": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "total_memory_limit_kb": 5730.87,
        "description": "why wherever that anxiously",
        "compress": False,
        "token": "<value>",
        "text_secret": "<value>",
        "username": "Jeremy12",
        "password": "Kaun7gP2PP7nR8C",
        "credentials_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7524.6,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7287.04,
        "pq_max_backpressure_sec": 5827.98,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesMicrosoftFabric" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "microsoft-fabric-output",
        "type": models.OutputMicrosoftFabricType.MICROSOFT_FABRIC,
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
        "topic": "logs",
        "ack": models.AcknowledgmentsOptions.NONE,
        "format_": models.RecordDataFormatOptions.RAW,
        "max_record_size_kb": 5491.84,
        "flush_event_count": 7850.09,
        "flush_period_sec": 9993.97,
        "connection_timeout": 6233.74,
        "request_timeout": 5606.2,
        "max_retries": 4955.03,
        "max_back_off": 9077.83,
        "initial_backoff": 9941.69,
        "backoff_rate": 6244.55,
        "authentication_timeout": 4271.75,
        "reauthentication_threshold": 8338.17,
        "sasl": {
            "disabled": False,
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Abner_Fritsch79",
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
            "disabled": True,
            "reject_unauthorized": True,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
        "description": "mutate surprisingly worriedly after fatally bleach worldly",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 6423.23,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 4887.41,
        "pq_max_backpressure_sec": 3522.04,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesMinio" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "minio-output",
        "type": models.OutputMinioType.MINIO,
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
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "<value>",
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "signature_version": models.SignatureVersionOptions5.V2,
        "object_acl": models.ObjectACLOptions.PUBLIC_READ,
        "storage_class": models.StorageClassOptions2.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionOptions.AES256,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "verify_permissions": False,
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.RAW,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6437.35,
        "max_open_files": 3981.69,
        "header_line": "<value>",
        "write_high_water_mark": 8983.21,
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 8039.1,
        "max_file_idle_time_sec": 2262.73,
        "max_concurrent_file_parts": 457.87,
        "description": "slipper meanwhile excepting giving dispense provided prime extroverted outside lest",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.NONE,
        "compression_level": models.CompressionLevelOptions.BEST_SPEED,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 1393.11,
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
        "enable_page_checksum": False,
        "empty_dir_cleanup_sec": 6647.23,
        "directory_batch_size": 1311.23,
        "deadletter_path": "<value>",
        "max_retry_num": 2082.71,
        "template_bucket": "<value>",
        "template_region": "<value>",
        "template_format": "<value>",
        "template_aws_api_key": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output=models.OutputMsk(
        id="msk-output",
        type=models.OutputMskType.MSK,
        pipeline="<value>",
        system_fields=[
            "<value 1>",
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
        compression=models.CompressionOptions3.NONE,
        max_record_size_kb=1115.17,
        flush_event_count=3467.83,
        flush_period_sec=2384.7,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType1(
            disabled=True,
            schema_registry_url="https://lighthearted-dredger.org",
            connection_timeout=7210.32,
            request_timeout=7627.12,
            max_retries=7494.42,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
                credentials_secret="<value>",
            ),
            tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
                disabled=True,
                reject_unauthorized=False,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
            default_key_schema_id=5091.61,
            default_value_schema_id=2259.59,
        ),
        connection_timeout=5007.18,
        request_timeout=581.3,
        max_retries=636.26,
        max_back_off=6902.71,
        initial_backoff=6572.27,
        backoff_rate=4364.27,
        authentication_timeout=4969.27,
        reauthentication_threshold=5111.56,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V4,
        reuse_connections=False,
        reject_unauthorized=True,
        enable_assume_role=True,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=3344.39,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        on_backpressure=models.BackpressureBehaviorOptions.BLOCK,
        description="till motivate near lady shadowbox pale aside naturally until",
        aws_api_key="<value>",
        aws_secret="<value>",
        protobuf_library_id="<id>",
        protobuf_encoding_id="<id>",
        pq_strict_ordering=False,
        pq_rate_per_sec=7271.21,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=1225.14,
        pq_max_backpressure_sec=6320.84,
        pq_max_file_size="<value>",
        pq_max_size="<value>",
        pq_path="<value>",
        pq_compress=models.CompressionOptionsPq.GZIP,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "netflow-output",
        "type": models.OutputNetflowType.NETFLOW,
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
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 9038.19,
        "enable_ip_spoofing": True,
        "description": "stealthily lest along",
        "max_record_size": 7756.42,
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesNewrelic

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesNewrelic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "region": models.RegionOptions.EU,
        "log_type": "<value>",
        "message_field": "<value>",
        "metadata": [
            {
                "name": models.FieldName.AUDIT_ID,
                "value": "<value>",
            },
        ],
        "concurrency": 9558.92,
        "max_payload_size_kb": 5115.13,
        "max_payload_events": 6174.66,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 4711.57,
        "flush_period_sec": 46.1,
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
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "total_memory_limit_kb": 2240.62,
        "description": "tectonics than briefly pish wildly",
        "custom_url": "https://quiet-wombat.info",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 602.38,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7480.49,
        "pq_max_backpressure_sec": 1506.62,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesNewrelicEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "newrelic-events-output",
        "type": models.OutputNewrelicEventsType.NEWRELIC_EVENTS,
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
        "region": models.RegionOptions.CUSTOM,
        "account_id": "123456",
        "event_type": "CriblEvent",
        "concurrency": 1490.13,
        "max_payload_size_kb": 23.35,
        "max_payload_events": 2495.92,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 5294.51,
        "flush_period_sec": 4825.42,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptions2.MANUAL,
        "description": "internalise greedy meanwhile wetly",
        "custom_url": "https://vague-hyphenation.net/",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7505.35,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7681.23,
        "pq_max_backpressure_sec": 3570.46,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "api_key": "your-api-key",
        "text_secret": "<value>",
        "template_region": "<value>",
        "template_account_id": "<id>",
        "template_event_type": "<value>",
        "template_custom_url": "https://twin-ferret.com",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 3>",
        ],
        "protocol": models.ProtocolOptions.HTTP,
        "endpoint": "http://localhost:4317",
        "otlp_version": models.OutputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0,
        "compress": models.CompressionOptions4.GZIP,
        "http_compress": models.CompressionOptions5.NONE,
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
        "concurrency": 7438.69,
        "max_payload_size_kb": 5961.44,
        "timeout_sec": 8866.44,
        "flush_period_sec": 3115.59,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 1681.74,
        "keep_alive_time": 783.35,
        "keep_alive": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "wherever after so grimy",
        "username": "Newell_Block",
        "password": "Pog3DCwYAVHYvXx",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 1273.92,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 3586.04,
        "pq_max_backpressure_sec": 3775.16,
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
### Example Usage: OutputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "metric_rename_expr": "<value>",
        "send_metadata": False,
        "concurrency": 3188.74,
        "max_payload_size_kb": 2790.51,
        "max_payload_events": 542.04,
        "reject_unauthorized": False,
        "timeout_sec": 3180.33,
        "flush_period_sec": 7593.86,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.TEXT_SECRET,
        "description": "unless sleepily instantly dwell per pitiful under broadly axe reporter",
        "metrics_flush_period_sec": 8599.01,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 5568.14,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 8622.36,
        "pq_max_backpressure_sec": 9787,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Alison31",
        "password": "zoUKDif9prN2TD0",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_url": "https://sociable-case.name/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRing

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesRing" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "ring-output",
        "type": models.OutputRingType.RING,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "format_": models.OutputRingDataFormat.RAW,
        "partition_expr": "<value>",
        "max_data_size": "<value>",
        "max_data_time": "<value>",
        "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
        "dest_path": "<value>",
        "on_backpressure": models.BackpressureBehaviorOptions1.DROP,
        "description": "vice bind for bah whenever below following",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesRouter

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesRouter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 2>",
        ],
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
                "description": "yearly hot accelerator darling energetically sedately without detective",
                "final": True,
            },
        ],
        "description": "dental oh how",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "s3-output",
        "type": models.OutputS3Type.S3,
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
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 4718.83,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "dest_path": "<value>",
        "object_acl": models.ObjectACLOptions.PUBLIC_READ_WRITE,
        "storage_class": models.StorageClassOptions.STANDARD,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": True,
        "partition_expr": "<value>",
        "format_": models.DataFormatOptions.JSON,
        "base_file_name": "<value>",
        "file_name_suffix": "<value>",
        "max_file_size_mb": 6192.09,
        "max_open_files": 3926.44,
        "header_line": "<value>",
        "write_high_water_mark": 8748.54,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": False,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.BLOCK,
        "force_close_on_shutdown": True,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 4324.66,
        "max_file_idle_time_sec": 2081.88,
        "max_concurrent_file_parts": 9218.14,
        "verify_permissions": False,
        "max_closing_files_to_backpressure": 6709.29,
        "description": "furthermore iterate within yuck inconsequential personalise puritan oh synthesise",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "compress": models.CompressionOptions2.GZIP,
        "compression_level": models.CompressionLevelOptions.BEST_COMPRESSION,
        "automatic_schema": True,
        "parquet_schema": "<value>",
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_6,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V2,
        "parquet_row_group_length": 6277.7,
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
        "empty_dir_cleanup_sec": 1725.86,
        "directory_batch_size": 4697.22,
        "deadletter_path": "<value>",
        "max_retry_num": 5211.8,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "security-lake-output",
        "type": models.OutputSecurityLakeType.SECURITY_LAKE,
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
        "region": "us-east-1",
        "aws_secret_key": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "endpoint": "<value>",
        "signature_version": models.OutputSecurityLakeSignatureVersion.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1265.03,
        "stage_path": "/tmp/staging",
        "add_id_to_stage_path": True,
        "object_acl": models.ObjectACLOptions.AWS_EXEC_READ,
        "storage_class": models.StorageClassOptions.INTELLIGENT_TIERING,
        "server_side_encryption": models.ServerSideEncryptionForUploadedObjectsOptions.AWS_KMS,
        "kms_key_id": "<id>",
        "remove_empty_dirs": False,
        "base_file_name": "<value>",
        "max_file_size_mb": 1025.66,
        "max_open_files": 8406.64,
        "header_line": "<value>",
        "write_high_water_mark": 6587.5,
        "on_backpressure": models.BackpressureBehaviorOptions1.BLOCK,
        "deadletter_enabled": True,
        "on_disk_full_backpressure": models.DiskSpaceProtectionOptions.DROP,
        "force_close_on_shutdown": False,
        "retry_settings": {
            "enabled": True,
            "initial_backoff_ms": 9741.71,
            "backoff_multiplier": 7684.82,
            "max_backoff_ms": 1991.93,
            "jitter_percent": 5686.77,
        },
        "max_file_open_time_sec": 3870.7,
        "max_file_idle_time_sec": 8758.85,
        "max_concurrent_file_parts": 2545.81,
        "verify_permissions": True,
        "max_closing_files_to_backpressure": 5493.06,
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
        "automatic_schema": False,
        "parquet_version": models.ParquetVersionOptions.PARQUET_2_4,
        "parquet_data_page_version": models.DataPageVersionOptions.DATA_PAGE_V1,
        "parquet_row_group_length": 4946.58,
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
        "enable_page_checksum": True,
        "description": "nor astride behind drat drum proliferate whether",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "empty_dir_cleanup_sec": 5174.85,
        "directory_batch_size": 6602.4,
        "parquet_schema": "<value>",
        "deadletter_path": "<value>",
        "max_retry_num": 641.9,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSentinel" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "sentinel-output",
        "type": models.OutputSentinelType.SENTINEL,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "keep_alive": False,
        "concurrency": 7452.54,
        "max_payload_size_kb": 259.52,
        "max_payload_events": 1734.02,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 8639.21,
        "flush_period_sec": 9332.14,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.OutputSentinelAuthType.OAUTH,
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "scope": "<value>",
        "endpoint_url_configuration": models.EndpointConfiguration.URL,
        "total_memory_limit_kb": 4882.5,
        "description": "best psst modulo pivot paralyse exotic prime outside hungrily",
        "format_": models.OutputSentinelFormat.CUSTOM,
        "custom_source_expression": "<value>",
        "custom_drop_when_null": True,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9126.79,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 136.07,
        "pq_max_backpressure_sec": 7727.78,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "url": "https://your-workspace.ingest.monitor.azure.com",
        "dcr_id": "<id>",
        "dce_endpoint": "<value>",
        "stream_name": "<value>",
        "template_login_url": "https://ill-lifestyle.name",
        "template_secret": "<value>",
        "template_client_id": "<id>",
        "template_scope": "<value>",
        "template_url": "https://irresponsible-suspension.net",
        "template_dcr_id": "<id>",
        "template_dce_endpoint": "<value>",
        "template_stream_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSentinelOneAiSiem

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSentinelOneAiSiem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "sentinel-one-ai-siem-output",
        "type": models.OutputSentinelOneAiSiemType.SENTINEL_ONE_AI_SIEM,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "region": models.Region.US,
        "endpoint": models.AISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
        "concurrency": 9061.93,
        "max_payload_size_kb": 8105.66,
        "max_payload_events": 5244.2,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 629.95,
        "flush_period_sec": 891.65,
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "apropos lace ugh illustrious lovingly attraction skeleton whenever wetly",
        "token": "<value>",
        "text_secret": "<value>",
        "base_url": "https://tidy-lox.net",
        "host_expression": "<value>",
        "source_expression": "<value>",
        "source_type_expression": "<value>",
        "data_source_category_expression": "<value>",
        "data_source_name_expression": "<value>",
        "data_source_vendor_expression": "<value>",
        "event_type_expression": "<value>",
        "host": "empty-asset.biz",
        "source": "<value>",
        "source_type": "<value>",
        "data_source_category": "<value>",
        "data_source_name": "<value>",
        "data_source_vendor": "<value>",
        "event_type": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9088.42,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 6644.04,
        "pq_max_backpressure_sec": 7125.85,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesServiceNow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "auth_token_name": "<value>",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "max_payload_size_kb": 9648.28,
        "protocol": models.ProtocolOptions.HTTP,
        "compress": models.CompressionOptions4.GZIP,
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
        "concurrency": 4338.53,
        "timeout_sec": 2341.74,
        "flush_period_sec": 6471.56,
        "failed_request_logging_mode": models.FailedRequestLoggingModeOptions.NONE,
        "connection_timeout": 1985.64,
        "keep_alive_time": 3282.21,
        "keep_alive": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "towards broadcast um er however wasabi worriedly afore",
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
            "<value 2>",
            "<value 3>",
        ],
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
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
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 1041.55,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 2544.94,
        "pq_max_backpressure_sec": 4506.9,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSignalfx" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 2>",
            "<value 3>",
        ],
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "realm": "us0",
        "concurrency": 8034.73,
        "max_payload_size_kb": 9984.9,
        "max_payload_events": 3261.65,
        "compress": False,
        "reject_unauthorized": False,
        "timeout_sec": 1420.03,
        "flush_period_sec": 7567.96,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "knavishly whale an impressionable in scholarship penalise below opposite along",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 7221.57,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 5552.89,
        "pq_max_backpressure_sec": 3344.59,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "snmp-output",
        "type": models.OutputSnmpType.SNMP,
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
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 9651.38,
        "description": "zowie but once outdo runny meh whereas",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSns

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSns" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "sns-output",
        "type": models.OutputSnsType.SNS,
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
        "max_retries": 2785.69,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.OutputSnsSignatureVersion.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8775.69,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "description": "bewail clumsy bank delightfully doodle splash collectivization gosh observe",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 5474.65,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 6128.21,
        "pq_max_backpressure_sec": 4668.8,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        ],
        "host": "localhost",
        "port": 9997,
        "nested_fields": models.NestedFieldSerializationOptions.JSON,
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 8728.82,
        "write_timeout": 9415.24,
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "enable_multi_metrics": True,
        "enable_ack": True,
        "log_failed_requests": False,
        "max_s2_sversion": models.MaxS2SVersionOptions.V4,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "woot solemnly bah plus supposing reassuringly summary perky but",
        "max_failed_health_checks": 7847.74,
        "compress": models.CompressionOptions.DISABLED,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2414.19,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9268.97,
        "pq_max_backpressure_sec": 7468.74,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "splunk-hec-output",
        "type": models.OutputSplunkHecType.SPLUNK_HEC,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "load_balanced": False,
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 2075.02,
        "max_payload_size_kb": 9369.83,
        "max_payload_events": 351.37,
        "compress": False,
        "reject_unauthorized": True,
        "timeout_sec": 2414.52,
        "flush_period_sec": 3436.47,
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
            "<value 3>",
        ],
        "enable_multi_metrics": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "description": "oof often truly difficult pish yuck",
        "url": "https://forceful-compromise.net",
        "use_round_robin_dns": False,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://puny-case.net/",
                "weight": 5487.59,
                "template_url": "https://stable-humor.net",
            },
        ],
        "dns_resolve_period_sec": 5280.98,
        "load_balance_stats_period_sec": 4197.66,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9986.63,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 3014.85,
        "pq_max_backpressure_sec": 9782.24,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://sudden-tributary.net",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSplunkLb

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSplunkLb" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output=models.OutputSplunkLb(
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
        dns_resolve_period_sec=5646.62,
        load_balance_stats_period_sec=9217.44,
        max_concurrent_senders=8658.99,
        nested_fields=models.NestedFieldSerializationOptions.JSON,
        throttle_rate_per_sec="<value>",
        connection_timeout=2955.33,
        write_timeout=8574.03,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        enable_multi_metrics=False,
        enable_ack=True,
        log_failed_requests=True,
        max_s2_sversion=models.MaxS2SVersionOptions.V4,
        on_backpressure=models.BackpressureBehaviorOptions.DROP,
        indexer_discovery=True,
        sender_unhealthy_time_allowance=7463.13,
        auth_type=models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        description="gadzooks founder in",
        max_failed_health_checks=5884.8,
        compress=models.CompressionOptions.DISABLED,
        indexer_discovery_configs=models.IndexerDiscoveryConfigs(
            site="<value>",
            master_uri="https://intrepid-warming.biz/",
            refresh_interval_sec=1878.89,
            reject_unauthorized=True,
            auth_tokens=[
                models.OutputSplunkLbAuthToken(
                    auth_type=models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
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
                weight=1733.48,
                template_host="<value>",
                template_port="<value>",
            ),
        ],
        pq_strict_ordering=False,
        pq_rate_per_sec=827.91,
        pq_mode=models.ModeOptions.BACKPRESSURE,
        pq_max_buffer_size=2331.28,
        pq_max_backpressure_sec=4424.21,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "create_queue": False,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8027.27,
        "max_queue_size": 1545.05,
        "max_record_size_kb": 2828.49,
        "flush_period_sec": 3670.2,
        "max_in_progress": 2921.36,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "fooey swordfish worst connect what hm paltry tributary",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 6796.85,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 4862.56,
        "pq_max_backpressure_sec": 4675.07,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesStatsd" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "statsd-output",
        "type": models.OutputStatsdType.STATSD,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 393.48,
        "flush_period_sec": 5.11,
        "dns_resolve_period_sec": 2355.45,
        "description": "great familiar make",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 1162.08,
        "write_timeout": 6512.05,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 8267.14,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 6245.22,
        "pq_max_backpressure_sec": 6436.69,
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
### Example Usage: OutputCreateExamplesStatsdExt

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesStatsdExt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "statsd-ext-output",
        "type": models.OutputStatsdExtType.STATSD_EXT,
        "pipeline": "<value>",
        "system_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "environment": "<value>",
        "streamtags": [
            "<value 1>",
        ],
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
        "mtu": 9805.29,
        "flush_period_sec": 8070.55,
        "dns_resolve_period_sec": 6532.22,
        "description": "phew meanwhile gee emulsify ew and next mechanically whereas",
        "throttle_rate_per_sec": "<value>",
        "connection_timeout": 2274.33,
        "write_timeout": 1209.76,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 9641.16,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 9213.48,
        "pq_max_backpressure_sec": 5873.87,
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
### Example Usage: OutputCreateExamplesSumoLogic

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSumoLogic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "sumo-logic-output",
        "type": models.OutputSumoLogicType.SUMO_LOGIC,
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
        "url": "https://endpoint1.collection.us2.sumologic.com",
        "custom_source": "<value>",
        "custom_category": "<value>",
        "format_": models.OutputSumoLogicDataFormat.RAW,
        "concurrency": 8191.14,
        "max_payload_size_kb": 2659.7,
        "max_payload_events": 7967.49,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 812.41,
        "flush_period_sec": 6680.93,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 1901.24,
        "description": "heighten blushing finally bah",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 3450.55,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 835.24,
        "pq_max_backpressure_sec": 491.18,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_url": "https://bowed-provider.com",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "syslog-output",
        "type": models.OutputSyslogType.SYSLOG,
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
        "protocol": models.OutputSyslogProtocol.UDP,
        "facility": models.Facility.TEN,
        "severity": models.OutputSyslogSeverity.INFO,
        "app_name": "<value>",
        "message_format": models.MessageFormat.RFC5424,
        "timestamp_format": models.TimestampFormat.ISO8601,
        "throttle_rate_per_sec": "<value>",
        "octet_count_framing": True,
        "log_failed_requests": False,
        "description": "shudder mockingly dispense gloomy anenst gosh until whenever",
        "load_balanced": False,
        "host": "localhost",
        "port": 514,
        "exclude_self": False,
        "hosts": [
            {
                "host": "webbed-import.com",
                "port": 5669.2,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 8579.92,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 9446.86,
        "load_balance_stats_period_sec": 417.62,
        "max_concurrent_senders": 9989.57,
        "connection_timeout": 6911.57,
        "write_timeout": 2379.31,
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "max_record_size": 6755.68,
        "udp_dns_resolve_period_sec": 4579.44,
        "enable_ip_spoofing": True,
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 9178.98,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2070.88,
        "pq_max_backpressure_sec": 6498.55,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "load_balanced": True,
        "compression": models.CompressionOptions1.GZIP,
        "log_failed_requests": True,
        "throttle_rate_per_sec": "<value>",
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "connection_timeout": 8843.62,
        "write_timeout": 3301.22,
        "token_ttl_minutes": 1770.13,
        "send_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "aside unabashedly while sometimes descent slump worriedly weary revoke",
        "host": "localhost",
        "port": 10090,
        "exclude_self": False,
        "hosts": [
            {
                "host": "webbed-import.com",
                "port": 5669.2,
                "tls": models.TLSOptionsHostsItems.OFF,
                "servername": "<value>",
                "weight": 8579.92,
                "template_host": "<value>",
                "template_port": "<value>",
            },
        ],
        "dns_resolve_period_sec": 1892.95,
        "load_balance_stats_period_sec": 2219.18,
        "max_concurrent_senders": 5741.69,
        "pq_strict_ordering": True,
        "pq_rate_per_sec": 2434.51,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 2098.8,
        "pq_max_backpressure_sec": 8241.17,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWavefront

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesWavefront" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "domain": "longboard",
        "concurrency": 6780.94,
        "max_payload_size_kb": 8710.76,
        "max_payload_events": 4977.62,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 1014.39,
        "flush_period_sec": 1863.25,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "description": "minority fork diligently consequently though absent whose ignorance dutiful",
        "token": "your-token",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 439.55,
        "pq_mode": models.ModeOptions.BACKPRESSURE,
        "pq_max_buffer_size": 984.45,
        "pq_max_backpressure_sec": 6714.61,
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
### Example Usage: OutputCreateExamplesWebhook

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
            "<value 3>",
        ],
        "method": models.MethodOptions.PUT,
        "format_": models.OutputWebhookFormat.ADVANCED,
        "keep_alive": True,
        "concurrency": 8755.55,
        "max_payload_size_kb": 6177.86,
        "max_payload_events": 3404.23,
        "compress": True,
        "reject_unauthorized": False,
        "timeout_sec": 3455.4,
        "flush_period_sec": 5135.61,
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
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "auth_type": models.OutputWebhookAuthenticationType.CREDENTIALS_SECRET,
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "total_memory_limit_kb": 7737.05,
        "load_balanced": False,
        "description": "notarize terribly bashfully aw woot",
        "custom_source_expression": "<value>",
        "custom_drop_when_null": True,
        "custom_event_delimiter": "<value>",
        "custom_content_type": "<value>",
        "custom_payload_expression": "<value>",
        "advanced_content_type": "<value>",
        "format_event_code": "<value>",
        "format_payload_code": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 3983.53,
        "pq_mode": models.ModeOptions.ALWAYS,
        "pq_max_buffer_size": 9465.91,
        "pq_max_backpressure_sec": 7319.75,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.NONE,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.DROP,
        "pq_controls": {},
        "username": "Helene_Brown",
        "password": "1IQ4If1hcFrV5EE",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://hateful-hutch.name",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 6873.12,
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
        "exclude_self": True,
        "urls": [
            {
                "url": "https://weekly-supplier.org",
                "weight": 7951.07,
                "template_url": "https://rectangular-accountability.name",
            },
        ],
        "dns_resolve_period_sec": 1730.18,
        "load_balance_stats_period_sec": 8338.46,
        "template_login_url": "https://carefree-cork.net",
        "template_secret": "<value>",
        "template_url": "https://excitable-bourgeoisie.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputCreateExamplesWizHec

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesWizHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
        "id": "wiz-hec-output",
        "type": models.OutputWizHecType.WIZ_HEC,
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
        "load_balanced": "<value>",
        "next_queue": "<value>",
        "tcp_routing": "<value>",
        "tls": {
            "disabled": True,
            "servername": "<value>",
            "certificate_name": "<value>",
            "ca_path": "<value>",
            "priv_key_path": "<value>",
            "cert_path": "<value>",
            "passphrase": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        },
        "concurrency": 653.76,
        "max_payload_size_kb": 8807.31,
        "max_payload_events": 2723.31,
        "compress": True,
        "reject_unauthorized": True,
        "timeout_sec": 1822.3,
        "flush_period_sec": 3768.44,
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
        "enable_multi_metrics": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": False,
        "on_backpressure": models.BackpressureBehaviorOptions.DROP,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
        "description": "midst unexpectedly boiling uh-huh reflecting veg pfft deserted excepting",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 7926.84,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 7504.19,
        "pq_max_backpressure_sec": 4345,
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

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputCreateExamplesXsiam" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
        "concurrency": 8207.39,
        "max_payload_size_kb": 1553.6,
        "max_payload_events": 5682.57,
        "reject_unauthorized": False,
        "timeout_sec": 9456.19,
        "flush_period_sec": 1832.2,
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
        "auth_type": models.OutputXsiamAuthenticationMethod.SECRET,
        "response_retry_settings": [
            {
                "http_status": 9145.72,
                "initial_backoff": 8049.35,
                "backoff_rate": 7506.18,
                "max_backoff": 8392.23,
            },
        ],
        "timeout_retry_settings": {
            "timeout_retry": False,
            "initial_backoff": 9705.48,
            "backoff_rate": 8513.57,
            "max_backoff": 3688.43,
        },
        "response_honor_retry_after_header": True,
        "throttle_rate_req_per_sec": 668286,
        "on_backpressure": models.BackpressureBehaviorOptions.QUEUE,
        "total_memory_limit_kb": 9706.26,
        "description": "qua cornet outside oil candid seemingly",
        "url": "https://inexperienced-pigsty.biz/",
        "use_round_robin_dns": True,
        "exclude_self": False,
        "urls": [
            {
                "url": "https://delirious-tackle.info/",
                "weight": 1722.99,
            },
        ],
        "dns_resolve_period_sec": 6218.76,
        "load_balance_stats_period_sec": 8569.53,
        "token": "<value>",
        "text_secret": "<value>",
        "pq_strict_ordering": False,
        "pq_rate_per_sec": 2675.25,
        "pq_mode": models.ModeOptions.ERROR,
        "pq_max_buffer_size": 8561.04,
        "pq_max_backpressure_sec": 325.7,
        "pq_max_file_size": "<value>",
        "pq_max_size": "<value>",
        "pq_path": "<value>",
        "pq_compress": models.CompressionOptionsPq.GZIP,
        "pq_on_backpressure": models.QueueFullBehaviorOptions.BLOCK,
        "pq_controls": {},
        "template_url": "https://distinct-management.biz/",
    })

    # Handle response
    print(res)

```
### Example Usage: OutputExamplesDefault

<!-- UsageSnippet language="python" operationID="updateOutputSystemByPackAndId" method="patch" path="/p/{pack}/system/outputs/{id}" example="OutputExamplesDefault" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.update(id="<id>", pack="<value>", output={
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
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to update.                          |
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

Delete the specified Destination within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOutputSystemByPackAndId" method="delete" path="/p/{pack}/system/outputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.destinations.delete(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Destination to delete.                   |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to delete.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedOutput](../../models/countedoutput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |