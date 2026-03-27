# GaugeUpdate

The operation to use when rolling up gauge metrics. Defaults to last.

## Example Usage

```python
from cribl_control_plane.models import GaugeUpdate

value = GaugeUpdate.LAST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `LAST` | last   |
| `MAX`  | max    |
| `MIN`  | min    |
| `AVG`  | avg    |