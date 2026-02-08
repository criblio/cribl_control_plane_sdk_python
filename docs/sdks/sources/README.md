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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 4887.41,
        "socket_idle_timeout": 2674.23,
        "socket_ending_max_wait": 7415.32,
        "socket_max_lifespan": 7847.75,
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
        "stale_channel_flush_ms": 3076.3,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://pointed-napkin.info/",
        },
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "repeatedly urban incidentally clean up",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "<value>",
        "visibility_timeout": 9845.2,
        "num_receivers": 7841.68,
        "max_messages": 2786.75,
        "service_period_secs": 3885.37,
        "skip_on_error": True,
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
        "stale_channel_flush_ms": 6690.08,
        "parquet_chunk_size_mb": 8742.16,
        "parquet_chunk_download_timeout": 5080,
        "auth_type": models.AuthenticationMethodOptions.SECRET,
        "description": "foodstuffs consequently cannibalise like an knowingly duffel gadzooks",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodCloudflareHec.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "culture reflate following hateful pike whose",
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 6936.75,
        "max_requests_per_socket": 226532,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 9442.97,
        "request_timeout": 5240.66,
        "socket_timeout": 9114.25,
        "keep_alive_timeout": 9265.08,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
            "<value 3>",
        ],
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 7807.01,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "emit_token_metrics": True,
        "description": "coaxingly probate slipper smoke aw meh of",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 5267.49,
        "preprocess": {
            "disabled": False,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "throttle_rate_per_sec": "<value>",
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
        ],
        connections=[
            models.ItemsTypeConnectionsOptional(
                pipeline="<value>",
                output="<value>",
            ),
        ],
        pq=models.PqType(
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=2055.73,
            commit_frequency=7905.42,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/bin",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        ),
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=False,
            schema_registry_url="https://ugly-availability.info",
            connection_timeout=8658.84,
            request_timeout=576.51,
            max_retries=7446.19,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
        ),
        connection_timeout=4267.71,
        request_timeout=3355.4,
        max_retries=7721.27,
        max_back_off=7462.03,
        initial_backoff=9154.04,
        backoff_rate=2946.47,
        authentication_timeout=1024.51,
        reauthentication_threshold=4426.91,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Etha51",
            password="XukwT9HxMYXOSPg",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.KERBEROS,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://swift-laughter.com",
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
        session_timeout=449.45,
        rebalance_timeout=8891,
        heartbeat_interval=6176.85,
        auto_commit_interval=4138.47,
        auto_commit_threshold=6728.18,
        max_bytes_per_partition=5098.28,
        max_bytes=1045.06,
        max_socket_errors=7315.82,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="violently throughout upwardly",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "with blah omelet pfft oddly bid regarding smuggle yuck goat",
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 2294.34,
        "max_requests_per_socket": 536087,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 8312.41,
        "request_timeout": 8291.86,
        "socket_timeout": 8516.65,
        "keep_alive_timeout": 4981.97,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "ha teriyaki prance",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 6791.17,
        "max_requests_per_socket": 816175,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 7079.71,
        "request_timeout": 5856.13,
        "socket_timeout": 3778.34,
        "keep_alive_timeout": 4936.4,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "cribl_api": "<value>",
        "elastic_api": "<value>",
        "splunk_hec_api": "<value>",
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
                "description": "neck below since blah whoa ridge",
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
        "description": "entice substantiate bossy",
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
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_cxn": 5339.54,
        "socket_idle_timeout": 7725.89,
        "socket_ending_max_wait": 7991.94,
        "socket_max_lifespan": 3827.27,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": True,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "with blah omelet pfft oddly bid regarding smuggle yuck goat",
            },
        ],
        "description": "cheerfully average lovingly meh heartfelt leading scratchy make courageously",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 8060.83,
        "max_messages": 1997.36,
        "visibility_timeout": 5226.76,
        "num_receivers": 8318.28,
        "socket_timeout": 2885.87,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1376.22,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": False,
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
            "retries": 7918.57,
        },
        "poll_timeout": 9197.78,
        "encoding": "<value>",
        "description": "brr zany ha understanding upbeat consequently invite newsstand though",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 8901.35,
        "max_requests_per_socket": 323919,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 9201.65,
        "request_timeout": 8623.93,
        "socket_timeout": 2668.82,
        "keep_alive_timeout": 5403.04,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "extract_metrics": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "proxy_mode": {
            "enabled": True,
            "reject_unauthorized": True,
        },
        "description": "meh vivacious geez however knight ah whenever bulky",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
        "description": "practical briefly through",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
        ],
        "discovery_type": models.DiscoveryTypeEdgePrometheus.STATIC,
        "interval": 60,
        "timeout": 1523.25,
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.CompressionOptionsPersistence.NONE,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodEdgePrometheus.SECRET,
        "description": "forenenst submitter individual french though analogy homeschool",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTP,
                "host": "localhost",
                "port": 5892.7,
                "path": "/opt/bin",
            },
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 9784.75,
        "name_list": [
            "<value 1>",
        ],
        "scrape_protocol": models.ProtocolOptionsTargetsItems.HTTP,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
        "search_filter": [
            {
                "name": "<value>",
                "values": [
                    "<value 1>",
                    "<value 2>",
                ],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7529.29,
        "scrape_protocol_expr": "<value>",
        "scrape_port_expr": "<value>",
        "scrape_path_expr": "<value>",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "true baseboard difficult accidentally even vainly pendant appropriate supposing meh",
            },
        ],
        "username": "Bret.Satterfield48",
        "password": "wQ8ho0Xc5FvvRdi",
        "credentials_secret": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 5262.84,
        "max_requests_per_socket": 560233,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 6514.74,
        "request_timeout": 9117.6,
        "socket_timeout": 8372.68,
        "keep_alive_timeout": 8300.75,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "elastic_api": "/",
        "auth_type": models.AuthenticationTypeElastic.AUTH_TOKENS,
        "api_version": models.CreateInputAPIVersion.CUSTOM,
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
            "auth_type": models.AuthenticationMethodElastic.SECRET,
            "username": "Nathanial_Vandervort",
            "password": "CBiRV0jzSu7ZO46",
            "credentials_secret": "<value>",
            "url": "https://minty-diver.name",
            "reject_unauthorized": True,
            "remove_headers": [
                "<value 1>",
            ],
            "timeout_sec": 7619.36,
        },
        "description": "mmm digital beneath summarise",
        "username": "Melyna_Wuckert61",
        "password": "kjFO782PUEcyGr_",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
        ],
        "custom_api_version": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
        "group_id": "<id>",
        "from_beginning": True,
        "connection_timeout": 4412.63,
        "request_timeout": 4590.77,
        "max_retries": 8313.38,
        "max_back_off": 3799.93,
        "initial_backoff": 1213.03,
        "backoff_rate": 6524.55,
        "authentication_timeout": 5485.95,
        "reauthentication_threshold": 5062.18,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "HuXGq8RA_UbNNDq",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Reina.Gutmann7",
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
            "disabled": True,
            "reject_unauthorized": True,
        },
        "session_timeout": 7156,
        "rebalance_timeout": 5931.63,
        "heartbeat_interval": 1103.94,
        "auto_commit_interval": 2956.72,
        "auto_commit_threshold": 8644.37,
        "max_bytes_per_partition": 2461.93,
        "max_bytes": 333.36,
        "max_socket_errors": 981.32,
        "minimize_duplicates": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "scale mmm lecture tag overfeed out nucleotidase",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 8796.61,
        "schedule_type": models.CreateInputScheduleType.INTERVAL,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 3310.64,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "weary throughout rotten um even",
        "interval": 60,
        "cron_schedule": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "mode": models.CreateInputInputFileMode.MANUAL,
        "interval": 1166.22,
        "filenames": [
            "<value 1>",
            "<value 2>",
        ],
        "filter_archived_files": True,
        "tail_only": True,
        "idle_timeout": 2482.99,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": False,
        "force_text": False,
        "hash_len": 7349.43,
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
        "stale_channel_flush_ms": 1810.26,
        "description": "sociable dime sympathetically provided jaywalk apud covenant",
        "path": "/home/user",
        "depth": 8602.37,
        "suppress_missing_path_errors": True,
        "delete_files": False,
        "salt_hash": True,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 6041.36,
        "max_requests_per_socket": 312291,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 6651.29,
        "request_timeout": 9017.19,
        "socket_timeout": 2313.05,
        "keep_alive_timeout": 5489.18,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "substantiate mortise yowza",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
        "monitor_subscription": False,
        "create_topic": False,
        "create_subscription": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.AUTO,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_backlog": 2713.89,
        "concurrency": 6818.77,
        "request_timeout": 1286.98,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "dramatic ouch if issue yuck diligent emotional",
        "ordered_delivery": True,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 4754.71,
        "max_requests_per_socket": 22276,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 1083.99,
        "request_timeout": 1977.59,
        "socket_timeout": 657.07,
        "keep_alive_timeout": 835.12,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/api/prom/push",
        "loki_api": "<value>",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.BASIC,
            "username": "Delbert_Yost21",
            "password": "X0GrESwkQOCR5y1",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
            "login_url": "https://mysterious-ruin.org",
            "secret_param_name": "<value>",
            "secret": "<value>",
            "token_attribute_name": "<value>",
            "auth_header_expr": "<value>",
            "token_timeout_secs": 8859.96,
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
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.TOKEN,
            "username": "Einar.Sawayn",
            "password": "QnAU6grcOdTFUeJ",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
            "login_url": "https://velvety-loyalty.net/",
            "secret_param_name": "<value>",
            "secret": "<value>",
            "token_attribute_name": "<value>",
            "auth_header_expr": "<value>",
            "token_timeout_secs": 8835.66,
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
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "solution satirise approximate psst jogging realistic greatly boohoo who curry",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 5123.99,
        "max_requests_per_socket": 286013,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 7569.11,
        "request_timeout": 2839.46,
        "socket_timeout": 5092.72,
        "keep_alive_timeout": 6429.04,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "cribl_api": "<value>",
        "elastic_api": "<value>",
        "splunk_hec_api": "<value>",
        "splunk_hec_acks": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "deeply very fiercely at total truthfully how frugal ah",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "voluminous lest guard distant ah custom masculinize multicolored proud",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 7394.97,
        "max_requests_per_socket": 313496,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4954.6,
        "request_timeout": 5720.36,
        "socket_timeout": 222.98,
        "keep_alive_timeout": 2239.85,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 1231.87,
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
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "deeply very fiercely at total truthfully how frugal ah",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "provider yet unsung past",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 5000.85,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "instead less till ew",
            },
        ],
        "current_boot": True,
        "max_age_dur": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "small phew before settler fortunately meh",
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
        disabled=True,
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
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=2055.73,
            commit_frequency=7905.42,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/bin",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=False,
            schema_registry_url="https://ugly-availability.info",
            connection_timeout=8658.84,
            request_timeout=576.51,
            max_retries=7446.19,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
        ),
        connection_timeout=9532.6,
        request_timeout=4317.54,
        max_retries=8891.09,
        max_back_off=5534.72,
        initial_backoff=6445.75,
        backoff_rate=575.57,
        authentication_timeout=6409.07,
        reauthentication_threshold=3829.31,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Etha51",
            password="XukwT9HxMYXOSPg",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.KERBEROS,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://swift-laughter.com",
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
        session_timeout=7980.65,
        rebalance_timeout=3256.62,
        heartbeat_interval=767.07,
        auto_commit_interval=1358.59,
        auto_commit_threshold=7136.81,
        max_bytes_per_partition=1942.41,
        max_bytes=9602.7,
        max_socket_errors=9414.81,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="too rebel convection low rebuild how commonly claw of",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 9559.98,
        "shard_expr": "<value>",
        "shard_iterator_type": models.CreateInputShardIteratorStart.TRIM_HORIZON,
        "payload_format": models.CreateInputRecordDataFormat.CRIBL,
        "get_records_limit": 9713.56,
        "get_records_limit_total": 4313.27,
        "load_balancing_algorithm": models.CreateInputShardLoadBalancing.ROUND_ROBIN,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V4,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1070.13,
        "verify_kpl_check_sums": False,
        "avoid_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "an eke vainly atop democratize per arrogantly gosh provision till",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "boo a yearly why genuine extroverted merry",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "barring sweetly whether wisely",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 9233.6,
        "rules": [
            {
                "filter_": "<value>",
                "description": "during microchip wallaby gracious beside till",
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.CompressionOptionsPersistence.NONE,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 9154.18,
        "enable_load_balancing": True,
        "description": "but uselessly whereas yum vet that while cautiously",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 2715.98,
        "rules": [
            {
                "filter_": "<value>",
                "description": "boo a yearly why genuine extroverted merry",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "description": "raw dream but to",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 1802.52,
        "max_requests_per_socket": 767657,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 2443.33,
        "request_timeout": 6185.88,
        "socket_timeout": 3691.15,
        "keep_alive_timeout": 1924.71,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "loki_api": "/loki/api/v1/push",
        "auth_type": models.AuthenticationTypeOptionsLokiAuth.TOKEN,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "which until yet",
        "username": "Elvera33",
        "password": "t1aJbdykpwYIGuq",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://glum-plugin.com",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 4899.83,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 5345.44,
        "max_buffer_size": 6534.85,
        "ip_whitelist_regex": "<value>",
        "enable_proxy_header": True,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 3564.68,
        "description": "supposing joyful investigate what",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 7010.9,
        "shutdown_timeout_ms": 8181.4,
        "description": "equally however advocate deduce thoughtfully muted categorise inasmuch suddenly",
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
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=2055.73,
            commit_frequency=7905.42,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/bin",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        session_timeout=4833.32,
        rebalance_timeout=2186.74,
        heartbeat_interval=9509.09,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=False,
            schema_registry_url="https://ugly-availability.info",
            connection_timeout=8658.84,
            request_timeout=576.51,
            max_retries=7446.19,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            ),
        ),
        connection_timeout=5413.46,
        request_timeout=6448.74,
        max_retries=8060.95,
        max_back_off=9433.89,
        initial_backoff=5411.14,
        backoff_rate=4695.65,
        authentication_timeout=1757.27,
        reauthentication_threshold=2863.12,
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
        duration_seconds=5932.72,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
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
        auto_commit_interval=7946.06,
        auto_commit_threshold=6583.38,
        max_bytes_per_partition=9381.06,
        max_bytes=734,
        max_socket_errors=2148.16,
        description="curry softly ack reconstitute failing against yet phooey via",
        aws_api_key="<value>",
        aws_secret="<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "udp_socket_rx_buf_size": 3658.46,
        "template_cache_minutes": 1855.48,
        "v5_enabled": True,
        "v9_enabled": False,
        "ipfix_enabled": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "muscat coil greatly badly outrank represent around",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 3487.37,
        "keep_alive_time": 3940.22,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 8407.86,
        "ttl": "<value>",
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
                "description": "outflank clean classic how capsize inasmuch adolescent microblog pish",
                "interval": 9559.88,
                "log_level": models.LogLevelOptionsContentConfigItems.WARN,
                "enabled": False,
            },
        ],
        "ingestion_lag": 7747.69,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 9780.72,
            "limit": 2123.94,
            "multiplier": 107.05,
            "codes": [
                4202.47,
                9242.01,
                2793.86,
            ],
            "enable_header": True,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.SECRET,
        "description": "whoever whose gee blah huzzah",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 7116.75,
        "disable_time_filter": True,
        "auth_type": models.AuthenticationMethodOffice365MsgTrace.OAUTH,
        "reschedule_dropped_tasks": True,
        "max_task_reschedule": 699.11,
        "log_level": models.LogLevelOffice365MsgTrace.WARN,
        "job_timeout": "<value>",
        "keep_alive_time": 7208.8,
        "max_missed_keep_alives": 557.68,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 9780.72,
            "limit": 2123.94,
            "multiplier": 107.05,
            "codes": [
                4202.47,
                9242.01,
                2793.86,
            ],
            "enable_header": True,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "description": "deflate woefully or robust over impact",
        "username": "Shaun.Bruen-Weimann",
        "password": "rhOhmiS7N3YIiLF",
        "credentials_secret": "<value>",
        "client_secret": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "resource": "<value>",
        "plan_type": models.SubscriptionPlanOptions.GCC_HIGH,
        "text_secret": "<value>",
        "cert_options": {
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
        },
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.DOD,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 6785.41,
        "keep_alive_time": 9440.55,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 2351.7,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "content_config": [
            {
                "content_type": "<value>",
                "description": "heavily sharply brook misjudge legitimize",
                "interval": 1247.02,
                "log_level": models.LogLevelOptionsContentConfigItems.WARN,
                "enabled": True,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 9780.72,
            "limit": 2123.94,
            "multiplier": 107.05,
            "codes": [
                4202.47,
                9242.01,
                2793.86,
            ],
            "enable_header": True,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "above gallivant finally",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 4380.05,
        "max_requests_per_socket": 446963,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 7040.74,
        "socket_timeout": 3566.12,
        "keep_alive_timeout": 58.19,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "protocol": models.CreateInputProtocol.HTTP,
        "extract_spans": True,
        "extract_metrics": False,
        "otlp_version": models.CreateInputOTLPVersion.ZERO_DOT_10_DOT_0,
        "auth_type": models.AuthenticationTypeOptions.BASIC,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 4758.14,
        "description": "furthermore while shampoo",
        "username": "Demetrius_Bernhard28",
        "password": "_HgrUnh66BPfzNt",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://alienated-cork.org/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 9512.38,
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
        "extract_logs": False,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
        ],
        "discovery_type": models.DiscoveryTypePrometheus.STATIC,
        "interval": 60,
        "log_level": models.LogLevelPrometheus.INFO,
        "reject_unauthorized": False,
        "timeout": 3147.32,
        "keep_alive_time": 305.84,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 2520.89,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.SECRET,
        "description": "barring anxiously break lavish whoa while really until",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 4700.87,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "scrape_protocol": models.CreateInputMetricsProtocol.HTTPS,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
        "search_filter": [
            {
                "name": "<value>",
                "values": [
                    "<value 1>",
                    "<value 2>",
                ],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V2,
        "reuse_connections": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 9002.52,
        "username": "Luciano_Fisher99",
        "password": "XWKuXRnFB74TRlD",
        "credentials_secret": "<value>",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 9688.99,
        "max_requests_per_socket": 95126,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4199.2,
        "request_timeout": 4007.06,
        "socket_timeout": 2378.84,
        "keep_alive_timeout": 3340.99,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "ugh frank wire circa",
        "username": "Keon93",
        "password": "Ph2diZRCGCwQh2B",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://cruel-bungalow.biz",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 7358.94,
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 2988.09,
        "ip_whitelist_regex": "<value>",
        "single_msg_udp_packets": True,
        "ingest_raw_bytes": True,
        "udp_socket_rx_buf_size": 3299.36,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "following cow shrilly lavish norm yahoo torn parsnip",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 7117.24,
        "max_messages": 7261.65,
        "visibility_timeout": 7076.16,
        "num_receivers": 3607.82,
        "socket_timeout": 434.52,
        "skip_on_error": True,
        "include_sqs_metadata": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8815.56,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": False,
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
        "parquet_chunk_size_mb": 7027.44,
        "parquet_chunk_download_timeout": 8114.55,
        "checkpointing": {
            "enabled": False,
            "retries": 7918.57,
        },
        "poll_timeout": 4127.07,
        "encoding": "<value>",
        "tag_after_processing": True,
        "description": "gah lest whoever wisely",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-inventory-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 2887.68,
        "max_messages": 437.47,
        "visibility_timeout": 2102.66,
        "num_receivers": 6213.22,
        "socket_timeout": 6368.62,
        "skip_on_error": True,
        "include_sqs_metadata": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2187.22,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": False,
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
        "parquet_chunk_size_mb": 8498.54,
        "parquet_chunk_download_timeout": 2090.07,
        "checkpointing": {
            "enabled": False,
            "retries": 7918.57,
        },
        "poll_timeout": 9820.73,
        "checksum_suffix": "<value>",
        "max_manifest_size_kb": 713420,
        "validate_inventory_files": False,
        "description": "woot what greedily blah until content along corner",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "security-lake-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 7998.97,
        "max_messages": 9902.64,
        "visibility_timeout": 6703.9,
        "num_receivers": 8995.16,
        "socket_timeout": 3363.78,
        "skip_on_error": False,
        "include_sqs_metadata": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6949.93,
        "enable_sqs_assume_role": True,
        "preprocess": {
            "disabled": False,
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
        "parquet_chunk_size_mb": 1512.5,
        "parquet_chunk_download_timeout": 4251.17,
        "checkpointing": {
            "enabled": False,
            "retries": 7918.57,
        },
        "poll_timeout": 5816.86,
        "encoding": "<value>",
        "description": "round since extra-large however tidy",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "192.168.1.1",
        "port": 161,
        "snmp_v3_auth": {
            "v3_auth_enabled": True,
            "allow_unmatched_trap": True,
            "v3_users": [
                {
                    "name": "<value>",
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.SHA384,
                    "auth_key": "<value>",
                    "priv_protocol": models.CreateInputPrivacyProtocol.NONE,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 6992.98,
        "ip_whitelist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 6052.66,
        "varbinds_with_types": True,
        "best_effort_parsing": False,
        "description": "yuck enthusiastically idolized now slowly disconnection crystallize than without besides",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 8429.15,
        "socket_idle_timeout": 5466.61,
        "socket_ending_max_wait": 1428.04,
        "socket_max_lifespan": 478.3,
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
        "stale_channel_flush_ms": 4231.52,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "descendant absent although mortally",
            },
        ],
        "max_s2_sversion": models.CreateInputMaxS2SVersion.V3,
        "description": "yahoo only formamide qua midst culminate creak lest",
        "use_fwd_timezone": True,
        "drop_control_fields": False,
        "extract_metrics": False,
        "compress": models.CreateInputCompression.ALWAYS,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": False,
                "description": "ack swiftly unscramble parody psst during stylish gum",
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 4327.63,
        "max_requests_per_socket": 198812,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 5619.85,
        "request_timeout": 2281.35,
        "socket_timeout": 3620.99,
        "keep_alive_timeout": 7989.57,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
        "stale_channel_flush_ms": 1561.91,
        "use_fwd_timezone": False,
        "drop_control_fields": True,
        "extract_metrics": True,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "emit_token_metrics": False,
        "description": "prioritize polarisation bourgeoisie decongestant behind degenerate turret exotic murky",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "earliest": "<value>",
        "latest": "<value>",
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
        "log_level": models.LogLevelSplunkSearch.WARN,
        "request_timeout": 1700.92,
        "use_round_robin_dns": True,
        "reject_unauthorized": False,
        "encoding": "<value>",
        "keep_alive_time": 9155.6,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 6019.15,
        "ttl": "<value>",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.NONE,
            "interval": 7746.55,
            "limit": 2960.85,
            "multiplier": 5912.74,
            "codes": [
                4045.69,
                7782.74,
                6687.35,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 9405.7,
        "auth_type": models.AuthenticationTypeSplunkSearch.BASIC,
        "description": "plugin roughly aboard hourly descendant pfft whoa",
        "username": "Terrance_Wolff-Roberts",
        "password": "DYJItRIXcRsFuTU",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://unaware-bar.biz",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 3722.95,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "my-queue",
        "queue_type": models.CreateInputQueueType.STANDARD,
        "aws_account_id": "<id>",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7049.71,
        "max_messages": 2368.62,
        "visibility_timeout": 2367.72,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 1405.07,
        "description": "instead afterwards who consequently",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 6199.83,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 2282.1,
        "max_buffer_size": 3011.12,
        "ip_whitelist_regex": "<value>",
        "timestamp_timezone": "<value>",
        "single_msg_udp_packets": False,
        "enable_proxy_header": True,
        "keep_fields_list": [
            "<value 1>",
            "<value 2>",
        ],
        "octet_counting": False,
        "infer_framing": True,
        "strictly_infer_octet_counting": False,
        "allow_non_standard_app_name": True,
        "max_active_cxn": 3194.4,
        "socket_idle_timeout": 1333.98,
        "socket_ending_max_wait": 8139.96,
        "socket_max_lifespan": 9377.11,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 7376.65,
        "enable_load_balancing": True,
        "description": "wavy however incidentally ownership valiantly climb tame",
        "enable_enhanced_proxy_header_parsing": False,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 688.04,
        "host": {
            "mode": models.ModeOptionsHost.CUSTOM,
            "custom": {
                "system": {
                    "mode": models.SystemModeSystemMetrics.CUSTOM,
                    "processes": True,
                },
                "cpu": {
                    "mode": models.CPUModeSystemMetrics.BASIC,
                    "per_cpu": False,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.MemoryModeSystemMetrics.CUSTOM,
                    "detail": False,
                },
                "network": {
                    "mode": models.NetworkModeSystemMetrics.CUSTOM,
                    "detail": False,
                    "protocols": True,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_interface": True,
                },
                "disk": {
                    "mode": models.DiskModeSystemMetrics.BASIC,
                    "detail": False,
                    "inodes": True,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "mountpoints": [
                        "<value 1>",
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
            "mode": models.ContainerModeSystemMetrics.DISABLED,
            "docker_socket": [
                "<value 1>",
            ],
            "docker_timeout": 9193.24,
            "filters": [
                {
                    "expr": "<value>",
                },
            ],
            "all_containers": False,
            "per_device": False,
            "detail": True,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "description": "into hmph bah clean which status cannon lively",
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
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 4335.6,
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
                "enable": False,
            },
            "disk": {
                "enable": True,
            },
            "metadata": {
                "enable": True,
            },
            "routes": {
                "enable": False,
            },
            "dns": {
                "enable": True,
            },
            "user": {
                "enable": False,
            },
            "firewall": {
                "enable": False,
            },
            "services": {
                "enable": False,
            },
            "ports": {
                "enable": False,
            },
            "login_users": {
                "enable": True,
            },
        },
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "disable_native_module": False,
        "disable_native_last_log_module": False,
        "description": "plus merit the",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 2458.75,
        "socket_idle_timeout": 6864.89,
        "socket_ending_max_wait": 9734.82,
        "socket_max_lifespan": 880.4,
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
        "stale_channel_flush_ms": 5128.48,
        "enable_header": False,
        "preprocess": {
            "disabled": False,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "description": "ape snoopy equally common er provider concerning unimpressively pish",
        "auth_token": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "text_secret": "<value>",
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
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": False,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 6182.84,
        "socket_idle_timeout": 5228.06,
        "socket_ending_max_wait": 1333.88,
        "socket_max_lifespan": 3762.69,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "ouch under even who dissemble gratefully slushy deceivingly",
        "auth_token": "<value>",
        "text_secret": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.AuthenticationMethodWef.KERBEROS,
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "request_cert": False,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "common_name_regex": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "ocsp_check": False,
            "keytab": "<value>",
            "principal": "<value>",
            "ocsp_check_fail_close": True,
        },
        "max_active_req": 9267.54,
        "max_requests_per_socket": 505940,
        "enable_proxy_header": False,
        "capture_headers": False,
        "keep_alive_timeout": 1430.74,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "socket_timeout": 5061.11,
        "ca_fingerprint": "<value>",
        "keytab": "<value>",
        "principal": "<value>",
        "allow_machine_id_mismatch": True,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "version": "<value>",
                "content_format": models.CreateInputFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "read_existing_events": True,
                "send_bookmarks": True,
                "compress": True,
                "targets": [],
                "locale": "de",
                "query_selector": models.CreateInputQueryBuilderMode.SIMPLE,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/home/user/dir",
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
        "description": "mockingly tenderly impressive scarification border ring",
        "log_fingerprint_mismatch": False,
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.CreateInputReadMode.NEWEST,
        "event_format": models.CreateInputEventFormat.XML,
        "disable_native_module": True,
        "interval": 852.74,
        "batch_size": 5653.41,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 4593.26,
        "description": "citizen premeditation dismal",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 5250.98,
        "host": {
            "mode": models.ModeOptionsHost.CUSTOM,
            "custom": {
                "system": {
                    "mode": models.SystemModeWindowsMetrics.BASIC,
                    "detail": True,
                },
                "cpu": {
                    "mode": models.CPUModeWindowsMetrics.CUSTOM,
                    "per_cpu": True,
                    "detail": False,
                    "time": True,
                },
                "memory": {
                    "mode": models.MemoryModeWindowsMetrics.BASIC,
                    "detail": True,
                },
                "network": {
                    "mode": models.NetworkModeWindowsMetrics.DISABLED,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.DiskModeWindowsMetrics.BASIC,
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "disable_native_module": True,
        "description": "soon out when towards sometimes",
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 1355.21,
        "keep_alive_time": 2315.99,
        "max_missed_keep_alives": 5797.18,
        "ttl": "<value>",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.NONE,
            "interval": 7746.55,
            "limit": 2960.85,
            "multiplier": 5912.74,
            "codes": [
                4045.69,
                7782.74,
                6687.35,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "gad wisecrack that meaningfully wherever",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 2391.82,
        "max_requests_per_socket": 444294,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 7567.99,
        "request_timeout": 3218.14,
        "socket_timeout": 2243.35,
        "keep_alive_timeout": 989.04,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 8737.45,
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
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "deeply very fiercely at total truthfully how frugal ah",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "veg anenst underpants degenerate",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 2055.73,
            "commit_frequency": 7905.42,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/bin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": False,
                "description": "about garrote complication gee woot",
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
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
        },
        "max_active_req": 4348.05,
        "max_requests_per_socket": 172464,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 9777.07,
        "request_timeout": 3114.25,
        "socket_timeout": 5229.35,
        "keep_alive_timeout": 4629.12,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
        "hec_acks": True,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": False,
        "description": "self-reliant nautical fold",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 3417.54,
        "socket_idle_timeout": 4799.95,
        "socket_ending_max_wait": 3730.65,
        "socket_max_lifespan": 4634.53,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 3362.61,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://distorted-translation.org/",
        },
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "incidentally down versus blah",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "<value>",
        "visibility_timeout": 5294.27,
        "num_receivers": 3992.62,
        "max_messages": 5686.02,
        "service_period_secs": 8039.05,
        "skip_on_error": True,
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
        "stale_channel_flush_ms": 9969.24,
        "parquet_chunk_size_mb": 1561.4,
        "parquet_chunk_download_timeout": 1595.41,
        "auth_type": models.AuthenticationMethodOptions.SECRET,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
                "description": "viciously left knuckle finally likewise before",
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 3960.65,
        "max_requests_per_socket": 684894,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 5621.37,
        "request_timeout": 8713.82,
        "socket_timeout": 8592.43,
        "keep_alive_timeout": 2174.26,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
        "stale_channel_flush_ms": 8605.29,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
        ],
        "emit_token_metrics": True,
        "description": "discourse into phooey fledgling along or since gadzooks purse",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 8452.47,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "throttle_rate_per_sec": "<value>",
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
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=9959.95,
            commit_frequency=4085.76,
            max_file_size="<value>",
            max_size="<value>",
            path="/usr/obj",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=True,
            schema_registry_url="https://concrete-petal.info",
            connection_timeout=2814.06,
            request_timeout=7605.14,
            max_retries=8934.79,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
        ),
        connection_timeout=6822.45,
        request_timeout=1289.1,
        max_retries=124.52,
        max_back_off=9242.82,
        initial_backoff=9313.77,
        backoff_rate=2563.57,
        authentication_timeout=4547.37,
        reauthentication_threshold=670.16,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Ruben.Prosacco",
            password="9KZ67ITYDbrbAZJ",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://brilliant-sustenance.net",
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
        session_timeout=2651.67,
        rebalance_timeout=8421.5,
        heartbeat_interval=5595.6,
        auto_commit_interval=2888.32,
        auto_commit_threshold=4884.37,
        max_bytes_per_partition=2952.38,
        max_bytes=9163.66,
        max_socket_errors=4977.5,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="furthermore pfft pace vague behold despite boulevard corrupt",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": True,
                "description": "fatal every rebuke ew forenenst millet",
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 539.26,
        "max_requests_per_socket": 239267,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 6330.35,
        "request_timeout": 6630.19,
        "socket_timeout": 2059.35,
        "keep_alive_timeout": 9652.08,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "wearily innovation proliferate tomorrow appliance",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 242.74,
        "max_requests_per_socket": 851306,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 8524.32,
        "request_timeout": 1684.81,
        "socket_timeout": 7908.19,
        "keep_alive_timeout": 6036.75,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "cribl_api": "<value>",
        "elastic_api": "<value>",
        "splunk_hec_api": "<value>",
        "splunk_hec_acks": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "before whereas provided although bore furthermore only closely deduce tousle",
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
                        "<value 3>",
                    ],
                },
                "elasticsearch_metadata": {
                    "enabled": True,
                    "default_dataset": "<value>",
                },
            },
        ],
        "description": "shrill for without lend awkwardly waft forgo monster service athletic",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_cxn": 8039.05,
        "socket_idle_timeout": 9275.52,
        "socket_ending_max_wait": 2495.06,
        "socket_max_lifespan": 858.03,
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
                "description": "fatal every rebuke ew forenenst millet",
            },
        ],
        "description": "supposing past honesty gah made-up solace bouncy which comfortable",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 7932.13,
        "max_messages": 999.63,
        "visibility_timeout": 554.2,
        "num_receivers": 3598.43,
        "socket_timeout": 256.82,
        "skip_on_error": True,
        "include_sqs_metadata": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3919.57,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
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
            "retries": 3583.79,
        },
        "poll_timeout": 2925.13,
        "encoding": "<value>",
        "description": "alert bungalow with obligation supposing twine halt tomography basic rowdy",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 9127.42,
        "max_requests_per_socket": 469633,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 2292.96,
        "request_timeout": 5623.59,
        "socket_timeout": 7916.97,
        "keep_alive_timeout": 2802.22,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
        "description": "tune-up sparkling assist impact",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
        "description": "duh calmly meander unfortunately upright wise zowie inside inasmuch until",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
        ],
        "discovery_type": models.InputEdgePrometheusDiscoveryType.STATIC,
        "interval": 60,
        "timeout": 7086.07,
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.CompressionOptionsPersistence.NONE,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.InputEdgePrometheusAuthenticationMethod.SECRET,
        "description": "though refine fully though because insist eek ick lest finally",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTPS,
                "host": "localhost",
                "port": 6264.12,
                "path": "/selinux",
            },
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 5626.37,
        "name_list": [
            "<value 1>",
        ],
        "scrape_protocol": models.ProtocolOptionsTargetsItems.HTTP,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
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
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8251.32,
        "scrape_protocol_expr": "<value>",
        "scrape_port_expr": "<value>",
        "scrape_path_expr": "<value>",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "flashy ick phony while who membership shell yesterday testimonial",
            },
        ],
        "username": "Carlos.Heaney67",
        "password": "gtl6f_Qdi1zxAJl",
        "credentials_secret": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 7696.27,
        "max_requests_per_socket": 8041,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 5052.41,
        "request_timeout": 7221.64,
        "socket_timeout": 3356.99,
        "keep_alive_timeout": 5056.05,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "elastic_api": "/",
        "auth_type": models.InputElasticAuthenticationType.CREDENTIALS_SECRET,
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
            "username": "Constance.Kuhlman",
            "password": "tfyqTaaDTgjB6pd",
            "credentials_secret": "<value>",
            "url": "https://fuzzy-mortise.info",
            "reject_unauthorized": False,
            "remove_headers": [
                "<value 1>",
                "<value 2>",
            ],
            "timeout_sec": 5673.09,
        },
        "description": "dependent cheerful hm plus qua developmental",
        "username": "Nat23",
        "password": "UtJZmJA2OMhDFcq",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "custom_api_version": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "brokers": [
            "myeventhub.servicebus.windows.net:9093",
        ],
        "topics": [
            "logs",
        ],
        "group_id": "<id>",
        "from_beginning": False,
        "connection_timeout": 2907.13,
        "request_timeout": 2951.08,
        "max_retries": 4807.76,
        "max_back_off": 2878.21,
        "initial_backoff": 5301.79,
        "backoff_rate": 7736.65,
        "authentication_timeout": 3975.06,
        "reauthentication_threshold": 3120.04,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "lzctsKxgHZhl5Rc",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Edmond.Konopelski31",
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
            "disabled": True,
            "reject_unauthorized": False,
        },
        "session_timeout": 8555.39,
        "rebalance_timeout": 1021.76,
        "heartbeat_interval": 3760.74,
        "auto_commit_interval": 1722.38,
        "auto_commit_threshold": 6339.7,
        "max_bytes_per_partition": 7169.23,
        "max_bytes": 8824.56,
        "max_socket_errors": 402.82,
        "minimize_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "furthermore frantically solvency likable after brr meh freely",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 9861.97,
        "schedule_type": models.ScheduleType.CRON_SCHEDULE,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 7410.31,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "though seriously per",
        "interval": 60,
        "cron_schedule": "<value>",
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "mode": models.InputFileMode.MANUAL,
        "interval": 6083.7,
        "filenames": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "filter_archived_files": False,
        "tail_only": True,
        "idle_timeout": 2495.48,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": True,
        "force_text": True,
        "hash_len": 6484.64,
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
        "stale_channel_flush_ms": 1432.48,
        "description": "ah afore however present hence what zowie",
        "path": "/usr/bin",
        "depth": 17.47,
        "suppress_missing_path_errors": False,
        "delete_files": False,
        "salt_hash": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 7597.77,
        "max_requests_per_socket": 759138,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 6878.65,
        "request_timeout": 4516.36,
        "socket_timeout": 2537.94,
        "keep_alive_timeout": 3392.09,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "sure-footed well-groomed monthly",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
        "max_backlog": 335.09,
        "concurrency": 6007.89,
        "request_timeout": 33.62,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "yuck redraw psst from mmm till",
        "ordered_delivery": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 4763.99,
        "max_requests_per_socket": 541461,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 1768.11,
        "request_timeout": 5812.82,
        "socket_timeout": 8267.83,
        "keep_alive_timeout": 4628.16,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/api/prom/push",
        "loki_api": "<value>",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.OAUTH,
            "username": "Laverne.Legros28",
            "password": "l9hg6sbGombuWWq",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
            "login_url": "https://self-reliant-millet.org",
            "secret_param_name": "<value>",
            "secret": "<value>",
            "token_attribute_name": "<value>",
            "auth_header_expr": "<value>",
            "token_timeout_secs": 1339.18,
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
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.BASIC,
            "username": "Jordane.Hartmann3",
            "password": "_qO39ImWhkAe8Pw",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
            "login_url": "https://realistic-league.name/",
            "secret_param_name": "<value>",
            "secret": "<value>",
            "token_attribute_name": "<value>",
            "auth_header_expr": "<value>",
            "token_timeout_secs": 1463.81,
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
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "aha inject winged even incandescence",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 1811.74,
        "max_requests_per_socket": 83718,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 3908.2,
        "request_timeout": 9581.8,
        "socket_timeout": 3433.67,
        "keep_alive_timeout": 1522.09,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "cribl_api": "<value>",
        "elastic_api": "<value>",
        "splunk_hec_api": "<value>",
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
                "description": "unless scuttle pixellate hm aw furthermore tensely pro how beloved",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "furthermore than pomelo supposing underneath spring smoothly brightly sew",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 4057.64,
        "max_requests_per_socket": 209241,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 9045.22,
        "request_timeout": 6925,
        "socket_timeout": 6768.3,
        "keep_alive_timeout": 2802.36,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 9818.06,
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
            "<value 3>",
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "unless scuttle pixellate hm aw furthermore tensely pro how beloved",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "than helpfully adjourn shoulder gee beside preregister",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 9499.26,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "pocket-watch given fondly abaft fluctuate whoever punctuation simple",
            },
        ],
        "current_boot": True,
        "max_age_dur": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "electronics yahoo phew drat boo",
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
        disabled=True,
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
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=9959.95,
            commit_frequency=4085.76,
            max_file_size="<value>",
            max_size="<value>",
            path="/usr/obj",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "localhost:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=True,
            schema_registry_url="https://concrete-petal.info",
            connection_timeout=2814.06,
            request_timeout=7605.14,
            max_retries=8934.79,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
        ),
        connection_timeout=3528.96,
        request_timeout=2367.78,
        max_retries=3399.14,
        max_back_off=2734.39,
        initial_backoff=1990.67,
        backoff_rate=5356.6,
        authentication_timeout=9107.44,
        reauthentication_threshold=9458.51,
        sasl=models.AuthenticationType(
            disabled=True,
            username="Ruben.Prosacco",
            password="9KZ67ITYDbrbAZJ",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://brilliant-sustenance.net",
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
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        session_timeout=4767.62,
        rebalance_timeout=9493.08,
        heartbeat_interval=8352.03,
        auto_commit_interval=8572.75,
        auto_commit_threshold=9008.21,
        max_bytes_per_partition=196.45,
        max_bytes=4443.15,
        max_socket_errors=9682.16,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="gee anaesthetise through deployment oh where drat snoop excepting inquisitively",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 1279.68,
        "shard_expr": "<value>",
        "shard_iterator_type": models.ShardIteratorStart.TRIM_HORIZON,
        "payload_format": models.RecordDataFormat.LINE,
        "get_records_limit": 7102.12,
        "get_records_limit_total": 9693.93,
        "load_balancing_algorithm": models.ShardLoadBalancing.CONSISTENT_HASHING,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V2,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 913.04,
        "verify_kpl_check_sums": False,
        "avoid_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "whose husky slink where woefully shallow",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "voluntarily on ack scornful narrowcast",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "stunt entice failing owlishly scout waterspout swine upon clamp",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 247.56,
        "rules": [
            {
                "filter_": "<value>",
                "description": "persecute anenst although source overfeed joint",
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.CompressionOptionsPersistence.NONE,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 8820.92,
        "enable_load_balancing": False,
        "description": "affect so ah lotion since sheathe",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 8394.01,
        "rules": [
            {
                "filter_": "<value>",
                "description": "voluntarily on ack scornful narrowcast",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "description": "before beneficial versus between instead",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 9872.6,
        "max_requests_per_socket": 492856,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 9146.1,
        "request_timeout": 8080.01,
        "socket_timeout": 4630.89,
        "keep_alive_timeout": 1005.63,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "loki_api": "/loki/api/v1/push",
        "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "reference yuck marimba analogy excess pish defiantly investigate mill sate",
        "username": "Renee_Daugherty",
        "password": "NM_vAnZWTlo0qt1",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://subdued-forager.com",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 1181.96,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 3455.14,
        "max_buffer_size": 2139.64,
        "ip_whitelist_regex": "<value>",
        "enable_proxy_header": False,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 4021.68,
        "description": "than in unaware concerning upright fencing deserted",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 1719.64,
        "shutdown_timeout_ms": 2136.89,
        "description": "pfft considering outlandish in bah yearly aw pharmacopoeia",
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
        disabled=True,
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
            mode=models.ModeOptionsPq.SMART,
            max_buffer_size=9959.95,
            commit_frequency=4085.76,
            max_file_size="<value>",
            max_size="<value>",
            path="/usr/obj",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
        brokers=[
            "b-1.example.xxxxx.c2.kafka.us-east-1.amazonaws.com:9092",
        ],
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=False,
        session_timeout=7039.27,
        rebalance_timeout=4496.31,
        heartbeat_interval=9974.47,
        metadata=[
            models.ItemsTypeNotificationMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=True,
            schema_registry_url="https://concrete-petal.info",
            connection_timeout=2814.06,
            request_timeout=7605.14,
            max_retries=8934.79,
            auth=models.AuthTypeKafkaSchemaRegistry(
                disabled=False,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            ),
        ),
        connection_timeout=9662.16,
        request_timeout=2520.43,
        max_retries=2222.88,
        max_back_off=5072.84,
        initial_backoff=9386.56,
        backoff_rate=5006.78,
        authentication_timeout=7646.22,
        reauthentication_threshold=6817.9,
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
        duration_seconds=8819.58,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=True,
            reject_unauthorized=True,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
        ),
        auto_commit_interval=37.9,
        auto_commit_threshold=1117.15,
        max_bytes_per_partition=7867.13,
        max_bytes=195.75,
        max_socket_errors=4728.15,
        description="until uh-huh grandiose notwithstanding via",
        aws_api_key="<value>",
        aws_secret="<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "udp_socket_rx_buf_size": 5371.74,
        "template_cache_minutes": 9557.55,
        "v5_enabled": True,
        "v9_enabled": False,
        "ipfix_enabled": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "pfft tusk until fiercely",
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
            "<value 3>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 483.16,
        "keep_alive_time": 549.83,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 5203.37,
        "ttl": "<value>",
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
                "description": "geez absent paintwork yippee evenly providence ha hover aw buzzing",
                "interval": 3262.39,
                "log_level": models.LogLevelOptionsContentConfigItems.INFO,
                "enabled": True,
            },
        ],
        "ingestion_lag": 3768.67,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 676.59,
            "limit": 6017.19,
            "multiplier": 1187.9,
            "codes": [
                9919.4,
                6531.17,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "positively indeed sizzle consequently swelter midst including",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 6172.32,
        "disable_time_filter": True,
        "auth_type": models.InputOffice365MsgTraceAuthenticationMethod.OAUTH_CERT,
        "reschedule_dropped_tasks": True,
        "max_task_reschedule": 82.22,
        "log_level": models.InputOffice365MsgTraceLogLevel.ERROR,
        "job_timeout": "<value>",
        "keep_alive_time": 218.99,
        "max_missed_keep_alives": 652.94,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 676.59,
            "limit": 6017.19,
            "multiplier": 1187.9,
            "codes": [
                9919.4,
                6531.17,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "description": "outfox absent pecan however why almighty failing",
        "username": "Carole_Medhurst86",
        "password": "fmYMLhi4cpq7mal",
        "credentials_secret": "<value>",
        "client_secret": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "resource": "<value>",
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "text_secret": "<value>",
        "cert_options": {
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
        },
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 6169.37,
        "keep_alive_time": 4019.57,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 474.64,
        "ttl": "<value>",
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
                "description": "ah whenever unlike bookcase towards gadzooks honestly",
                "interval": 6065.54,
                "log_level": models.LogLevelOptionsContentConfigItems.WARN,
                "enabled": False,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 676.59,
            "limit": 6017.19,
            "multiplier": 1187.9,
            "codes": [
                9919.4,
                6531.17,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.SECRET,
        "description": "following nice of till whose gadzooks",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 2734.59,
        "max_requests_per_socket": 231358,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 3507.86,
        "socket_timeout": 8180.94,
        "keep_alive_timeout": 3269.77,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "protocol": models.InputOpenTelemetryProtocol.HTTP,
        "extract_spans": True,
        "extract_metrics": False,
        "otlp_version": models.InputOpenTelemetryOTLPVersion.ONE_DOT_3_DOT_1,
        "auth_type": models.AuthenticationTypeOptions.CREDENTIALS_SECRET,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 3610.61,
        "description": "poorly on reckon joyously",
        "username": "Eleanore_Lockman27",
        "password": "fbcKwHWOY7xmVhY",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://round-help.com",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 958.28,
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
        "extract_logs": True,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "discovery_type": models.InputPrometheusDiscoveryType.STATIC,
        "interval": 60,
        "log_level": models.InputPrometheusLogLevel.INFO,
        "reject_unauthorized": False,
        "timeout": 6391.07,
        "keep_alive_time": 5417.12,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 7932.03,
        "ttl": "<value>",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.MANUAL,
        "description": "so wherever after polarisation by backbone hoarse which duh inside",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 8978.36,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "scrape_protocol": models.MetricsProtocol.HTTPS,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
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
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6388.96,
        "username": "Brenden_Reynolds97",
        "password": "KmtcztBL2FtzSkj",
        "credentials_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 86.47,
        "max_requests_per_socket": 665371,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 7550.39,
        "request_timeout": 133.32,
        "socket_timeout": 798.3,
        "keep_alive_timeout": 899.7,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.BASIC,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "circa legitimize since along gah chapel when controvert overcharge",
        "username": "Ernesto.Rodriguez",
        "password": "332YGCpd1VZujJu",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://perky-bin.biz/",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 9331.96,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 6951.72,
        "ip_whitelist_regex": "<value>",
        "single_msg_udp_packets": True,
        "ingest_raw_bytes": True,
        "udp_socket_rx_buf_size": 3490.77,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "testing king knottily magnetize um meh tepid",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 5497.69,
        "max_messages": 1410.35,
        "visibility_timeout": 1210.91,
        "num_receivers": 5475.5,
        "socket_timeout": 1024.79,
        "skip_on_error": True,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 796.75,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 4479.73,
        "parquet_chunk_download_timeout": 9106.64,
        "checkpointing": {
            "enabled": False,
            "retries": 3583.79,
        },
        "poll_timeout": 859.89,
        "encoding": "<value>",
        "tag_after_processing": False,
        "description": "after airbrush oh ick safely essay",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-inventory-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 8110.89,
        "max_messages": 3914.52,
        "visibility_timeout": 7725.89,
        "num_receivers": 6531.06,
        "socket_timeout": 2786.87,
        "skip_on_error": True,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 2863.98,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 4137.96,
        "parquet_chunk_download_timeout": 1617.35,
        "checkpointing": {
            "enabled": False,
            "retries": 3583.79,
        },
        "poll_timeout": 1459.26,
        "checksum_suffix": "<value>",
        "max_manifest_size_kb": 373833,
        "validate_inventory_files": True,
        "description": "bolster whenever phooey reckon ocelot",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.FALSE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "security-lake-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 8028.96,
        "max_messages": 4156.44,
        "visibility_timeout": 639.7,
        "num_receivers": 2329.37,
        "socket_timeout": 9281.87,
        "skip_on_error": True,
        "include_sqs_metadata": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 312.72,
        "enable_sqs_assume_role": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "parquet_chunk_size_mb": 4503.14,
        "parquet_chunk_download_timeout": 5363.34,
        "checkpointing": {
            "enabled": False,
            "retries": 3583.79,
        },
        "poll_timeout": 7033.68,
        "encoding": "<value>",
        "description": "ew apropos convection meanwhile why almost",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "tag_after_processing": models.TagAfterProcessingOptions.TRUE,
        "processed_tag_key": "<value>",
        "processed_tag_value": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.MD5,
                    "auth_key": "<value>",
                    "priv_protocol": models.PrivacyProtocol.AES256R,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 5382.63,
        "ip_whitelist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 2276.89,
        "varbinds_with_types": True,
        "best_effort_parsing": True,
        "description": "difficult giving whose since dramatize about upon",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 5164.85,
        "socket_idle_timeout": 2368.59,
        "socket_ending_max_wait": 8933.92,
        "socket_max_lifespan": 4695.77,
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
        "stale_channel_flush_ms": 2286.63,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "catalog past whitewash seafood",
            },
        ],
        "max_s2_sversion": models.MaxS2SVersion.V4,
        "description": "clinch phew indeed untrue",
        "use_fwd_timezone": False,
        "drop_control_fields": True,
        "extract_metrics": True,
        "compress": models.InputSplunkCompression.ALWAYS,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": False,
                "description": "wring pfft apostrophize wherever familiarize amused phooey over",
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 784.34,
        "max_requests_per_socket": 120376,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 6037.04,
        "request_timeout": 2114.37,
        "socket_timeout": 6749.64,
        "keep_alive_timeout": 3764.94,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
        ],
        "splunk_hec_acks": False,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 7030.61,
        "use_fwd_timezone": False,
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
        ],
        "emit_token_metrics": False,
        "description": "defenseless majestically lightly blah though unlike accentuate huzzah candid instruction",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "search_head": "https://localhost:8089",
        "search": "index=main",
        "earliest": "<value>",
        "latest": "<value>",
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
        "request_timeout": 355.18,
        "use_round_robin_dns": False,
        "reject_unauthorized": False,
        "encoding": "<value>",
        "keep_alive_time": 9456.75,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 2620.85,
        "ttl": "<value>",
        "ignore_group_jobs_limit": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.STATIC,
            "interval": 5778.31,
            "limit": 8782.9,
            "multiplier": 6364.93,
            "codes": [
                2078.11,
                6342.8,
                4459.44,
            ],
            "enable_header": False,
            "retry_connect_timeout": False,
            "retry_connect_reset": True,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 7185.57,
        "auth_type": models.InputSplunkSearchAuthenticationType.NONE,
        "description": "hm wicked embossing",
        "username": "Trace_Schmeler1",
        "password": "tQ5UHa3ZYCIdjOk",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "login_url": "https://dull-finer.com",
        "secret_param_name": "<value>",
        "secret": "<value>",
        "token_attribute_name": "<value>",
        "auth_header_expr": "<value>",
        "token_timeout_secs": 6381.01,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "my-queue",
        "queue_type": models.InputSqsQueueType.STANDARD,
        "aws_account_id": "<id>",
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
        "duration_seconds": 8576.28,
        "max_messages": 8042.98,
        "visibility_timeout": 251.38,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 4246.51,
        "description": "onto blah gasp circa overproduce hence when inspection",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 9993.95,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 6165.25,
        "max_buffer_size": 4800.75,
        "ip_whitelist_regex": "<value>",
        "timestamp_timezone": "<value>",
        "single_msg_udp_packets": True,
        "enable_proxy_header": False,
        "keep_fields_list": [
            "<value 1>",
        ],
        "octet_counting": False,
        "infer_framing": False,
        "strictly_infer_octet_counting": False,
        "allow_non_standard_app_name": True,
        "max_active_cxn": 3407.16,
        "socket_idle_timeout": 3828.73,
        "socket_ending_max_wait": 8099.43,
        "socket_max_lifespan": 2179.09,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 748.79,
        "enable_load_balancing": True,
        "description": "than apud obtrude hmph boo boo following story opera litter",
        "enable_enhanced_proxy_header_parsing": False,
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
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 2717.34,
        "host": {
            "mode": models.ModeOptionsHost.DISABLED,
            "custom": {
                "system": {
                    "mode": models.InputSystemMetricsSystemMode.ALL,
                    "processes": True,
                },
                "cpu": {
                    "mode": models.InputSystemMetricsCPUMode.DISABLED,
                    "per_cpu": False,
                    "detail": True,
                    "time": False,
                },
                "memory": {
                    "mode": models.InputSystemMetricsMemoryMode.BASIC,
                    "detail": True,
                },
                "network": {
                    "mode": models.InputSystemMetricsNetworkMode.CUSTOM,
                    "detail": False,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "per_interface": True,
                },
                "disk": {
                    "mode": models.InputSystemMetricsDiskMode.BASIC,
                    "detail": False,
                    "inodes": False,
                    "devices": [
                        "<value 1>",
                    ],
                    "mountpoints": [
                        "<value 1>",
                    ],
                    "fstypes": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "per_device": True,
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
                "<value 2>",
            ],
            "docker_timeout": 6763.69,
            "filters": [
                {
                    "expr": "<value>",
                },
            ],
            "all_containers": True,
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "description": "supposing pale ack provider finding pace nippy",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 1268.95,
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
                "enable": False,
            },
            "disk": {
                "enable": False,
            },
            "metadata": {
                "enable": False,
            },
            "routes": {
                "enable": False,
            },
            "dns": {
                "enable": True,
            },
            "user": {
                "enable": False,
            },
            "firewall": {
                "enable": True,
            },
            "services": {
                "enable": True,
            },
            "ports": {
                "enable": False,
            },
            "login_users": {
                "enable": False,
            },
        },
        "persistence": {
            "enable": False,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "disable_native_module": True,
        "disable_native_last_log_module": False,
        "description": "um preheat unto bolster supposing besides",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 3827.91,
        "socket_idle_timeout": 5013.14,
        "socket_ending_max_wait": 1943.33,
        "socket_max_lifespan": 7818.52,
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
        "stale_channel_flush_ms": 2553.44,
        "enable_header": False,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "description": "through underneath nervously rejoin collaborate mmm",
        "auth_token": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "text_secret": "<value>",
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
            "<value 2>",
        ],
        "connections": [
            {
                "pipeline": "<value>",
                "output": "<value>",
            },
        ],
        "pq": {
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 4131.12,
        "socket_idle_timeout": 8956.21,
        "socket_ending_max_wait": 8941.39,
        "socket_max_lifespan": 9020.4,
        "enable_proxy_header": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": False,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "despite flashy oof gigantic ramp oh",
        "auth_token": "<value>",
        "text_secret": "<value>",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.InputWefAuthenticationMethod.CLIENT_CERT,
        "tls": {
            "disabled": False,
            "reject_unauthorized": True,
            "request_cert": False,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "common_name_regex": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "ocsp_check": False,
            "keytab": "<value>",
            "principal": "<value>",
            "ocsp_check_fail_close": False,
        },
        "max_active_req": 7532.69,
        "max_requests_per_socket": 631259,
        "enable_proxy_header": False,
        "capture_headers": True,
        "keep_alive_timeout": 9531.47,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "socket_timeout": 9065.47,
        "ca_fingerprint": "<value>",
        "keytab": "<value>",
        "principal": "<value>",
        "allow_machine_id_mismatch": True,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "version": "<value>",
                "content_format": models.InputWefFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "read_existing_events": True,
                "send_bookmarks": False,
                "compress": False,
                "targets": [],
                "locale": "hi",
                "query_selector": models.QueryBuilderMode.XML,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/opt/sbin",
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
        "description": "brr dearly woot furthermore apropos save cultivated",
        "log_fingerprint_mismatch": False,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.ReadMode.OLDEST,
        "event_format": models.EventFormat.XML,
        "disable_native_module": True,
        "interval": 5532.44,
        "batch_size": 5477.98,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 7625.68,
        "description": "thankfully without badly eventually yet mid desk what stool jellyfish",
        "disable_json_rendering": True,
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 359.49,
        "host": {
            "mode": models.ModeOptionsHost.ALL,
            "custom": {
                "system": {
                    "mode": models.InputWindowsMetricsSystemMode.DISABLED,
                    "detail": True,
                },
                "cpu": {
                    "mode": models.InputWindowsMetricsCPUMode.CUSTOM,
                    "per_cpu": False,
                    "detail": True,
                    "time": True,
                },
                "memory": {
                    "mode": models.InputWindowsMetricsMemoryMode.CUSTOM,
                    "detail": True,
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
                    "per_volume": True,
                    "detail": True,
                    "volumes": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "disable_native_module": True,
        "description": "scout wherever criminal busily past",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 2712.73,
        "keep_alive_time": 422.95,
        "max_missed_keep_alives": 1889.25,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.STATIC,
            "interval": 5778.31,
            "limit": 8782.9,
            "multiplier": 6364.93,
            "codes": [
                2078.11,
                6342.8,
                4459.44,
            ],
            "enable_header": False,
            "retry_connect_timeout": False,
            "retry_connect_reset": True,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "freely longingly clearly near shush busily consequently where",
        "client_secret": "<value>",
        "text_secret": "<value>",
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 2628.01,
        "max_requests_per_socket": 872518,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 2983.78,
        "request_timeout": 3666.47,
        "socket_timeout": 3047.72,
        "keep_alive_timeout": 4969.63,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 4980.59,
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
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "unless scuttle pixellate hm aw furthermore tensely pro how beloved",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "equally tremendously lest pace starboard legal adventurously gosh because",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": False,
                "description": "petal pro what interesting",
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
            "request_cert": True,
            "reject_unauthorized": False,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        },
        "max_active_req": 3918.05,
        "max_requests_per_socket": 400843,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 1080.72,
        "request_timeout": 9338.93,
        "socket_timeout": 6021.36,
        "keep_alive_timeout": 5654.66,
        "enable_health_check": "<value>",
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
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
            "<value 3>",
        ],
        "hec_acks": True,
        "access_control_allow_origin": [
            "<value 1>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
        ],
        "emit_token_metrics": False,
        "description": "supposing naturally through characterization hm blank reproach ferociously midwife selfish",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "filter_": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "now snowplow because agreement forenenst shabby treble",
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
        "disabled": True,
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
            "mode": models.ModeOptionsPq.SMART,
            "max_buffer_size": 9959.95,
            "commit_frequency": 4085.76,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/usr/obj",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "prefix": "<value>",
        "full_fidelity": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "waterspout lest utterly minus pomelo sandy now zowie",
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