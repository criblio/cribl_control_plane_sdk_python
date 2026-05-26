# OutputResponseQueueType

The queue type used (or created). Defaults to Standard.

## Example Usage

```python
from cribl_control_plane.models import OutputResponseQueueType

value = OutputResponseQueueType.STANDARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `STANDARD` | standard   |
| `FIFO`     | fifo       |