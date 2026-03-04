# CreateOutputSystemByPackQueueType

The queue type used (or created). Defaults to Standard.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackQueueType

value = CreateOutputSystemByPackQueueType.STANDARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `STANDARD` | standard   |
| `FIFO`     | fifo       |