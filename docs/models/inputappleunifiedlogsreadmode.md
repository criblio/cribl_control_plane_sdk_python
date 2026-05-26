# InputAppleUnifiedLogsReadMode

Read all log entries (historical and upcoming), or only upcoming, from the last entry

## Example Usage

```python
from cribl_control_plane.models import InputAppleUnifiedLogsReadMode

value = InputAppleUnifiedLogsReadMode.OLDEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OLDEST` | oldest   |
| `NEWEST` | newest   |