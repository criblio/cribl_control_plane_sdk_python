# Sources

## Overview

Actions related to Sources

### Available Operations

* [list](#list) - List all Sources
* [create](#create) - Create a Source
* [get](#get) - Get a Source
* [update](#update) - Update a Source
* [delete](#delete) - Delete a Source

## list

Get a list of all Sources.

### Example Usage: InputResponseExamplesHttpSource

<!-- UsageSnippet language="python" operationID="listInput" method="get" path="/system/inputs" example="InputResponseExamplesHttpSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSplunkHecSource

<!-- UsageSnippet language="python" operationID="listInput" method="get" path="/system/inputs" example="InputResponseExamplesSplunkHecSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSyslogSource

<!-- UsageSnippet language="python" operationID="listInput" method="get" path="/system/inputs" example="InputResponseExamplesSyslogSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                      | List[*str*]                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                          | Type of Source to include in the results. Each request can include only one <code>type</code> parameter; multiple parameters per request are not supported. |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |

### Response

**[models.CountedInputResponse](../../models/countedinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Source. The system-managed provenance field (JSON <code>criblSourceProvenance</code>) must be omitted from the request body.

### Example Usage: InputCreateExamplesAnthropicCompliance

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesAnthropicCompliance" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "anthropic-compliance-source",
        "type": models.CreateInputTypeAnthropicCompliance.ANTHROPIC_COMPLIANCE,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "anthropic-api-key-secret",
        "content_config": [
            {
                "content_type": "activities",
                "content_description": "Compliance Activities",
                "enabled": True,
                "state_tracking": True,
                "state_update_expression": "__timestampExtracted !== false && {latestTime: (state.latestTime || 0) > _time ? state.latestTime : _time}",
                "state_merge_expression": "prevState.latestTime > newState.latestTime ? prevState : newState",
                "cron_schedule": "*/5 * * * *",
                "earliest": "-7d@d",
                "latest": "now",
                "job_timeout": "300",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAppleUnifiedLogs

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesAppleUnifiedLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "apple-unified-logs-source",
        "type": models.CreateInputTypeAppleUnifiedLogs.APPLE_UNIFIED_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "predicate": "subsystem == \"com.apple.security\"",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "appscope-source",
        "type": models.CreateInputTypeAppscope.APPSCOPE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9109,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "azure-blob-source",
        "type": models.CreateInputTypeAzureBlob.AZURE_BLOB,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "azure-blob-queue",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCloudflareHec

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCloudflareHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cloudflare-hec-source",
        "type": models.CreateInputTypeCloudflareHec.CLOUDFLARE_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCollection

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCollection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "collection-source",
        "type": models.CreateInputTypeCollection.COLLECTION,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputConfluentCloud(
        id="confluent-cloud-source",
        type=models.CreateInputTypeConfluentCloud.CONFLUENT_CLOUD,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-http-source",
        "type": models.CreateInputTypeCriblHTTP.CRIBL_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblLakeHttp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCriblLakeHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-lake-http-source",
        "type": models.CreateInputTypeCriblLakeHTTP.CRIBL_LAKE_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-tcp-source",
        "type": models.CreateInputTypeCriblTCP.CRIBL_TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCrowdstrike

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesCrowdstrike" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "crowdstrike-source",
        "type": models.CreateInputTypeCrowdstrike.CROWDSTRIKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "crowdstrike-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "datadog-agent-source",
        "type": models.CreateInputTypeDatadogAgent.DATADOG_AGENT,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8126,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatagen

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesDatagen" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "datagen-source",
        "type": models.CreateInputTypeDatagen.DATAGEN,
        "send_to_routes": True,
        "pq_enabled": False,
        "samples": [
            {
                "sample": "sample.json",
                "events_per_sec": 10,
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEdgePrometheus

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesEdgePrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "edge-prometheus-source",
        "type": models.CreateInputTypeEdgePrometheus.EDGE_PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.CreateInputDiscoveryTypeEdgePrometheus.STATIC,
        "interval": 60,
        "targets": [
            {
                "host": "localhost",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesElastic

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "elastic-source",
        "type": models.CreateInputTypeElastic.ELASTIC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "localhost",
        "port": 9200,
        "elastic_api": "/",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEventhub

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "eventhub-source",
        "type": models.CreateInputTypeEventhub.EVENTHUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEventhubAmqp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesEventhubAmqp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "eventhub-amqp-source",
        "type": models.CreateInputTypeEventhubAmqp.EVENTHUB_AMQP,
        "send_to_routes": True,
        "pq_enabled": False,
        "event_hub_name": "my-event-hub",
        "consumer_group": "$Default",
        "checkpointing": {
            "blob_store": {
                "container_name": "my-container",
            },
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesExec

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesExec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "exec-source",
        "type": models.CreateInputInputExecType.EXEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "command": "echo \"Hello World\"",
        "interval": 60,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFile

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "file-source",
        "type": models.CreateInputInputFileType.FILE,
        "send_to_routes": True,
        "pq_enabled": False,
        "mode": models.CreateInputInputFileMode.MANUAL,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFirehose

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesFirehose" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "firehose-source",
        "type": models.CreateInputTypeFirehose.FIREHOSE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "google-pubsub-source",
        "type": models.CreateInputTypeGooglePubsub.GOOGLE_PUBSUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGrafana

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesGrafana" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "grafana-source",
        "type": models.CreateInputInputGrafanaType1.GRAFANA,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/api/prom/push",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesHttp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "http-source",
        "type": models.CreateInputTypeHTTP.HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesHttpRaw

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesHttpRaw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "http-raw-source",
        "type": models.CreateInputTypeHTTPRaw.HTTP_RAW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesJournalFiles

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesJournalFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "journal-files-source",
        "type": models.CreateInputInputJournalFilesType.JOURNAL_FILES,
        "send_to_routes": True,
        "pq_enabled": False,
        "path": "/var/log/journal",
        "journals": [
            "system",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputKafka(
        id="kafka-source",
        type=models.CreateInputTypeKafka.KAFKA,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kinesis-source",
        "type": models.CreateInputTypeKinesis.KINESIS,
        "send_to_routes": True,
        "pq_enabled": False,
        "stream_name": "my-stream",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-events-source",
        "type": models.CreateInputTypeKubeEvents.KUBE_EVENTS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeLogs

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKubeLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-logs-source",
        "type": models.CreateInputTypeKubeLogs.KUBE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeMetrics

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKubeMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-metrics-source",
        "type": models.CreateInputTypeKubeMetrics.KUBE_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "loki-source",
        "type": models.CreateInputTypeLoki.LOKI,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "loki_api": "/loki/api/v1/push",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMetrics

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "metrics-source",
        "type": models.CreateInputTypeMetrics.METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 8125,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMicrosoftGraph

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesMicrosoftGraph" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "microsoft-graph-source",
        "type": models.CreateInputTypeMicrosoftGraph.MICROSOFT_GRAPH,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://graph.microsoft.com/v1.0/admin/exchange/tracing/messageTraces",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesModelDrivenTelemetry

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesModelDrivenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "mdt-source",
        "type": models.CreateInputTypeModelDrivenTelemetry.MODEL_DRIVEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 57000,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputMsk(
        id="msk-source",
        type=models.CreateInputTypeMsk.MSK,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        region="us-east-1",
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesNetflow

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "netflow-source",
        "type": models.CreateInputTypeNetflow.NETFLOW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 2055,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Mgmt

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOffice365Mgmt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-mgmt-source",
        "type": models.CreateInputTypeOffice365Mgmt.OFFICE365_MGMT,
        "send_to_routes": True,
        "pq_enabled": False,
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365MsgTrace

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOffice365MsgTrace" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-msg-trace-source",
        "type": models.CreateInputTypeOffice365MsgTrace.OFFICE365_MSG_TRACE,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Service

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOffice365Service" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-service-source",
        "type": models.CreateInputTypeOffice365Service.OFFICE365_SERVICE,
        "send_to_routes": True,
        "pq_enabled": False,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOkta

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOkta" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "okta-source",
        "type": models.CreateInputTypeOkta.OKTA,
        "send_to_routes": True,
        "pq_enabled": False,
        "okta_domain": "your-org",
        "text_secret": "okta-api-token-secret",
        "cron_schedule": "*/5 * * * *",
        "earliest": "-7d@d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenAI

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOpenAI" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "openai-source",
        "type": models.CreateInputTypeOpenai.OPENAI,
        "send_to_routes": True,
        "pq_enabled": False,
        "content_config": [
            {
                "disabled": False,
                "request_params": [
                    {
                        "name": "effective_at[gt]",
                        "value": "`${Math.round(Date.now()/1000 - 3600)}`",
                    },
                    {
                        "name": "limit",
                        "value": "100",
                    },
                ],
                "pagination_type": models.CreateInputPaginationType.RESPONSE_BODY,
                "pagination_attribute": [
                    "last_id",
                ],
                "pagination_last_page_expr": "has_more === false",
                "cron_schedule": "0 * * * *",
                "earliest": "-1h",
                "latest": "now",
            },
        ],
        "text_secret": "openai-api-key-secret",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenAIComplianceLogs

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOpenAIComplianceLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "openai-compliance-logs-source",
        "type": models.CreateInputTypeOpenaiComplianceLogs.OPENAI_COMPLIANCE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "openai-api-key-secret",
        "account_type": models.CreateInputAccountType.WORKSPACE,
        "cron_schedule": "*/15 * * * *",
        "earliest": "-1h",
        "latest": "now",
        "workspace_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "workspace_event_types": [
            "AUDIT_LOG",
            "AUTH_LOG",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "otel-source",
        "type": models.CreateInputTypeOpenTelemetry.OPEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 4317,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "prometheus-source",
        "type": models.CreateInputTypePrometheus.PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.CreateInputDiscoveryTypePrometheus.STATIC,
        "interval": 60,
        "log_level": models.LogLevelOptions.INFO,
        "target_list": [
            "http://localhost:9090/metrics",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheusRw

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesPrometheusRw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "prometheus-rw-source",
        "type": models.CreateInputTypePrometheusRw.PROMETHEUS_RW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/write",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesRawUdp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesRawUdp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "raw-udp-source",
        "type": models.CreateInputTypeRawUDP.RAW_UDP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "s3-source",
        "type": models.CreateInputTypeS3.S3,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-notifications-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "s3-inventory-source",
        "type": models.CreateInputTypeS3Inventory.S3_INVENTORY,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-inventory-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "security-lake-source",
        "type": models.CreateInputTypeSecurityLake.SECURITY_LAKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "security-lake-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesServiceNowTable

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesServiceNowTable" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "servicenow-table-source",
        "type": models.CreateInputTypeServicenowTable.SERVICENOW_TABLE,
        "send_to_routes": True,
        "pq_enabled": False,
        "instance": "https://example.service-now.com",
        "table_name": "incident",
        "fields": [
            "sys_id",
            "number",
            "short_description",
        ],
        "page_size": 10000,
        "cron_schedule": "0 * * * *",
        "earliest": "-1d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "snmp-source",
        "type": models.CreateInputTypeSnmp.SNMP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "192.168.1.1",
        "port": 161,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunk

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-source",
        "type": models.CreateInputTypeSplunk.SPLUNK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9997,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-hec-source",
        "type": models.CreateInputTypeSplunkHec.SPLUNK_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "splunk_hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunkSearch

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSplunkSearch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-search-source",
        "type": models.CreateInputTypeSplunkSearch.SPLUNK_SEARCH,
        "send_to_routes": True,
        "pq_enabled": False,
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "cron_schedule": "*/15 * * * *",
        "endpoint": "/services/search/v2/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
        "auth_type": models.CreateInputAuthenticationTypeSplunkSearch.BASIC,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "sqs-source",
        "type": models.CreateInputTypeSqs.SQS,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "my-queue",
        "queue_type": models.CreateInputQueueType.STANDARD,
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSysdigHec

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSysdigHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "sysdig-hec-source",
        "type": models.CreateInputTypeSysdigHec.SYSDIG_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "syslog-source",
        "type": models.CreateInputInputSyslogType1.SYSLOG,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemMetrics

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSystemMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "system-metrics-source",
        "type": models.CreateInputTypeSystemMetrics.SYSTEM_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemState

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSystemState" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "system-state-source",
        "type": models.CreateInputTypeSystemState.SYSTEM_STATE,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "tcp-source",
        "type": models.CreateInputTypeTCP.TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "tcpjson-source",
        "type": models.CreateInputTypeTcpjson.TCPJSON,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWef

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesWef" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wef-source",
        "type": models.CreateInputTypeWef.WEF,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 5985,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "content_format": models.CreateInputFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "targets": [],
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWinEventLogs

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesWinEventLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "win-event-logs-source",
        "type": models.CreateInputTypeWinEventLogs.WIN_EVENT_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "log_names": [
            "Application",
            "System",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWindowsMetrics

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesWindowsMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "windows-metrics-source",
        "type": models.CreateInputTypeWindowsMetrics.WINDOWS_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWiz

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesWiz" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wiz-source",
        "type": models.CreateInputTypeWiz.WIZ,
        "send_to_routes": True,
        "pq_enabled": False,
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "client_id": "client-id",
        "content_config": [],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWizWebhook

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesWizWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wiz-webhook-source",
        "type": models.CreateInputTypeWizWebhook.WIZ_WEBHOOK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesZscalerHec

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesZscalerHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "zscaler-hec-source",
        "type": models.CreateInputTypeZscalerHec.ZSCALER_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesHttpSource

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputResponseExamplesHttpSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "<id>",
        "type": models.CreateInputTypeCrowdstrike.CROWDSTRIKE,
        "queue_name": "<value>",
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSplunkHecSource

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputResponseExamplesSplunkHecSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "<id>",
        "type": models.CreateInputTypeRawUDP.RAW_UDP,
        "host": "lumbering-doubter.net",
        "port": 7847.75,
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSyslogSource

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputResponseExamplesSyslogSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "<id>",
        "type": models.CreateInputTypeWiz.WIZ,
        "endpoint": "<value>",
        "auth_url": "https://hungry-crest.net/",
        "client_id": "<id>",
        "content_config": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateInputRequest](../../models/createinputrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInputResponse](../../models/countedinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Source.

### Example Usage: InputResponseExamplesHttpSource

<!-- UsageSnippet language="python" operationID="getInputById" method="get" path="/system/inputs/{id}" example="InputResponseExamplesHttpSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.get(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSplunkHecSource

<!-- UsageSnippet language="python" operationID="getInputById" method="get" path="/system/inputs/{id}" example="InputResponseExamplesSplunkHecSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.get(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSyslogSource

<!-- UsageSnippet language="python" operationID="getInputById" method="get" path="/system/inputs/{id}" example="InputResponseExamplesSyslogSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to get.                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInputResponse](../../models/countedinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Source.<br/><br/>Provide a complete representation of the Source that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Source.<br/><br/>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Source might not function as expected.<br/><br/>Cribl preserves <code>criblSourceProvenance</code> when you omit it from the request body, and you cannot overwrite it through this endpoint.

### Example Usage: InputCreateExamplesAnthropicCompliance

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesAnthropicCompliance" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "anthropic-compliance-source",
        "type": models.InputAnthropicComplianceType.ANTHROPIC_COMPLIANCE,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "anthropic-api-key-secret",
        "content_config": [
            {
                "content_type": "activities",
                "content_description": "Compliance Activities",
                "enabled": True,
                "state_tracking": True,
                "state_update_expression": "__timestampExtracted !== false && {latestTime: (state.latestTime || 0) > _time ? state.latestTime : _time}",
                "state_merge_expression": "prevState.latestTime > newState.latestTime ? prevState : newState",
                "cron_schedule": "*/5 * * * *",
                "earliest": "-7d@d",
                "latest": "now",
                "job_timeout": "300",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAppleUnifiedLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesAppleUnifiedLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "apple-unified-logs-source",
        "type": models.InputAppleUnifiedLogsType.APPLE_UNIFIED_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "predicate": "subsystem == \"com.apple.security\"",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "appscope-source",
        "type": models.InputAppscopeType.APPSCOPE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9109,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "azure-blob-source",
        "type": models.InputAzureBlobType.AZURE_BLOB,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "azure-blob-queue",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCloudflareHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCloudflareHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cloudflare-hec-source",
        "type": models.InputCloudflareHecType.CLOUDFLARE_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCollection

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCollection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "collection-source",
        "type": models.InputCollectionType.COLLECTION,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputConfluentCloudInput(
        id="confluent-cloud-source",
        type=models.InputConfluentCloudType.CONFLUENT_CLOUD,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-http-source",
        "type": models.InputCriblHTTPType.CRIBL_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblLakeHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCriblLakeHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-lake-http-source",
        "type": models.InputCriblLakeHTTPType.CRIBL_LAKE_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-tcp-source",
        "type": models.InputCriblTCPType.CRIBL_TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCrowdstrike

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesCrowdstrike" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "crowdstrike-source",
        "type": models.InputCrowdstrikeType.CROWDSTRIKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "crowdstrike-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datadog-agent-source",
        "type": models.InputDatadogAgentType.DATADOG_AGENT,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8126,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatagen

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesDatagen" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datagen-source",
        "type": models.InputDatagenType.DATAGEN,
        "send_to_routes": True,
        "pq_enabled": False,
        "samples": [
            {
                "sample": "sample.json",
                "events_per_sec": 10,
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEdgePrometheus

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesEdgePrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "edge-prometheus-source",
        "type": models.InputEdgePrometheusType.EDGE_PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.InputEdgePrometheusDiscoveryType.STATIC,
        "interval": 60,
        "targets": [
            {
                "host": "localhost",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesElastic

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "elastic-source",
        "type": models.InputElasticType.ELASTIC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "localhost",
        "port": 9200,
        "elastic_api": "/",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEventhub

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "eventhub-source",
        "type": models.InputEventhubType.EVENTHUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesEventhubAmqp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesEventhubAmqp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "eventhub-amqp-source",
        "type": models.InputEventhubAmqpType.EVENTHUB_AMQP,
        "send_to_routes": True,
        "pq_enabled": False,
        "event_hub_name": "my-event-hub",
        "consumer_group": "$Default",
        "checkpointing": {
            "blob_store": {
                "container_name": "my-container",
            },
        },
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesExec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesExec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "exec-source",
        "type": models.InputExecType.EXEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "command": "echo \"Hello World\"",
        "interval": 60,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFile

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "file-source",
        "type": models.InputFileType.FILE,
        "send_to_routes": True,
        "pq_enabled": False,
        "mode": models.InputFileMode.MANUAL,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFirehose

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesFirehose" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "firehose-source",
        "type": models.InputFirehoseType.FIREHOSE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "google-pubsub-source",
        "type": models.InputGooglePubsubType.GOOGLE_PUBSUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGrafana

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesGrafana" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "grafana-source",
        "type": models.InputGrafanaType1.GRAFANA,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/api/prom/push",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-source",
        "type": models.InputHTTPType.HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesHttpRaw

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesHttpRaw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-raw-source",
        "type": models.InputHTTPRawType.HTTP_RAW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesJournalFiles

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesJournalFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "journal-files-source",
        "type": models.InputJournalFilesType.JOURNAL_FILES,
        "send_to_routes": True,
        "pq_enabled": False,
        "path": "/var/log/journal",
        "journals": [
            "system",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKafka

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputKafkaInput(
        id="kafka-source",
        type=models.InputKafkaType.KAFKA,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKinesis

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kinesis-source",
        "type": models.InputKinesisType.KINESIS,
        "send_to_routes": True,
        "pq_enabled": False,
        "stream_name": "my-stream",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-events-source",
        "type": models.InputKubeEventsType.KUBE_EVENTS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKubeLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-logs-source",
        "type": models.InputKubeLogsType.KUBE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKubeMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-metrics-source",
        "type": models.InputKubeMetricsType.KUBE_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "loki-source",
        "type": models.InputLokiType.LOKI,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "loki_api": "/loki/api/v1/push",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "metrics-source",
        "type": models.InputMetricsType.METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 8125,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMicrosoftGraph

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesMicrosoftGraph" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "microsoft-graph-source",
        "type": models.InputMicrosoftGraphType.MICROSOFT_GRAPH,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://graph.microsoft.com/v1.0/admin/exchange/tracing/messageTraces",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesModelDrivenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesModelDrivenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "mdt-source",
        "type": models.InputModelDrivenTelemetryType.MODEL_DRIVEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 57000,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputMskInput(
        id="msk-source",
        type=models.InputMskType.MSK,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        region="us-east-1",
    ))

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesNetflow

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "netflow-source",
        "type": models.InputNetflowType.NETFLOW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 2055,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Mgmt

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOffice365Mgmt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-mgmt-source",
        "type": models.InputOffice365MgmtType.OFFICE365_MGMT,
        "send_to_routes": True,
        "pq_enabled": False,
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365MsgTrace

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOffice365MsgTrace" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-msg-trace-source",
        "type": models.InputOffice365MsgTraceType.OFFICE365_MSG_TRACE,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Service

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOffice365Service" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-service-source",
        "type": models.InputOffice365ServiceType.OFFICE365_SERVICE,
        "send_to_routes": True,
        "pq_enabled": False,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOkta

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOkta" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "okta-source",
        "type": models.InputOktaType.OKTA,
        "send_to_routes": True,
        "pq_enabled": False,
        "okta_domain": "your-org",
        "text_secret": "okta-api-token-secret",
        "cron_schedule": "*/5 * * * *",
        "earliest": "-7d@d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenAI

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOpenAI" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "openai-source",
        "type": models.InputOpenaiType.OPENAI,
        "send_to_routes": True,
        "pq_enabled": False,
        "content_config": [
            {
                "disabled": False,
                "request_params": [
                    {
                        "name": "effective_at[gt]",
                        "value": "`${Math.round(Date.now()/1000 - 3600)}`",
                    },
                    {
                        "name": "limit",
                        "value": "100",
                    },
                ],
                "pagination_type": models.InputOpenaiPaginationType.RESPONSE_BODY,
                "pagination_attribute": [
                    "last_id",
                ],
                "pagination_last_page_expr": "has_more === false",
                "cron_schedule": "0 * * * *",
                "earliest": "-1h",
                "latest": "now",
            },
        ],
        "text_secret": "openai-api-key-secret",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenAIComplianceLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOpenAIComplianceLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "openai-compliance-logs-source",
        "type": models.InputOpenaiComplianceLogsType.OPENAI_COMPLIANCE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "openai-api-key-secret",
        "account_type": models.InputOpenaiComplianceLogsAccountType.WORKSPACE,
        "cron_schedule": "*/15 * * * *",
        "earliest": "-1h",
        "latest": "now",
        "workspace_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "workspace_event_types": [
            "AUDIT_LOG",
            "AUTH_LOG",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "otel-source",
        "type": models.InputOpenTelemetryType.OPEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 4317,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-source",
        "type": models.InputPrometheusType.PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.InputPrometheusDiscoveryType.STATIC,
        "interval": 60,
        "log_level": models.LogLevelOptions.INFO,
        "target_list": [
            "http://localhost:9090/metrics",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheusRw

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesPrometheusRw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-rw-source",
        "type": models.InputPrometheusRwType.PROMETHEUS_RW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/write",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesRawUdp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesRawUdp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "raw-udp-source",
        "type": models.InputRawUDPType.RAW_UDP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-source",
        "type": models.InputS3Type.S3,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-notifications-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-inventory-source",
        "type": models.InputS3InventoryType.S3_INVENTORY,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-inventory-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "security-lake-source",
        "type": models.InputSecurityLakeType.SECURITY_LAKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "security-lake-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesServiceNowTable

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesServiceNowTable" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "servicenow-table-source",
        "type": models.InputServicenowTableType.SERVICENOW_TABLE,
        "send_to_routes": True,
        "pq_enabled": False,
        "instance": "https://example.service-now.com",
        "table_name": "incident",
        "fields": [
            "sys_id",
            "number",
            "short_description",
        ],
        "page_size": 10000,
        "cron_schedule": "0 * * * *",
        "earliest": "-1d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "snmp-source",
        "type": models.InputSnmpType.SNMP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "192.168.1.1",
        "port": 161,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-source",
        "type": models.InputSplunkType.SPLUNK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9997,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-hec-source",
        "type": models.InputSplunkHecType.SPLUNK_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "splunk_hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunkSearch

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSplunkSearch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-search-source",
        "type": models.InputSplunkSearchType.SPLUNK_SEARCH,
        "send_to_routes": True,
        "pq_enabled": False,
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "cron_schedule": "*/15 * * * *",
        "endpoint": "/services/search/v2/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
        "auth_type": models.InputSplunkSearchAuthenticationType.BASIC,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "sqs-source",
        "type": models.InputSqsType.SQS,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "my-queue",
        "queue_type": models.InputSqsQueueType.STANDARD,
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "syslog-source",
        "type": models.InputSyslogType1.SYSLOG,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSystemMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-metrics-source",
        "type": models.InputSystemMetricsType.SYSTEM_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemState

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSystemState" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-state-source",
        "type": models.InputSystemStateType.SYSTEM_STATE,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcp-source",
        "type": models.InputTCPType.TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcpjson-source",
        "type": models.InputTcpjsonType.TCPJSON,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWef

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesWef" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wef-source",
        "type": models.InputWefType.WEF,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 5985,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "content_format": models.InputWefFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "targets": [],
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWinEventLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesWinEventLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "win-event-logs-source",
        "type": models.InputWinEventLogsType.WIN_EVENT_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "log_names": [
            "Application",
            "System",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWindowsMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesWindowsMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "windows-metrics-source",
        "type": models.InputWindowsMetricsType.WINDOWS_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWiz

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesWiz" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-source",
        "type": models.InputWizType.WIZ,
        "send_to_routes": True,
        "pq_enabled": False,
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "client_id": "client-id",
        "content_config": [],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWizWebhook

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesWizWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-webhook-source",
        "type": models.InputWizWebhookType.WIZ_WEBHOOK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesZscalerHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesZscalerHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "zscaler-hec-source",
        "type": models.InputZscalerHecType.ZSCALER_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: InputExamplesCribl

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputExamplesCribl" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-source",
        "type": models.InputCriblType.CRIBL,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputExamplesCriblMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputExamplesCriblMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-metrics-source",
        "type": models.InputCriblmetricsType.CRIBLMETRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesHttpSource

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputResponseExamplesHttpSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "type": models.InputCriblType.CRIBL,
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSplunkHecSource

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputResponseExamplesSplunkHecSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "type": models.InputWizType.WIZ,
        "endpoint": "<value>",
        "auth_url": "https://grouchy-invite.info",
        "client_id": "<id>",
        "content_config": [],
    })

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSyslogSource

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputResponseExamplesSyslogSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "type": models.InputDatadogAgentType.DATADOG_AGENT,
        "host": "focused-invite.org",
        "port": 4085.76,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesAnthropicCompliance

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesAnthropicCompliance" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "anthropic-compliance-source",
        "type": models.InputAnthropicComplianceType.ANTHROPIC_COMPLIANCE,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "anthropic-api-key-secret",
        "content_config": [
            {
                "content_type": "activities",
                "content_description": "Compliance Activities",
                "enabled": True,
                "state_tracking": True,
                "state_update_expression": "__timestampExtracted !== false && {latestTime: (state.latestTime || 0) > _time ? state.latestTime : _time}",
                "state_merge_expression": "prevState.latestTime > newState.latestTime ? prevState : newState",
                "cron_schedule": "*/5 * * * *",
                "earliest": "-7d@d",
                "latest": "now",
                "job_timeout": "300",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesAppleUnifiedLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesAppleUnifiedLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "apple-unified-logs-source",
        "type": models.InputAppleUnifiedLogsType.APPLE_UNIFIED_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "predicate": "subsystem == \"com.apple.security\"",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesAppscope

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "appscope-source",
        "type": models.InputAppscopeType.APPSCOPE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9109,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "azure-blob-source",
        "type": models.InputAzureBlobType.AZURE_BLOB,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "azure-blob-queue",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCloudflareHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCloudflareHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cloudflare-hec-source",
        "type": models.InputCloudflareHecType.CLOUDFLARE_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCollection

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCollection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "collection-source",
        "type": models.InputCollectionType.COLLECTION,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputConfluentCloudInput(
        id="confluent-cloud-source",
        type=models.InputConfluentCloudType.CONFLUENT_CLOUD,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "pkc-xxxxx.us-east-1.aws.confluent.cloud:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCribl

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCribl" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-source",
        "type": models.InputCriblType.CRIBL,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCriblHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-http-source",
        "type": models.InputCriblHTTPType.CRIBL_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCriblLakeHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCriblLakeHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-lake-http-source",
        "type": models.InputCriblLakeHTTPType.CRIBL_LAKE_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCriblMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCriblMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-metrics-source",
        "type": models.InputCriblmetricsType.CRIBLMETRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-tcp-source",
        "type": models.InputCriblTCPType.CRIBL_TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesCrowdstrike

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesCrowdstrike" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "crowdstrike-source",
        "type": models.InputCrowdstrikeType.CROWDSTRIKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "crowdstrike-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datadog-agent-source",
        "type": models.InputDatadogAgentType.DATADOG_AGENT,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8126,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesDatagen

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesDatagen" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datagen-source",
        "type": models.InputDatagenType.DATAGEN,
        "send_to_routes": True,
        "pq_enabled": False,
        "samples": [
            {
                "sample": "sample.json",
                "events_per_sec": 10,
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesEdgePrometheus

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesEdgePrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "edge-prometheus-source",
        "type": models.InputEdgePrometheusType.EDGE_PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.InputEdgePrometheusDiscoveryType.STATIC,
        "interval": 60,
        "targets": [
            {
                "host": "localhost",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesElastic

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "elastic-source",
        "type": models.InputElasticType.ELASTIC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "localhost",
        "port": 9200,
        "elastic_api": "/",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesEventhub

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "eventhub-source",
        "type": models.InputEventhubType.EVENTHUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesEventhubAmqp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesEventhubAmqp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "eventhub-amqp-source",
        "type": models.InputEventhubAmqpType.EVENTHUB_AMQP,
        "send_to_routes": True,
        "pq_enabled": False,
        "event_hub_name": "my-event-hub",
        "consumer_group": "$Default",
        "checkpointing": {
            "blob_store": {
                "container_name": "my-container",
            },
        },
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesExec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesExec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "exec-source",
        "type": models.InputExecType.EXEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "command": "echo \"Hello World\"",
        "interval": 60,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesFile

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "file-source",
        "type": models.InputFileType.FILE,
        "send_to_routes": True,
        "pq_enabled": False,
        "mode": models.InputFileMode.MANUAL,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesFirehose

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesFirehose" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "firehose-source",
        "type": models.InputFirehoseType.FIREHOSE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "google-pubsub-source",
        "type": models.InputGooglePubsubType.GOOGLE_PUBSUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesGrafana

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesGrafana" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "grafana-source",
        "type": models.InputGrafanaType1.GRAFANA,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/api/prom/push",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesHttp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-source",
        "type": models.InputHTTPType.HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesHttpRaw

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesHttpRaw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-raw-source",
        "type": models.InputHTTPRawType.HTTP_RAW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesJournalFiles

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesJournalFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "journal-files-source",
        "type": models.InputJournalFilesType.JOURNAL_FILES,
        "send_to_routes": True,
        "pq_enabled": False,
        "path": "/var/log/journal",
        "journals": [
            "system",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesKafka

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputKafkaInput(
        id="kafka-source",
        type=models.InputKafkaType.KAFKA,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesKinesis

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kinesis-source",
        "type": models.InputKinesisType.KINESIS,
        "send_to_routes": True,
        "pq_enabled": False,
        "stream_name": "my-stream",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-events-source",
        "type": models.InputKubeEventsType.KUBE_EVENTS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesKubeLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesKubeLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-logs-source",
        "type": models.InputKubeLogsType.KUBE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesKubeMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesKubeMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-metrics-source",
        "type": models.InputKubeMetricsType.KUBE_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesLoki

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "loki-source",
        "type": models.InputLokiType.LOKI,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "loki_api": "/loki/api/v1/push",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "metrics-source",
        "type": models.InputMetricsType.METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 8125,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesMicrosoftGraph

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesMicrosoftGraph" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "microsoft-graph-source",
        "type": models.InputMicrosoftGraphType.MICROSOFT_GRAPH,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://graph.microsoft.com/v1.0/admin/exchange/tracing/messageTraces",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesModelDrivenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesModelDrivenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "mdt-source",
        "type": models.InputModelDrivenTelemetryType.MODEL_DRIVEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 57000,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesMsk

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputMskInput(
        id="msk-source",
        type=models.InputMskType.MSK,
        send_to_routes=True,
        pq_enabled=False,
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        region="us-east-1",
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesNetflow

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "netflow-source",
        "type": models.InputNetflowType.NETFLOW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 2055,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOffice365Mgmt

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOffice365Mgmt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-mgmt-source",
        "type": models.InputOffice365MgmtType.OFFICE365_MGMT,
        "send_to_routes": True,
        "pq_enabled": False,
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOffice365MsgTrace

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOffice365MsgTrace" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-msg-trace-source",
        "type": models.InputOffice365MsgTraceType.OFFICE365_MSG_TRACE,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOffice365Service

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOffice365Service" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-service-source",
        "type": models.InputOffice365ServiceType.OFFICE365_SERVICE,
        "send_to_routes": True,
        "pq_enabled": False,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOkta

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOkta" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "okta-source",
        "type": models.InputOktaType.OKTA,
        "send_to_routes": True,
        "pq_enabled": False,
        "okta_domain": "your-org",
        "text_secret": "okta-api-token-secret",
        "cron_schedule": "*/5 * * * *",
        "earliest": "-7d@d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOpenAI

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOpenAI" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "openai-source",
        "type": models.InputOpenaiType.OPENAI,
        "send_to_routes": True,
        "pq_enabled": False,
        "content_config": [
            {
                "disabled": False,
                "request_params": [
                    {
                        "name": "effective_at[gt]",
                        "value": "`${Math.round(Date.now()/1000 - 3600)}`",
                    },
                    {
                        "name": "limit",
                        "value": "100",
                    },
                ],
                "pagination_type": models.InputOpenaiPaginationType.RESPONSE_BODY,
                "pagination_attribute": [
                    "last_id",
                ],
                "pagination_last_page_expr": "has_more === false",
                "cron_schedule": "0 * * * *",
                "earliest": "-1h",
                "latest": "now",
            },
        ],
        "text_secret": "openai-api-key-secret",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOpenAIComplianceLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOpenAIComplianceLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "openai-compliance-logs-source",
        "type": models.InputOpenaiComplianceLogsType.OPENAI_COMPLIANCE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "text_secret": "openai-api-key-secret",
        "account_type": models.InputOpenaiComplianceLogsAccountType.WORKSPACE,
        "cron_schedule": "*/15 * * * *",
        "earliest": "-1h",
        "latest": "now",
        "workspace_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "workspace_event_types": [
            "AUDIT_LOG",
            "AUTH_LOG",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "otel-source",
        "type": models.InputOpenTelemetryType.OPEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 4317,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesPrometheus

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-source",
        "type": models.InputPrometheusType.PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.InputPrometheusDiscoveryType.STATIC,
        "interval": 60,
        "log_level": models.LogLevelOptions.INFO,
        "target_list": [
            "http://localhost:9090/metrics",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesPrometheusRw

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesPrometheusRw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-rw-source",
        "type": models.InputPrometheusRwType.PROMETHEUS_RW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
        "prometheus_api": "/write",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesRawUdp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesRawUdp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "raw-udp-source",
        "type": models.InputRawUDPType.RAW_UDP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesS3

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-source",
        "type": models.InputS3Type.S3,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-notifications-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-inventory-source",
        "type": models.InputS3InventoryType.S3_INVENTORY,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-inventory-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "security-lake-source",
        "type": models.InputSecurityLakeType.SECURITY_LAKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "security-lake-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesServiceNowTable

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesServiceNowTable" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "servicenow-table-source",
        "type": models.InputServicenowTableType.SERVICENOW_TABLE,
        "send_to_routes": True,
        "pq_enabled": False,
        "instance": "https://example.service-now.com",
        "table_name": "incident",
        "fields": [
            "sys_id",
            "number",
            "short_description",
        ],
        "page_size": 10000,
        "cron_schedule": "0 * * * *",
        "earliest": "-1d",
        "latest": "now",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSnmp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "snmp-source",
        "type": models.InputSnmpType.SNMP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "192.168.1.1",
        "port": 161,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-source",
        "type": models.InputSplunkType.SPLUNK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9997,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-hec-source",
        "type": models.InputSplunkHecType.SPLUNK_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "splunk_hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSplunkSearch

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSplunkSearch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-search-source",
        "type": models.InputSplunkSearchType.SPLUNK_SEARCH,
        "send_to_routes": True,
        "pq_enabled": False,
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "cron_schedule": "*/15 * * * *",
        "endpoint": "/services/search/v2/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
        "auth_type": models.InputSplunkSearchAuthenticationType.BASIC,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSqs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "sqs-source",
        "type": models.InputSqsType.SQS,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "my-queue",
        "queue_type": models.InputSqsQueueType.STANDARD,
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSysdigHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSysdigHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "sysdig-hec-source",
        "type": models.InputSysdigHecType.SYSDIG_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSyslog

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "syslog-source",
        "type": models.InputSyslogType1.SYSLOG,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSystemMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSystemMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-metrics-source",
        "type": models.InputSystemMetricsType.SYSTEM_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesSystemState

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesSystemState" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-state-source",
        "type": models.InputSystemStateType.SYSTEM_STATE,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesTcp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcp-source",
        "type": models.InputTCPType.TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesTcpjson

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcpjson-source",
        "type": models.InputTcpjsonType.TCPJSON,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesWef

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesWef" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wef-source",
        "type": models.InputWefType.WEF,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 5985,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "content_format": models.InputWefFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "targets": [],
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesWinEventLogs

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesWinEventLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "win-event-logs-source",
        "type": models.InputWinEventLogsType.WIN_EVENT_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
        "log_names": [
            "Application",
            "System",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesWindowsMetrics

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesWindowsMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "windows-metrics-source",
        "type": models.InputWindowsMetricsType.WINDOWS_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesWiz

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesWiz" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-source",
        "type": models.InputWizType.WIZ,
        "send_to_routes": True,
        "pq_enabled": False,
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "client_id": "client-id",
        "content_config": [],
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesWizWebhook

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesWizWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-webhook-source",
        "type": models.InputWizWebhookType.WIZ_WEBHOOK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateInputExamplesZscalerHec

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="UpdateInputExamplesZscalerHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "zscaler-hec-source",
        "type": models.InputZscalerHecType.ZSCALER_HEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8088,
        "hec_api": "/services/collector",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to update.                        |
| `input`                                                             | [models.Input](../../models/input.md)                               | :heavy_check_mark:                                                  | Input object.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInputResponse](../../models/countedinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Source.

### Example Usage: InputResponseExamplesHttpSource

<!-- UsageSnippet language="python" operationID="deleteInputById" method="delete" path="/system/inputs/{id}" example="InputResponseExamplesHttpSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.delete(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSplunkHecSource

<!-- UsageSnippet language="python" operationID="deleteInputById" method="delete" path="/system/inputs/{id}" example="InputResponseExamplesSplunkHecSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.delete(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: InputResponseExamplesSyslogSource

<!-- UsageSnippet language="python" operationID="deleteInputById" method="delete" path="/system/inputs/{id}" example="InputResponseExamplesSyslogSource" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to delete.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInputResponse](../../models/countedinputresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |