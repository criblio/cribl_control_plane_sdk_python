# ReadMode

Read all stored and future event logs, or only future events

## Example Usage

```python
from cribl_control_plane.models import ReadMode

value = ReadMode.OLDEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OLDEST` | oldest   |
| `NEWEST` | newest   |