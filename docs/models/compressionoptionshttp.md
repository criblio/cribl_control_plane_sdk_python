# CompressionOptionsHTTP

Data compression format to apply to HTTP content before it is delivered

## Example Usage

```python
from cribl_control_plane.models import CompressionOptionsHTTP

value = CompressionOptionsHTTP.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `GZIP` | gzip   |