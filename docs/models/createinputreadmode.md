# CreateInputReadMode

Read all stored and future event logs, or only future events

## Example Usage

```python
from cribl_control_plane.models import CreateInputReadMode

value = CreateInputReadMode.OLDEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OLDEST` | oldest   |
| `NEWEST` | newest   |