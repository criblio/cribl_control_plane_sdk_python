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

### Example Usage

<!-- UsageSnippet language="python" operationID="listInput" method="get" path="/system/inputs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Source.

### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "appscope-source",
        "type": models.CreateInputTypeAppscope.APPSCOPE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://drab-scrap.info/",
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/appscope",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "if deserted boohoo red chops excepting know stay bah",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "unix_socket_path": "$CRIBL_HOME/state/appscope.sock",
        "unix_socket_perms": "<value>",
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "azure-blob-source",
        "type": models.CreateInputTypeAzureBlob.AZURE_BLOB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "/.*/",
        "visibility_timeout": 600,
        "num_receivers": 1,
        "max_messages": 1,
        "service_period_secs": 5,
        "skip_on_error": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "description": "while brisk meanwhile kaleidoscopic ack ah above psst throughout guide",
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
        "template_queue_name": "<value>",
        "template_connection_string": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cloudflare-hec-source",
        "type": models.CreateInputTypeCloudflareHec.CLOUDFLARE_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.CreateInputAuthenticationMethodCloudflareHec.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "aha hydrocarbon after plain",
                "allowed_indexes_at_token": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
            "<value 2>",
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "emit_token_metrics": False,
        "description": "hateful pike whose or interestingly exotic",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "collection-source",
        "type": models.CreateInputTypeCollection.COLLECTION,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "throttle_rate_per_sec": "0",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "output": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputConfluentCloud(
        id="confluent-cloud-source",
        type=models.CreateInputTypeConfluentCloud.CONFLUENT_CLOUD,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
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
            username="Monte_Thiel32",
            password="KI_orHyojtOdRdG",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://dependable-pulse.net",
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
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        auto_commit_interval=4914.59,
        auto_commit_threshold=5168.01,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="comfortable whole veto certainly",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-http-source",
        "type": models.CreateInputTypeCriblHTTP.CRIBL_HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "weary likewise meh stoop upwardly amount violently throughout upwardly bathrobe",
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "fledgling although substantial mmm but what immaculate hmph",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-lake-http-source",
        "type": models.CreateInputTypeCriblLakeHTTP.CRIBL_LAKE_HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "cribl_api": "/cribl",
        "elastic_api": "/elastic",
        "splunk_hec_api": "/services/collector",
        "splunk_hec_acks": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "goat thorough like",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "splunk_hec_metadata": {
                    "enabled": True,
                    "default_dataset": "<value>",
                    "allowed_indexes_at_token": [
                        "<value 1>",
                        "<value 2>",
                    ],
                },
                "elasticsearch_metadata": {
                    "enabled": False,
                    "default_dataset": "<value>",
                },
            },
        ],
        "description": "out regarding until pull avow hunt",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "cribl-tcp-source",
        "type": models.CreateInputTypeCriblTCP.CRIBL_TCP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": False,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "easily bah hierarchy truthfully how brr victoriously",
            },
        ],
        "description": "whenever cheerfully average lovingly meh heartfelt leading scratchy make",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "crowdstrike-source",
        "type": models.CreateInputTypeCrowdstrike.CROWDSTRIKE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 21600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "description": "aha wherever tooth ack",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.FALSE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "datadog-agent-source",
        "type": models.CreateInputTypeDatadogAgent.DATADOG_AGENT,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "extract_metrics": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "proxy_mode": {
            "enabled": False,
            "reject_unauthorized": True,
        },
        "description": "meanwhile trusting scrutinise except settle",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "datagen-source",
        "type": models.CreateInputTypeDatagen.DATAGEN,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "samples": [
            {
                "sample": "sample.json",
                "events_per_sec": 10,
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "quiet indeed arrogantly circumnavigate greedily wheel",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "edge-prometheus-source",
        "type": models.CreateInputTypeEdgePrometheus.EDGE_PROMETHEUS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "discovery_type": models.CreateInputDiscoveryTypeEdgePrometheus.STATIC,
        "interval": 60,
        "timeout": 5000,
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.CreateInputAuthenticationMethodEdgePrometheus.MANUAL,
        "description": "geez however knight ah whenever bulky throughout troubled although daintily",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTP,
                "host": "localhost",
                "port": 9090,
                "path": "/metrics",
            },
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 9090,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "scrape_protocol": models.ProtocolOptionsTargetsItems.HTTP,
        "scrape_path": "/metrics",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": True,
        "search_filter": [
            {
                "name": "<value>",
                "values": [],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "scrape_protocol_expr": "metadata.annotations['prometheus.io/scheme'] || 'http'",
        "scrape_port_expr": "metadata.annotations['prometheus.io/port'] || 9090",
        "scrape_path_expr": "metadata.annotations['prometheus.io/path'] || '/metrics'",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "stay strictly under including corner ick hearten",
            },
        ],
        "username": "Hadley97",
        "password": "Hkq7Phu4rXHsZ3j",
        "credentials_secret": "<value>",
        "template_aws_api_key": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "elastic-source",
        "type": models.CreateInputTypeElastic.ELASTIC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "elastic_api": "/",
        "auth_type": models.CreateInputAuthenticationTypeElastic.NONE,
        "api_version": models.CreateInputAPIVersion.EIGHT_DOT_3_DOT_2,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "proxy_mode": {
            "enabled": False,
            "auth_type": models.CreateInputAuthenticationMethodElastic.NONE,
            "username": "Kathryn_Senger78",
            "password": "WPXuh03pB0ItRx8",
            "credentials_secret": "<value>",
            "url": "https://likely-abacus.info",
            "reject_unauthorized": False,
            "remove_headers": [
                "<value 1>",
            ],
            "timeout_sec": 60,
            "template_url": "https://amused-glider.biz",
        },
        "description": "passionate gratefully usually miserably uh-huh",
        "username": "Caterina_McClure27",
        "password": "5FvvRdikRVomwpo",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
        ],
        "custom_api_version": "{\n    \"name\": \"AzU84iL\",\n    \"cluster_name\": \"cribl\",\n    \"cluster_uuid\": \"Js6_Z2VKS3KbfRSxPmPbaw\",\n    \"version\": {\n        \"number\": \"8.3.2\",\n        \"build_type\": \"tar\",\n        \"build_hash\": \"bca0c8d\",\n        \"build_date\": \"2019-10-16T06:19:49.319352Z\",\n        \"build_snapshot\": false,\n        \"lucene_version\": \"9.7.2\",\n        \"minimum_wire_compatibility_version\": \"7.17.0\",\n        \"minimum_index_compatibility_version\": \"7.0.0\"\n    },\n    \"tagline\": \"You Know, for Search\"\n}",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "eventhub-source",
        "type": models.CreateInputTypeEventhub.EVENTHUB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
        "group_id": "Cribl",
        "from_beginning": True,
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
            "password": "rkhgMwb5YCBiRV0",
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
        "session_timeout": 30000,
        "rebalance_timeout": 60000,
        "heartbeat_interval": 3000,
        "auto_commit_interval": 7747.29,
        "auto_commit_threshold": 9425.98,
        "max_bytes_per_partition": 1048576,
        "max_bytes": 10485760,
        "max_socket_errors": 0,
        "minimize_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "nerve inside gerbil orient yowza maroon ha",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "exec-source",
        "type": models.CreateInputInputExecType.EXEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 10,
        "schedule_type": models.CreateInputScheduleType.INTERVAL,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "hence after waft whoa a oof robust",
        "interval": 60,
        "cron_schedule": "* * * * *",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "file-source",
        "type": models.CreateInputInputFileType.FILE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "mode": models.CreateInputInputFileMode.MANUAL,
        "interval": 10,
        "filenames": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "filter_archived_files": False,
        "tail_only": True,
        "idle_timeout": 300,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": False,
        "force_text": False,
        "hash_len": 256,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "description": "oh whoa entice when phooey address",
        "path": "/usr/local/src",
        "depth": 9351.84,
        "suppress_missing_path_errors": False,
        "delete_files": False,
        "salt_hash": False,
        "include_unidentifiable_binary": False,
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "firehose-source",
        "type": models.CreateInputTypeFirehose.FIREHOSE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "though instead talkative mid eek deadly these",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "google-pubsub-source",
        "type": models.CreateInputTypeGooglePubsub.GOOGLE_PUBSUB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
        "monitor_subscription": False,
        "create_topic": False,
        "create_subscription": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_backlog": 1000,
        "concurrency": 5,
        "request_timeout": 60000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "mortise yowza clearly er yippee taxicab never onto nor singe",
        "ordered_delivery": False,
        "template_topic_name": "<value>",
        "template_subscription_name": "<value>",
        "template_region": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "grafana-source",
        "type": models.CreateInputInputGrafanaType1.GRAFANA,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "prometheus_api": "/api/prom/push",
        "loki_api": "/loki/api/v1/push",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
            "username": "Salvador1",
            "password": "ZQk_l_P10FR08Qf",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
            "username": "Philip50",
            "password": "IKe8kW3jPl5Tei7",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "fooey after properly often charlatan",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "http-source",
        "type": models.CreateInputTypeHTTP.HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "cribl_api": "/cribl",
        "elastic_api": "/elastic",
        "splunk_hec_api": "/services/collector",
        "splunk_hec_acks": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "though transplant dreary sweetly which",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "calmly ethyl scramble thick formamide a unfortunately",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "http-raw-source",
        "type": models.CreateInputTypeHTTPRaw.HTTP_RAW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_paths": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "allowed_methods": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "since reconsideration scoff",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "grave carnival siege uh-huh through behind excepting notwithstanding",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "journal-files-source",
        "type": models.CreateInputInputJournalFilesType.JOURNAL_FILES,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 10,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "yuck drat ew our the lecture likewise",
            },
        ],
        "current_boot": False,
        "max_age_dur": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "oof depart loyalty reapply bog",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputKafka(
        id="kafka-source",
        type=models.CreateInputTypeKafka.KAFKA,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
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
            username="Monte_Thiel32",
            password="KI_orHyojtOdRdG",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://dependable-pulse.net",
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
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        auto_commit_interval=2313.91,
        auto_commit_threshold=7394.97,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="deliberately greatly hmph mom fatally",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kinesis-source",
        "type": models.CreateInputTypeKinesis.KINESIS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 1,
        "shard_expr": "true",
        "shard_iterator_type": models.CreateInputShardIteratorStart.TRIM_HORIZON,
        "payload_format": models.CreateInputRecordDataFormat.CRIBL,
        "get_records_limit": 5000,
        "get_records_limit_total": 20000,
        "load_balancing_algorithm": models.CreateInputShardLoadBalancing.CONSISTENT_HASHING,
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
        "verify_kpl_check_sums": False,
        "avoid_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "finally instead less till ew duh ew",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
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
### Example Usage: InputCreateExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-events-source",
        "type": models.CreateInputTypeKubeEvents.KUBE_EVENTS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "before settler fortunately meh nice bludgeon under soybean jam-packed",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "stall unpleasant newsprint",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-logs-source",
        "type": models.CreateInputTypeKubeLogs.KUBE_LOGS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 15,
        "rules": [
            {
                "filter_": "<value>",
                "description": "over questionably yesterday",
            },
        ],
        "timestamps": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_load_balancing": False,
        "description": "warp verbally through amnesty",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "kube-metrics-source",
        "type": models.CreateInputTypeKubeMetrics.KUBE_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 15,
        "rules": [
            {
                "filter_": "<value>",
                "description": "saloon where faithfully",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/kube_metrics",
        },
        "description": "traduce calculus where fun calculating uh-huh delightfully",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "loki-source",
        "type": models.CreateInputTypeLoki.LOKI,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "loki_api": "/loki/api/v1/push",
        "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "nudge valley instead sun er",
        "username": "Werner47",
        "password": "b7xIUX8OdaWkQ40",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "metrics-source",
        "type": models.CreateInputTypeMetrics.METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 4526.8,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "enable_proxy_header": False,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 86.97,
        "description": "contrast kindly arcade total while warmly",
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "mdt-source",
        "type": models.CreateInputTypeModelDrivenTelemetry.MODEL_DRIVEN_TELEMETRY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 1000,
        "shutdown_timeout_ms": 5000,
        "description": "unnecessarily forenenst finally ick qua far or pack outlandish",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request=models.CreateInputInputMsk(
        id="msk-source",
        type=models.CreateInputTypeMsk.MSK,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
                disabled=False,
                reject_unauthorized=True,
                servername="<value>",
                certificate_name="<value>",
                ca_path="<value>",
                priv_key_path="<value>",
                cert_path="<value>",
                passphrase="<value>",
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
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
            disabled=False,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        auto_commit_interval=8981.95,
        auto_commit_threshold=7775.93,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        description="whereas gah internationalize",
        aws_api_key="<value>",
        aws_secret="<value>",
        template_aws_secret_key="<value>",
        template_region="<value>",
        template_assume_role_arn="<value>",
        template_assume_role_external_id="<id>",
        template_aws_api_key="<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "netflow-source",
        "type": models.CreateInputTypeNetflow.NETFLOW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "udp_socket_rx_buf_size": 1130.9,
        "template_cache_minutes": 30,
        "v5_enabled": True,
        "v9_enabled": True,
        "ipfix_enabled": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "dicker sans scarper amid which until yet yin",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-mgmt-source",
        "type": models.CreateInputTypeOffice365Mgmt.OFFICE365_MGMT,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 300,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "publisher_identifier": "<value>",
        "content_config": [
            {
                "content_type": "<value>",
                "description": "er aha till deploy",
                "interval": 3564.68,
                "log_level": models.LogLevelOptionsContentConfigItems.ERROR,
                "enabled": True,
            },
        ],
        "ingestion_lag": 0,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                3152.61,
                1476.48,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "overfeed bitterly notwithstanding tidy equally however",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_tenant_id": "<id>",
        "template_app_id": "<id>",
        "template_publisher_identifier": "<value>",
        "template_client_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-msg-trace-source",
        "type": models.CreateInputTypeOffice365MsgTrace.OFFICE365_MSG_TRACE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 300,
        "disable_time_filter": True,
        "auth_type": models.CreateInputAuthenticationMethodOffice365MsgTrace.OAUTH,
        "reschedule_dropped_tasks": True,
        "max_task_reschedule": 1,
        "log_level": models.CreateInputLogLevelOffice365MsgTrace.INFO,
        "job_timeout": "0",
        "keep_alive_time": 30,
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                3152.61,
                1476.48,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "description": "mould schnitzel regarding yawningly",
        "username": "Gennaro86",
        "password": "pKemi5kWxN5TmzT",
        "credentials_secret": "<value>",
        "client_secret": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "resource": "https://outlook.office365.com",
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "text_secret": "<value>",
        "cert_options": {
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
        },
        "template_url": "https://parched-iridescence.org",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_resource": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "office365-service-source",
        "type": models.CreateInputTypeOffice365Service.OFFICE365_SERVICE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 300,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "content_config": [
            {
                "content_type": "<value>",
                "description": "sew queasily interior seriously",
                "interval": 2838.92,
                "log_level": models.LogLevelOptionsContentConfigItems.ERROR,
                "enabled": False,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                3152.61,
                1476.48,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "outside bah inside",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_tenant_id": "<id>",
        "template_app_id": "<id>",
        "template_client_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "otel-source",
        "type": models.CreateInputTypeOpenTelemetry.OPEN_TELEMETRY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 15,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "protocol": models.CreateInputProtocol.GRPC,
        "extract_spans": False,
        "extract_metrics": False,
        "otlp_version": models.CreateInputOTLPVersion.ZERO_DOT_10_DOT_0,
        "auth_type": models.AuthenticationTypeOptions.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 1000,
        "description": "indeed circa because",
        "username": "Myles.Lueilwitz-Ryan",
        "password": "RyYhbE0tvmVGPg6",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "extract_logs": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "prometheus-source",
        "type": models.CreateInputTypePrometheus.PROMETHEUS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
        ],
        "discovery_type": models.CreateInputDiscoveryTypePrometheus.STATIC,
        "interval": 60,
        "log_level": models.CreateInputLogLevelPrometheus.INFO,
        "reject_unauthorized": True,
        "timeout": 0,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.MANUAL,
        "description": "barring across fat who astride lowball",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 9090,
        "name_list": [
            "<value 1>",
        ],
        "scrape_protocol": models.CreateInputMetricsProtocol.HTTP,
        "scrape_path": "/metrics",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": True,
        "search_filter": [
            {
                "name": "<value>",
                "values": [
                    "<value 1>",
                ],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V4,
        "reuse_connections": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "username": "Edgardo39",
        "password": "BvIzohhpUOO9Ez7",
        "credentials_secret": "<value>",
        "template_log_level": "<value>",
        "template_aws_api_key": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "prometheus-rw-source",
        "type": models.CreateInputTypePrometheusRw.PROMETHEUS_RW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "openly likewise gruesome whoever whose gee",
        "username": "Dean.Keebler",
        "password": "0POH0dLKHeOMaH5",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_prometheus_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "raw-udp-source",
        "type": models.CreateInputTypeRawUDP.RAW_UDP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "single_msg_udp_packets": False,
        "ingest_raw_bytes": False,
        "udp_socket_rx_buf_size": 343.08,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "or robust over impact instead round near since joshingly except",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "s3-source",
        "type": models.CreateInputTypeS3.S3,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "tag_after_processing": False,
        "description": "into keenly towards",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "s3-inventory-source",
        "type": models.CreateInputTypeS3Inventory.S3_INVENTORY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "s3-inventory-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "checksum_suffix": "checksum",
        "max_manifest_size_kb": 4096,
        "validate_inventory_files": False,
        "description": "finally divert if lively seriously",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.FALSE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "security-lake-source",
        "type": models.CreateInputTypeSecurityLake.SECURITY_LAKE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "security-lake-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "description": "mmm lest pfft likewise rule what comparison amidst median gullible",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.FALSE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "snmp-source",
        "type": models.CreateInputTypeSnmp.SNMP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "192.168.1.1",
        "port": 161,
        "snmp_v3_auth": {
            "v3_auth_enabled": False,
            "allow_unmatched_trap": False,
            "v3_users": [
                {
                    "name": "<value>",
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.NONE,
                    "auth_key": "<value>",
                    "priv_protocol": models.CreateInputPrivacyProtocol.NONE,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 4917.68,
        "varbinds_with_types": False,
        "best_effort_parsing": False,
        "description": "um pinion wash however meanwhile yesterday separately zowie",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-source",
        "type": models.CreateInputTypeSplunk.SPLUNK,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "so obedience aw waft incidentally brr responsibility even furthermore kiss",
            },
        ],
        "max_s2_sversion": models.CreateInputMaxS2SVersion.V3,
        "description": "why event apropos row paralyse upbeat amidst pish joyously ack",
        "use_fwd_timezone": True,
        "drop_control_fields": True,
        "extract_metrics": False,
        "compress": models.CreateInputCompression.DISABLED,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-hec-source",
        "type": models.CreateInputTypeSplunkHec.SPLUNK_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "meh earnest numeracy sardonic stack about",
                "allowed_indexes_at_token": [
                    "<value 1>",
                    "<value 2>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "splunk_hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
        ],
        "splunk_hec_acks": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "use_fwd_timezone": True,
        "drop_control_fields": True,
        "extract_metrics": False,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
        ],
        "emit_token_metrics": False,
        "description": "executor given wheel evenly scowl arid boulevard whoa yuck",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "splunk-search-source",
        "type": models.CreateInputTypeSplunkSearch.SPLUNK_SEARCH,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "earliest": "-16m@m",
        "latest": "-1m@m",
        "cron_schedule": "0 * * * *",
        "endpoint": "/services/search/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
        "endpoint_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "endpoint_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "log_level": models.CreateInputLogLevelSplunkSearch.ERROR,
        "request_timeout": 0,
        "use_round_robin_dns": False,
        "reject_unauthorized": False,
        "encoding": "<value>",
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                5227.09,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "auth_type": models.CreateInputAuthenticationTypeSplunkSearch.BASIC,
        "description": "until content along",
        "username": "Jalyn43",
        "password": "2wxXTLiflvFCcIX",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "sqs-source",
        "type": models.CreateInputTypeSqs.SQS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "my-queue",
        "queue_type": models.CreateInputQueueType.STANDARD,
        "aws_account_id": "<id>",
        "create_queue": False,
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
        "max_messages": 10,
        "visibility_timeout": 600,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 10,
        "description": "anxiously wilted gee once icebreaker unkempt",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 3,
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
### Example Usage: InputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="createInput" method="post" path="/system/inputs" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "syslog-source",
        "type": models.CreateInputInputSyslogType1.SYSLOG,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 2766.66,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "timestamp_timezone": "local",
        "single_msg_udp_packets": False,
        "enable_proxy_header": False,
        "keep_fields_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "octet_counting": False,
        "infer_framing": True,
        "strictly_infer_octet_counting": True,
        "allow_non_standard_app_name": False,
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 2673.89,
        "enable_load_balancing": False,
        "description": "enthusiastically idolized now",
        "enable_enhanced_proxy_header_parsing": True,
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "system-metrics-source",
        "type": models.CreateInputTypeSystemMetrics.SYSTEM_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 10,
        "host": {
            "mode": models.ModeOptionsHost.BASIC,
            "custom": {
                "system": {
                    "mode": models.CreateInputSystemModeSystemMetrics.BASIC,
                    "processes": False,
                },
                "cpu": {
                    "mode": models.CreateInputCPUModeSystemMetrics.BASIC,
                    "per_cpu": False,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.CreateInputMemoryModeSystemMetrics.BASIC,
                    "detail": False,
                },
                "network": {
                    "mode": models.CreateInputNetworkModeSystemMetrics.BASIC,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.CreateInputDiskModeSystemMetrics.BASIC,
                    "detail": False,
                    "inodes": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "mountpoints": [
                        "<value 1>",
                    ],
                    "fstypes": [
                        "<value 1>",
                    ],
                    "per_device": False,
                },
            },
        },
        "process": {
            "sets": [
                {
                    "name": "<value>",
                    "filter_": "<value>",
                    "include_children": False,
                },
            ],
        },
        "container": {
            "mode": models.CreateInputContainerMode.BASIC,
            "docker_socket": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "docker_timeout": 5,
            "filters": [
                {
                    "expr": "<value>",
                },
            ],
            "all_containers": False,
            "per_device": False,
            "detail": False,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/system_metrics",
        },
        "description": "although jealously forswear clamor",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "system-state-source",
        "type": models.CreateInputTypeSystemState.SYSTEM_STATE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 300,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "collectors": {
            "hostsfile": {
                "enable": True,
            },
            "interfaces": {
                "enable": True,
            },
            "disk": {
                "enable": True,
            },
            "metadata": {
                "enable": True,
            },
            "routes": {
                "enable": True,
            },
            "dns": {
                "enable": True,
            },
            "user": {
                "enable": True,
            },
            "firewall": {
                "enable": True,
            },
            "services": {
                "enable": True,
            },
            "ports": {
                "enable": True,
            },
            "login_users": {
                "enable": True,
            },
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "$CRIBL_HOME/state/system_state",
        },
        "disable_native_module": False,
        "disable_native_last_log_module": False,
        "description": "times even descendant absent although mortally",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "tcp-source",
        "type": models.CreateInputTypeTCP.TCP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_header": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "description": "clumsy eternity than save both hover",
        "auth_token": "",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "tcpjson-source",
        "type": models.CreateInputTypeTcpjson.TCPJSON,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "merrily scaly unless",
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wef-source",
        "type": models.CreateInputTypeWef.WEF,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.CreateInputAuthenticationMethodWef.CLIENT_CERT,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "request_cert": True,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "common_name_regex": "/.*/",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "ocsp_check": False,
            "keytab": "<value>",
            "principal": "<value>",
            "ocsp_check_fail_close": False,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "keep_alive_timeout": 90,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "socket_timeout": 0,
        "ca_fingerprint": "<value>",
        "keytab": "<value>",
        "principal": "<value>",
        "allow_machine_id_mismatch": False,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "version": "<value>",
                "content_format": models.CreateInputFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "read_existing_events": False,
                "send_bookmarks": True,
                "compress": True,
                "targets": [],
                "locale": "en-US",
                "query_selector": models.CreateInputQueryBuilderMode.SIMPLE,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/usr/src",
                        "query_expression": "<value>",
                    },
                ],
                "xml_query": "<value>",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "before whenever circa geez youthfully lest off",
        "log_fingerprint_mismatch": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "win-event-logs-source",
        "type": models.CreateInputTypeWinEventLogs.WIN_EVENT_LOGS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.CreateInputReadMode.NEWEST,
        "event_format": models.CreateInputEventFormat.JSON,
        "disable_native_module": False,
        "interval": 10,
        "batch_size": 500,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 51200,
        "description": "conclude sesame prioritize polarisation bourgeoisie decongestant behind",
        "disable_json_rendering": False,
        "disable_xml_rendering": True,
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "windows-metrics-source",
        "type": models.CreateInputTypeWindowsMetrics.WINDOWS_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 10,
        "host": {
            "mode": models.ModeOptionsHost.BASIC,
            "custom": {
                "system": {
                    "mode": models.CreateInputSystemModeWindowsMetrics.BASIC,
                    "detail": False,
                },
                "cpu": {
                    "mode": models.CreateInputCPUModeWindowsMetrics.BASIC,
                    "per_cpu": False,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.CreateInputMemoryModeWindowsMetrics.BASIC,
                    "detail": False,
                },
                "network": {
                    "mode": models.CreateInputNetworkModeWindowsMetrics.BASIC,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.CreateInputDiskModeWindowsMetrics.BASIC,
                    "per_volume": False,
                    "detail": False,
                    "volumes": [
                        "<value 1>",
                    ],
                },
            },
        },
        "process": {
            "sets": [
                {
                    "name": "<value>",
                    "filter_": "<value>",
                    "include_children": False,
                },
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/windows_metrics",
        },
        "disable_native_module": False,
        "description": "handle unsung mediocre delightfully save grown whose circa",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wiz-source",
        "type": models.CreateInputTypeWiz.WIZ,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 300,
        "keep_alive_time": 30,
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                5227.09,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "quarrelsomely furthermore deserted excitable liberalize",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_endpoint": "<value>",
        "template_auth_url": "https://misguided-pine.org",
        "template_client_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "wiz-webhook-source",
        "type": models.CreateInputTypeWizWebhook.WIZ_WEBHOOK,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_paths": [
            "<value 1>",
            "<value 2>",
        ],
        "allowed_methods": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "swath misfire object saw presume yum",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "above anti underneath geez wing fuel untidy verbally stir-fry lasting",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.create(request={
        "id": "zscaler-hec-source",
        "type": models.CreateInputTypeZscalerHec.ZSCALER_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "boohoo restaurant ouch braid short",
                "allowed_indexes_at_token": [
                    "<value 1>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
        ],
        "hec_acks": False,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
        ],
        "emit_token_metrics": False,
        "description": "vastly against stable down pfft likely",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_hec_api": "<value>",
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

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInputById" method="get" path="/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
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

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Source.</br></br>Provide a complete representation of the Source that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Source.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Source might not function as expected.

### Example Usage: InputCreateExamplesAppscope

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesAppscope" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "appscope-source",
        "type": models.InputAppscopeType.APPSCOPE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://youthful-hammock.net/",
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/appscope",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "beyond hidden supposing ghost fictionalize disarm geez",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "unix_socket_path": "$CRIBL_HOME/state/appscope.sock",
        "unix_socket_perms": "<value>",
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "azure-blob-source",
        "type": models.InputAzureBlobType.AZURE_BLOB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "/.*/",
        "visibility_timeout": 600,
        "num_receivers": 1,
        "max_messages": 1,
        "service_period_secs": 5,
        "skip_on_error": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "description": "understated extroverted intensely hello gentle ouch hmph rule density design",
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
        "template_queue_name": "<value>",
        "template_connection_string": "<value>",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cloudflare-hec-source",
        "type": models.InputCloudflareHecType.CLOUDFLARE_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.InputCloudflareHecAuthenticationMethod.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "ha irresponsible patiently",
                "allowed_indexes_at_token": [
                    "<value 1>",
                    "<value 2>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": False,
        "description": "abaft deliberately function",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "collection-source",
        "type": models.InputCollectionType.COLLECTION,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "throttle_rate_per_sec": "0",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "output": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputConfluentCloud(
        id="confluent-cloud-source",
        type=models.InputConfluentCloudType.CONFLUENT_CLOUD,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
            "<value 2>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
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
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
            username="Maximus30",
            password="6TQ9JUSPWUKvYWA",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://sudden-polarisation.info/",
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
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        auto_commit_interval=443.17,
        auto_commit_threshold=3647.04,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="or since gadzooks",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-http-source",
        "type": models.InputCriblHTTPType.CRIBL_HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "but capitalise clear unfortunate ignorance gah sans despite hydrocarbon tankful",
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "ride even among",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-lake-http-source",
        "type": models.InputCriblLakeHTTPType.CRIBL_LAKE_HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "cribl_api": "/cribl",
        "elastic_api": "/elastic",
        "splunk_hec_api": "/services/collector",
        "splunk_hec_acks": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "extract vice instead fatal every rebuke ew forenenst millet crest",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "splunk_hec_metadata": {
                    "enabled": False,
                    "default_dataset": "<value>",
                    "allowed_indexes_at_token": [
                        "<value 1>",
                    ],
                },
                "elasticsearch_metadata": {
                    "enabled": True,
                    "default_dataset": "<value>",
                },
            },
        ],
        "description": "authentic yuck better as where splash but behind",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-tcp-source",
        "type": models.InputCriblTCPType.CRIBL_TCP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": False,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "delightfully scarily chromakey oh hm sour",
            },
        ],
        "description": "refer redevelop mid reproach waterspout lest utterly",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "crowdstrike-source",
        "type": models.InputCrowdstrikeType.CROWDSTRIKE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 21600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "description": "corporation joyously retention only transcend save however likely shanghai",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesDatadogAgent

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesDatadogAgent" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datadog-agent-source",
        "type": models.InputDatadogAgentType.DATADOG_AGENT,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "extract_metrics": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "proxy_mode": {
            "enabled": False,
            "reject_unauthorized": True,
        },
        "description": "made-up solace bouncy which comfortable gadzooks",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "datagen-source",
        "type": models.InputDatagenType.DATAGEN,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "samples": [
            {
                "sample": "sample.json",
                "events_per_sec": 10,
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "aha reflecting now",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "edge-prometheus-source",
        "type": models.InputEdgePrometheusType.EDGE_PROMETHEUS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
        ],
        "discovery_type": models.InputEdgePrometheusDiscoveryType.STATIC,
        "interval": 60,
        "timeout": 5000,
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.InputEdgePrometheusAuthenticationMethod.MANUAL,
        "description": "hmph jagged minus fondly affect cinch prioritize",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTP,
                "host": "localhost",
                "port": 9090,
                "path": "/metrics",
            },
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 9090,
        "name_list": [
            "<value 1>",
            "<value 2>",
        ],
        "scrape_protocol": models.ProtocolOptionsTargetsItems.HTTP,
        "scrape_path": "/metrics",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": True,
        "search_filter": [
            {
                "name": "<value>",
                "values": [],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "scrape_protocol_expr": "metadata.annotations['prometheus.io/scheme'] || 'http'",
        "scrape_port_expr": "metadata.annotations['prometheus.io/port'] || 9090",
        "scrape_path_expr": "metadata.annotations['prometheus.io/path'] || '/metrics'",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "severe furthermore concrete hunger muffled",
            },
        ],
        "username": "Orrin_Yundt20",
        "password": "alXPvLywpTQbHyi",
        "credentials_secret": "<value>",
        "template_aws_api_key": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "elastic-source",
        "type": models.InputElasticType.ELASTIC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "elastic_api": "/",
        "auth_type": models.InputElasticAuthenticationType.NONE,
        "api_version": models.InputElasticAPIVersion.EIGHT_DOT_3_DOT_2,
        "extra_http_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "proxy_mode": {
            "enabled": False,
            "auth_type": models.InputElasticAuthenticationMethod.NONE,
            "username": "Abigayle.Ledner38",
            "password": "VDPV4GrdklqLt4A",
            "credentials_secret": "<value>",
            "url": "https://yellowish-pearl.org",
            "reject_unauthorized": False,
            "remove_headers": [
                "<value 1>",
                "<value 2>",
            ],
            "timeout_sec": 60,
            "template_url": "https://focused-invite.org",
        },
        "description": "ouch snarling duh",
        "username": "Xander_Graham",
        "password": "1duIyiiwRASxBVc",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
        ],
        "custom_api_version": "{\n    \"name\": \"AzU84iL\",\n    \"cluster_name\": \"cribl\",\n    \"cluster_uuid\": \"Js6_Z2VKS3KbfRSxPmPbaw\",\n    \"version\": {\n        \"number\": \"8.3.2\",\n        \"build_type\": \"tar\",\n        \"build_hash\": \"bca0c8d\",\n        \"build_date\": \"2019-10-16T06:19:49.319352Z\",\n        \"build_snapshot\": false,\n        \"lucene_version\": \"9.7.2\",\n        \"minimum_wire_compatibility_version\": \"7.17.0\",\n        \"minimum_index_compatibility_version\": \"7.0.0\"\n    },\n    \"tagline\": \"You Know, for Search\"\n}",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "eventhub-source",
        "type": models.InputEventhubType.EVENTHUB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
        "group_id": "Cribl",
        "from_beginning": True,
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
            "password": "xop7OD_LxhffeRA",
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
        "session_timeout": 30000,
        "rebalance_timeout": 60000,
        "heartbeat_interval": 3000,
        "auto_commit_interval": 4392.98,
        "auto_commit_threshold": 3134.99,
        "max_bytes_per_partition": 1048576,
        "max_bytes": 10485760,
        "max_socket_errors": 0,
        "minimize_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "beard hoot rotten than unfortunately slushy",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "exec-source",
        "type": models.InputExecType.EXEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 10,
        "schedule_type": models.ScheduleType.INTERVAL,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "er relaunch rudely bug when",
        "interval": 60,
        "cron_schedule": "* * * * *",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "file-source",
        "type": models.InputFileType.FILE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "mode": models.InputFileMode.MANUAL,
        "interval": 10,
        "filenames": [
            "<value 1>",
            "<value 2>",
        ],
        "filter_archived_files": False,
        "tail_only": True,
        "idle_timeout": 300,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": False,
        "force_text": False,
        "hash_len": 256,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "description": "shell yesterday testimonial afore though sedately profuse",
        "path": "/Network",
        "depth": 4361.93,
        "suppress_missing_path_errors": False,
        "delete_files": False,
        "salt_hash": False,
        "include_unidentifiable_binary": False,
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "firehose-source",
        "type": models.InputFirehoseType.FIREHOSE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "fluffy now to",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "google-pubsub-source",
        "type": models.InputGooglePubsubType.GOOGLE_PUBSUB,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
        "monitor_subscription": False,
        "create_topic": False,
        "create_subscription": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_backlog": 1000,
        "concurrency": 5,
        "request_timeout": 60000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "across splosh anticodon beautifully",
        "ordered_delivery": False,
        "template_topic_name": "<value>",
        "template_subscription_name": "<value>",
        "template_region": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "grafana-source",
        "type": models.InputGrafanaType1.GRAFANA,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "prometheus_api": "/api/prom/push",
        "loki_api": "/loki/api/v1/push",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
            "username": "Gage.Rippin77",
            "password": "B6pdaXMgVOmyEDo",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
            "username": "Zion18",
            "password": "NTgCCy2le8of9ZE",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "ironclad meh to merrily besmirch whoa slimy",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-source",
        "type": models.InputHTTPType.HTTP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "cribl_api": "/cribl",
        "elastic_api": "/elastic",
        "splunk_hec_api": "/services/collector",
        "splunk_hec_acks": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "gee qua gee afterwards aboard begonia um where absent geez",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "via supportive so dial into valuable instructive of between",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "http-raw-source",
        "type": models.InputHTTPRawType.HTTP_RAW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_paths": [
            "<value 1>",
            "<value 2>",
        ],
        "allowed_methods": [
            "<value 1>",
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "afore gah odd alive pant overload mob rise throughout",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "ultimately needily whether hope quinoa gadzooks above where hierarchy",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "journal-files-source",
        "type": models.InputJournalFilesType.JOURNAL_FILES,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 10,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "fedora until anguished jump famously beside consequently tender decision",
            },
        ],
        "current_boot": False,
        "max_age_dur": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "suffocate vamoose fortunately than kaleidoscopic",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputKafka(
        id="kafka-source",
        type=models.InputKafkaType.KAFKA,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
            username="Maximus30",
            password="6TQ9JUSPWUKvYWA",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://sudden-polarisation.info/",
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
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        auto_commit_interval=5373.51,
        auto_commit_threshold=3922.91,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="to before brr including",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kinesis-source",
        "type": models.InputKinesisType.KINESIS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 1,
        "shard_expr": "true",
        "shard_iterator_type": models.ShardIteratorStart.TRIM_HORIZON,
        "payload_format": models.RecordDataFormat.CRIBL,
        "get_records_limit": 5000,
        "get_records_limit_total": 20000,
        "load_balancing_algorithm": models.ShardLoadBalancing.CONSISTENT_HASHING,
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
        "verify_kpl_check_sums": False,
        "avoid_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "factorize than bah trained shinny regarding fooey",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
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
### Example Usage: InputCreateExamplesKubeEvents

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesKubeEvents" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-events-source",
        "type": models.InputKubeEventsType.KUBE_EVENTS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "worse back second psst overspend prejudge homely gah rim",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "concerning know overconfidently carelessly throughout even before",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-logs-source",
        "type": models.InputKubeLogsType.KUBE_LOGS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 15,
        "rules": [
            {
                "filter_": "<value>",
                "description": "bravely compromise lest SUV deliberately",
            },
        ],
        "timestamps": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_load_balancing": False,
        "description": "after taxicab agreeable pulverize whenever atop",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "kube-metrics-source",
        "type": models.InputKubeMetricsType.KUBE_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 15,
        "rules": [
            {
                "filter_": "<value>",
                "description": "ack fathom incidentally doing kinase",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/kube_metrics",
        },
        "description": "excepting inquisitively violin brown during frizzy aw zowie powerless",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "loki-source",
        "type": models.InputLokiType.LOKI,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "loki_api": "/loki/api/v1/push",
        "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "physical below elementary disclosure",
        "username": "Diana.Kerluke41",
        "password": "5VWIKl4RcP6DYtZ",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "metrics-source",
        "type": models.InputMetricsType.METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 8643.34,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "enable_proxy_header": False,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 7392.9,
        "description": "reboot because clonk meh etch boo uh-huh fumigate pip coaxingly",
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "mdt-source",
        "type": models.InputModelDrivenTelemetryType.MODEL_DRIVEN_TELEMETRY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 1000,
        "shutdown_timeout_ms": 5000,
        "description": "lotion since sheathe fooey truly",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_=models.InputMsk(
        id="msk-source",
        type=models.InputMskType.MSK,
        disabled=False,
        pipeline="<value>",
        send_to_routes=True,
        environment="<value>",
        pq_enabled=False,
        streamtags=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=1000,
            commit_frequency=42,
            max_file_size="1 MB",
            max_size="5GB",
            path="$CRIBL_HOME/state/queues",
            compress=models.CompressionOptionsPq.NONE,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="Cribl",
        from_beginning=True,
        session_timeout=30000,
        rebalance_timeout=60000,
        heartbeat_interval=3000,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
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
        auto_commit_interval=621.07,
        auto_commit_threshold=3924.6,
        max_bytes_per_partition=1048576,
        max_bytes=10485760,
        max_socket_errors=0,
        description="minor midst rebound left supposing ugh",
        aws_api_key="<value>",
        aws_secret="<value>",
        template_aws_secret_key="<value>",
        template_region="<value>",
        template_assume_role_arn="<value>",
        template_assume_role_external_id="<id>",
        template_aws_api_key="<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "netflow-source",
        "type": models.InputNetflowType.NETFLOW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "udp_socket_rx_buf_size": 2462.99,
        "template_cache_minutes": 30,
        "v5_enabled": True,
        "v9_enabled": True,
        "ipfix_enabled": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "boastfully hearten ick intend meanwhile jaywalk wallaby",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-mgmt-source",
        "type": models.InputOffice365MgmtType.OFFICE365_MGMT,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 300,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "publisher_identifier": "<value>",
        "content_config": [
            {
                "content_type": "<value>",
                "description": "superb consequently below",
                "interval": 9014.67,
                "log_level": models.LogLevelOptionsContentConfigItems.INFO,
                "enabled": True,
            },
        ],
        "ingestion_lag": 0,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                2729.52,
                6010.16,
                5724.14,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "solemnly forearm yahoo brr sweet until brown",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_tenant_id": "<id>",
        "template_app_id": "<id>",
        "template_publisher_identifier": "<value>",
        "template_client_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-msg-trace-source",
        "type": models.InputOffice365MsgTraceType.OFFICE365_MSG_TRACE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 300,
        "disable_time_filter": True,
        "auth_type": models.InputOffice365MsgTraceAuthenticationMethod.OAUTH,
        "reschedule_dropped_tasks": True,
        "max_task_reschedule": 1,
        "log_level": models.InputOffice365MsgTraceLogLevel.INFO,
        "job_timeout": "0",
        "keep_alive_time": 30,
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                2729.52,
                6010.16,
                5724.14,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "description": "though gadzooks pace",
        "username": "Domingo.Funk20",
        "password": "zEomPhRXS2K3PJN",
        "credentials_secret": "<value>",
        "client_secret": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "resource": "https://outlook.office365.com",
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "text_secret": "<value>",
        "cert_options": {
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
        },
        "template_url": "https://valuable-stall.name/",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_resource": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "office365-service-source",
        "type": models.InputOffice365ServiceType.OFFICE365_SERVICE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 300,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "content_config": [
            {
                "content_type": "<value>",
                "description": "actually that after hyphenation psst",
                "interval": 7646.22,
                "log_level": models.LogLevelOptionsContentConfigItems.INFO,
                "enabled": True,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                2729.52,
                6010.16,
                5724.14,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "or oh apropos in analogy lobotomise lender gadzooks between fully",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_tenant_id": "<id>",
        "template_app_id": "<id>",
        "template_client_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "otel-source",
        "type": models.InputOpenTelemetryType.OPEN_TELEMETRY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 15,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "protocol": models.InputOpenTelemetryProtocol.GRPC,
        "extract_spans": False,
        "extract_metrics": False,
        "otlp_version": models.InputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0,
        "auth_type": models.AuthenticationTypeOptions.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 1000,
        "description": "augment before serialize",
        "username": "Monique.Lakin",
        "password": "Ig92bVAWqo4_P8d",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "extract_logs": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-source",
        "type": models.InputPrometheusType.PROMETHEUS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
        ],
        "discovery_type": models.InputPrometheusDiscoveryType.STATIC,
        "interval": 60,
        "log_level": models.InputPrometheusLogLevel.INFO,
        "reject_unauthorized": True,
        "timeout": 0,
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.MANUAL,
        "description": "hover aw buzzing part unethically apud down scornful",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 9090,
        "name_list": [
            "<value 1>",
        ],
        "scrape_protocol": models.MetricsProtocol.HTTP,
        "scrape_path": "/metrics",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": True,
        "search_filter": [
            {
                "name": "<value>",
                "values": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V4,
        "reuse_connections": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "username": "Martina10",
        "password": "R9HovxE2l_Ve3VU",
        "credentials_secret": "<value>",
        "template_log_level": "<value>",
        "template_aws_api_key": "<value>",
        "template_aws_secret_key": "<value>",
        "template_region": "<value>",
        "template_assume_role_arn": "<value>",
        "template_assume_role_external_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "prometheus-rw-source",
        "type": models.InputPrometheusRwType.PROMETHEUS_RW,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "almost calmly against wherever gratefully versus",
        "username": "Johnathon.Wolf",
        "password": "xMC_bK0VYnsfmYM",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_prometheus_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "raw-udp-source",
        "type": models.InputRawUDPType.RAW_UDP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "single_msg_udp_packets": False,
        "ingest_raw_bytes": False,
        "udp_socket_rx_buf_size": 6988.17,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "yuck trust hopelessly toward instead gadzooks oil solidly now",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-source",
        "type": models.InputS3Type.S3,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "tag_after_processing": False,
        "description": "lively oddly brood optimistically extremely soliloquy inquisitively",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesS3Inventory

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesS3Inventory" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "s3-inventory-source",
        "type": models.InputS3InventoryType.S3_INVENTORY,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "s3-inventory-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "checksum_suffix": "checksum",
        "max_manifest_size_kb": 4096,
        "validate_inventory_files": False,
        "description": "extract until abandoned perky gladly unless yippee oh version successfully",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesSecurityLake

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSecurityLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "security-lake-source",
        "type": models.InputSecurityLakeType.SECURITY_LAKE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "security-lake-queue",
        "file_filter": "/.*/",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 10000,
        "max_messages": 1,
        "visibility_timeout": 600,
        "num_receivers": 1,
        "socket_timeout": 300,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3600,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 5,
        "parquet_chunk_download_timeout": 600,
        "checkpointing": {
            "enabled": False,
            "retries": 5,
        },
        "poll_timeout": 10,
        "encoding": "<value>",
        "description": "source happily how always helplessly quixotic relative what often",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.FALSE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
### Example Usage: InputCreateExamplesSnmp

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSnmp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "snmp-source",
        "type": models.InputSnmpType.SNMP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "192.168.1.1",
        "port": 161,
        "snmp_v3_auth": {
            "v3_auth_enabled": False,
            "allow_unmatched_trap": False,
            "v3_users": [
                {
                    "name": "<value>",
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.NONE,
                    "auth_key": "<value>",
                    "priv_protocol": models.PrivacyProtocol.NONE,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 6815.48,
        "varbinds_with_types": False,
        "best_effort_parsing": False,
        "description": "reproach meh wallaby uncommon lotion repurpose how",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-source",
        "type": models.InputSplunkType.SPLUNK,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "boo oof insignificant pfft opposite hunt",
            },
        ],
        "max_s2_sversion": models.MaxS2SVersion.V3,
        "description": "until scoop fold indeed engender",
        "use_fwd_timezone": True,
        "drop_control_fields": True,
        "extract_metrics": False,
        "compress": models.InputSplunkCompression.DISABLED,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-hec-source",
        "type": models.InputSplunkHecType.SPLUNK_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "before unless pinstripe knowledgeably courteous slide lighthearted",
                "allowed_indexes_at_token": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "splunk_hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "splunk_hec_acks": False,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "use_fwd_timezone": True,
        "drop_control_fields": True,
        "extract_metrics": False,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": False,
        "description": "meh yowza manner failing",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "splunk-search-source",
        "type": models.InputSplunkSearchType.SPLUNK_SEARCH,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "earliest": "-16m@m",
        "latest": "-1m@m",
        "cron_schedule": "0 * * * *",
        "endpoint": "/services/search/jobs/export",
        "output_mode": models.OutputModeOptionsSplunkCollectorConf.JSON,
        "endpoint_params": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "endpoint_headers": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "log_level": models.InputSplunkSearchLogLevel.ERROR,
        "request_timeout": 0,
        "use_round_robin_dns": False,
        "reject_unauthorized": False,
        "encoding": "<value>",
        "keep_alive_time": 30,
        "job_timeout": "0",
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                4786.8,
                4387.89,
                7031.34,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 10000,
        "auth_type": models.InputSplunkSearchAuthenticationType.BASIC,
        "description": "sprinkles deflate fooey pricey below but quarrelsome",
        "username": "Dulce28",
        "password": "H0D8DX8APbKrKvi",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "sqs-source",
        "type": models.InputSqsType.SQS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "queue_name": "my-queue",
        "queue_type": models.InputSqsQueueType.STANDARD,
        "aws_account_id": "<id>",
        "create_queue": False,
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
        "max_messages": 10,
        "visibility_timeout": 600,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 10,
        "description": "blah yum intent er loyalty anenst gadzooks",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 3,
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
### Example Usage: InputCreateExamplesSyslog

<!-- UsageSnippet language="python" operationID="updateInputById" method="patch" path="/system/inputs/{id}" example="InputCreateExamplesSyslog" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "syslog-source",
        "type": models.InputSyslogType1.SYSLOG,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 1808.19,
        "max_buffer_size": 1000,
        "ip_whitelist_regex": "/.*/",
        "timestamp_timezone": "local",
        "single_msg_udp_packets": False,
        "enable_proxy_header": False,
        "keep_fields_list": [
            "<value 1>",
        ],
        "octet_counting": False,
        "infer_framing": True,
        "strictly_infer_octet_counting": True,
        "allow_non_standard_app_name": False,
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 1683.94,
        "enable_load_balancing": False,
        "description": "omelet helpless sunbathe hmph mothball difficult",
        "enable_enhanced_proxy_header_parsing": True,
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-metrics-source",
        "type": models.InputSystemMetricsType.SYSTEM_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 10,
        "host": {
            "mode": models.ModeOptionsHost.BASIC,
            "custom": {
                "system": {
                    "mode": models.InputSystemMetricsSystemMode.BASIC,
                    "processes": False,
                },
                "cpu": {
                    "mode": models.InputSystemMetricsCPUMode.BASIC,
                    "per_cpu": False,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.InputSystemMetricsMemoryMode.BASIC,
                    "detail": False,
                },
                "network": {
                    "mode": models.InputSystemMetricsNetworkMode.BASIC,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.InputSystemMetricsDiskMode.BASIC,
                    "detail": False,
                    "inodes": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "mountpoints": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "fstypes": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_device": False,
                },
            },
        },
        "process": {
            "sets": [
                {
                    "name": "<value>",
                    "filter_": "<value>",
                    "include_children": False,
                },
            ],
        },
        "container": {
            "mode": models.InputSystemMetricsContainerMode.BASIC,
            "docker_socket": [
                "<value 1>",
            ],
            "docker_timeout": 5,
            "filters": [
                {
                    "expr": "<value>",
                },
            ],
            "all_containers": False,
            "per_device": False,
            "detail": False,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/system_metrics",
        },
        "description": "oddball boohoo perfectly libel culminate somber",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "system-state-source",
        "type": models.InputSystemStateType.SYSTEM_STATE,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 300,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "collectors": {
            "hostsfile": {
                "enable": True,
            },
            "interfaces": {
                "enable": True,
            },
            "disk": {
                "enable": True,
            },
            "metadata": {
                "enable": True,
            },
            "routes": {
                "enable": True,
            },
            "dns": {
                "enable": True,
            },
            "user": {
                "enable": True,
            },
            "firewall": {
                "enable": True,
            },
            "services": {
                "enable": True,
            },
            "ports": {
                "enable": True,
            },
            "login_users": {
                "enable": True,
            },
        },
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "$CRIBL_HOME/state/system_state",
        },
        "disable_native_module": False,
        "disable_native_last_log_module": False,
        "description": "catalog past whitewash seafood",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcp-source",
        "type": models.InputTCPType.TCP,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "enable_header": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
            ],
        },
        "description": "decongestant schnitzel supplier selfish mushy milestone heavy giant",
        "auth_token": "",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "tcpjson-source",
        "type": models.InputTcpjsonType.TCPJSON,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "/.*/",
        "max_active_cxn": 1000,
        "socket_idle_timeout": 0,
        "socket_ending_max_wait": 30,
        "socket_max_lifespan": 0,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "abandoned sturdy phooey print charter quickly vol including towards preside",
        "auth_token": "",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wef-source",
        "type": models.InputWefType.WEF,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.InputWefAuthenticationMethod.CLIENT_CERT,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "request_cert": True,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "common_name_regex": "/.*/",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "ocsp_check": False,
            "keytab": "<value>",
            "principal": "<value>",
            "ocsp_check_fail_close": False,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "keep_alive_timeout": 90,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "socket_timeout": 0,
        "ca_fingerprint": "<value>",
        "keytab": "<value>",
        "principal": "<value>",
        "allow_machine_id_mismatch": False,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "version": "<value>",
                "content_format": models.InputWefFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "read_existing_events": False,
                "send_bookmarks": True,
                "compress": True,
                "targets": [],
                "locale": "en-US",
                "query_selector": models.QueryBuilderMode.SIMPLE,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/usr/sbin",
                        "query_expression": "<value>",
                    },
                ],
                "xml_query": "<value>",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "eek boohoo meh heartache legend oof where reopen",
        "log_fingerprint_mismatch": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "win-event-logs-source",
        "type": models.InputWinEventLogsType.WIN_EVENT_LOGS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.ReadMode.NEWEST,
        "event_format": models.EventFormat.JSON,
        "disable_native_module": False,
        "interval": 10,
        "batch_size": 500,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 51200,
        "description": "when upward hovercraft ill trick after part",
        "disable_json_rendering": False,
        "disable_xml_rendering": True,
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "windows-metrics-source",
        "type": models.InputWindowsMetricsType.WINDOWS_METRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "interval": 10,
        "host": {
            "mode": models.ModeOptionsHost.BASIC,
            "custom": {
                "system": {
                    "mode": models.InputWindowsMetricsSystemMode.BASIC,
                    "detail": False,
                },
                "cpu": {
                    "mode": models.InputWindowsMetricsCPUMode.BASIC,
                    "per_cpu": False,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.InputWindowsMetricsMemoryMode.BASIC,
                    "detail": False,
                },
                "network": {
                    "mode": models.InputWindowsMetricsNetworkMode.BASIC,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.InputWindowsMetricsDiskMode.BASIC,
                    "per_volume": False,
                    "detail": False,
                    "volumes": [
                        "<value 1>",
                        "<value 2>",
                    ],
                },
            },
        },
        "process": {
            "sets": [
                {
                    "name": "<value>",
                    "filter_": "<value>",
                    "include_children": False,
                },
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": False,
            "time_window": "10m",
            "max_data_size": "1GB",
            "max_data_time": "24h",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "$CRIBL_HOME/state/windows_metrics",
        },
        "disable_native_module": False,
        "description": "if quizzically ha zowie inferior pop now fundraising",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-source",
        "type": models.InputWizType.WIZ,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 300,
        "keep_alive_time": 30,
        "max_missed_keep_alives": 3,
        "ttl": "4h",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1000,
            "limit": 5,
            "multiplier": 2,
            "codes": [
                4786.8,
                4387.89,
                7031.34,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "hence when inspection um jovially comparison filter",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_endpoint": "<value>",
        "template_auth_url": "https://spiteful-ghost.name",
        "template_client_id": "<id>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "wiz-webhook-source",
        "type": models.InputWizWebhookType.WIZ_WEBHOOK,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": False,
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 10000,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_paths": [
            "<value 1>",
        ],
        "allowed_methods": [
            "<value 1>",
            "<value 2>",
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "mostly incidentally nearly with meanwhile",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "yowza upliftingly firm regarding",
        "template_host": "<value>",
        "template_port": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "zscaler-hec-source",
        "type": models.InputZscalerHecType.ZSCALER_HEC,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "wearily after minor daintily modulo amid",
                "allowed_indexes_at_token": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "/.*/",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 256,
        "max_requests_per_socket": 0,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 100,
        "request_timeout": 0,
        "socket_timeout": 0,
        "keep_alive_timeout": 5,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "/.*/",
        "ip_denylist_regex": "/^$/",
        "hec_api": "/services/collector",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "allowed_indexes": [
            "<value 1>",
            "<value 2>",
        ],
        "hec_acks": False,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": False,
        "description": "unaccountably often via till",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_hec_api": "<value>",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-source",
        "type": models.InputCriblType.CRIBL,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "filter_": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "colonialism gradient acknowledge hmph yuck astride boo but boo now",
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
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.update(id="<id>", input_={
        "id": "cribl-metrics-source",
        "type": models.InputCriblmetricsType.CRIBLMETRICS,
        "disabled": False,
        "pipeline": "<value>",
        "send_to_routes": True,
        "environment": "<value>",
        "pq_enabled": False,
        "streamtags": [
            "<value 1>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 1000,
            "commit_frequency": 42,
            "max_file_size": "1 MB",
            "max_size": "5GB",
            "path": "$CRIBL_HOME/state/queues",
            "compress": models.CompressionOptionsPq.NONE,
            "pq_controls": {},
        },
        "prefix": "cribl.logstream.",
        "full_fidelity": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "correctly biodegrade for zowie boo irk instead mockingly considering",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Source to update.                        |
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

Delete the specified Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteInputById" method="delete" path="/system/inputs/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
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

**[models.CountedInput](../../models/countedinput.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |