# ScanMode

Acceleration scan mode. <code>quick</code> collects object-level metadata; <code>detailed</code> also collects field-level statistics.

## Example Usage

```python
from cribl_control_plane.models import ScanMode

value = ScanMode.DETAILED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DETAILED` | detailed   |
| `QUICK`    | quick      |