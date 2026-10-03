# MetricsProtocol

Protocol to use when collecting metrics

## Example Usage

```python
from cribl_control_plane.models import MetricsProtocol

value = MetricsProtocol.HTTP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `HTTP`  | http    |
| `HTTPS` | https   |