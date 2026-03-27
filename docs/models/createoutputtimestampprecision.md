# CreateOutputTimestampPrecision

Sets the precision for the supplied Unix time values. Defaults to milliseconds.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputTimestampPrecision

value = CreateOutputTimestampPrecision.NS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `NS`  | ns    |
| `U`   | u     |
| `MS`  | ms    |
| `S`   | s     |
| `M`   | m     |
| `H`   | h     |