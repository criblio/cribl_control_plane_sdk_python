# SendAs

Which signals this Destination carries. Logs sends everything to log search, including metric events. Metrics routes metric events to the metric store and drops everything else. Logs and Metrics routes metric events to the metric store and sends the rest to log search. Metric routing requires the receiving Cribl Search Source to be enabled for metrics storage; if it is not, metric events are discarded rather than stored as logs.

## Example Usage

```python
from cribl_control_plane.models import SendAs

value = SendAs.LOGS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `LOGS`    | logs      |
| `METRICS` | metrics   |
| `BOTH`    | both      |