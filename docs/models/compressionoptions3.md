# CompressionOptions3

Codec to use to compress the data before sending to Kafka

## Example Usage

```python
from cribl_control_plane.models import CompressionOptions3

value = CompressionOptions3.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `NONE`   | none     |
| `GZIP`   | gzip     |
| `SNAPPY` | snappy   |
| `LZ4`    | lz4      |
| `ZSTD`   | zstd     |