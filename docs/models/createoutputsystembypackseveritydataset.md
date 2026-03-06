# CreateOutputSystemByPackSeverityDataset

Default value for event severity. If the `sev` or `__severity` fields are set on an event, the first one matching will override this value.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackSeverityDataset

value = CreateOutputSystemByPackSeverityDataset.FINEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FINEST`  | finest    |
| `FINER`   | finer     |
| `FINE`    | fine      |
| `INFO`    | info      |
| `WARNING` | warning   |
| `ERROR`   | error     |
| `FATAL`   | fatal     |