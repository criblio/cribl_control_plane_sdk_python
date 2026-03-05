# AcknowledgmentsOptions

Control the number of required acknowledgments

## Example Usage

```python
from cribl_control_plane.models import AcknowledgmentsOptions

value = AcknowledgmentsOptions.LEADER

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name     | Value    |
| -------- | -------- |
| `LEADER` | 1        |
| `NONE`   | 0        |
| `ALL`    | -1       |