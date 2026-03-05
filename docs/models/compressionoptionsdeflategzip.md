# CompressionOptionsDeflateGzip

Type of compression to apply to messages sent to the OpenTelemetry endpoint

## Example Usage

```python
from cribl_control_plane.models import CompressionOptionsDeflateGzip

value = CompressionOptionsDeflateGzip.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `NONE`    | none      |
| `DEFLATE` | deflate   |
| `GZIP`    | gzip      |