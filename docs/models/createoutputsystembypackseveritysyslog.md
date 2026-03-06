# CreateOutputSystemByPackSeveritySyslog

Default value for message severity. Will be overwritten by value of __severity if set. Defaults to notice.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackSeveritySyslog

value = CreateOutputSystemByPackSeveritySyslog.EMERGENCY

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `EMERGENCY` | 0           |
| `ALERT`     | 1           |
| `CRITICAL`  | 2           |
| `ERROR`     | 3           |
| `WARNING`   | 4           |
| `NOTICE`    | 5           |
| `INFO`      | 6           |
| `DEBUG`     | 7           |