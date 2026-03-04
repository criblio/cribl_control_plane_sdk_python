# CreateOutputSystemByPackTimestampFormat

Timestamp format to use when serializing event's time field

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackTimestampFormat

value = CreateOutputSystemByPackTimestampFormat.SYSLOG

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SYSLOG`  | syslog    |
| `ISO8601` | iso8601   |