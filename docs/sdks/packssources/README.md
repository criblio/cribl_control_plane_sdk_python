# Packs.Sources

## Overview

### Available Operations

* [list](#list) - List all Sources within a Pack
* [create](#create) - Create a Source within a Pack
* [get](#get) - Get a Source within a Pack
* [update](#update) - Update a Source within a Pack
* [delete](#delete) - Delete a Source within a Pack

## list

Get a list of all Sources within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputSystemByPack" method="get" path="/p/{pack}/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Source within the specified Pack.

### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "appscope-source",
        "type": models.CreateInputSystemByPackTypeAppscope.APPSCOPE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9109,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "azure-blob-source",
        "type": models.CreateInputSystemByPackTypeAzureBlob.AZURE_BLOB,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "azure-blob-queue",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCloudflareHec

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCloudflareHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "cloudflare-hec-source",
        "type": models.CreateInputSystemByPackTypeCloudflareHec.CLOUDFLARE_HEC,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCollection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "collection-source",
        "type": models.CreateInputSystemByPackTypeCollection.COLLECTION,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body=models.CreateInputSystemByPackInputConfluentCloud(
        id="confluent-cloud-source",
        type=models.CreateInputSystemByPackTypeConfluentCloud.CONFLUENT_CLOUD,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "cribl-http-source",
        "type": models.CreateInputSystemByPackTypeCriblHTTP.CRIBL_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblLakeHttp

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCriblLakeHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "cribl-lake-http-source",
        "type": models.CreateInputSystemByPackTypeCriblLakeHTTP.CRIBL_LAKE_HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCriblTcp

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "cribl-tcp-source",
        "type": models.CreateInputSystemByPackTypeCriblTCP.CRIBL_TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesCrowdstrike

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesCrowdstrike" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "crowdstrike-source",
        "type": models.CreateInputSystemByPackTypeCrowdstrike.CROWDSTRIKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "crowdstrike-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "datadog-agent-source",
        "type": models.CreateInputSystemByPackTypeDatadogAgent.DATADOG_AGENT,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 8126,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesDatagen

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesDatagen" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "datagen-source",
        "type": models.CreateInputSystemByPackTypeDatagen.DATAGEN,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesEdgePrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "edge-prometheus-source",
        "type": models.CreateInputSystemByPackTypeEdgePrometheus.EDGE_PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.CreateInputSystemByPackDiscoveryTypeEdgePrometheus.STATIC,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "elastic-source",
        "type": models.CreateInputSystemByPackTypeElastic.ELASTIC,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "eventhub-source",
        "type": models.CreateInputSystemByPackTypeEventhub.EVENTHUB,
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
### Example Usage: InputCreateExamplesExec

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesExec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "exec-source",
        "type": models.CreateInputSystemByPackInputExecType.EXEC,
        "send_to_routes": True,
        "pq_enabled": False,
        "command": "echo \"Hello World\"",
        "interval": 60,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFile

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "file-source",
        "type": models.CreateInputSystemByPackInputFileType.FILE,
        "send_to_routes": True,
        "pq_enabled": False,
        "mode": models.CreateInputSystemByPackInputFileMode.MANUAL,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesFirehose

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesFirehose" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "firehose-source",
        "type": models.CreateInputSystemByPackTypeFirehose.FIREHOSE,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGooglePubsub

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "google-pubsub-source",
        "type": models.CreateInputSystemByPackTypeGooglePubsub.GOOGLE_PUBSUB,
        "send_to_routes": True,
        "pq_enabled": False,
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesGrafana

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesGrafana" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "grafana-source",
        "type": models.CreateInputSystemByPackInputGrafanaType1.GRAFANA,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "http-source",
        "type": models.CreateInputSystemByPackTypeHTTP.HTTP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesHttpRaw

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesHttpRaw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "http-raw-source",
        "type": models.CreateInputSystemByPackTypeHTTPRaw.HTTP_RAW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesJournalFiles

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesJournalFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "journal-files-source",
        "type": models.CreateInputSystemByPackInputJournalFilesType.JOURNAL_FILES,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body=models.CreateInputSystemByPackInputKafka(
        id="kafka-source",
        type=models.CreateInputSystemByPackTypeKafka.KAFKA,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "kinesis-source",
        "type": models.CreateInputSystemByPackTypeKinesis.KINESIS,
        "send_to_routes": True,
        "pq_enabled": False,
        "stream_name": "my-stream",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "kube-events-source",
        "type": models.CreateInputSystemByPackTypeKubeEvents.KUBE_EVENTS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeLogs

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesKubeLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "kube-logs-source",
        "type": models.CreateInputSystemByPackTypeKubeLogs.KUBE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeMetrics

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesKubeMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "kube-metrics-source",
        "type": models.CreateInputSystemByPackTypeKubeMetrics.KUBE_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "loki-source",
        "type": models.CreateInputSystemByPackTypeLoki.LOKI,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "metrics-source",
        "type": models.CreateInputSystemByPackTypeMetrics.METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 8125,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesModelDrivenTelemetry

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesModelDrivenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "mdt-source",
        "type": models.CreateInputSystemByPackTypeModelDrivenTelemetry.MODEL_DRIVEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 57000,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesMsk

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body=models.CreateInputSystemByPackInputMsk(
        id="msk-source",
        type=models.CreateInputSystemByPackTypeMsk.MSK,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "netflow-source",
        "type": models.CreateInputSystemByPackTypeNetflow.NETFLOW,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 2055,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Mgmt

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesOffice365Mgmt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "office365-mgmt-source",
        "type": models.CreateInputSystemByPackTypeOffice365Mgmt.OFFICE365_MGMT,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesOffice365MsgTrace" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "office365-msg-trace-source",
        "type": models.CreateInputSystemByPackTypeOffice365MsgTrace.OFFICE365_MSG_TRACE,
        "send_to_routes": True,
        "pq_enabled": False,
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOffice365Service

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesOffice365Service" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "office365-service-source",
        "type": models.CreateInputSystemByPackTypeOffice365Service.OFFICE365_SERVICE,
        "send_to_routes": True,
        "pq_enabled": False,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "otel-source",
        "type": models.CreateInputSystemByPackTypeOpenTelemetry.OPEN_TELEMETRY,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 4317,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheus

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "prometheus-source",
        "type": models.CreateInputSystemByPackTypePrometheus.PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.CreateInputSystemByPackDiscoveryTypePrometheus.STATIC,
        "interval": 60,
        "log_level": models.CreateInputSystemByPackLogLevelPrometheus.INFO,
        "target_list": [
            "http://localhost:9090/metrics",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheusRw

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesPrometheusRw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "prometheus-rw-source",
        "type": models.CreateInputSystemByPackTypePrometheusRw.PROMETHEUS_RW,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesRawUdp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "raw-udp-source",
        "type": models.CreateInputSystemByPackTypeRawUDP.RAW_UDP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "s3-source",
        "type": models.CreateInputSystemByPackTypeS3.S3,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-notifications-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "s3-inventory-source",
        "type": models.CreateInputSystemByPackTypeS3Inventory.S3_INVENTORY,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "s3-inventory-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "security-lake-source",
        "type": models.CreateInputSystemByPackTypeSecurityLake.SECURITY_LAKE,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "security-lake-queue",
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "snmp-source",
        "type": models.CreateInputSystemByPackTypeSnmp.SNMP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "192.168.1.1",
        "port": 161,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunk

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "splunk-source",
        "type": models.CreateInputSystemByPackTypeSplunk.SPLUNK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 9997,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSplunkHec

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "splunk-hec-source",
        "type": models.CreateInputSystemByPackTypeSplunkHec.SPLUNK_HEC,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSplunkSearch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "splunk-search-source",
        "type": models.CreateInputSystemByPackTypeSplunkSearch.SPLUNK_SEARCH,
        "send_to_routes": True,
        "pq_enabled": False,
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "cron_schedule": "0 * * * *",
        "endpoint": "/services/search/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "sqs-source",
        "type": models.CreateInputSystemByPackTypeSqs.SQS,
        "send_to_routes": True,
        "pq_enabled": False,
        "queue_name": "my-queue",
        "queue_type": models.CreateInputSystemByPackQueueType.STANDARD,
        "region": "us-east-1",
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "syslog-source",
        "type": models.CreateInputSystemByPackInputSyslogType1.SYSLOG,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "udp_port": 514,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemMetrics

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSystemMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "system-metrics-source",
        "type": models.CreateInputSystemByPackTypeSystemMetrics.SYSTEM_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemState

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesSystemState" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "system-state-source",
        "type": models.CreateInputSystemByPackTypeSystemState.SYSTEM_STATE,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcp

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "tcp-source",
        "type": models.CreateInputSystemByPackTypeTCP.TCP,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcpjson

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "tcpjson-source",
        "type": models.CreateInputSystemByPackTypeTcpjson.TCPJSON,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10090,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWef

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesWef" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "wef-source",
        "type": models.CreateInputSystemByPackTypeWef.WEF,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 5985,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "content_format": models.CreateInputSystemByPackFormat.RENDERED_TEXT,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesWinEventLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "win-event-logs-source",
        "type": models.CreateInputSystemByPackTypeWinEventLogs.WIN_EVENT_LOGS,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesWindowsMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "windows-metrics-source",
        "type": models.CreateInputSystemByPackTypeWindowsMetrics.WINDOWS_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWiz

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesWiz" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "wiz-source",
        "type": models.CreateInputSystemByPackTypeWiz.WIZ,
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

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesWizWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "wiz-webhook-source",
        "type": models.CreateInputSystemByPackTypeWizWebhook.WIZ_WEBHOOK,
        "send_to_routes": True,
        "pq_enabled": False,
        "host": "0.0.0.0",
        "port": 10080,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesZscalerHec

<!-- UsageSnippet language="python" operationID="createInputSystemByPack" method="post" path="/p/{pack}/system/inputs" example="InputCreateExamplesZscalerHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.create(pack="<value>", request_body={
        "id": "zscaler-hec-source",
        "type": models.CreateInputSystemByPackTypeZscalerHec.ZSCALER_HEC,
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

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `pack`                                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | The <code>id</code> of the Pack to create.                                                      |
| `request_body`                                                                                  | [models.CreateInputSystemByPackRequestBody](../../models/createinputsystembypackrequestbody.md) | :heavy_check_mark:                                                                              | Input object                                                                                    |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputSystemByPackAndId" method="get" path="/p/{pack}/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to get.                           |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to get.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Source.</br></br>Provide a complete representation of the Source that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Source.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Source might not function as expected within the specified Pack.

### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCloudflareHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCollection" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "collection-source",
        "type": models.InputCollectionType.COLLECTION,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesConfluentCloud

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesConfluentCloud" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_=models.InputConfluentCloud(
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCriblHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCriblLakeHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCriblTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesCrowdstrike" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesDatagen" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesEdgePrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesElastic" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesEventhub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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
### Example Usage: InputCreateExamplesExec

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesExec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesFirehose" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesGooglePubsub" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesGrafana" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesHttp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesHttpRaw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesJournalFiles" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesKafka" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_=models.InputKafka(
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesKinesis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "kube-events-source",
        "type": models.InputKubeEventsType.KUBE_EVENTS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeLogs

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesKubeLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "kube-logs-source",
        "type": models.InputKubeLogsType.KUBE_LOGS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesKubeMetrics

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesKubeMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "kube-metrics-source",
        "type": models.InputKubeMetricsType.KUBE_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesLoki

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesLoki" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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
### Example Usage: InputCreateExamplesModelDrivenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesModelDrivenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesMsk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_=models.InputMsk(
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesNetflow" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesOffice365Mgmt" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesOffice365MsgTrace" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesOffice365Service" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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
### Example Usage: InputCreateExamplesOpenTelemetry

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesOpenTelemetry" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesPrometheus" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "prometheus-source",
        "type": models.InputPrometheusType.PROMETHEUS,
        "send_to_routes": True,
        "pq_enabled": False,
        "discovery_type": models.InputPrometheusDiscoveryType.STATIC,
        "interval": 60,
        "log_level": models.InputPrometheusLogLevel.INFO,
        "target_list": [
            "http://localhost:9090/metrics",
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesPrometheusRw

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesPrometheusRw" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesRawUdp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSplunkHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSplunkSearch" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "splunk-search-source",
        "type": models.InputSplunkSearchType.SPLUNK_SEARCH,
        "send_to_routes": True,
        "pq_enabled": False,
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "cron_schedule": "0 * * * *",
        "endpoint": "/services/search/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSqs

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSqs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSystemMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "system-metrics-source",
        "type": models.InputSystemMetricsType.SYSTEM_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesSystemState

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesSystemState" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "system-state-source",
        "type": models.InputSystemStateType.SYSTEM_STATE,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesTcp

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesTcp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesTcpjson" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesWef" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesWinEventLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesWindowsMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "windows-metrics-source",
        "type": models.InputWindowsMetricsType.WINDOWS_METRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputCreateExamplesWiz

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesWiz" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesWizWebhook" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputCreateExamplesZscalerHec" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
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

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputExamplesCribl" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "cribl-source",
        "type": models.InputCriblType.CRIBL,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```
### Example Usage: InputExamplesCriblMetrics

<!-- UsageSnippet language="python" operationID="updateInputSystemByPackAndId" method="patch" path="/p/{pack}/system/inputs/{id}" example="InputExamplesCriblMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.update(id="<id>", pack="<value>", input_={
        "id": "cribl-metrics-source",
        "type": models.InputCriblmetricsType.CRIBLMETRICS,
        "send_to_routes": True,
        "pq_enabled": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to update.                        |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to update.                          |
| `input`                                                             | [models.Input](../../models/input.md)                               | :heavy_check_mark:                                                  | Input object                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Source within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteInputSystemByPackAndId" method="delete" path="/p/{pack}/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.delete(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to delete.                        |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to delete.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |