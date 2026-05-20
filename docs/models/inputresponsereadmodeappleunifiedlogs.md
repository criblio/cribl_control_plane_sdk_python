# InputResponseReadModeAppleUnifiedLogs

Read all log entries (historical and upcoming), or only upcoming, from the last entry

## Example Usage

```python
from cribl_control_plane.models import InputResponseReadModeAppleUnifiedLogs

value = InputResponseReadModeAppleUnifiedLogs.OLDEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OLDEST` | oldest   |
| `NEWEST` | newest   |