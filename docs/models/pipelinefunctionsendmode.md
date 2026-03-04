# PipelineFunctionSendMode

In Sender mode, forwards search results directly to the destination. In Metrics mode, accumulates metrics from federated send operators, and forwards the aggregate metrics.

## Example Usage

```python
from cribl_control_plane.models import PipelineFunctionSendMode

value = PipelineFunctionSendMode.SENDER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SENDER`  | sender    |
| `METRICS` | metrics   |