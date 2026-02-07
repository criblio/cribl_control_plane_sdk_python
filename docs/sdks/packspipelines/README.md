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
                "description": "case afore bashfully smooth",
                "disabled": True,
                "final": False,
                "conf": {
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "prefix": "<value>",
                    "time_window": "10s",
                    "aggregations": [
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.GAUGE,
                            "agg": "avg(_value || proc.cpu_perc).as(proc.cpu_perc_avg)",
                        },
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.GAUGE,
                            "agg": "sum(_value || proc.mem_perc).as(proc.mem_perc_sum)",
                        },
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.COUNTER,
                            "agg": "count(_value || proc.bytes_in).as(proc.bytes_in_count)",
                        },
                    ],
                    "groupbys": [
                        "proc",
                    ],
                    "flush_event_limit": 7595.29,
                    "flush_mem_limit": "<value>",
                    "cumulative": False,
                    "should_treat_dots_as_literals": True,
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "eek harvest horse ragged till ack",
                "disabled": True,
                "final": True,
                "conf": {
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "metrics_mode": False,
                    "prefix": "<value>",
                    "time_window": "10s",
                    "aggregations": [
                        "sum(bytes).where(action==\"REJECT\").as(TotalBytes)",
                    ],
                    "groupbys": [
                        "srcaddr",
                    ],
                    "flush_event_limit": 7135.24,
                    "flush_mem_limit": "<value>",
                    "cumulative": False,
                    "search_agg_mode": "<value>",
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "should_treat_dots_as_literals": False,
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "garage whoa meanwhile blind er apropos",
                "disabled": True,
                "final": False,
                "conf": {
                    "src_field": "_raw",
                    "dst_field": "_time",
                    "default_timezone": "local",
                    "time_expression": "time.getTime() / 1000",
                    "offset": 0,
                    "max_len": 150,
                    "default_time": models.DefaultTime.NOW,
                    "latest_date_allowed": "+1week",
                    "spacer": "<value>",
                    "earliest_date_allowed": "-420weeks",
                    "timestamps": [
                        {
                            "regex": "/(\\d{1,2}\\/\\d{2}\\/\\d{4}\\s\\d{1,2}:\\d{2}:\\d{2}\\s\\w{2})/",
                            "strptime": "%Y-%m-%d %H:%M:%S",
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "nice ick which brr um pro times mammoth",
                "disabled": False,
                "final": False,
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
                "group_id": "<id>",
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
                "description": "quip excepting psst jungle configuration hence",
                "disabled": True,
                "final": False,
                "conf": {
                    "processor": "prometheus_metrics",
                },
                "group_id": "<id>",
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
                "description": "pfft rout battle",
                "disabled": True,
                "final": False,
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
                "group_id": "<id>",
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
                "description": "knavishly accentuate helplessly concrete factorize drat meaty quaff essence",
                "disabled": False,
                "final": True,
                "conf": {
                    "comment": "This function processes security events and enriches them with DNS lookups",
                },
                "group_id": "<id>",
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
                description="near greatly midst kinase concerning gratefully whose",
                disabled=False,
                final=True,
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
                    dns_servers=[
                        "<value 1>",
                        "<value 2>",
                    ],
                    cache_ttl=30,
                    max_cache_size=5000,
                    use_resolv_conf=False,
                    lookup_fallback=False,
                    domain_overrides=[
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    lookup_fail_log_level=models.LogLevelForFailedLookups.ERROR,
                ),
                group_id="<id>",
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
                "description": "cassava interestingly boss commandeer",
                "disabled": True,
                "final": False,
                "conf": {},
                "group_id": "<id>",
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
                "description": "vacantly boohoo where gorgeous notarize",
                "disabled": True,
                "final": True,
                "conf": {
                    "time_window": "10s",
                    "drop_dimensions": [
                        "proc",
                        "pie",
                        "unit",
                    ],
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "meanwhile starch cheerful what in whose soft",
                "disabled": True,
                "final": False,
                "conf": {
                    "mode": models.SampleMode.SQRT,
                    "key_expr": "`${domain}:${httpCode}`",
                    "sample_period": 20,
                    "min_events": 3,
                    "max_sample_rate": 3,
                },
                "group_id": "<id>",
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
                "description": "repeatedly upon derby gently suffocate inquisitively when oh along whereas",
                "disabled": False,
                "final": True,
                "conf": {
                    "add": [
                        {
                            "name": "action",
                            "value": "login == 'error' ? 'blocked' : action",
                            "disabled": True,
                        },
                        {
                            "name": "myTags",
                            "value": "login == 'error' ? [...myTags, 'error'] : myTags",
                            "disabled": False,
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
                "group_id": "<id>",
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionEventBreakerID.EVENT_BREAKER,
                "description": "about gleaming beside",
                "disabled": False,
                "final": False,
                "conf": {
                    "existing_or_new": models.ExistingOrNew.NEW,
                    "should_mark_cribl_breaker": True,
                },
                "group_id": "<id>",
            },
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
                "description": "helpless mmm oh pace meanwhile below above",
                "disabled": True,
                "final": True,
                "conf": {
                    "fields": [],
                    "prefix": "",
                    "depth": 5,
                    "delimiter": "_",
                },
                "group_id": "<id>",
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
                "description": "concerning mothball worth during",
                "disabled": True,
                "final": True,
                "conf": {
                    "delete_original": True,
                    "separator": "_",
                    "selection_reg_exp": "^data",
                },
                "group_id": "<id>",
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
                "description": "until jaunty mid jazz tame trial",
                "disabled": True,
                "final": True,
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
                    "out_field_mappings": {},
                },
                "group_id": "<id>",
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
                "description": "usually natural impeccable official louse custody",
                "disabled": False,
                "final": False,
                "conf": {
                    "pattern": "%{TIMESTAMP_ISO8601:event_time} %{LOGLEVEL:log_level} %{GREEDYDATA:log_message}",
                    "pattern_list": [],
                    "source": "_raw",
                },
                "group_id": "<id>",
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
                "description": "under morning worriedly",
                "disabled": True,
                "final": True,
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
                    "background_detection": False,
                },
                "group_id": "<id>",
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
                "description": "beneath flickering as",
                "disabled": True,
                "final": False,
                "conf": {
                    "path": "allCars",
                    "name": "cars",
                },
                "group_id": "<id>",
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
                "description": "shampoo why internalize masquerade boohoo right talkative even until",
                "disabled": False,
                "final": True,
                "conf": {
                    "file": "ip_locations.csv",
                    "db_lookup": False,
                    "match_mode": "exact",
                    "match_type": "<value>",
                    "reload_period_sec": -1,
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
                    "ignore_case": False,
                },
                "group_id": "<id>",
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
                "description": "list quirkily yahoo cantaloupe perfectly outrageous carefully lucky",
                "disabled": False,
                "final": False,
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
                    "flags": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "somber furthermore crumble during spherical geez but",
                "disabled": False,
                "final": False,
                "conf": {
                    "depth": 5,
                    "ignore_fields": [],
                    "filter_expr": "",
                    "format_": models.FunctionConfSchemaNumerifyFormat.NONE,
                },
                "group_id": "<id>",
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
                "description": "abaft who catalyze cuckoo past woeful woot",
                "disabled": False,
                "final": True,
                "conf": {
                    "drop_non_log_events": False,
                    "batch_otlp_logs": True,
                },
                "group_id": "<id>",
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
            {
                "filter_": "__inputId=='prometheus_rw:prom_rw_in'",
                "id": models.PipelineFunctionOtlpMetricsID.OTLP_METRICS,
                "description": "eek aching fort qua likewise brr",
                "disabled": False,
                "final": False,
                "conf": {
                    "resource_attribute_prefixes": [
                        "service",
                        "system",
                        "telemetry",
                        "k8s",
                        "cloud",
                        "host",
                        "process",
                    ],
                    "drop_non_metric_events": False,
                    "otlp_version": models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                    "batch_otlp_metrics": True,
                },
                "group_id": "<id>",
            },
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
            {
                "filter_": "__inputId=='open_telemetry:open_telemetry'",
                "id": models.PipelineFunctionOtlpTracesID.OTLP_TRACES,
                "description": "provided spirited whenever in like knowledgeably however",
                "disabled": False,
                "final": False,
                "conf": {
                    "drop_non_trace_events": False,
                    "otlp_version": models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                    "batch_otlp_traces": True,
                },
                "group_id": "<id>",
            },
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionSerdeID.SERDE,
                "description": "madly aw fast sympathetically swear hence excluding",
                "disabled": True,
                "final": False,
                "conf": {
                    "mode": models.OperationMode.EXTRACT,
                    "type": models.TypeOptions.KVP,
                    "delim_char": "<value>",
                    "quote_char": "<value>",
                    "escape_char": "<value>",
                    "null_value": "<value>",
                    "src_field": "_raw",
                    "dst_field": "<value>",
                    "clean_fields": False,
                },
                "group_id": "<id>",
            },
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
                "description": "ack scorpion that sad than since backbone yippee",
                "disabled": True,
                "final": False,
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
                "group_id": "<id>",
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionRedisID.REDIS,
                "description": "whale minor weekly qua writhing gee continually",
                "disabled": False,
                "final": True,
                "conf": {
                    "commands": [
                        {
                            "out_field": "cached_value",
                            "command": "get",
                            "key_expr": "'user_session'",
                            "args_expr": "",
                        },
                    ],
                    "deployment_type": models.DeploymentType.STANDALONE,
                    "auth_type": models.PipelineFunctionRedisAuthenticationMethod.NONE,
                    "max_block_secs": 60,
                    "enable_client_side_caching": False,
                },
                "group_id": "<id>",
            },
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
                "description": "blah inasmuch pearl till than rust the sediment stir-fry give",
                "disabled": True,
                "final": True,
                "conf": {
                    "regex": "/metric1=(?<metric1>\\d+)/",
                    "regex_list": [
                        {
                            "regex": "<value>",
                        },
                    ],
                    "source": "_raw",
                    "iterations": 100,
                    "field_name_expression": "<value>",
                    "overwrite": False,
                },
                "group_id": "<id>",
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
                "description": "where sans surprised pace ah",
                "disabled": True,
                "final": True,
                "conf": {
                    "regex": "/Opera/",
                    "regex_list": [
                        {
                            "regex": "<value>",
                        },
                    ],
                    "field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "topsail harmful although telescope woot why pro insistent dimly blissfully",
                "disabled": False,
                "final": True,
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
                "group_id": "<id>",
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
                "description": "scorpion brand consequently aside unaccountably phew where quirkily know jubilantly",
                "disabled": False,
                "final": False,
                "conf": {
                    "dimensions": [
                        "*",
                    ],
                    "time_window": "30s",
                    "gauge_rollup": models.GaugeUpdate.LAST,
                },
                "group_id": "<id>",
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
                "description": "untrue frugal anenst inasmuch smug",
                "disabled": True,
                "final": True,
                "conf": {
                    "strict": True,
                    "drop_failed_events": True,
                    "v3_user": {
                        "name": "<value>",
                        "auth_protocol": models.AuthenticationProtocolOptionsV3User.SHA256,
                        "auth_key": "<value>",
                        "priv_protocol": "<value>",
                    },
                },
                "group_id": "<id>",
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
                "description": "by correctly forecast cumbersome an astride bran",
                "disabled": True,
                "final": False,
                "conf": {
                    "rules": [
                        {
                            "filter_": "__status == 200",
                            "rate": 5,
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "knowledgeably ligate optimal scotch wombat plus ugh print",
                "disabled": False,
                "final": False,
                "conf": {
                    "type": models.PipelineFunctionSerializeType.JSON,
                    "delim_char": "<value>",
                    "quote_char": "<value>",
                    "escape_char": "<value>",
                    "null_value": "<value>",
                    "fields": [
                        "city",
                        "state",
                    ],
                    "src_field": "",
                    "dst_field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "merit aw through inasmuch scholarship exempt jacket sinful wisely",
                "disabled": True,
                "final": True,
                "conf": {
                    "key_expr": "`${ip}:${port}`",
                    "allow": 1,
                    "suppress_period_sec": 30,
                    "drop_events_mode": True,
                    "max_cache_size": 50000,
                    "cache_idle_timeout_periods": 2,
                    "num_events_idle_timeout_trigger": 10000,
                },
                "group_id": "<id>",
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
                "description": "through furthermore woot designation",
                "disabled": False,
                "final": True,
                "conf": {
                    "command": "tee",
                    "args": [
                        "/opt/cribl/foo.log",
                    ],
                    "restart_on_exit": True,
                    "env": {

                    },
                },
                "group_id": "<id>",
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
                "description": "interior indeed loftily contrast um stigmatize accomplished endow geez",
                "disabled": False,
                "final": False,
                "conf": {
                    "src_expr": "_raw.split(/\\n/)",
                    "dst_field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "hollow awful hmph",
                "disabled": False,
                "final": False,
                "conf": {
                    "unroll": "^Parent\\.Child$",
                    "inherit": "^Parent\\.(myID|branchLocation)$",
                    "unroll_idx_field": "unroll_idx",
                    "pretty": False,
                },
                "group_id": "<id>",
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
                "description": "yearn until think needy serialize",
                "disabled": False,
                "final": False,
                "conf": {
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "prefix": "<value>",
                    "time_window": "10s",
                    "aggregations": [
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.GAUGE,
                            "agg": "avg(_value || proc.cpu_perc).as(proc.cpu_perc_avg)",
                        },
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.GAUGE,
                            "agg": "sum(_value || proc.mem_perc).as(proc.mem_perc_sum)",
                        },
                        {
                            "metric_type": models.PipelineFunctionAggregateMetricsMetricType.COUNTER,
                            "agg": "count(_value || proc.bytes_in).as(proc.bytes_in_count)",
                        },
                    ],
                    "groupbys": [
                        "proc",
                    ],
                    "flush_event_limit": 2771.87,
                    "flush_mem_limit": "<value>",
                    "cumulative": False,
                    "should_treat_dots_as_literals": True,
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "yak handle internal unless conjecture ride trash thorough crossly failing",
                "disabled": False,
                "final": False,
                "conf": {
                    "passthrough": False,
                    "preserve_group_bys": False,
                    "sufficient_stats_only": False,
                    "metrics_mode": False,
                    "prefix": "<value>",
                    "time_window": "10s",
                    "aggregations": [
                        "sum(bytes).where(action==\"REJECT\").as(TotalBytes)",
                    ],
                    "groupbys": [
                        "srcaddr",
                    ],
                    "flush_event_limit": 1229.32,
                    "flush_mem_limit": "<value>",
                    "cumulative": False,
                    "search_agg_mode": "<value>",
                    "add": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                    "should_treat_dots_as_literals": False,
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "lest however which doodle pushy capitalise holster chops respectful",
                "disabled": False,
                "final": True,
                "conf": {
                    "src_field": "_raw",
                    "dst_field": "_time",
                    "default_timezone": "local",
                    "time_expression": "time.getTime() / 1000",
                    "offset": 0,
                    "max_len": 150,
                    "default_time": models.DefaultTime.NOW,
                    "latest_date_allowed": "+1week",
                    "spacer": "<value>",
                    "earliest_date_allowed": "-420weeks",
                    "timestamps": [
                        {
                            "regex": "/(\\d{1,2}\\/\\d{2}\\/\\d{4}\\s\\d{1,2}:\\d{2}:\\d{2}\\s\\w{2})/",
                            "strptime": "%Y-%m-%d %H:%M:%S",
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "hospitable although experienced carpool numeracy like stool",
                "disabled": False,
                "final": False,
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
                "group_id": "<id>",
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
                "description": "whenever a carelessly doting",
                "disabled": False,
                "final": True,
                "conf": {
                    "processor": "prometheus_metrics",
                },
                "group_id": "<id>",
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
                "description": "acclaimed celsius sideboard",
                "disabled": True,
                "final": False,
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
                "group_id": "<id>",
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
                "description": "internationalize meanwhile earnest shipper",
                "disabled": True,
                "final": True,
                "conf": {
                    "comment": "This function processes security events and enriches them with DNS lookups",
                },
                "group_id": "<id>",
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
                description="lumpy however cleverly cleaner knowledgeable defrag impact helplessly",
                disabled=True,
                final=True,
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
                    dns_servers=[
                        "<value 1>",
                        "<value 2>",
                    ],
                    cache_ttl=30,
                    max_cache_size=5000,
                    use_resolv_conf=False,
                    lookup_fallback=False,
                    domain_overrides=[
                        "<value 1>",
                        "<value 2>",
                        "<value 3>",
                    ],
                    lookup_fail_log_level=models.LogLevelForFailedLookups.ERROR,
                ),
                group_id="<id>",
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
                "description": "brightly mortise lamp sardonic because sure-footed narrowcast",
                "disabled": True,
                "final": True,
                "conf": {},
                "group_id": "<id>",
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
                "description": "young times crocodile great masticate why ornate atop bah",
                "disabled": True,
                "final": False,
                "conf": {
                    "time_window": "10s",
                    "drop_dimensions": [
                        "proc",
                        "pie",
                        "unit",
                    ],
                    "flush_on_input_close": True,
                },
                "group_id": "<id>",
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
                "description": "whether lady where",
                "disabled": True,
                "final": False,
                "conf": {
                    "mode": models.SampleMode.SQRT,
                    "key_expr": "`${domain}:${httpCode}`",
                    "sample_period": 20,
                    "min_events": 3,
                    "max_sample_rate": 3,
                },
                "group_id": "<id>",
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
                "description": "than nor following",
                "disabled": True,
                "final": False,
                "conf": {
                    "add": [
                        {
                            "name": "action",
                            "value": "login == 'error' ? 'blocked' : action",
                            "disabled": False,
                        },
                        {
                            "name": "myTags",
                            "value": "login == 'error' ? [...myTags, 'error'] : myTags",
                            "disabled": False,
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
                "group_id": "<id>",
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionEventBreakerID.EVENT_BREAKER,
                "description": "incidentally scornful past vivaciously aha genuine essence",
                "disabled": True,
                "final": True,
                "conf": {
                    "existing_or_new": models.ExistingOrNew.NEW,
                    "should_mark_cribl_breaker": True,
                },
                "group_id": "<id>",
            },
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
                "description": "skyline beautifully of firm championship clamour impanel order",
                "disabled": False,
                "final": False,
                "conf": {
                    "fields": [],
                    "prefix": "",
                    "depth": 5,
                    "delimiter": "_",
                },
                "group_id": "<id>",
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
                "description": "amidst utterly loyally mould",
                "disabled": False,
                "final": False,
                "conf": {
                    "delete_original": True,
                    "separator": "_",
                    "selection_reg_exp": "^data",
                },
                "group_id": "<id>",
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
                "description": "catch nippy gah brightly gadzooks amused",
                "disabled": True,
                "final": False,
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
                    "out_field_mappings": {},
                },
                "group_id": "<id>",
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
                "description": "afore sardonic glittering whether provided negligible pasta even opposite",
                "disabled": False,
                "final": False,
                "conf": {
                    "pattern": "%{TIMESTAMP_ISO8601:event_time} %{LOGLEVEL:log_level} %{GREEDYDATA:log_message}",
                    "pattern_list": [],
                    "source": "_raw",
                },
                "group_id": "<id>",
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
                "description": "circa corral crushing vision",
                "disabled": False,
                "final": True,
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
                    "background_detection": False,
                },
                "group_id": "<id>",
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
                "description": "revitalise yippee forgather although republican diligently near microchip gosh",
                "disabled": False,
                "final": True,
                "conf": {
                    "path": "allCars",
                    "name": "cars",
                },
                "group_id": "<id>",
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
                "description": "slimy warmhearted meaningfully ack unabashedly pish likewise timely shore sprinkles",
                "disabled": False,
                "final": True,
                "conf": {
                    "file": "ip_locations.csv",
                    "db_lookup": False,
                    "match_mode": "exact",
                    "match_type": "<value>",
                    "reload_period_sec": -1,
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
                    "ignore_case": False,
                },
                "group_id": "<id>",
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
                "description": "anenst cop-out loftily illusion sugary passport astride",
                "disabled": False,
                "final": False,
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
                    "flags": [
                        {
                            "name": "<value>",
                            "value": "<value>",
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "blah cautious rudely for since",
                "disabled": True,
                "final": True,
                "conf": {
                    "depth": 5,
                    "ignore_fields": [],
                    "filter_expr": "",
                    "format_": models.FunctionConfSchemaNumerifyFormat.NONE,
                },
                "group_id": "<id>",
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
                "description": "yummy bare absent as jagged owlishly pish upright",
                "disabled": False,
                "final": False,
                "conf": {
                    "drop_non_log_events": False,
                    "batch_otlp_logs": True,
                },
                "group_id": "<id>",
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
            {
                "filter_": "__inputId=='prometheus_rw:prom_rw_in'",
                "id": models.PipelineFunctionOtlpMetricsID.OTLP_METRICS,
                "description": "unlearn worthwhile tall questionable",
                "disabled": True,
                "final": True,
                "conf": {
                    "resource_attribute_prefixes": [
                        "service",
                        "system",
                        "telemetry",
                        "k8s",
                        "cloud",
                        "host",
                        "process",
                    ],
                    "drop_non_metric_events": False,
                    "otlp_version": models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                    "batch_otlp_metrics": True,
                },
                "group_id": "<id>",
            },
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
            {
                "filter_": "__inputId=='open_telemetry:open_telemetry'",
                "id": models.PipelineFunctionOtlpTracesID.OTLP_TRACES,
                "description": "aha interchange tabulate considering square",
                "disabled": False,
                "final": True,
                "conf": {
                    "drop_non_trace_events": False,
                    "otlp_version": models.OtlpVersionOptions.ZERO_DOT_10_DOT_0,
                    "batch_otlp_traces": True,
                },
                "group_id": "<id>",
            },
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionSerdeID.SERDE,
                "description": "schlep insolence gadzooks",
                "disabled": True,
                "final": True,
                "conf": {
                    "mode": models.OperationMode.EXTRACT,
                    "type": models.TypeOptions.KVP,
                    "delim_char": "<value>",
                    "quote_char": "<value>",
                    "escape_char": "<value>",
                    "null_value": "<value>",
                    "src_field": "_raw",
                    "dst_field": "<value>",
                    "clean_fields": False,
                },
                "group_id": "<id>",
            },
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
                "description": "coast if qua wear tuxedo likewise",
                "disabled": True,
                "final": True,
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
                "group_id": "<id>",
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
            {
                "filter_": "true",
                "id": models.PipelineFunctionRedisID.REDIS,
                "description": "though emphasise conservation selfish aside gently amendment internationalize submitter indeed",
                "disabled": False,
                "final": False,
                "conf": {
                    "commands": [
                        {
                            "out_field": "cached_value",
                            "command": "get",
                            "key_expr": "'user_session'",
                            "args_expr": "",
                        },
                    ],
                    "deployment_type": models.DeploymentType.STANDALONE,
                    "auth_type": models.PipelineFunctionRedisAuthenticationMethod.NONE,
                    "max_block_secs": 60,
                    "enable_client_side_caching": True,
                },
                "group_id": "<id>",
            },
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
                "description": "simplistic tankful consequently optimistically inferior bide as aha eek sharply",
                "disabled": True,
                "final": False,
                "conf": {
                    "regex": "/metric1=(?<metric1>\\d+)/",
                    "regex_list": [
                        {
                            "regex": "<value>",
                        },
                    ],
                    "source": "_raw",
                    "iterations": 100,
                    "field_name_expression": "<value>",
                    "overwrite": False,
                },
                "group_id": "<id>",
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
                "description": "rough voluminous woot sans",
                "disabled": False,
                "final": False,
                "conf": {
                    "regex": "/Opera/",
                    "regex_list": [
                        {
                            "regex": "<value>",
                        },
                    ],
                    "field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "closely lack vivaciously below needily draft norm sarong for robust",
                "disabled": True,
                "final": True,
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
                "group_id": "<id>",
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
                "description": "ignorance phooey offset insert",
                "disabled": False,
                "final": False,
                "conf": {
                    "dimensions": [
                        "*",
                    ],
                    "time_window": "30s",
                    "gauge_rollup": models.GaugeUpdate.LAST,
                },
                "group_id": "<id>",
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
                "description": "junior ah over sour",
                "disabled": True,
                "final": True,
                "conf": {
                    "strict": True,
                    "drop_failed_events": True,
                    "v3_user": {
                        "name": "<value>",
                        "auth_protocol": models.AuthenticationProtocolOptionsV3User.SHA384,
                        "auth_key": "<value>",
                        "priv_protocol": "<value>",
                    },
                },
                "group_id": "<id>",
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
                "description": "briefly summarise old mmm redress yowza",
                "disabled": False,
                "final": True,
                "conf": {
                    "rules": [
                        {
                            "filter_": "__status == 200",
                            "rate": 5,
                        },
                    ],
                },
                "group_id": "<id>",
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
                "description": "language gulp pish bonnet keenly helpfully unit manner",
                "disabled": True,
                "final": True,
                "conf": {
                    "type": models.PipelineFunctionSerializeType.JSON,
                    "delim_char": "<value>",
                    "quote_char": "<value>",
                    "escape_char": "<value>",
                    "null_value": "<value>",
                    "fields": [
                        "city",
                        "state",
                    ],
                    "src_field": "",
                    "dst_field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "membership infatuated inquisitively save brr abaft puff before coarse nauseate",
                "disabled": True,
                "final": False,
                "conf": {
                    "key_expr": "`${ip}:${port}`",
                    "allow": 1,
                    "suppress_period_sec": 30,
                    "drop_events_mode": True,
                    "max_cache_size": 50000,
                    "cache_idle_timeout_periods": 2,
                    "num_events_idle_timeout_trigger": 10000,
                },
                "group_id": "<id>",
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
                "description": "horse punctually barring intently bootleg till",
                "disabled": False,
                "final": False,
                "conf": {
                    "command": "tee",
                    "args": [
                        "/opt/cribl/foo.log",
                    ],
                    "restart_on_exit": True,
                    "env": {

                    },
                },
                "group_id": "<id>",
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
                "description": "unto confusion ha row premier intensely advertisement woot",
                "disabled": False,
                "final": True,
                "conf": {
                    "src_expr": "_raw.split(/\\n/)",
                    "dst_field": "_raw",
                },
                "group_id": "<id>",
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
                "description": "yet misappropriate beyond conceptualize hawk tomorrow electric viability kettledrum",
                "disabled": True,
                "final": True,
                "conf": {
                    "unroll": "^Parent\\.Child$",
                    "inherit": "^Parent\\.(myID|branchLocation)$",
                    "unroll_idx_field": "unroll_idx",
                    "pretty": False,
                },
                "group_id": "<id>",
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