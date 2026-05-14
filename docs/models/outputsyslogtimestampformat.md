# OutputSyslogTimestampFormat

Timestamp format to use when serializing event's time field

## Example Usage

```python
from cribl_control_plane.models import OutputSyslogTimestampFormat

value = OutputSyslogTimestampFormat.SYSLOG

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SYSLOG`  | syslog    |
| `ISO8601` | iso8601   |