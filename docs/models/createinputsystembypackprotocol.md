# CreateInputSystemByPackProtocol

Select whether to leverage gRPC or HTTP for OpenTelemetry

## Example Usage

```python
from cribl_control_plane.models import CreateInputSystemByPackProtocol

value = CreateInputSystemByPackProtocol.GRPC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `GRPC` | grpc   |
| `HTTP` | http   |