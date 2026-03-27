# DefaultTime

How to set the time field if no timestamp is found

## Example Usage

```python
from cribl_control_plane.models import DefaultTime

value = DefaultTime.NOW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NOW`  | now    |
| `LAST` | last   |
| `NONE` | none   |