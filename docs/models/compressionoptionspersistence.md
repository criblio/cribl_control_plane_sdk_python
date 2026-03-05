# CompressionOptionsPersistence

Data compression format. Default is gzip.

## Example Usage

```python
from cribl_control_plane.models import CompressionOptionsPersistence

value = CompressionOptionsPersistence.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `GZIP` | gzip   |