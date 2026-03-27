# CreateInputLogLevelSplunkSearch

Collector runtime log level (verbosity)

## Example Usage

```python
from cribl_control_plane.models import CreateInputLogLevelSplunkSearch

value = CreateInputLogLevelSplunkSearch.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `ERROR` | error   |
| `WARN`  | warn    |
| `INFO`  | info    |
| `DEBUG` | debug   |