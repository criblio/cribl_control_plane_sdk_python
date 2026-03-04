# LogLevelOptions

Log Level (verbosity) for collection runtime behavior.

## Example Usage

```python
from cribl_control_plane.models import LogLevelOptions

value = LogLevelOptions.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `ERROR` | error   |
| `WARN`  | warn    |
| `INFO`  | info    |
| `DEBUG` | debug   |
| `SILLY` | silly   |