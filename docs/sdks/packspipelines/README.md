# Packs.Pipelines

## Overview

### Available Operations

* [create](#create) - Create a Pipeline within a Pack
* [list](#list) - List all Pipelines within a Pack
* [delete](#delete) - Delete a Pipeline within a Pack
* [get](#get) - Get a Pipeline within a Pack
* [update](#update) - Update a Pipeline within a Pack

## create

Create a new Pipeline within the specified Pack.

### Example Usage: PipelineExamplesAggregateMetrics

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesAggregateMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="aggregate-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that aggregates process metrics: CPU, memory, and bytes over time windows",
        "streamtags": [],
        "functions": [
            {
                "filter_": "(_metric == 'proc.cpu_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.cpu_perc'\")) || (_metric == 'proc.mem_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.mem_perc'\")) || (_metric == 'proc.bytes_in' || __criblMetrics[0].nameExpr.includes(\"'proc.bytes_in'\"))",
                "id": models.PipelineFunctionAggregateMetricsID.AGGREGATE_METRICS,
                "conf": {
                    "cumulative": False,
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "time_window": "10s",
                    "aggregations": [
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.GAUGE,
                            "agg": "avg(_value || proc.cpu_perc).as(proc.cpu_perc_avg)",
                        },
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.GAUGE,
                            "agg": "sum(_value || proc.mem_perc).as(proc.mem_perc_sum)",
                        },
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.COUNTER,
                            "agg": "count(_value || proc.bytes_in).as(proc.bytes_in_count)",
                        },
                    ],
                    "groupbys": [
                        "proc",
                    ],
                    "should_treat_dots_as_literals": True,
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesAggregations

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesAggregations" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="aggregation-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that aggregates rejected bytes grouped by source address every 10 seconds",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionAggregationID.AGGREGATION,
                "conf": {
                    "cumulative": False,
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "metrics_mode": False,
                    "time_window": "10s",
                    "aggregations": [
                        "sum(bytes).where(action==\"REJECT\").as(TotalBytes)",
                    ],
                    "groupbys": [
                        "srcaddr",
                    ],
                    "should_treat_dots_as_literals": False,
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesAutoTimestamp

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesAutoTimestamp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="auto-timestamp-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts timestamps from event data using auto timestamp function",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionAutoTimestampID.AUTO_TIMESTAMP,
                "conf": {
                    "src_field": "_raw",
                    "dst_field": "_time",
                    "default_timezone": "local",
                    "time_expression": "time.getTime() / 1000",
                    "offset": 0,
                    "max_len": 150,
                    "default_time": models.DefaultTime.NOW,
                    "latest_date_allowed": "+1week",
                    "earliest_date_allowed": "-420weeks",
                    "timestamps": [
                        {
                            "regex": "/(\\d{1,2}\\/\\d{2}\\/\\d{4}\\s\\d{1,2}:\\d{2}:\\d{2}\\s\\w{2})/",
                            "strptime": "%Y-%m-%d %H:%M:%S",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesCEFSerializer

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesCEFSerializer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="cef-serializer-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that formats events in CEF format with custom header and extension fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCefID.CEF,
                "conf": {
                    "output_field": "_raw",
                    "header": [
                        {
                            "value": "'CEF:0'",
                        },
                        {
                            "value": "'Cribl'",
                        },
                        {
                            "value": "'Cribl'",
                        },
                        {
                            "value": "C.version",
                        },
                        {
                            "value": "420",
                        },
                        {
                            "value": "'Cribl Event'",
                        },
                        {
                            "value": "6",
                        },
                    ],
                    "extension": [
                        {
                            "name": "c6a1Label",
                            "value": "'Colorado_Ext_Bldg7'",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesChain

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesChain" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="chain-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that chains to another pipeline for sequential data processing",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionChainID.CHAIN,
                "conf": {
                    "processor": "prometheus_metrics",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesClone

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesClone" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="clone-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that creates cloned events with additional fields for comparison or routing",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCloneID.CLONE,
                "conf": {
                    "clones": [
                        {
                            "env": "staging",
                        },
                        {
                            "index": "clones",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesComment

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesComment" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="comment-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline with comment function for documentation",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCommentID.COMMENT,
                "conf": {
                    "comment": "This function processes security events and enriches them with DNS lookups",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDNSLookup

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesDNSLookup" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="dns-lookup-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that performs DNS lookups to resolve hostnames and IP addresses",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionDNSLookup(
                filter_="true",
                id=models.PipelineFunctionDNSLookupID.DNS_LOOKUP,
                conf=models.FunctionConfSchemaDNSLookup(
                    dns_lookup_fields=[
                        models.DNSLookupField(
                            in_field_name="hostname",
                            resource_record_type=models.ResourceRecordType.A,
                            out_field_name="hostname_ip",
                        ),
                    ],
                    reverse_lookup_fields=[
                        models.ReverseLookupField(
                            in_field_name="src_ip",
                            out_field_name="src_hostname",
                        ),
                    ],
                    cache_ttl=30,
                    max_cache_size=5000,
                    use_resolv_conf=False,
                    lookup_fallback=False,
                    lookup_fail_log_level=models.LogLevelForFailedLookups.ERROR,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDrop

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesDrop" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="drop-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that drops events containing success messages",
        "streamtags": [],
        "functions": [
            {
                "filter_": "_raw.search(/success/i)>=0",
                "id": models.PipelineFunctionDropID.DROP,
                "conf": {},
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDropDimensions

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesDropDimensions" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="drop-dimensions-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that drops specified dimensions from metrics to reduce cardinality",
        "streamtags": [],
        "functions": [
            {
                "filter_": "(_metric == 'proc.cpu_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.cpu_perc'\")) && (__criblMetrics[0].dims.includes(\"proc\"))",
                "id": models.PipelineFunctionDropDimensionsID.DROP_DIMENSIONS,
                "conf": {
                    "time_window": "10s",
                    "drop_dimensions": [
                        "proc",
                        "pie",
                        "unit",
                    ],
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDynamicSampling

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesDynamicSampling" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="dynamic-sampling-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that dynamically samples events based on volume using square root mode",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionDynamicSamplingID.DYNAMIC_SAMPLING,
                "conf": {
                    "mode": models.SampleMode.SQRT,
                    "key_expr": "`${domain}:${httpCode}`",
                    "sample_period": 20,
                    "min_events": 3,
                    "max_sample_rate": 3,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEmpty

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesEmpty" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="empty-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "",
        "streamtags": [],
        "functions": [],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEval

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesEval" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="eval-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that evaluates JavaScript expressions to add, modify, and remove fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionEvalID.EVAL,
                "conf": {
                    "add": [
                        {
                            "name": "action",
                            "value": "login == 'error' ? 'blocked' : action",
                        },
                        {
                            "name": "myTags",
                            "value": "login == 'error' ? [...myTags, 'error'] : myTags",
                        },
                    ],
                    "keep": [
                        "host",
                        "source",
                        "action",
                        "myTags",
                    ],
                    "remove": [
                        "identification",
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEventBreaker

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesEventBreaker" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="event-breaker-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that breaks large event streams into discrete events using regex",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionEventBreaker(
                filter_="true",
                id=models.PipelineFunctionEventBreakerID.EVENT_BREAKER,
                conf=models.EventBreakerExistingOrNewNewRuleTypeRegex(
                    rule_type=models.EventBreakerTypeOptionsEventBreakerExistingOrNewNew.REGEX,
                    event_breaker_regex="/[\\n\\r]+(?!\\s)/",
                    existing_or_new=models.EventBreakerExistingOrNewNewRuleTypeRegexExistingOrNew.NEW,
                    max_event_bytes=51200,
                    timestamp_anchor_regex="/^/",
                    timestamp=models.EventBreakerExistingOrNewNewRuleTypeRegexTimestampFormat(
                        type=models.TimestampTypeOptionsEventBreakerExistingOrNewNewTimestamp.AUTO,
                        length=150,
                    ),
                    timestamp_timezone="local",
                    timestamp_earliest="-420weeks",
                    timestamp_latest="+1week",
                    should_mark_cribl_breaker=True,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesFlatten

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesFlatten" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="flatten-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that flattens nested JSON structures into top-level fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionFlattenID.FLATTEN,
                "conf": {
                    "fields": [],
                    "prefix": "",
                    "depth": 5,
                    "delimiter": "_",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesFoldKeys

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesFoldKeys" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="fold-keys-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that transforms flat field names with separators into nested structures",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionFoldkeysID.FOLDKEYS,
                "conf": {
                    "delete_original": True,
                    "separator": "_",
                    "selection_reg_exp": "^data",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGeoIP

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesGeoIP" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="geoip-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that enriches events with geolocation data from IP addresses",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionGeoipID.GEOIP,
                "conf": {
                    "file": "GeoLite2-City.mmdb",
                    "in_field": "ip",
                    "out_field": "geoip",
                    "additional_fields": [
                        {
                            "extra_in_field": "src_ip",
                            "extra_out_field": "src_geoip",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGrok

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesGrok" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="grok-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts structured fields from log data using Grok patterns",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionGrokID.GROK,
                "conf": {
                    "pattern": "%{TIMESTAMP_ISO8601:event_time} %{LOGLEVEL:log_level} %{GREEDYDATA:log_message}",
                    "pattern_list": [],
                    "source": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGuard

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesGuard" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="guard-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that scans for sensitive data and applies mitigation expressions",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSensitiveDataScannerID.SENSITIVE_DATA_SCANNER,
                "conf": {
                    "rules": [
                        {
                            "ruleset_id": "Finance_Global",
                            "replace_expr": "'REDACTED'",
                            "disabled": False,
                        },
                    ],
                    "fields": [
                        "_raw",
                    ],
                    "exclude_fields": [],
                    "flags": [
                        {
                            "name": "_sensitive",
                            "value": "true",
                        },
                    ],
                    "include_detected_rules": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesJSONUnroll

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesJSONUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="json-unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls JSON arrays into individual events while retaining parent fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionJSONUnrollID.JSON_UNROLL,
                "conf": {
                    "path": "allCars",
                    "name": "cars",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesLookup

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesLookup" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="lookup-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that enriches events with location data from IP address lookups",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionLookupID.LOOKUP,
                "conf": {
                    "match_mode": models.LookupDbLookupFalseMatchModeExactMatchMode.EXACT,
                    "ignore_case": False,
                    "db_lookup": False,
                    "reload_period_sec": -1,
                    "file": "ip_locations.csv",
                    "in_fields": [
                        {
                            "event_field": "destination_ip",
                            "lookup_field": "ip",
                        },
                    ],
                    "out_fields": [
                        {
                            "lookup_field": "location",
                            "event_field": "location",
                            "default_value": "Unknown",
                        },
                    ],
                    "add_to_event": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesMask

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesMask" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="mask-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that masks Social Security numbers and other sensitive data",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionMaskID.MASK,
                "conf": {
                    "rules": [
                        {
                            "match_regex": "/(social=)(\\d+)/",
                            "replace_expr": "`${g1}${C.Mask.md5(g2)}`",
                            "disabled": False,
                        },
                    ],
                    "fields": [
                        "_raw",
                    ],
                    "depth": 5,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesNumerify

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesNumerify" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="numerify-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that converts string numbers to numeric type for mathematical operations",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionNumerifyID.NUMERIFY,
                "conf": {
                    "format_": models.NumerifyFormatNoneFormat.NONE,
                    "depth": 5,
                    "ignore_fields": [],
                    "filter_expr": "",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPLogs

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesOTLPLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="otlp-logs-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that normalizes and batches OTLP log events from OpenTelemetry sources",
        "streamtags": [],
        "functions": [
            {
                "filter_": "__inputId=='open_telemetry:open_telemetry'",
                "id": models.PipelineFunctionOtlpLogsID.OTLP_LOGS,
                "conf": {
                    "batch_otlp_logs": True,
                    "send_batch_size": 8192,
                    "timeout": 200,
                    "send_batch_max_size": 0,
                    "metadata_keys": [],
                    "metadata_cardinality_limit": 1000,
                    "drop_non_log_events": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPMetrics

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesOTLPMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="otlp-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that converts dimensional metrics to OTLP format and batches them by resource attributes",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionOtlpMetrics(
                filter_="__inputId=='prometheus_rw:prom_rw_in'",
                id=models.PipelineFunctionOtlpMetricsID.OTLP_METRICS,
                conf=models.OTLPMetricsBatchOTLPMetricsTrue(
                    batch_otlp_metrics=True,
                    send_batch_size=8192,
                    timeout=200,
                    send_batch_max_size=0,
                    metadata_keys=[],
                    metadata_cardinality_limit=1000,
                    resource_attribute_prefixes=[
                        "service",
                        "system",
                        "telemetry",
                        "k8s",
                        "cloud",
                        "host",
                        "process",
                    ],
                    drop_non_metric_events=False,
                    otlp_version=models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPTraces

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesOTLPTraces" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="otlp-traces-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that normalizes and batches OTLP trace events from OpenTelemetry sources",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionOtlpTraces(
                filter_="__inputId=='open_telemetry:open_telemetry'",
                id=models.PipelineFunctionOtlpTracesID.OTLP_TRACES,
                conf=models.OTLPTracesBatchOTLPTracesTrue(
                    batch_otlp_traces=True,
                    send_batch_size=8192,
                    timeout=200,
                    send_batch_max_size=0,
                    metadata_keys=[],
                    metadata_cardinality_limit=1000,
                    drop_non_trace_events=False,
                    otlp_version=models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesParser

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesParser" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="parser-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts fields from key-value pair formatted data",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionSerde(
                filter_="true",
                id=models.PipelineFunctionSerdeID.SERDE,
                conf=models.SerdeTypeKvp(
                    type=models.TypeOptions.KVP,
                    keep=[
                        "a",
                        "b",
                        "c",
                    ],
                    remove=[
                        "*",
                    ],
                    clean_fields=False,
                    mode=models.SerdeTypeKvpOperationMode.EXTRACT,
                    src_field="_raw",
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesPublishMetrics

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesPublishMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="publish-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts metrics from events and formats them for metrics aggregation platforms",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionPublishMetricsID.PUBLISH_METRICS,
                "conf": {
                    "fields": [
                        {
                            "in_field_name": "bytes",
                            "out_field_expr": "'metric_name.bytes'",
                            "metric_type": models.FunctionConfSchemaPublishMetricsMetricType.GAUGE,
                        },
                        {
                            "in_field_name": "packets",
                            "out_field_expr": "'metric_name.packets'",
                            "metric_type": models.FunctionConfSchemaPublishMetricsMetricType.GAUGE,
                        },
                    ],
                    "overwrite": False,
                    "dimensions": [
                        "action",
                        "interface_id",
                        "dstaddr",
                    ],
                    "remove_metrics": [],
                    "remove_dimensions": [],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRedis

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesRedis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="redis-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that retrieves values from Redis using GET command",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionRedis(
                filter_="true",
                id=models.PipelineFunctionRedisID.REDIS,
                conf=models.RedisAuthTypeNone(
                    auth_type=models.RedisAuthTypeNoneAuthenticationMethod.NONE,
                    commands=[
                        models.RedisAuthTypeNoneCommand(
                            out_field="cached_value",
                            command="get",
                            key_expr="'user_session'",
                            args_expr="",
                        ),
                    ],
                    deployment_type=models.RedisAuthTypeNoneDeploymentType.STANDALONE,
                    max_block_secs=60,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRegexExtract

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesRegexExtract" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="regex-extract-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts structured fields from log data using regex patterns with named capture groups",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRegexExtractID.REGEX_EXTRACT,
                "conf": {
                    "regex": "/metric1=(?<metric1>\\d+)/",
                    "source": "_raw",
                    "iterations": 100,
                    "overwrite": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRegexFilter

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesRegexFilter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="regex-filter-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that filters out events matching specific regex patterns",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRegexFilterID.REGEX_FILTER,
                "conf": {
                    "regex": "/Opera/",
                    "field": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRename

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesRename" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="rename-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that renames fields using key-value pairs and expressions",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRenameID.RENAME,
                "conf": {
                    "base_fields": [],
                    "rename": [
                        {
                            "current_name": "level",
                            "new_name": "LEVEL",
                        },
                    ],
                    "rename_expr": "name.startsWith('out') ? name.toUpperCase() : name",
                    "wildcard_depth": 5,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRollupMetrics

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesRollupMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="rollup-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that consolidates high-frequency metrics into manageable time windows",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRollupMetricsID.ROLLUP_METRICS,
                "conf": {
                    "dimensions": [
                        "*",
                    ],
                    "time_window": "30s",
                    "gauge_rollup": models.GaugeUpdate.LAST,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSNMPTrapSerialize

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesSNMPTrapSerialize" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="snmp-trap-serialize-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that serializes events into SNMP trap format for SNMP trap destinations",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSnmpTrapSerializeID.SNMP_TRAP_SERIALIZE,
                "conf": {
                    "strict": True,
                    "drop_failed_events": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSampling

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesSampling" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="sampling-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that samples events at specified rates based on filter criteria",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSamplingID.SAMPLING,
                "conf": {
                    "rules": [
                        {
                            "filter_": "__status == 200",
                            "rate": 5,
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSerialize

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesSerialize" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="serialize-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that serializes event fields into JSON format",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSerializeID.SERIALIZE,
                "conf": {
                    "type": models.SerializeTypeCsvType.CSV,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSuppress

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesSuppress" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="suppress-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that suppresses duplicate events based on a key expression",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSuppressID.SUPPRESS,
                "conf": {
                    "key_expr": "`${ip}:${port}`",
                    "allow": 1,
                    "suppress_period_sec": 30,
                    "drop_events_mode": True,
                    "max_cache_size": 50000,
                    "cache_idle_timeout_periods": 2,
                    "num_events_idle_timeout_trigger": 10000,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesTee

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesTee" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="tee-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that sends events to a command via stdin for debugging purposes",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionTeeID.TEE,
                "conf": {
                    "command": "tee",
                    "args": [
                        "/opt/cribl/foo.log",
                    ],
                    "restart_on_exit": True,
                    "env": {

                    },
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesUnroll

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls array fields into separate events",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionUnrollID.UNROLL,
                "conf": {
                    "src_expr": "_raw.split(/\\n/)",
                    "dst_field": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesXMLUnroll

<!-- UsageSnippet language="python" operationID="createPipelinesByPack" method="post" path="/p/{pack}/pipelines" example="PipelineExamplesXMLUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.create(pack="<value>", id="xml-unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls XML elements into separate events",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionXMLUnrollID.XML_UNROLL,
                "conf": {
                    "unroll": "^Parent\\.Child$",
                    "inherit": "^Parent\\.(myID|branchLocation)$",
                    "unroll_idx_field": "unroll_idx",
                    "pretty": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to create.                          |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conf`                                                              | [models.ConfInput](../../models/confinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPipeline](../../models/countedpipeline.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of all Pipelines within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPipelinesByPack" method="get" path="/p/{pack}/pipelines" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.list(pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to list.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPipeline](../../models/countedpipeline.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Pipeline within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePipelinesByPackAndId" method="delete" path="/p/{pack}/pipelines/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.delete(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pipeline to delete.                      |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to delete.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPipeline](../../models/countedpipeline.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Pipeline within the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPipelinesByPackAndId" method="get" path="/p/{pack}/pipelines/{id}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.get(id="<id>", pack="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pipeline to get.                         |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to get.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPipeline](../../models/countedpipeline.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Pipeline within the specified Pack.</br></br>Provide a complete representation of the Pipeline that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Pipeline.</br></br>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Pipeline might not function as expected.

### Example Usage: PipelineExamplesAggregateMetrics

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesAggregateMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="aggregate-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that aggregates process metrics: CPU, memory, and bytes over time windows",
        "streamtags": [],
        "functions": [
            {
                "filter_": "(_metric == 'proc.cpu_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.cpu_perc'\")) || (_metric == 'proc.mem_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.mem_perc'\")) || (_metric == 'proc.bytes_in' || __criblMetrics[0].nameExpr.includes(\"'proc.bytes_in'\"))",
                "id": models.PipelineFunctionAggregateMetricsID.AGGREGATE_METRICS,
                "conf": {
                    "cumulative": False,
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "time_window": "10s",
                    "aggregations": [
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.GAUGE,
                            "agg": "avg(_value || proc.cpu_perc).as(proc.cpu_perc_avg)",
                        },
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.GAUGE,
                            "agg": "sum(_value || proc.mem_perc).as(proc.mem_perc_sum)",
                        },
                        {
                            "metric_type": models.AggregateMetricsCumulativeTrueMetricType.COUNTER,
                            "agg": "count(_value || proc.bytes_in).as(proc.bytes_in_count)",
                        },
                    ],
                    "groupbys": [
                        "proc",
                    ],
                    "should_treat_dots_as_literals": True,
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesAggregations

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesAggregations" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="aggregation-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that aggregates rejected bytes grouped by source address every 10 seconds",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionAggregationID.AGGREGATION,
                "conf": {
                    "cumulative": False,
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "metrics_mode": False,
                    "time_window": "10s",
                    "aggregations": [
                        "sum(bytes).where(action==\"REJECT\").as(TotalBytes)",
                    ],
                    "groupbys": [
                        "srcaddr",
                    ],
                    "should_treat_dots_as_literals": False,
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesAutoTimestamp

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesAutoTimestamp" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="auto-timestamp-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts timestamps from event data using auto timestamp function",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionAutoTimestampID.AUTO_TIMESTAMP,
                "conf": {
                    "src_field": "_raw",
                    "dst_field": "_time",
                    "default_timezone": "local",
                    "time_expression": "time.getTime() / 1000",
                    "offset": 0,
                    "max_len": 150,
                    "default_time": models.DefaultTime.NOW,
                    "latest_date_allowed": "+1week",
                    "earliest_date_allowed": "-420weeks",
                    "timestamps": [
                        {
                            "regex": "/(\\d{1,2}\\/\\d{2}\\/\\d{4}\\s\\d{1,2}:\\d{2}:\\d{2}\\s\\w{2})/",
                            "strptime": "%Y-%m-%d %H:%M:%S",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesCEFSerializer

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesCEFSerializer" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="cef-serializer-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that formats events in CEF format with custom header and extension fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCefID.CEF,
                "conf": {
                    "output_field": "_raw",
                    "header": [
                        {
                            "value": "'CEF:0'",
                        },
                        {
                            "value": "'Cribl'",
                        },
                        {
                            "value": "'Cribl'",
                        },
                        {
                            "value": "C.version",
                        },
                        {
                            "value": "420",
                        },
                        {
                            "value": "'Cribl Event'",
                        },
                        {
                            "value": "6",
                        },
                    ],
                    "extension": [
                        {
                            "name": "c6a1Label",
                            "value": "'Colorado_Ext_Bldg7'",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesChain

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesChain" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="chain-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that chains to another pipeline for sequential data processing",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionChainID.CHAIN,
                "conf": {
                    "processor": "prometheus_metrics",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesClone

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesClone" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="clone-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that creates cloned events with additional fields for comparison or routing",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCloneID.CLONE,
                "conf": {
                    "clones": [
                        {
                            "env": "staging",
                        },
                        {
                            "index": "clones",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesComment

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesComment" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="comment-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline with comment function for documentation",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionCommentID.COMMENT,
                "conf": {
                    "comment": "This function processes security events and enriches them with DNS lookups",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDNSLookup

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesDNSLookup" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="dns-lookup-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that performs DNS lookups to resolve hostnames and IP addresses",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionDNSLookup(
                filter_="true",
                id=models.PipelineFunctionDNSLookupID.DNS_LOOKUP,
                conf=models.FunctionConfSchemaDNSLookup(
                    dns_lookup_fields=[
                        models.DNSLookupField(
                            in_field_name="hostname",
                            resource_record_type=models.ResourceRecordType.A,
                            out_field_name="hostname_ip",
                        ),
                    ],
                    reverse_lookup_fields=[
                        models.ReverseLookupField(
                            in_field_name="src_ip",
                            out_field_name="src_hostname",
                        ),
                    ],
                    cache_ttl=30,
                    max_cache_size=5000,
                    use_resolv_conf=False,
                    lookup_fallback=False,
                    lookup_fail_log_level=models.LogLevelForFailedLookups.ERROR,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDrop

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesDrop" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="drop-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that drops events containing success messages",
        "streamtags": [],
        "functions": [
            {
                "filter_": "_raw.search(/success/i)>=0",
                "id": models.PipelineFunctionDropID.DROP,
                "conf": {},
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDropDimensions

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesDropDimensions" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="drop-dimensions-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that drops specified dimensions from metrics to reduce cardinality",
        "streamtags": [],
        "functions": [
            {
                "filter_": "(_metric == 'proc.cpu_perc' || __criblMetrics[0].nameExpr.includes(\"'proc.cpu_perc'\")) && (__criblMetrics[0].dims.includes(\"proc\"))",
                "id": models.PipelineFunctionDropDimensionsID.DROP_DIMENSIONS,
                "conf": {
                    "time_window": "10s",
                    "drop_dimensions": [
                        "proc",
                        "pie",
                        "unit",
                    ],
                    "flush_on_input_close": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesDynamicSampling

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesDynamicSampling" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="dynamic-sampling-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that dynamically samples events based on volume using square root mode",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionDynamicSamplingID.DYNAMIC_SAMPLING,
                "conf": {
                    "mode": models.SampleMode.SQRT,
                    "key_expr": "`${domain}:${httpCode}`",
                    "sample_period": 20,
                    "min_events": 3,
                    "max_sample_rate": 3,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEmpty

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesEmpty" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="empty-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "",
        "streamtags": [],
        "functions": [],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEval

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesEval" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="eval-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that evaluates JavaScript expressions to add, modify, and remove fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionEvalID.EVAL,
                "conf": {
                    "add": [
                        {
                            "name": "action",
                            "value": "login == 'error' ? 'blocked' : action",
                        },
                        {
                            "name": "myTags",
                            "value": "login == 'error' ? [...myTags, 'error'] : myTags",
                        },
                    ],
                    "keep": [
                        "host",
                        "source",
                        "action",
                        "myTags",
                    ],
                    "remove": [
                        "identification",
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesEventBreaker

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesEventBreaker" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="event-breaker-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that breaks large event streams into discrete events using regex",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionEventBreaker(
                filter_="true",
                id=models.PipelineFunctionEventBreakerID.EVENT_BREAKER,
                conf=models.EventBreakerExistingOrNewNewRuleTypeRegex(
                    rule_type=models.EventBreakerTypeOptionsEventBreakerExistingOrNewNew.REGEX,
                    event_breaker_regex="/[\\n\\r]+(?!\\s)/",
                    existing_or_new=models.EventBreakerExistingOrNewNewRuleTypeRegexExistingOrNew.NEW,
                    max_event_bytes=51200,
                    timestamp_anchor_regex="/^/",
                    timestamp=models.EventBreakerExistingOrNewNewRuleTypeRegexTimestampFormat(
                        type=models.TimestampTypeOptionsEventBreakerExistingOrNewNewTimestamp.AUTO,
                        length=150,
                    ),
                    timestamp_timezone="local",
                    timestamp_earliest="-420weeks",
                    timestamp_latest="+1week",
                    should_mark_cribl_breaker=True,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesFlatten

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesFlatten" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="flatten-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that flattens nested JSON structures into top-level fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionFlattenID.FLATTEN,
                "conf": {
                    "fields": [],
                    "prefix": "",
                    "depth": 5,
                    "delimiter": "_",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesFoldKeys

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesFoldKeys" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="fold-keys-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that transforms flat field names with separators into nested structures",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionFoldkeysID.FOLDKEYS,
                "conf": {
                    "delete_original": True,
                    "separator": "_",
                    "selection_reg_exp": "^data",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGeoIP

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesGeoIP" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="geoip-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that enriches events with geolocation data from IP addresses",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionGeoipID.GEOIP,
                "conf": {
                    "file": "GeoLite2-City.mmdb",
                    "in_field": "ip",
                    "out_field": "geoip",
                    "additional_fields": [
                        {
                            "extra_in_field": "src_ip",
                            "extra_out_field": "src_geoip",
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGrok

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesGrok" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="grok-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts structured fields from log data using Grok patterns",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionGrokID.GROK,
                "conf": {
                    "pattern": "%{TIMESTAMP_ISO8601:event_time} %{LOGLEVEL:log_level} %{GREEDYDATA:log_message}",
                    "pattern_list": [],
                    "source": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesGuard

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesGuard" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="guard-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that scans for sensitive data and applies mitigation expressions",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSensitiveDataScannerID.SENSITIVE_DATA_SCANNER,
                "conf": {
                    "rules": [
                        {
                            "ruleset_id": "Finance_Global",
                            "replace_expr": "'REDACTED'",
                            "disabled": False,
                        },
                    ],
                    "fields": [
                        "_raw",
                    ],
                    "exclude_fields": [],
                    "flags": [
                        {
                            "name": "_sensitive",
                            "value": "true",
                        },
                    ],
                    "include_detected_rules": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesJSONUnroll

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesJSONUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="json-unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls JSON arrays into individual events while retaining parent fields",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionJSONUnrollID.JSON_UNROLL,
                "conf": {
                    "path": "allCars",
                    "name": "cars",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesLookup

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesLookup" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="lookup-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that enriches events with location data from IP address lookups",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionLookupID.LOOKUP,
                "conf": {
                    "match_mode": models.LookupDbLookupFalseMatchModeExactMatchMode.EXACT,
                    "ignore_case": False,
                    "db_lookup": False,
                    "reload_period_sec": -1,
                    "file": "ip_locations.csv",
                    "in_fields": [
                        {
                            "event_field": "destination_ip",
                            "lookup_field": "ip",
                        },
                    ],
                    "out_fields": [
                        {
                            "lookup_field": "location",
                            "event_field": "location",
                            "default_value": "Unknown",
                        },
                    ],
                    "add_to_event": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesMask

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesMask" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="mask-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that masks Social Security numbers and other sensitive data",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionMaskID.MASK,
                "conf": {
                    "rules": [
                        {
                            "match_regex": "/(social=)(\\d+)/",
                            "replace_expr": "`${g1}${C.Mask.md5(g2)}`",
                            "disabled": False,
                        },
                    ],
                    "fields": [
                        "_raw",
                    ],
                    "depth": 5,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesNumerify

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesNumerify" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="numerify-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that converts string numbers to numeric type for mathematical operations",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionNumerifyID.NUMERIFY,
                "conf": {
                    "format_": models.NumerifyFormatNoneFormat.NONE,
                    "depth": 5,
                    "ignore_fields": [],
                    "filter_expr": "",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPLogs

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesOTLPLogs" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="otlp-logs-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that normalizes and batches OTLP log events from OpenTelemetry sources",
        "streamtags": [],
        "functions": [
            {
                "filter_": "__inputId=='open_telemetry:open_telemetry'",
                "id": models.PipelineFunctionOtlpLogsID.OTLP_LOGS,
                "conf": {
                    "batch_otlp_logs": True,
                    "send_batch_size": 8192,
                    "timeout": 200,
                    "send_batch_max_size": 0,
                    "metadata_keys": [],
                    "metadata_cardinality_limit": 1000,
                    "drop_non_log_events": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPMetrics

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesOTLPMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="otlp-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that converts dimensional metrics to OTLP format and batches them by resource attributes",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionOtlpMetrics(
                filter_="__inputId=='prometheus_rw:prom_rw_in'",
                id=models.PipelineFunctionOtlpMetricsID.OTLP_METRICS,
                conf=models.OTLPMetricsBatchOTLPMetricsTrue(
                    batch_otlp_metrics=True,
                    send_batch_size=8192,
                    timeout=200,
                    send_batch_max_size=0,
                    metadata_keys=[],
                    metadata_cardinality_limit=1000,
                    resource_attribute_prefixes=[
                        "service",
                        "system",
                        "telemetry",
                        "k8s",
                        "cloud",
                        "host",
                        "process",
                    ],
                    drop_non_metric_events=False,
                    otlp_version=models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesOTLPTraces

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesOTLPTraces" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="otlp-traces-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that normalizes and batches OTLP trace events from OpenTelemetry sources",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionOtlpTraces(
                filter_="__inputId=='open_telemetry:open_telemetry'",
                id=models.PipelineFunctionOtlpTracesID.OTLP_TRACES,
                conf=models.OTLPTracesBatchOTLPTracesTrue(
                    batch_otlp_traces=True,
                    send_batch_size=8192,
                    timeout=200,
                    send_batch_max_size=0,
                    metadata_keys=[],
                    metadata_cardinality_limit=1000,
                    drop_non_trace_events=False,
                    otlp_version=models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesParser

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesParser" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="parser-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts fields from key-value pair formatted data",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionSerde(
                filter_="true",
                id=models.PipelineFunctionSerdeID.SERDE,
                conf=models.SerdeTypeKvp(
                    type=models.TypeOptions.KVP,
                    keep=[
                        "a",
                        "b",
                        "c",
                    ],
                    remove=[
                        "*",
                    ],
                    clean_fields=False,
                    mode=models.SerdeTypeKvpOperationMode.EXTRACT,
                    src_field="_raw",
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesPublishMetrics

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesPublishMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="publish-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts metrics from events and formats them for metrics aggregation platforms",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionPublishMetricsID.PUBLISH_METRICS,
                "conf": {
                    "fields": [
                        {
                            "in_field_name": "bytes",
                            "out_field_expr": "'metric_name.bytes'",
                            "metric_type": models.FunctionConfSchemaPublishMetricsMetricType.GAUGE,
                        },
                        {
                            "in_field_name": "packets",
                            "out_field_expr": "'metric_name.packets'",
                            "metric_type": models.FunctionConfSchemaPublishMetricsMetricType.GAUGE,
                        },
                    ],
                    "overwrite": False,
                    "dimensions": [
                        "action",
                        "interface_id",
                        "dstaddr",
                    ],
                    "remove_metrics": [],
                    "remove_dimensions": [],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRedis

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesRedis" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="redis-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that retrieves values from Redis using GET command",
        "streamtags": [],
        "functions": [
            models.PipelineFunctionRedis(
                filter_="true",
                id=models.PipelineFunctionRedisID.REDIS,
                conf=models.RedisAuthTypeNone(
                    auth_type=models.RedisAuthTypeNoneAuthenticationMethod.NONE,
                    commands=[
                        models.RedisAuthTypeNoneCommand(
                            out_field="cached_value",
                            command="get",
                            key_expr="'user_session'",
                            args_expr="",
                        ),
                    ],
                    deployment_type=models.RedisAuthTypeNoneDeploymentType.STANDALONE,
                    max_block_secs=60,
                ),
            ),
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRegexExtract

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesRegexExtract" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="regex-extract-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that extracts structured fields from log data using regex patterns with named capture groups",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRegexExtractID.REGEX_EXTRACT,
                "conf": {
                    "regex": "/metric1=(?<metric1>\\d+)/",
                    "source": "_raw",
                    "iterations": 100,
                    "overwrite": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRegexFilter

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesRegexFilter" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="regex-filter-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that filters out events matching specific regex patterns",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRegexFilterID.REGEX_FILTER,
                "conf": {
                    "regex": "/Opera/",
                    "field": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRename

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesRename" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="rename-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that renames fields using key-value pairs and expressions",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRenameID.RENAME,
                "conf": {
                    "base_fields": [],
                    "rename": [
                        {
                            "current_name": "level",
                            "new_name": "LEVEL",
                        },
                    ],
                    "rename_expr": "name.startsWith('out') ? name.toUpperCase() : name",
                    "wildcard_depth": 5,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesRollupMetrics

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesRollupMetrics" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="rollup-metrics-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that consolidates high-frequency metrics into manageable time windows",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionRollupMetricsID.ROLLUP_METRICS,
                "conf": {
                    "dimensions": [
                        "*",
                    ],
                    "time_window": "30s",
                    "gauge_rollup": models.GaugeUpdate.LAST,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSNMPTrapSerialize

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesSNMPTrapSerialize" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="snmp-trap-serialize-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that serializes events into SNMP trap format for SNMP trap destinations",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSnmpTrapSerializeID.SNMP_TRAP_SERIALIZE,
                "conf": {
                    "strict": True,
                    "drop_failed_events": True,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSampling

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesSampling" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="sampling-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that samples events at specified rates based on filter criteria",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSamplingID.SAMPLING,
                "conf": {
                    "rules": [
                        {
                            "filter_": "__status == 200",
                            "rate": 5,
                        },
                    ],
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSerialize

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesSerialize" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="serialize-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that serializes event fields into JSON format",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSerializeID.SERIALIZE,
                "conf": {
                    "type": models.SerializeTypeCsvType.CSV,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesSuppress

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesSuppress" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="suppress-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that suppresses duplicate events based on a key expression",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionSuppressID.SUPPRESS,
                "conf": {
                    "key_expr": "`${ip}:${port}`",
                    "allow": 1,
                    "suppress_period_sec": 30,
                    "drop_events_mode": True,
                    "max_cache_size": 50000,
                    "cache_idle_timeout_periods": 2,
                    "num_events_idle_timeout_trigger": 10000,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesTee

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesTee" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="tee-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that sends events to a command via stdin for debugging purposes",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionTeeID.TEE,
                "conf": {
                    "command": "tee",
                    "args": [
                        "/opt/cribl/foo.log",
                    ],
                    "restart_on_exit": True,
                    "env": {

                    },
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesUnroll

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls array fields into separate events",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionUnrollID.UNROLL,
                "conf": {
                    "src_expr": "_raw.split(/\\n/)",
                    "dst_field": "_raw",
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```
### Example Usage: PipelineExamplesXMLUnroll

<!-- UsageSnippet language="python" operationID="updatePipelinesByPackAndId" method="patch" path="/p/{pack}/pipelines/{id}" example="PipelineExamplesXMLUnroll" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.pipelines.update(id_param="<value>", pack="<value>", id="xml-unroll-pipeline", conf={
        "async_func_timeout": 1000,
        "output": "default",
        "description": "Pipeline that unrolls XML elements into separate events",
        "streamtags": [],
        "functions": [
            {
                "filter_": "true",
                "id": models.PipelineFunctionXMLUnrollID.XML_UNROLL,
                "conf": {
                    "unroll": "^Parent\\.Child$",
                    "inherit": "^Parent\\.(myID|branchLocation)$",
                    "unroll_idx_field": "unroll_idx",
                    "pretty": False,
                },
            },
        ],
        "groups": {

        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id_param`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pipeline to update.                      |
| `pack`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Pack to update.                          |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conf`                                                              | [models.ConfInput](../../models/confinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPipeline](../../models/countedpipeline.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |