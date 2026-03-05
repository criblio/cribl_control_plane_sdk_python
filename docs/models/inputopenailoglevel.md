# InputOpenaiLogLevel

Collector runtime log level.

## Example Usage

```python
from cribl_control_plane.models import InputOpenaiLogLevel

value = InputOpenaiLogLevel.ERROR

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