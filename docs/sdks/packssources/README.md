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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 4067.15,
        "socket_idle_timeout": 1373.9,
        "socket_ending_max_wait": 5473.3,
        "socket_max_lifespan": 7426.73,
        "enable_proxy_header": True,
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
        "stale_channel_flush_ms": 4309.15,
        "enable_unix_path": True,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://negative-asset.info/",
        },
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.NONE,
            "dest_path": "<value>",
        },
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "char antagonize yuck",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "<value>",
        "visibility_timeout": 1300.01,
        "num_receivers": 5230.25,
        "max_messages": 9524.03,
        "service_period_secs": 3487.96,
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
            "<value 3>",
        ],
        "stale_channel_flush_ms": 2705.97,
        "parquet_chunk_size_mb": 473.24,
        "parquet_chunk_download_timeout": 6975.07,
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "description": "aw woot what how paltry fondly",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.CreateInputSystemByPackAuthenticationMethodCloudflareHec.SECRET,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": True,
                "description": "consequently meanwhile stormy after pfft willow corrupt athwart as thoughtfully",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 6512.35,
        "max_requests_per_socket": 679079,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 9591.92,
        "request_timeout": 6094.6,
        "socket_timeout": 4715.53,
        "keep_alive_timeout": 9357.22,
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
        ],
        "stale_channel_flush_ms": 9219.13,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
        ],
        "emit_token_metrics": True,
        "description": "ravage perfectly perfection by",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 6997.78,
        "preprocess": {
            "disabled": True,
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
            mode=models.ModeOptionsPq.ALWAYS,
            max_buffer_size=5236.78,
            commit_frequency=8788.99,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=True,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=False,
            schema_registry_url="https://whispered-tenant.biz",
            connection_timeout=9267.71,
            request_timeout=3003.41,
            max_retries=2353.64,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
        ),
        connection_timeout=1224.48,
        request_timeout=2839.68,
        max_retries=7884,
        max_back_off=755.04,
        initial_backoff=5844.08,
        backoff_rate=8812.41,
        authentication_timeout=8013.48,
        reauthentication_threshold=7182.09,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Cleta65",
            password="cHVFBWuIATR5WfJ",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://gorgeous-marketplace.info/",
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
        session_timeout=2225.59,
        rebalance_timeout=6180.1,
        heartbeat_interval=1597.69,
        auto_commit_interval=2161.53,
        auto_commit_threshold=1571.03,
        max_bytes_per_partition=3391.74,
        max_bytes=2488.61,
        max_socket_errors=9103.56,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="dandelion loyally graceful advertisement embed",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "while onto optimistically",
            },
        ],
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 2037.88,
        "max_requests_per_socket": 426932,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 1112.43,
        "request_timeout": 6983.36,
        "socket_timeout": 8499.52,
        "keep_alive_timeout": 3693.39,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "whoever spear incidentally ceramics endow underneath",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 6139.72,
        "max_requests_per_socket": 758726,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 1986.26,
        "request_timeout": 3150.95,
        "socket_timeout": 8728.17,
        "keep_alive_timeout": 3056.32,
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
                "description": "whether modulo within woot soft faithfully lounge lightly twine deeply",
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
        "description": "competent blah athwart",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_cxn": 3010.37,
        "socket_idle_timeout": 7092.34,
        "socket_ending_max_wait": 1608,
        "socket_max_lifespan": 284.46,
        "enable_proxy_header": False,
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
                "enabled": False,
                "description": "while onto optimistically",
            },
        ],
        "description": "unless around bah via interestingly reckless excluding till",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
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
        "stale_channel_flush_ms": 399.49,
        "max_messages": 8799.77,
        "visibility_timeout": 8015.03,
        "num_receivers": 1114.44,
        "socket_timeout": 4966.7,
        "skip_on_error": True,
        "include_sqs_metadata": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 9794.09,
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
            "enabled": True,
            "retries": 9654.85,
        },
        "poll_timeout": 4339.54,
        "encoding": "<value>",
        "description": "ha shout reluctantly upward meh",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 7677.42,
        "max_requests_per_socket": 622686,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4227.76,
        "request_timeout": 6896.39,
        "socket_timeout": 8316.26,
        "keep_alive_timeout": 9658.8,
        "enable_health_check": False,
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
            "enabled": True,
            "reject_unauthorized": True,
        },
        "description": "prickly across sleepily",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
        "description": "scram intrigue mindless wicked some account whack digitize instead",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "discovery_type": models.CreateInputSystemByPackDiscoveryTypeEdgePrometheus.STATIC,
        "interval": 60,
        "timeout": 2723.41,
        "persistence": {
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.CreateInputSystemByPackAuthenticationMethodEdgePrometheus.SECRET,
        "description": "jacket however than feather worth",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTP,
                "host": "localhost",
                "port": 2109.95,
                "path": "/var/yp",
            },
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 2432.75,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
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
                "values": [],
            },
        ],
        "aws_secret_key": "<value>",
        "region": "<value>",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions1.V4,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 4088.79,
        "scrape_protocol_expr": "<value>",
        "scrape_port_expr": "<value>",
        "scrape_path_expr": "<value>",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "depute roughly delightfully behind scratch confide",
            },
        ],
        "username": "Tierra.Robel61",
        "password": "h4KF6fMhw8MSDfs",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 8146.25,
        "max_requests_per_socket": 935089,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 2256.18,
        "request_timeout": 4023.32,
        "socket_timeout": 6972.5,
        "keep_alive_timeout": 8055.81,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "elastic_api": "/",
        "auth_type": models.CreateInputSystemByPackAuthenticationTypeElastic.NONE,
        "api_version": models.CreateInputSystemByPackAPIVersion.EIGHT_DOT_3_DOT_2,
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
            "auth_type": models.CreateInputSystemByPackAuthenticationMethodElastic.NONE,
            "username": "Kendra.Boyle23",
            "password": "D2e7BSQLaiQdZTl",
            "credentials_secret": "<value>",
            "url": "https://somber-lifestyle.net/",
            "reject_unauthorized": True,
            "remove_headers": [
                "<value 1>",
            ],
            "timeout_sec": 3117.64,
            "template_url": "https://great-carnival.info",
        },
        "description": "amid loudly aw warmly sunder",
        "username": "Roosevelt_Harvey",
        "password": "IH6wSIiQ9TSKVRp",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
            "<value 2>",
        ],
        "custom_api_version": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
        "connection_timeout": 3380.61,
        "request_timeout": 5386.27,
        "max_retries": 4499.43,
        "max_back_off": 9459.16,
        "initial_backoff": 8116.71,
        "backoff_rate": 2300.62,
        "authentication_timeout": 2678.27,
        "reauthentication_threshold": 4698.72,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.MANUAL,
            "password": "DCPZ4YAq7I_kSEB",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.PLAIN,
            "username": "Nelda_Schimmel",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.SECRET,
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
            "reject_unauthorized": True,
        },
        "session_timeout": 2076.59,
        "rebalance_timeout": 1206.91,
        "heartbeat_interval": 6706.77,
        "auto_commit_interval": 5810.7,
        "auto_commit_threshold": 3246.62,
        "max_bytes_per_partition": 188.46,
        "max_bytes": 596.83,
        "max_socket_errors": 1607.63,
        "minimize_duplicates": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "where correctly yet now",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 5952.7,
        "schedule_type": models.CreateInputSystemByPackScheduleType.CRON_SCHEDULE,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 9068.17,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "sometimes especially microchip amend abaft for shrill hydrolyze minus",
        "interval": 60,
        "cron_schedule": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "mode": models.CreateInputSystemByPackInputFileMode.MANUAL,
        "interval": 4675.92,
        "filenames": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "filter_archived_files": True,
        "tail_only": True,
        "idle_timeout": 1871.84,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": True,
        "force_text": True,
        "hash_len": 7884.41,
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
        "stale_channel_flush_ms": 1656.19,
        "description": "gosh mysteriously inculcate guzzle",
        "path": "/usr/include",
        "depth": 6009.53,
        "suppress_missing_path_errors": True,
        "delete_files": False,
        "salt_hash": True,
        "include_unidentifiable_binary": True,
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            "<value 1>",
        ],
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3142.84,
        "max_requests_per_socket": 955945,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4010.69,
        "request_timeout": 3023.14,
        "socket_timeout": 6368.71,
        "keep_alive_timeout": 2167.16,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "solemnly beside uh-huh likewise",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
        "monitor_subscription": True,
        "create_topic": False,
        "create_subscription": True,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.AUTO,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_backlog": 6431.72,
        "concurrency": 2906.9,
        "request_timeout": 540.55,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "since connect from hm toward",
        "ordered_delivery": True,
        "template_topic_name": "<value>",
        "template_subscription_name": "<value>",
        "template_region": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 4438.1,
        "max_requests_per_socket": 307170,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4876.48,
        "request_timeout": 426.95,
        "socket_timeout": 6721.71,
        "keep_alive_timeout": 2204.22,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/api/prom/push",
        "loki_api": "<value>",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.TEXT_SECRET,
            "username": "Jaydon47",
            "password": "tGyFIJt0S4YWEdr",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.CREDENTIALS_SECRET,
            "username": "Paolo_Bode54",
            "password": "svqKZTSbPBO1aP5",
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
        "description": "connect divert yippee upliftingly",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 302.66,
        "max_requests_per_socket": 773604,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 3413.93,
        "request_timeout": 7022.73,
        "socket_timeout": 6410.62,
        "keep_alive_timeout": 3667.37,
        "enable_health_check": True,
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
                "description": "beside incidentally helpfully pfft where concerned cute though",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "effector tinted longingly but reflate",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 5088.84,
        "max_requests_per_socket": 756062,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 4982.95,
        "request_timeout": 7715.91,
        "socket_timeout": 6053.41,
        "keep_alive_timeout": 3626.73,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 7415.55,
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
                "description": "beside incidentally helpfully pfft where concerned cute though",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "provision fervently whoever within perfumed after eyebrow toothpick suddenly",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 7548.42,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "yippee even intellect ouch captain sans",
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
        "description": "um idolized atomize",
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
            max_buffer_size=5236.78,
            commit_frequency=8788.99,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt",
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
            schema_registry_url="https://whispered-tenant.biz",
            connection_timeout=9267.71,
            request_timeout=3003.41,
            max_retries=2353.64,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
        ),
        connection_timeout=4621.97,
        request_timeout=5155.41,
        max_retries=3618.58,
        max_back_off=982.45,
        initial_backoff=2.32,
        backoff_rate=7861.13,
        authentication_timeout=8805.41,
        reauthentication_threshold=6939.52,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Cleta65",
            password="cHVFBWuIATR5WfJ",
            auth_type=models.AuthenticationMethodOptionsSasl.MANUAL,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.PLAIN,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=False,
            token_url="https://gorgeous-marketplace.info/",
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        session_timeout=9720.45,
        rebalance_timeout=9699.16,
        heartbeat_interval=7946.94,
        auto_commit_interval=7362.72,
        auto_commit_threshold=521.6,
        max_bytes_per_partition=9012.3,
        max_bytes=6175.18,
        max_socket_errors=9416.76,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="entomb hm supportive mysterious because per",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 3703.04,
        "shard_expr": "<value>",
        "shard_iterator_type": models.CreateInputSystemByPackShardIteratorStart.TRIM_HORIZON,
        "payload_format": models.CreateInputSystemByPackRecordDataFormat.NDJSON,
        "get_records_limit": 3184.84,
        "get_records_limit_total": 9046.79,
        "load_balancing_algorithm": models.CreateInputSystemByPackShardLoadBalancing.ROUND_ROBIN,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V4,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8280.04,
        "verify_kpl_check_sums": True,
        "avoid_duplicates": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "clinking tennis solemnly willfully judgementally upliftingly yuck",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "until jovially tense concerning playfully inside psst",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "nearly married electric finished forgather",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 5360.43,
        "rules": [
            {
                "filter_": "<value>",
                "description": "unimpressively per gape whoever witty",
            },
        ],
        "timestamps": True,
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
            "compress": models.CompressionOptionsPersistence.GZIP,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 8648.79,
        "enable_load_balancing": False,
        "description": "doodle through unto doubtfully",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 6774.01,
        "rules": [
            {
                "filter_": "<value>",
                "description": "until jovially tense concerning playfully inside psst",
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
        "description": "deck why save portly phooey",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 6182.53,
        "max_requests_per_socket": 155987,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 2973.11,
        "request_timeout": 6216.26,
        "socket_timeout": 1396.24,
        "keep_alive_timeout": 8913.6,
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
        "description": "pace marketplace usefully restfully yet",
        "username": "Sarah.Hartmann45",
        "password": "Ks0TpSSaC_SEGSx",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 395.37,
        "max_buffer_size": 1774.9,
        "ip_whitelist_regex": "<value>",
        "enable_proxy_header": True,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
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
        "udp_socket_rx_buf_size": 793.23,
        "description": "handle deceivingly as gee wholly ha square schlep mmm sans",
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
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
        "max_active_cxn": 427.15,
        "shutdown_timeout_ms": 9059.89,
        "description": "attribute excepting duh",
        "template_host": "<value>",
        "template_port": "<value>",
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
            max_buffer_size=5236.78,
            commit_frequency=8788.99,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt",
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
        session_timeout=4131.83,
        rebalance_timeout=2415.81,
        heartbeat_interval=5806.57,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=False,
            schema_registry_url="https://whispered-tenant.biz",
            connection_timeout=9267.71,
            request_timeout=3003.41,
            max_retries=2353.64,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
            ),
        ),
        connection_timeout=8780.38,
        request_timeout=8587.64,
        max_retries=1558.78,
        max_back_off=2081.32,
        initial_backoff=3106.55,
        backoff_rate=3892.36,
        authentication_timeout=3410.14,
        reauthentication_threshold=6033.21,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V4,
        reuse_connections=True,
        reject_unauthorized=False,
        enable_assume_role=True,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=2987.55,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        ),
        auto_commit_interval=7928.25,
        auto_commit_threshold=5480.06,
        max_bytes_per_partition=4767.67,
        max_bytes=5592.47,
        max_socket_errors=2244.45,
        description="pluck ack which pfft afore populist",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "udp_socket_rx_buf_size": 6270.31,
        "template_cache_minutes": 6537.85,
        "v5_enabled": True,
        "v9_enabled": True,
        "ipfix_enabled": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "woefully hassle fooey quixotic incidentally outgoing messy ouch circa",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 2972.66,
        "keep_alive_time": 2696.03,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 7253.42,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
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
                "description": "knuckle twist opposite",
                "interval": 2830.93,
                "log_level": models.LogLevelOptionsContentConfigItems.ERROR,
                "enabled": False,
            },
        ],
        "ingestion_lag": 5013.97,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1360.25,
            "limit": 2039.55,
            "multiplier": 2148.96,
            "codes": [
                1001.17,
                8763.82,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "alert humidity ham whenever till whoever bicycle abnormally vice",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 267.65,
        "disable_time_filter": True,
        "auth_type": models.CreateInputSystemByPackAuthenticationMethodOffice365MsgTrace.OAUTH,
        "reschedule_dropped_tasks": True,
        "max_task_reschedule": 3220.01,
        "log_level": models.CreateInputSystemByPackLogLevelOffice365MsgTrace.WARN,
        "job_timeout": "<value>",
        "keep_alive_time": 3233.18,
        "max_missed_keep_alives": 1313.3,
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
            "interval": 1360.25,
            "limit": 2039.55,
            "multiplier": 2148.96,
            "codes": [
                1001.17,
                8763.82,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "description": "blah tremendously rural folklore responsible which",
        "username": "Novella.Zieme",
        "password": "EqzTKJKZW7lLPjz",
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
        "template_url": "https://nocturnal-blight.info/",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_resource": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 4315.93,
        "keep_alive_time": 9735.61,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 3387.92,
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
                "description": "since encode minion noisily likewise log nice whoever fiercely godparent",
                "interval": 2011.47,
                "log_level": models.LogLevelOptionsContentConfigItems.DEBUG,
                "enabled": False,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.BACKOFF,
            "interval": 1360.25,
            "limit": 2039.55,
            "multiplier": 2148.96,
            "codes": [
                1001.17,
                8763.82,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.SECRET,
        "description": "unused optimistically after flame freely for save than",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 5055.67,
        "max_requests_per_socket": 403392,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 1257.27,
        "socket_timeout": 9748.69,
        "keep_alive_timeout": 1466.36,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "protocol": models.CreateInputSystemByPackProtocol.HTTP,
        "extract_spans": True,
        "extract_metrics": False,
        "otlp_version": models.CreateInputSystemByPackOTLPVersion.ONE_DOT_3_DOT_1,
        "auth_type": models.AuthenticationTypeOptions.CREDENTIALS_SECRET,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 7521.37,
        "description": "serene whenever successfully or gadzooks hence sticker",
        "username": "Alexandria68",
        "password": "dapjfc3A65SEzo6",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
        ],
        "discovery_type": models.CreateInputSystemByPackDiscoveryTypePrometheus.STATIC,
        "interval": 60,
        "log_level": models.CreateInputSystemByPackLogLevelPrometheus.INFO,
        "reject_unauthorized": False,
        "timeout": 818.76,
        "keep_alive_time": 5981.93,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 2614.37,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.MANUAL,
        "description": "unto pop by owlishly bob",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 9590.33,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "scrape_protocol": models.CreateInputSystemByPackMetricsProtocol.HTTP,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
        "search_filter": [
            {
                "name": "<value>",
                "values": [],
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
        "duration_seconds": 9641.84,
        "username": "Sadie66",
        "password": "MIXMRs1eHGRG9mE",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3451.54,
        "max_requests_per_socket": 666276,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 345.03,
        "request_timeout": 1040.03,
        "socket_timeout": 9328.18,
        "keep_alive_timeout": 4879.06,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.CREDENTIALS_SECRET,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "etch peony deliberately veto reassemble idolized opposite vibraphone",
        "username": "Rebekah89",
        "password": "fucs7ltCWdWpggg",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 1812.93,
        "ip_whitelist_regex": "<value>",
        "single_msg_udp_packets": False,
        "ingest_raw_bytes": False,
        "udp_socket_rx_buf_size": 9029.64,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "huzzah clamor ack afterwards fast converse toward",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
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
        "stale_channel_flush_ms": 7305.53,
        "max_messages": 5911.43,
        "visibility_timeout": 2807.36,
        "num_receivers": 8937.56,
        "socket_timeout": 6211.1,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 6237.52,
        "enable_sqs_assume_role": True,
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
        "parquet_chunk_size_mb": 8131.77,
        "parquet_chunk_download_timeout": 8009.46,
        "checkpointing": {
            "enabled": True,
            "retries": 9654.85,
        },
        "poll_timeout": 5408.26,
        "encoding": "<value>",
        "tag_after_processing": True,
        "description": "woefully lanky trench deafening zesty surprised on sunbeam vivaciously",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 1222.88,
        "max_messages": 5180.52,
        "visibility_timeout": 4259.65,
        "num_receivers": 110.51,
        "socket_timeout": 5880.6,
        "skip_on_error": False,
        "include_sqs_metadata": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3102.38,
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
        "parquet_chunk_size_mb": 7589.41,
        "parquet_chunk_download_timeout": 7741.71,
        "checkpointing": {
            "enabled": True,
            "retries": 9654.85,
        },
        "poll_timeout": 2413.82,
        "checksum_suffix": "<value>",
        "max_manifest_size_kb": 157753,
        "validate_inventory_files": False,
        "description": "which misjudge cultivated daintily",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 3107.21,
        "max_messages": 5612.34,
        "visibility_timeout": 5057.17,
        "num_receivers": 9683.62,
        "socket_timeout": 61.29,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 979.79,
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
        "parquet_chunk_size_mb": 8862.21,
        "parquet_chunk_download_timeout": 822.35,
        "checkpointing": {
            "enabled": True,
            "retries": 9654.85,
        },
        "poll_timeout": 8602.63,
        "encoding": "<value>",
        "description": "concerning pfft heartache knowledgeable satirize with",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "192.168.1.1",
        "port": 161,
        "snmp_v3_auth": {
            "v3_auth_enabled": True,
            "allow_unmatched_trap": False,
            "v3_users": [
                {
                    "name": "<value>",
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.MD5,
                    "auth_key": "<value>",
                    "priv_protocol": models.CreateInputSystemByPackPrivacyProtocol.AES256B,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 1460.46,
        "ip_whitelist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 212.18,
        "varbinds_with_types": True,
        "best_effort_parsing": True,
        "description": "concerning onset vainly obnoxiously whenever duh lazy selfishly",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 8042.81,
        "socket_idle_timeout": 8701.69,
        "socket_ending_max_wait": 4800.75,
        "socket_max_lifespan": 7418.06,
        "enable_proxy_header": True,
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
        "stale_channel_flush_ms": 4573.81,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "secret whenever indolent but yuck even aside or turbulent",
            },
        ],
        "max_s2_sversion": models.CreateInputSystemByPackMaxS2SVersion.V4,
        "description": "youthfully closely behind for",
        "use_fwd_timezone": False,
        "drop_control_fields": True,
        "extract_metrics": True,
        "compress": models.CreateInputSystemByPackCompression.AUTO,
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
                "description": "oh vivacious quick than gah vibration",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3435.92,
        "max_requests_per_socket": 85570,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 2741.76,
        "request_timeout": 5414.67,
        "socket_timeout": 369.47,
        "keep_alive_timeout": 4427.77,
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
        "splunk_hec_acks": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 2692.65,
        "use_fwd_timezone": False,
        "drop_control_fields": False,
        "extract_metrics": False,
        "access_control_allow_origin": [
            "<value 1>",
            "<value 2>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": True,
        "description": "fondly substantial tune black-and-white aw banish and",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
        "log_level": models.CreateInputSystemByPackLogLevelSplunkSearch.WARN,
        "request_timeout": 9887.21,
        "use_round_robin_dns": False,
        "reject_unauthorized": False,
        "encoding": "<value>",
        "keep_alive_time": 5030.92,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 4125.49,
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
            "interval": 2446.49,
            "limit": 8984.5,
            "multiplier": 2926.4,
            "codes": [
                9786.9,
                1849.73,
            ],
            "enable_header": True,
            "retry_connect_timeout": True,
            "retry_connect_reset": True,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 2506.09,
        "auth_type": models.CreateInputSystemByPackAuthenticationTypeSplunkSearch.BASIC,
        "description": "plagiarise enthusiastically phew",
        "username": "Darren.Murphy46",
        "password": "HNMkkOA8S0ww7hv",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "my-queue",
        "queue_type": models.CreateInputSystemByPackQueueType.STANDARD,
        "aws_account_id": "<id>",
        "create_queue": True,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions3.V2,
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 1332.59,
        "max_messages": 3646.79,
        "visibility_timeout": 2160.76,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 988.49,
        "description": "which more vivaciously woot avalanche disinherit slowly",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 8199.22,
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 5767.97,
        "max_buffer_size": 7898.91,
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
        "max_active_cxn": 8532.26,
        "socket_idle_timeout": 5176.78,
        "socket_ending_max_wait": 1688.68,
        "socket_max_lifespan": 7987.09,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
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
        "udp_socket_rx_buf_size": 40.98,
        "enable_load_balancing": False,
        "description": "porter whine ethical pleasure seemingly incidentally irritably",
        "enable_enhanced_proxy_header_parsing": True,
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 8247.04,
        "host": {
            "mode": models.ModeOptionsHost.ALL,
            "custom": {
                "system": {
                    "mode": models.CreateInputSystemByPackSystemModeSystemMetrics.DISABLED,
                    "processes": False,
                },
                "cpu": {
                    "mode": models.CreateInputSystemByPackCPUModeSystemMetrics.DISABLED,
                    "per_cpu": False,
                    "detail": True,
                    "time": False,
                },
                "memory": {
                    "mode": models.CreateInputSystemByPackMemoryModeSystemMetrics.BASIC,
                    "detail": True,
                },
                "network": {
                    "mode": models.CreateInputSystemByPackNetworkModeSystemMetrics.ALL,
                    "detail": True,
                    "protocols": False,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.CreateInputSystemByPackDiskModeSystemMetrics.ALL,
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
                        "<value 2>",
                        "<value 3>",
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
                    "include_children": True,
                },
            ],
        },
        "container": {
            "mode": models.CreateInputSystemByPackContainerMode.ALL,
            "docker_socket": [
                "<value 1>",
                "<value 2>",
            ],
            "docker_timeout": 3262.59,
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
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "description": "demobilise because lampoon equal wisely",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 8964.86,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "collectors": {
            "hostsfile": {
                "enable": False,
            },
            "interfaces": {
                "enable": True,
            },
            "disk": {
                "enable": True,
            },
            "metadata": {
                "enable": False,
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
                "enable": False,
            },
            "services": {
                "enable": True,
            },
            "ports": {
                "enable": True,
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
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "disable_native_module": True,
        "disable_native_last_log_module": True,
        "description": "longingly bah till forgo ick",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 2500.34,
        "socket_idle_timeout": 5317.11,
        "socket_ending_max_wait": 1943.71,
        "socket_max_lifespan": 6816.93,
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
        "stale_channel_flush_ms": 1670.1,
        "enable_header": True,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
            ],
        },
        "description": "given fiddle and tight without until fooey",
        "auth_token": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 6808.64,
        "socket_idle_timeout": 8728.65,
        "socket_ending_max_wait": 1097.72,
        "socket_max_lifespan": 1900.76,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "description": "rowdy triumphantly including boo toward monthly once conceal progress surprisingly",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.CreateInputSystemByPackAuthenticationMethodWef.CLIENT_CERT,
        "tls": {
            "disabled": True,
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
        "max_active_req": 9533.2,
        "max_requests_per_socket": 251300,
        "enable_proxy_header": False,
        "capture_headers": True,
        "keep_alive_timeout": 6579.6,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "socket_timeout": 9544.3,
        "ca_fingerprint": "<value>",
        "keytab": "<value>",
        "principal": "<value>",
        "allow_machine_id_mismatch": False,
        "subscriptions": [
            {
                "subscription_name": "subscription-1",
                "version": "<value>",
                "content_format": models.CreateInputSystemByPackFormat.RENDERED_TEXT,
                "heartbeat_interval": 60,
                "batch_timeout": 5,
                "read_existing_events": True,
                "send_bookmarks": False,
                "compress": True,
                "targets": [],
                "locale": "pt",
                "query_selector": models.CreateInputSystemByPackQueryBuilderMode.SIMPLE,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/var",
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
        "description": "jaggedly merit shell bah cruelly pale aha whose urban filthy",
        "log_fingerprint_mismatch": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.CreateInputSystemByPackReadMode.NEWEST,
        "event_format": models.CreateInputSystemByPackEventFormat.JSON,
        "disable_native_module": True,
        "interval": 5728.75,
        "batch_size": 9950.94,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 2912.98,
        "description": "mozzarella ew pfft freezing",
        "disable_json_rendering": False,
        "disable_xml_rendering": False,
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 4750.79,
        "host": {
            "mode": models.ModeOptionsHost.ALL,
            "custom": {
                "system": {
                    "mode": models.CreateInputSystemByPackSystemModeWindowsMetrics.BASIC,
                    "detail": False,
                },
                "cpu": {
                    "mode": models.CreateInputSystemByPackCPUModeWindowsMetrics.ALL,
                    "per_cpu": True,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.CreateInputSystemByPackMemoryModeWindowsMetrics.CUSTOM,
                    "detail": True,
                },
                "network": {
                    "mode": models.CreateInputSystemByPackNetworkModeWindowsMetrics.CUSTOM,
                    "detail": True,
                    "protocols": True,
                    "devices": [
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.CreateInputSystemByPackDiskModeWindowsMetrics.ALL,
                    "per_volume": True,
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
                    "include_children": True,
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
        "description": "settler tomorrow cappelletti unlike aw limping",
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
            "mode": models.ModeOptionsPq.ALWAYS,
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 1426.41,
        "keep_alive_time": 3632.41,
        "max_missed_keep_alives": 6059.42,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.NONE,
            "interval": 2446.49,
            "limit": 8984.5,
            "multiplier": 2926.4,
            "codes": [
                9786.9,
                1849.73,
            ],
            "enable_header": True,
            "retry_connect_timeout": True,
            "retry_connect_reset": True,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "understanding finally furthermore than shanghai onto book scarcely incidentally apud",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_endpoint": "<value>",
        "template_auth_url": "https://tense-newsstand.net/",
        "template_client_id": "<id>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 1486.77,
        "max_requests_per_socket": 688186,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 4859.08,
        "request_timeout": 4334.25,
        "socket_timeout": 7422.5,
        "keep_alive_timeout": 6074.22,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 3865.53,
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
        ],
        "auth_tokens_ext": [
            {
                "token": "<value>",
                "description": "beside incidentally helpfully pfft where concerned cute though",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "screw male recompense deliberately even hoof lady since flawed",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5236.78,
            "commit_frequency": 8788.99,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt",
            "compress": models.CompressionOptionsPq.GZIP,
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
                "description": "slime whoa psst than yahoo",
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
            "disabled": False,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 1622.31,
        "max_requests_per_socket": 330485,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 4882.74,
        "request_timeout": 8838.66,
        "socket_timeout": 5051.73,
        "keep_alive_timeout": 7256.83,
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
        ],
        "emit_token_metrics": True,
        "description": "trash underpants overplay pillory muddy highly after uh-huh",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_hec_api": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 2177.87,
        "socket_idle_timeout": 1131.76,
        "socket_ending_max_wait": 2476.4,
        "socket_max_lifespan": 8980.2,
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
        "stale_channel_flush_ms": 5201.14,
        "enable_unix_path": False,
        "filter_": {
            "allow": [
                {
                    "procname": "<value>",
                    "arg": "<value>",
                    "config": "<value>",
                },
            ],
            "transport_url": "https://stable-transparency.org/",
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
        "description": "graffiti yawningly absent when times sonata or uselessly woeful amidst",
        "host": "0.0.0.0",
        "port": 9109,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "unix_socket_path": "<value>",
        "unix_socket_perms": "<value>",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "azure-blob-queue",
        "file_filter": "<value>",
        "visibility_timeout": 3094.63,
        "num_receivers": 7570.95,
        "max_messages": 2253.54,
        "service_period_secs": 7697.99,
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
        "stale_channel_flush_ms": 2956.83,
        "parquet_chunk_size_mb": 7633.01,
        "parquet_chunk_download_timeout": 4156.74,
        "auth_type": models.AuthenticationMethodOptions.MANUAL,
        "description": "knavishly vivaciously sympathetically",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
                "enabled": False,
                "description": "convalesce after sympathetically",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 8504.29,
        "max_requests_per_socket": 808412,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 8898.86,
        "request_timeout": 2032.33,
        "socket_timeout": 3074.69,
        "keep_alive_timeout": 8911.87,
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
        ],
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 7424.11,
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
        "description": "successfully ecstatic if woefully apprehensive soulful nicely butter even deprave",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 2306.82,
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
            max_buffer_size=5318.64,
            commit_frequency=3762.63,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/sbin",
            compress=models.CompressionOptionsPq.GZIP,
            pq_controls=models.PqTypePqControls(),
        ),
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        ),
        topics=[
            "logs",
        ],
        group_id="<id>",
        from_beginning=False,
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=True,
            schema_registry_url="https://foolish-lace.name",
            connection_timeout=9222.03,
            request_timeout=2060.92,
            max_retries=4747.86,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            ),
        ),
        connection_timeout=2191.22,
        request_timeout=9306.44,
        max_retries=9430.74,
        max_back_off=5234.73,
        initial_backoff=5835.16,
        backoff_rate=8876.61,
        authentication_timeout=4184.48,
        reauthentication_threshold=2863.18,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Hallie.Wisozk",
            password="oF6ULVD266SvlIK",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://rewarding-courtroom.net/",
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
        session_timeout=789.56,
        rebalance_timeout=6327.46,
        heartbeat_interval=6024.79,
        auto_commit_interval=2783,
        auto_commit_threshold=9984.03,
        max_bytes_per_partition=214.49,
        max_bytes=1937.09,
        max_socket_errors=7019.66,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="qua simple retention gratefully huzzah hefty crazy because",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "auth_tokens": [
            {
                "token_secret": "<value>",
                "enabled": False,
                "description": "that convince gift ha maroon sadly above fraternise affect always",
            },
        ],
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 94.06,
        "max_requests_per_socket": 995636,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 7620.39,
        "request_timeout": 5316.13,
        "socket_timeout": 5927.22,
        "keep_alive_timeout": 984.97,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "meanwhile atomize receptor wildly whether competent intelligent",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3932.24,
        "max_requests_per_socket": 381048,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 7154.34,
        "request_timeout": 5542.72,
        "socket_timeout": 5091.92,
        "keep_alive_timeout": 4354.07,
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
                "description": "joyfully duh once among",
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
                    "enabled": False,
                    "default_dataset": "<value>",
                },
            },
        ],
        "description": "suitcase hm um selfish",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_cxn": 3802.79,
        "socket_idle_timeout": 4455.7,
        "socket_ending_max_wait": 7985.02,
        "socket_max_lifespan": 275.69,
        "enable_proxy_header": True,
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
                "enabled": False,
                "description": "that convince gift ha maroon sadly above fraternise affect always",
            },
        ],
        "description": "consequently wise out yuck in option emboss silt",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "crowdstrike-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V4,
        "reuse_connections": True,
        "reject_unauthorized": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 1413.78,
        "max_messages": 1324.06,
        "visibility_timeout": 6723.13,
        "num_receivers": 6219.39,
        "socket_timeout": 8635.01,
        "skip_on_error": False,
        "include_sqs_metadata": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7464.28,
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
            "retries": 1555.53,
        },
        "poll_timeout": 1226.29,
        "encoding": "<value>",
        "description": "partridge gah and instructor plus",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8126,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3701.81,
        "max_requests_per_socket": 562306,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 6427.39,
        "request_timeout": 6528.52,
        "socket_timeout": 4974.13,
        "keep_alive_timeout": 3714.31,
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
            "enabled": True,
            "reject_unauthorized": True,
        },
        "description": "gradient alongside bug fill which woot considering deadly",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "description": "that apud awkwardly reclassify bid ha ew sardonic boo ameliorate",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "dimension_list": [
            "<value 1>",
        ],
        "discovery_type": models.InputEdgePrometheusDiscoveryType.STATIC,
        "interval": 60,
        "timeout": 256.89,
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
        "description": "those boo seafood but across around",
        "targets": [
            {
                "protocol": models.ProtocolOptionsTargetsItems.HTTP,
                "host": "localhost",
                "port": 2116.57,
                "path": "/opt/lib",
            },
        ],
        "record_type": models.RecordTypeOptions.SRV,
        "scrape_port": 8442.04,
        "name_list": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "scrape_protocol": models.ProtocolOptionsTargetsItems.HTTP,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.MANUAL,
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "use_public_ip": False,
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
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 5608.71,
        "scrape_protocol_expr": "<value>",
        "scrape_port_expr": "<value>",
        "scrape_path_expr": "<value>",
        "pod_filter": [
            {
                "filter_": "<value>",
                "description": "toaster whenever reflecting indeed rationale",
            },
        ],
        "username": "Karlee.Prohaska",
        "password": "Lx6EeJZLVVlDkZb",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "localhost",
        "port": 9200,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 2608.82,
        "max_requests_per_socket": 179171,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 7866.63,
        "request_timeout": 7159.18,
        "socket_timeout": 5602.34,
        "keep_alive_timeout": 3586.64,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "elastic_api": "/",
        "auth_type": models.InputElasticAuthenticationType.CREDENTIALS_SECRET,
        "api_version": models.InputElasticAPIVersion.SIX_DOT_8_DOT_4,
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
            "enabled": True,
            "auth_type": models.InputElasticAuthenticationMethod.SECRET,
            "username": "Courtney.Welch",
            "password": "Lge4i0P6LwZldaN",
            "credentials_secret": "<value>",
            "url": "https://scientific-interior.name",
            "reject_unauthorized": True,
            "remove_headers": [
                "<value 1>",
            ],
            "timeout_sec": 9619.23,
            "template_url": "https://exalted-turret.net",
        },
        "description": "geez elderly concerning translation",
        "username": "Marcus75",
        "password": "Nx2JR_RGCX4Zt2A",
        "credentials_secret": "<value>",
        "auth_tokens": [
            "<value 1>",
        ],
        "custom_api_version": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "connection_timeout": 1083.7,
        "request_timeout": 7233.09,
        "max_retries": 584.36,
        "max_back_off": 9713.26,
        "initial_backoff": 4326.99,
        "backoff_rate": 8957.69,
        "authentication_timeout": 3151.51,
        "reauthentication_threshold": 4345.38,
        "sasl": {
            "disabled": False,
            "auth_type": models.AuthenticationMethodOptionsSasl1.SECRET,
            "password": "5xOWKBHPhbLS62p",
            "text_secret": "<value>",
            "mechanism": models.SaslMechanismOptionsSasl1.OAUTHBEARER,
            "username": "Rosalinda89",
            "client_secret_auth_type": models.AuthenticationMethodOptionsSasl2.CERTIFICATE,
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
        "session_timeout": 1137.77,
        "rebalance_timeout": 6787.34,
        "heartbeat_interval": 7898.58,
        "auto_commit_interval": 3538.75,
        "auto_commit_threshold": 8585.97,
        "max_bytes_per_partition": 1564.23,
        "max_bytes": 3331.78,
        "max_socket_errors": 7530.35,
        "minimize_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "down yippee yowza meanwhile when fireplace solemnly",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "command": "echo \"Hello World\"",
        "retries": 357.57,
        "schedule_type": models.ScheduleType.CRON_SCHEDULE,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 347.07,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "rot cap eek finally",
        "interval": 60,
        "cron_schedule": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "mode": models.InputFileMode.MANUAL,
        "interval": 2045.59,
        "filenames": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "filter_archived_files": True,
        "tail_only": False,
        "idle_timeout": 5068.88,
        "min_age_dur": "<value>",
        "max_age_dur": "<value>",
        "check_file_mod_time": True,
        "force_text": True,
        "hash_len": 475.25,
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
        "stale_channel_flush_ms": 8347.38,
        "description": "to own daily redraw squiggly aside probate",
        "path": "/etc/namedb",
        "depth": 8225.75,
        "suppress_missing_path_errors": False,
        "delete_files": False,
        "salt_hash": False,
        "include_unidentifiable_binary": False,
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 4121.05,
        "max_requests_per_socket": 447263,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 8495.08,
        "request_timeout": 3063.22,
        "socket_timeout": 9184.91,
        "keep_alive_timeout": 226.13,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "both merry exactly congregate",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "topic_name": "my-topic",
        "subscription_name": "my-subscription",
        "monitor_subscription": False,
        "create_topic": False,
        "create_subscription": False,
        "region": "<value>",
        "google_auth_method": models.GoogleAuthenticationMethodOptions.MANUAL,
        "service_account_credentials": "<value>",
        "secret": "<value>",
        "max_backlog": 538.05,
        "concurrency": 42.36,
        "request_timeout": 4688.25,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "ugh mismatch soon sunny apropos hmph",
        "ordered_delivery": False,
        "template_topic_name": "<value>",
        "template_subscription_name": "<value>",
        "template_region": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 7432.78,
        "max_requests_per_socket": 363916,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 9141.19,
        "request_timeout": 8174.29,
        "socket_timeout": 7036.5,
        "keep_alive_timeout": 3091.06,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/api/prom/push",
        "loki_api": "<value>",
        "prometheus_auth": {
            "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.BASIC,
            "username": "Elody.Wintheiser",
            "password": "wz_3eL1dGvlO6eV",
            "token": "<value>",
            "credentials_secret": "<value>",
            "text_secret": "<value>",
        },
        "loki_auth": {
            "auth_type": models.AuthenticationTypeOptionsLokiAuth.NONE,
            "username": "Buck26",
            "password": "dlVcDmpeEG4LHgq",
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
        "description": "pilot to fatally authentic chime bah",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3968.12,
        "max_requests_per_socket": 834950,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 9398.33,
        "request_timeout": 2620.6,
        "socket_timeout": 689.57,
        "keep_alive_timeout": 1105.14,
        "enable_health_check": True,
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
                "description": "ew phooey unless aha plus woot zowie unless",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "finally whole outnumber over apropos frozen",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 2155.01,
        "max_requests_per_socket": 339648,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 4438.78,
        "request_timeout": 9645.86,
        "socket_timeout": 804.45,
        "keep_alive_timeout": 5141.74,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "stale_channel_flush_ms": 3358.37,
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
                "description": "ew phooey unless aha plus woot zowie unless",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "quizzically blight athwart ugh invite aha tenant multicolored if wherever",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "path": "/var/log/journal",
        "interval": 6340.49,
        "journals": [
            "system",
        ],
        "rules": [
            {
                "filter_": "<value>",
                "description": "mmm by yesterday",
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
        "description": "likewise off atop instead never",
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
            max_buffer_size=5318.64,
            commit_frequency=3762.63,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/sbin",
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
            schema_registry_url="https://foolish-lace.name",
            connection_timeout=9222.03,
            request_timeout=2060.92,
            max_retries=4747.86,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            ),
        ),
        connection_timeout=8097.01,
        request_timeout=6229.98,
        max_retries=6946.19,
        max_back_off=3258.42,
        initial_backoff=5604.23,
        backoff_rate=3668.67,
        authentication_timeout=8087.17,
        reauthentication_threshold=1502.06,
        sasl=models.AuthenticationType(
            disabled=False,
            username="Hallie.Wisozk",
            password="oF6ULVD266SvlIK",
            auth_type=models.AuthenticationMethodOptionsSasl.SECRET,
            credentials_secret="<value>",
            mechanism=models.SaslMechanismOptionsSasl.SCRAM_SHA_512,
            keytab_location="<value>",
            principal="<value>",
            broker_service_class="<value>",
            oauth_enabled=True,
            token_url="https://rewarding-courtroom.net/",
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
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        ),
        session_timeout=1415.5,
        rebalance_timeout=5063.07,
        heartbeat_interval=1418.21,
        auto_commit_interval=5495.4,
        auto_commit_threshold=3976.66,
        max_bytes_per_partition=7857.05,
        max_bytes=8759.77,
        max_socket_errors=5618.92,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        description="tousle draw excess",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "stream_name": "my-stream",
        "service_interval": 9387.25,
        "shard_expr": "<value>",
        "shard_iterator_type": models.ShardIteratorStart.LATEST,
        "payload_format": models.RecordDataFormat.LINE,
        "get_records_limit": 3821.23,
        "get_records_limit_total": 4535.77,
        "load_balancing_algorithm": models.ShardLoadBalancing.CONSISTENT_HASHING,
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptions2.V2,
        "reuse_connections": False,
        "reject_unauthorized": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 7175.07,
        "verify_kpl_check_sums": True,
        "avoid_duplicates": False,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "circa annually yahoo suckle the apropos divine out at too",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "rules": [
            {
                "filter_": "<value>",
                "description": "chow vamoose devastation",
            },
        ],
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "lone petticoat frightfully evil yum",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 1273.6,
        "rules": [
            {
                "filter_": "<value>",
                "description": "suddenly foolish quiet breastplate sophisticated drat what",
            },
        ],
        "timestamps": True,
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
            "<value 3>",
        ],
        "stale_channel_flush_ms": 2370.87,
        "enable_load_balancing": True,
        "description": "alb athletic bourgeoisie rapidly ew anenst license",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 8777.96,
        "rules": [
            {
                "filter_": "<value>",
                "description": "chow vamoose devastation",
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
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "description": "duster when flood",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 2261.6,
        "max_requests_per_socket": 403885,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 391.58,
        "request_timeout": 7446.1,
        "socket_timeout": 7887.34,
        "keep_alive_timeout": 7085.76,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "loki_api": "/loki/api/v1/push",
        "auth_type": models.AuthenticationTypeOptionsLokiAuth.BASIC,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "on christen including behind annually disclosure boo whenever rubric printer",
        "username": "Lou_Heathcote",
        "password": "qSN2owb1cWSvjjh",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 8125,
        "tcp_port": 3449.96,
        "max_buffer_size": 840.01,
        "ip_whitelist_regex": "<value>",
        "enable_proxy_header": False,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 6578.52,
        "description": "furthermore brilliant wretched geez gee",
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 57000,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 4616.35,
        "shutdown_timeout_ms": 8224.03,
        "description": "boastfully past siege knavishly spellcheck scale frank",
        "template_host": "<value>",
        "template_port": "<value>",
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
            max_buffer_size=5318.64,
            commit_frequency=3762.63,
            max_file_size="<value>",
            max_size="<value>",
            path="/opt/sbin",
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
        session_timeout=9034.08,
        rebalance_timeout=5113.84,
        heartbeat_interval=9292.28,
        metadata=[
            models.ItemsTypeMetadata(
                name="<value>",
                value="<value>",
            ),
        ],
        kafka_schema_registry=models.KafkaSchemaRegistryAuthenticationType(
            disabled=True,
            schema_registry_url="https://foolish-lace.name",
            connection_timeout=9222.03,
            request_timeout=2060.92,
            max_retries=4747.86,
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
                min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
                max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            ),
        ),
        connection_timeout=5239.83,
        request_timeout=7415.72,
        max_retries=3350.38,
        max_back_off=1085.96,
        initial_backoff=2915.63,
        backoff_rate=5562.81,
        authentication_timeout=3485.6,
        reauthentication_threshold=1186.43,
        aws_authentication_method=models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        aws_secret_key="<value>",
        region="us-east-1",
        endpoint="<value>",
        signature_version=models.SignatureVersionOptions.V4,
        reuse_connections=False,
        reject_unauthorized=False,
        enable_assume_role=True,
        assume_role_arn="<value>",
        assume_role_external_id="<id>",
        duration_seconds=3369.8,
        tls=models.TLSSettingsClientSideTypeKafkaSchemaRegistry(
            disabled=False,
            reject_unauthorized=False,
            servername="<value>",
            certificate_name="<value>",
            ca_path="<value>",
            priv_key_path="<value>",
            cert_path="<value>",
            passphrase="<value>",
            min_version=models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            max_version=models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
        ),
        auto_commit_interval=3782.76,
        auto_commit_threshold=5370.18,
        max_bytes_per_partition=493.58,
        max_bytes=7523.73,
        max_socket_errors=392.88,
        description="upon deceivingly vanish profane sans furthermore um even",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 2055,
        "enable_pass_through": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "udp_socket_rx_buf_size": 9889.4,
        "template_cache_minutes": 2571.11,
        "v5_enabled": False,
        "v9_enabled": True,
        "ipfix_enabled": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "fearless ha what gym when",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.ENTERPRISE_GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 7322.78,
        "keep_alive_time": 2466.82,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 3801.89,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
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
                "description": "truthfully ragged apropos better since now whoever as oof without",
                "interval": 9148.23,
                "log_level": models.LogLevelOptionsContentConfigItems.ERROR,
                "enabled": True,
            },
        ],
        "ingestion_lag": 8798.19,
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.STATIC,
            "interval": 3819.89,
            "limit": 6889.97,
            "multiplier": 1601.39,
            "codes": [
                8528.61,
                6036.97,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": True,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "aha er finally",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "url": "https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace",
        "interval": 15,
        "start_date": "<value>",
        "end_date": "<value>",
        "timeout": 2553.49,
        "disable_time_filter": False,
        "auth_type": models.InputOffice365MsgTraceAuthenticationMethod.OAUTH,
        "reschedule_dropped_tasks": False,
        "max_task_reschedule": 8433.78,
        "log_level": models.InputOffice365MsgTraceLogLevel.WARN,
        "job_timeout": "<value>",
        "keep_alive_time": 8444.87,
        "max_missed_keep_alives": 3651.45,
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
            "interval": 3819.89,
            "limit": 6889.97,
            "multiplier": 1601.39,
            "codes": [
                8528.61,
                6036.97,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": True,
        },
        "description": "apropos brr deliquesce cheese ah",
        "username": "Vernice_Langworth35",
        "password": "_pAlCa3zWUZn969",
        "credentials_secret": "<value>",
        "client_secret": "<value>",
        "tenant_id": "<id>",
        "client_id": "<id>",
        "resource": "<value>",
        "plan_type": models.SubscriptionPlanOptions.DOD,
        "text_secret": "<value>",
        "cert_options": {
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
        },
        "template_url": "https://icy-finding.name/",
        "template_tenant_id": "<id>",
        "template_client_id": "<id>",
        "template_resource": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "plan_type": models.SubscriptionPlanOptions.GCC,
        "tenant_id": "tenant-id",
        "app_id": "app-id",
        "timeout": 3852.82,
        "keep_alive_time": 5227.5,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 7117.28,
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
                "description": "alligator helpfully definitive perp scarily",
                "interval": 8076.88,
                "log_level": models.LogLevelOptionsContentConfigItems.DEBUG,
                "enabled": False,
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.STATIC,
            "interval": 3819.89,
            "limit": 6889.97,
            "multiplier": 1601.39,
            "codes": [
                8528.61,
                6036.97,
            ],
            "enable_header": True,
            "retry_connect_timeout": False,
            "retry_connect_reset": True,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "via selfishly plus puppet contrast pfft considering",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 4317,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3469,
        "max_requests_per_socket": 295125,
        "enable_proxy_header": "<value>",
        "capture_headers": "<value>",
        "activity_log_sample_rate": "<value>",
        "request_timeout": 6472.11,
        "socket_timeout": 8701.9,
        "keep_alive_timeout": 8352.78,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "protocol": models.InputOpenTelemetryProtocol.HTTP,
        "extract_spans": True,
        "extract_metrics": True,
        "otlp_version": models.InputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0,
        "auth_type": models.AuthenticationTypeOptions.CREDENTIALS_SECRET,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_active_cxn": 4972.97,
        "description": "lively gadzooks gestate dowse depute carelessly highly",
        "username": "Jess22",
        "password": "2_mROJCOhV3vY75",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
        "extract_logs": True,
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
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
        "timeout": 8250.81,
        "keep_alive_time": 4617.44,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 4814.04,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "auth_type": models.AuthenticationMethodOptionsSasl.SECRET,
        "description": "hm instead gosh whack undergo",
        "target_list": [
            "http://localhost:9090/metrics",
        ],
        "record_type": models.RecordTypeOptions.AAAA,
        "scrape_port": 8151.75,
        "name_list": [
            "<value 1>",
        ],
        "scrape_protocol": models.MetricsProtocol.HTTP,
        "scrape_path": "<value>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.SECRET,
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
        "signature_version": models.SignatureVersionOptions1.V2,
        "reuse_connections": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 5682.66,
        "username": "Delia_Emmerich-Hamill36",
        "password": "Y7ZzsJA55UXc4BZ",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10080,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 6875.17,
        "max_requests_per_socket": 794108,
        "enable_proxy_header": True,
        "capture_headers": True,
        "activity_log_sample_rate": 9587.33,
        "request_timeout": 1496.41,
        "socket_timeout": 9308.64,
        "keep_alive_timeout": 2890.6,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "prometheus_api": "/write",
        "auth_type": models.AuthenticationTypeOptionsPrometheusAuth.TEXT_SECRET,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "endow chainstay bracelet around plus",
        "username": "Anastasia.Lesch69",
        "password": "SRxtqO4Gdh5YJEX",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 514,
        "max_buffer_size": 1843.53,
        "ip_whitelist_regex": "<value>",
        "single_msg_udp_packets": False,
        "ingest_raw_bytes": True,
        "udp_socket_rx_buf_size": 9334.16,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "description": "healthily following redact worth aha yuck baseboard hold crazy",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "s3-notifications-queue",
        "file_filter": "<value>",
        "aws_account_id": "<id>",
        "aws_authentication_method": models.AuthenticationMethodOptionsS3CollectorConf.AUTO,
        "aws_secret_key": "<value>",
        "region": "us-east-1",
        "endpoint": "<value>",
        "signature_version": models.SignatureVersionOptionsS3CollectorConf.V2,
        "reuse_connections": True,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 342.52,
        "max_messages": 7313.83,
        "visibility_timeout": 1095.75,
        "num_receivers": 9862.68,
        "socket_timeout": 8762.59,
        "skip_on_error": True,
        "include_sqs_metadata": False,
        "enable_assume_role": True,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 8770.51,
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
        "parquet_chunk_size_mb": 2205.22,
        "parquet_chunk_download_timeout": 8634.03,
        "checkpointing": {
            "enabled": False,
            "retries": 1555.53,
        },
        "poll_timeout": 177.43,
        "encoding": "<value>",
        "tag_after_processing": False,
        "description": "search joshingly than gullible spectacles consequently pish giggle",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "reuse_connections": True,
        "reject_unauthorized": False,
        "breaker_rulesets": [
            "<value 1>",
        ],
        "stale_channel_flush_ms": 5846.84,
        "max_messages": 4965.89,
        "visibility_timeout": 5753.06,
        "num_receivers": 3855.04,
        "socket_timeout": 226.54,
        "skip_on_error": False,
        "include_sqs_metadata": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3140.74,
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
        "parquet_chunk_size_mb": 5540.32,
        "parquet_chunk_download_timeout": 4211.1,
        "checkpointing": {
            "enabled": False,
            "retries": 1555.53,
        },
        "poll_timeout": 9620.31,
        "checksum_suffix": "<value>",
        "max_manifest_size_kb": 517204,
        "validate_inventory_files": False,
        "description": "whoa beard mythology",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "queue_name": "security-lake-queue",
        "file_filter": "<value>",
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
            "<value 3>",
        ],
        "stale_channel_flush_ms": 2414.36,
        "max_messages": 9764.93,
        "visibility_timeout": 8497.5,
        "num_receivers": 9501.16,
        "socket_timeout": 9459.68,
        "skip_on_error": False,
        "include_sqs_metadata": True,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 3820.59,
        "enable_sqs_assume_role": True,
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
        "parquet_chunk_size_mb": 6915.79,
        "parquet_chunk_download_timeout": 118.76,
        "checkpointing": {
            "enabled": False,
            "retries": 1555.53,
        },
        "poll_timeout": 428.49,
        "encoding": "<value>",
        "description": "internal likewise aha whose those upwardly gosh sharply",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "192.168.1.1",
        "port": 161,
        "snmp_v3_auth": {
            "v3_auth_enabled": True,
            "allow_unmatched_trap": False,
            "v3_users": [
                {
                    "name": "<value>",
                    "auth_protocol": models.AuthenticationProtocolOptionsV3User.SHA384,
                    "auth_key": "<value>",
                    "priv_protocol": models.PrivacyProtocol.DES,
                    "priv_key": "<value>",
                },
            ],
        },
        "max_buffer_size": 6656.71,
        "ip_whitelist_regex": "<value>",
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 5082.57,
        "varbinds_with_types": True,
        "best_effort_parsing": False,
        "description": "gah blue majestically hence",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 9997,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 9578.9,
        "socket_idle_timeout": 4638.02,
        "socket_ending_max_wait": 1229.66,
        "socket_max_lifespan": 4340.71,
        "enable_proxy_header": True,
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
        "stale_channel_flush_ms": 7556.18,
        "auth_tokens": [
            {
                "token": "<value>",
                "description": "reopen blond yawningly huzzah yuck armchair ugh",
            },
        ],
        "max_s2_sversion": models.MaxS2SVersion.V3,
        "description": "than sentimental happy-go-lucky tempting",
        "use_fwd_timezone": True,
        "drop_control_fields": True,
        "extract_metrics": False,
        "compress": models.InputSplunkCompression.ALWAYS,
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
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
                "description": "better lest pfft during fervently dulcimer selfish custom whale somber",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 3944.77,
        "max_requests_per_socket": 799168,
        "enable_proxy_header": True,
        "capture_headers": False,
        "activity_log_sample_rate": 6427.77,
        "request_timeout": 8822.66,
        "socket_timeout": 1922.13,
        "keep_alive_timeout": 924.02,
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
        "splunk_hec_acks": True,
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 9829.02,
        "use_fwd_timezone": False,
        "drop_control_fields": True,
        "extract_metrics": False,
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
        "description": "torn whenever who fortunately whenever",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_splunk_hec_api": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "log_level": models.InputSplunkSearchLogLevel.WARN,
        "request_timeout": 6006.12,
        "use_round_robin_dns": False,
        "reject_unauthorized": True,
        "encoding": "<value>",
        "keep_alive_time": 1901.73,
        "job_timeout": "<value>",
        "max_missed_keep_alives": 244.27,
        "ttl": "<value>",
        "ignore_group_jobs_limit": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "retry_rules": {
            "type": models.RetryTypeOptionsHealthCheckCollectorConfRetryRules.NONE,
            "interval": 8023.69,
            "limit": 8538.93,
            "multiplier": 6735.17,
            "codes": [
                3551.76,
                3444.04,
                2558.51,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 1276.17,
        "auth_type": models.InputSplunkSearchAuthenticationType.BASIC,
        "description": "below mmm bulky gee approach phew monthly controvert volunteer if",
        "username": "Milton.Gottlieb",
        "password": "1Xwpask7BiTVNBz",
        "token": "<value>",
        "credentials_secret": "<value>",
        "text_secret": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
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
        "reuse_connections": False,
        "reject_unauthorized": False,
        "enable_assume_role": False,
        "assume_role_arn": "<value>",
        "assume_role_external_id": "<id>",
        "duration_seconds": 9240.08,
        "max_messages": 8942.09,
        "visibility_timeout": 8052.76,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "poll_timeout": 9292.66,
        "description": "outlaw nervously past",
        "aws_api_key": "<value>",
        "aws_secret": "<value>",
        "num_receivers": 8601.43,
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "udp_port": 514,
        "tcp_port": 1690.04,
        "max_buffer_size": 835.96,
        "ip_whitelist_regex": "<value>",
        "timestamp_timezone": "<value>",
        "single_msg_udp_packets": False,
        "enable_proxy_header": True,
        "keep_fields_list": [
            "<value 1>",
            "<value 2>",
        ],
        "octet_counting": True,
        "infer_framing": True,
        "strictly_infer_octet_counting": True,
        "allow_non_standard_app_name": False,
        "max_active_cxn": 3622.72,
        "socket_idle_timeout": 193.15,
        "socket_ending_max_wait": 3247.34,
        "socket_max_lifespan": 688.7,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "udp_socket_rx_buf_size": 1084.02,
        "enable_load_balancing": False,
        "description": "mysteriously concerning yahoo however ick kiss downchange handover out when",
        "enable_enhanced_proxy_header_parsing": True,
        "template_host": "<value>",
        "template_udp_port": "<value>",
        "template_tcp_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 5017.67,
        "host": {
            "mode": models.ModeOptionsHost.CUSTOM,
            "custom": {
                "system": {
                    "mode": models.InputSystemMetricsSystemMode.DISABLED,
                    "processes": False,
                },
                "cpu": {
                    "mode": models.InputSystemMetricsCPUMode.CUSTOM,
                    "per_cpu": True,
                    "detail": False,
                    "time": False,
                },
                "memory": {
                    "mode": models.InputSystemMetricsMemoryMode.DISABLED,
                    "detail": False,
                },
                "network": {
                    "mode": models.InputSystemMetricsNetworkMode.DISABLED,
                    "detail": True,
                    "protocols": True,
                    "devices": [
                        "<value 1>",
                    ],
                    "per_interface": True,
                },
                "disk": {
                    "mode": models.InputSystemMetricsDiskMode.CUSTOM,
                    "detail": False,
                    "inodes": False,
                    "devices": [
                        "<value 1>",
                    ],
                    "mountpoints": [
                        "<value 1>",
                        "<value 2>",
                    ],
                    "fstypes": [
                        "<value 1>",
                        "<value 2>",
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
                    "include_children": True,
                },
            ],
        },
        "container": {
            "mode": models.InputSystemMetricsContainerMode.BASIC,
            "docker_socket": [
                "<value 1>",
                "<value 2>",
            ],
            "docker_timeout": 7531.98,
            "filters": [
                {
                    "expr": "<value>",
                },
            ],
            "all_containers": True,
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
        "description": "worth alongside till during pharmacopoeia psst broadly",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 3542.37,
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
                "enable": True,
            },
            "dns": {
                "enable": False,
            },
            "user": {
                "enable": False,
            },
            "firewall": {
                "enable": False,
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
            "enable": True,
            "time_window": "<value>",
            "max_data_size": "<value>",
            "max_data_time": "<value>",
            "compress": models.DataCompressionFormatOptionsPersistence.GZIP,
            "dest_path": "<value>",
        },
        "disable_native_module": True,
        "disable_native_last_log_module": False,
        "description": "bustling overconfidently gleefully hmph slimy aha ultimately that as boohoo",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 1120.04,
        "socket_idle_timeout": 5926.54,
        "socket_ending_max_wait": 3298.44,
        "socket_max_lifespan": 6550.73,
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
        "stale_channel_flush_ms": 6014.24,
        "enable_header": True,
        "preprocess": {
            "disabled": True,
            "command": "<value>",
            "args": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "description": "failing behind uh-huh into mentor which cop-out",
        "auth_token": "<value>",
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.SECRET,
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 10090,
        "tls": {
            "disabled": True,
            "request_cert": True,
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "ip_whitelist_regex": "<value>",
        "max_active_cxn": 8150.03,
        "socket_idle_timeout": 4509.33,
        "socket_ending_max_wait": 8256.64,
        "socket_max_lifespan": 6518.95,
        "enable_proxy_header": True,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "enable_load_balancing": True,
        "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
        "description": "up for weary although obediently inwardly",
        "auth_token": "<value>",
        "text_secret": "<value>",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 5985,
        "auth_method": models.InputWefAuthenticationMethod.KERBEROS,
        "tls": {
            "disabled": True,
            "reject_unauthorized": False,
            "request_cert": True,
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "common_name_regex": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "ocsp_check": False,
            "keytab": "<value>",
            "principal": "<value>",
            "ocsp_check_fail_close": True,
        },
        "max_active_req": 7309.03,
        "max_requests_per_socket": 798308,
        "enable_proxy_header": False,
        "capture_headers": True,
        "keep_alive_timeout": 6011.4,
        "enable_health_check": False,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "socket_timeout": 5503.51,
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
                "locale": "fi",
                "query_selector": models.QueryBuilderMode.SIMPLE,
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
                "queries": [
                    {
                        "path": "/lost+found",
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
        "description": "before next usually barring yuppify um pace yuck drat since",
        "log_fingerprint_mismatch": False,
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "log_names": [
            "Application",
            "System",
        ],
        "read_mode": models.ReadMode.OLDEST,
        "event_format": models.EventFormat.JSON,
        "disable_native_module": True,
        "interval": 161.53,
        "batch_size": 2676.97,
        "metadata": [
            {
                "name": "<value>",
                "value": "<value>",
            },
        ],
        "max_event_bytes": 3989.15,
        "description": "outdo pear amidst unscramble forenenst mid analyse cow",
        "disable_json_rendering": True,
        "disable_xml_rendering": True,
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "interval": 7895.52,
        "host": {
            "mode": models.ModeOptionsHost.ALL,
            "custom": {
                "system": {
                    "mode": models.InputWindowsMetricsSystemMode.CUSTOM,
                    "detail": True,
                },
                "cpu": {
                    "mode": models.InputWindowsMetricsCPUMode.BASIC,
                    "per_cpu": True,
                    "detail": False,
                    "time": False,
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
                        "<value 2>",
                        "<value 3>",
                    ],
                    "per_interface": False,
                },
                "disk": {
                    "mode": models.InputWindowsMetricsDiskMode.DISABLED,
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
                    "include_children": True,
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
        "disable_native_module": False,
        "description": "shanghai bonfire cauliflower indeed",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "endpoint": "https://api.wiz.io",
        "auth_url": "https://auth.wiz.io/oauth/token",
        "auth_audience_override": "<value>",
        "client_id": "client-id",
        "content_config": [],
        "request_timeout": 968.17,
        "keep_alive_time": 3750.97,
        "max_missed_keep_alives": 9118.86,
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
            "interval": 8023.69,
            "limit": 8538.93,
            "multiplier": 6735.17,
            "codes": [
                3551.76,
                3444.04,
                2558.51,
            ],
            "enable_header": False,
            "retry_connect_timeout": True,
            "retry_connect_reset": False,
        },
        "auth_type": models.AuthenticationMethodOptions1.MANUAL,
        "description": "madly whoa subtle coop or stratify",
        "client_secret": "<value>",
        "text_secret": "<value>",
        "template_endpoint": "<value>",
        "template_auth_url": "https://shocked-responsibility.info",
        "template_client_id": "<id>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 8977.16,
        "max_requests_per_socket": 153946,
        "enable_proxy_header": False,
        "capture_headers": True,
        "activity_log_sample_rate": 4062.3,
        "request_timeout": 4871.45,
        "socket_timeout": 5909.3,
        "keep_alive_timeout": 634.62,
        "enable_health_check": True,
        "ip_allowlist_regex": "<value>",
        "ip_denylist_regex": "<value>",
        "breaker_rulesets": [
            "<value 1>",
            "<value 2>",
        ],
        "stale_channel_flush_ms": 3516.58,
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
                "description": "ew phooey unless aha plus woot zowie unless",
                "metadata": [
                    {
                        "name": "<value>",
                        "value": "<value>",
                    },
                ],
            },
        ],
        "description": "trusty coast furthermore finally so ape mystify impressionable",
        "template_host": "<value>",
        "template_port": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
            "compress": models.CompressionOptionsPq.GZIP,
            "pq_controls": {},
        },
        "host": "0.0.0.0",
        "port": 8088,
        "auth_tokens": [
            {
                "auth_type": models.AuthenticationMethodOptionsAuthTokensItems.MANUAL,
                "token_secret": "<value>",
                "token": "<value>",
                "enabled": False,
                "description": "versus an thankfully and or inside playfully whether daintily",
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
            "reject_unauthorized": True,
            "common_name_regex": "<value>",
            "certificate_name": "<value>",
            "priv_key_path": "<value>",
            "passphrase": "<value>",
            "cert_path": "<value>",
            "ca_path": "<value>",
            "min_version": models.MinimumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_3,
            "max_version": models.MaximumTLSVersionOptionsKafkaSchemaRegistryTLS.TL_SV1_2,
        },
        "max_active_req": 77.42,
        "max_requests_per_socket": 147184,
        "enable_proxy_header": False,
        "capture_headers": False,
        "activity_log_sample_rate": 5157.16,
        "request_timeout": 3819.67,
        "socket_timeout": 4473.94,
        "keep_alive_timeout": 665.59,
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
            "<value 2>",
            "<value 3>",
        ],
        "access_control_allow_headers": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "emit_token_metrics": True,
        "description": "valiantly and whisper",
        "template_host": "<value>",
        "template_port": "<value>",
        "template_hec_api": "<value>",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "description": "wherever qualified questionably fork amid",
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
            "max_buffer_size": 5318.64,
            "commit_frequency": 3762.63,
            "max_file_size": "<value>",
            "max_size": "<value>",
            "path": "/opt/sbin",
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
        "description": "word what fall expense tromp nerve",
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