# LogLevelForFailedLookups

Log level to use when a DNS lookup fails.

## Example Usage

```python
from cribl_control_plane.models import LogLevelForFailedLookups

value = LogLevelForFailedLookups.SILLY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `SILLY` | silly   |
| `DEBUG` | debug   |
| `INFO`  | info    |
| `WARN`  | warn    |
| `ERROR` | error   |