# CreateInputShardIteratorStart

Location at which to start reading a shard for the first time

## Example Usage

```python
from cribl_control_plane.models import CreateInputShardIteratorStart

value = CreateInputShardIteratorStart.TRIM_HORIZON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `TRIM_HORIZON` | TRIM_HORIZON   |
| `LATEST`       | LATEST         |