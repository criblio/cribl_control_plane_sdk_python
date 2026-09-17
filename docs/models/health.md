# Health

Health status of the persistent queue.

## Example Usage

```python
from cribl_control_plane.models import Health

value = Health.GREEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `GREEN`   | Green     |
| `RED`     | Red       |
| `UNKNOWN` | Unknown   |
| `YELLOW`  | Yellow    |