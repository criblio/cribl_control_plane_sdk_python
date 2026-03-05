# CompressionLevelOptions

Compression level to apply before moving files to final destination

## Example Usage

```python
from cribl_control_plane.models import CompressionLevelOptions

value = CompressionLevelOptions.BEST_SPEED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `BEST_SPEED`       | best_speed         |
| `NORMAL`           | normal             |
| `BEST_COMPRESSION` | best_compression   |