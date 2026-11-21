# EndpointSourceOptions

Whether to use statically configured endpoints or an Endpoint List

## Example Usage

```python
from cribl_control_plane.models import EndpointSourceOptions

value = EndpointSourceOptions.STATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `STATIC`        | static          |
| `ENDPOINT_LIST` | endpointList    |