# FunctionConfSchemaPublishMetricsMetricType

The type of metric to publish (counter, timer, gauge, distribution, summary, or histogram).

## Example Usage

```python
from cribl_control_plane.models import FunctionConfSchemaPublishMetricsMetricType

value = FunctionConfSchemaPublishMetricsMetricType.COUNTER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `COUNTER`      | counter        |
| `TIMER`        | timer          |
| `GAUGE`        | gauge          |
| `DISTRIBUTION` | distribution   |
| `SUMMARY`      | summary        |
| `HISTOGRAM`    | histogram      |