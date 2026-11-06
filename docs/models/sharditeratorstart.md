# ShardIteratorStart

Location at which to start reading a shard for the first time

## Example Usage

```python
from cribl_control_plane.models import ShardIteratorStart

value = ShardIteratorStart.TRIM_HORIZON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `TRIM_HORIZON` | TRIM_HORIZON   |
| `LATEST`       | LATEST         |