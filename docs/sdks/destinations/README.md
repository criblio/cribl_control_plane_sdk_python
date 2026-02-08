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
        "container_name": "my-container",
        "stage_path": "/tmp/staging",
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
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "ingest_mode": models.CreateOutputIngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.CreateOutputAuthenticationMethodAzureDataExplorer.CLIENT_SECRET,
        "client_secret": "client-secret",
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
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
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
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
        "log_type": "Cribl",
        "auth_type": models.CreateOutputAuthenticationMethodAzureLogs.MANUAL,
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
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
        "region": "us",
        "log_type": "UNKNOWN",
        "gcp_project_id": "my-project",
        "gcp_instance": "customer-id",
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
        "url": "http://localhost:8123/",
        "database": "mydb",
        "table_name": "mytable",
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
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "stage_path": "/tmp/staging",
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
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "region": "us-east-1",
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
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        topic="logs",
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
        "system_fields": [
            "cribl_pipe",
        ],
        "streamtags": [],
        "load_balanced": False,
        "tls": {
            "disabled": True,
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
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "url": "https://0.0.0.0:10200",
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
        "host": "localhost",
        "port": 10090,
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
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "token": "your-token",
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
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
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
        "api_key": "your-api-key",
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "stage_path": "/tmp/staging",
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
        "auth_type": models.CreateOutputAuthenticationTypeDynatraceHTTP.TOKEN,
        "format_": models.CreateOutputFormatDynatraceHTTP.JSON_ARRAY,
        "endpoint": models.CreateOutputEndpoint.CLOUD,
        "telemetry_type": models.CreateOutputTelemetryType.LOGS,
        "token": "your-api-key",
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
        "protocol": models.CreateOutputProtocolDynatraceOtlp.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "endpoint_type": models.CreateOutputEndpointType.SAAS,
        "token_secret": "your-token-secret",
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
        "index": "logs",
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
        "url": "my-cloud-id",
        "index": "logs",
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
        "bucket": "my-bucket",
        "region": "us-east1",
        "stage_path": "/tmp/staging",
        "endpoint": "https://storage.googleapis.com",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
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
        "dest_path": "/var/log/output",
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
        "log_format_type": models.CreateOutputSendEventsAs.UNSTRUCTURED,
        "region": "us",
        "customer_id": "customer-id",
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
        "log_location_type": models.CreateOutputLogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "log_location_expression": "my-project",
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
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "stage_path": "/tmp/staging",
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
        "topic_name": "my-topic",
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
        loki_url="https://logs-prod-us-central1.grafana.net",
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
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
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
        "dataset": "my-dataset",
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
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "token": "your-token",
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
        "url": "http://localhost:8086",
        "database": "mydb",
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
        brokers=[
            "localhost:9092",
        ],
        topic="logs",
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
        "stream_name": "my-stream",
        "region": "us-east-1",
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
        "url": "http://localhost:3100/loki/api/v1/push",
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
        "topic": "logs",
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
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
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "stage_path": "/tmp/staging",
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
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topic="logs",
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        region="us-east-1",
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
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
            },
        ],
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
        "api_key": "your-api-key",
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
        "account_id": "123456",
        "event_type": "CriblEvent",
        "api_key": "your-api-key",
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
        "endpoint": "http://localhost:4317",
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
        "url": "http://localhost:9091/api/v1/write",
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
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
            },
        ],
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "stage_path": "/tmp/staging",
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "stage_path": "/tmp/staging",
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
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
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "endpoint_url_configuration": models.CreateOutputEndpointConfiguration.URL,
        "url": "https://your-workspace.ingest.monitor.azure.com",
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
        "region": models.CreateOutputRegion.US,
        "endpoint": models.CreateOutputAISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
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
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "protocol": models.ProtocolOptions.HTTP,
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
        "realm": "us0",
        "token": "your-token",
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
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
            },
        ],
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
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "region": "us-east-1",
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
        "host": "localhost",
        "port": 9997,
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
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
            ),
        ],
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
        "queue_name": "my-queue",
        "queue_type": models.CreateOutputQueueType.STANDARD,
        "region": "us-east-1",
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
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
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
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
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
        "url": "https://endpoint1.collection.us2.sumologic.com",
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
        "host": "localhost",
        "port": 514,
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
        "host": "localhost",
        "port": 10090,
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
        "domain": "longboard",
        "token": "your-token",
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
        "url": "https://example.com/webhook",
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
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
        "container_name": "my-container",
        "stage_path": "/tmp/staging",
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
        "cluster_url": "https://mycluster.kusto.windows.net",
        "database": "mydatabase",
        "table": "mytable",
        "ingest_mode": models.IngestionMode.STREAMING,
        "oauth_endpoint": models.MicrosoftEntraIDAuthenticationEndpointOptionsSasl.HTTPS_LOGIN_MICROSOFTONLINE_COM,
        "tenant_id": "tenant-id",
        "client_id": "client-id",
        "scope": "https://mycluster.kusto.windows.net/.default",
        "oauth_type": models.OutputAzureDataExplorerAuthenticationMethod.CLIENT_SECRET,
        "client_secret": "client-secret",
        "format_": models.DataFormatOptions.JSON,
        "compress": models.CompressionOptions2.GZIP,
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
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topic": "logs",
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
        "log_type": "Cribl",
        "auth_type": models.OutputAzureLogsAuthenticationMethod.MANUAL,
        "workspace_id": "workspace-id",
        "workspace_key": "workspace-key",
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
        "region": "us",
        "log_type": "UNKNOWN",
        "gcp_project_id": "my-project",
        "gcp_instance": "customer-id",
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
        "url": "http://localhost:8123/",
        "database": "mydb",
        "table_name": "mytable",
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
        "endpoint": "https://account-id.r2.cloudflarestorage.com",
        "bucket": "my-bucket",
        "stage_path": "/tmp/staging",
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
        "log_group_name": "my-log-group",
        "log_stream_name": "my-log-stream",
        "region": "us-east-1",
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
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        topic="logs",
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
        "system_fields": [
            "cribl_pipe",
        ],
        "streamtags": [],
        "load_balanced": False,
        "tls": {
            "disabled": True,
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
        },
        "response_honor_retry_after_header": True,
        "on_backpressure": models.BackpressureBehaviorOptions.BLOCK,
        "use_round_robin_dns": True,
        "url": "https://0.0.0.0:10200",
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
        "host": "localhost",
        "port": 10090,
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
        "url": "https://ingest.us.crowdstrike.com/api/ingest/hec/connection-id/v1/services/collector",
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "token": "your-token",
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
        "workspace_id": "your-workspace-id",
        "scope": "my-scope",
        "client_id": "your-client-id",
        "catalog": "my-catalog",
        "schema_": "my-schema",
        "events_volume_name": "my-volume",
        "client_text_secret": "your-client-secret",
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
        "api_key": "your-api-key",
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "stage_path": "/tmp/staging",
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
        "auth_type": models.OutputDynatraceHTTPAuthenticationType.TOKEN,
        "format_": models.OutputDynatraceHTTPFormat.JSON_ARRAY,
        "endpoint": models.Endpoint.CLOUD,
        "telemetry_type": models.TelemetryType.LOGS,
        "token": "your-api-key",
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
        "protocol": models.OutputDynatraceOtlpProtocol.HTTP,
        "endpoint": "https://your-environment.live.dynatrace.com/api/v2/otlp",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "endpoint_type": models.EndpointType.SAAS,
        "token_secret": "your-token-secret",
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
        "index": "logs",
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
        "url": "my-cloud-id",
        "index": "logs",
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
        "bucket": "my-bucket",
        "region": "us-east1",
        "stage_path": "/tmp/staging",
        "endpoint": "https://storage.googleapis.com",
        "collector_instance_id": "11112222-3333-4444-5555-666677778888",
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
        "dest_path": "/var/log/output",
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
        "log_format_type": models.SendEventsAs.UNSTRUCTURED,
        "region": "us",
        "customer_id": "customer-id",
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
        "log_location_type": models.LogLocationType.PROJECT,
        "log_name_expression": "my-log",
        "log_location_expression": "my-project",
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
        "bucket": "my-bucket",
        "region": "us-east1",
        "endpoint": "https://storage.googleapis.com",
        "stage_path": "/tmp/staging",
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
        "topic_name": "my-topic",
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
        loki_url="https://logs-prod-us-central1.grafana.net",
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
        "protocol": models.DestinationProtocolOptions.TCP,
        "host": "localhost",
        "port": 2003,
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
        "dataset": "my-dataset",
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
        "url": "https://cloud.us.humio.com/api/v1/ingest/hec",
        "format_": models.RequestFormatOptions.JSON,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "token": "your-token",
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
        "url": "http://localhost:8086",
        "database": "mydb",
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
        brokers=[
            "localhost:9092",
        ],
        topic="logs",
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
        "stream_name": "my-stream",
        "region": "us-east-1",
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
        "url": "http://localhost:3100/loki/api/v1/push",
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
        "topic": "logs",
        "bootstrap_server": "myeventstream.servicebus.windows.net:9093",
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
        "endpoint": "http://localhost:9000",
        "bucket": "my-bucket",
        "stage_path": "/tmp/staging",
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
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topic="logs",
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        region="us-east-1",
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
        "hosts": [
            {
                "host": "localhost",
                "port": 2055,
            },
        ],
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
        "api_key": "your-api-key",
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
        "account_id": "123456",
        "event_type": "CriblEvent",
        "api_key": "your-api-key",
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
        "endpoint": "http://localhost:4317",
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
        "url": "http://localhost:9091/api/v1/write",
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
        "rules": [
            {
                "filter_": "true",
                "output": "my-output",
            },
        ],
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "stage_path": "/tmp/staging",
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
        "bucket": "my-bucket",
        "region": "us-east-1",
        "assume_role_arn": "arn:aws:iam::123456789012:role/my-role",
        "stage_path": "/tmp/staging",
        "account_id": "123456789012",
        "custom_source": "my-custom-source",
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
        "login_url": "https://login.microsoftonline.com",
        "secret": "client-secret",
        "client_id": "client-id",
        "endpoint_url_configuration": models.EndpointConfiguration.URL,
        "url": "https://your-workspace.ingest.monitor.azure.com",
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
        "region": models.Region.US,
        "endpoint": models.AISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT,
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
        "endpoint": "ingest.lightstep.com:443",
        "token_secret": "your-token-secret",
        "otlp_version": models.OtlpVersionOptions1.ONE_DOT_3_DOT_1,
        "protocol": models.ProtocolOptions.HTTP,
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
        "realm": "us0",
        "token": "your-token",
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
        "hosts": [
            {
                "host": "192.168.1.1",
                "port": 161,
            },
        ],
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
        "topic_arn": "arn:aws:sns:us-east-1:123456789012:my-topic",
        "message_group_id": "my-message-group",
        "region": "us-east-1",
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
        "host": "localhost",
        "port": 9997,
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
        hosts=[
            models.ItemsTypeHosts(
                host="localhost",
                port=9997,
            ),
        ],
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
        "queue_name": "my-queue",
        "queue_type": models.OutputSqsQueueType.STANDARD,
        "region": "us-east-1",
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
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
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
        "protocol": models.DestinationProtocolOptions.UDP,
        "host": "localhost",
        "port": 8125,
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
        "url": "https://endpoint1.collection.us2.sumologic.com",
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
        "host": "localhost",
        "port": 514,
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
        "host": "localhost",
        "port": 10090,
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
        "domain": "longboard",
        "token": "your-token",
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
        "url": "https://example.com/webhook",
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
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "wiz_connector_id": "00000000-0000-0000-0000-000000000000",
        "wiz_environment": "test",
        "data_center": "us1",
        "wiz_sourcetype": "placeholder",
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