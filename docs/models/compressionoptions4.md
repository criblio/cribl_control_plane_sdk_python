# CompressionOptions4

Type of compression to apply to messages sent to the OpenTelemetry endpoint

## Example Usage

```python
from cribl_control_plane.models import CompressionOptions4

value = CompressionOptions4.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `NONE`    | none      |
| `DEFLATE` | deflate   |
| `GZIP`    | gzip      |