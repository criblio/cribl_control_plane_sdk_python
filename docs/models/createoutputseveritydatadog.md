# CreateOutputSeverityDatadog

Default value for message severity. When you send logs as JSON objects, the event's '__severity' field (if set) will override this value.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSeverityDatadog

value = CreateOutputSeverityDatadog.EMERGENCY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `EMERGENCY` | emergency   |
| `ALERT`     | alert       |
| `CRITICAL`  | critical    |
| `ERROR`     | error       |
| `WARNING`   | warning     |
| `NOTICE`    | notice      |
| `INFO`      | info        |
| `DEBUG`     | debug       |