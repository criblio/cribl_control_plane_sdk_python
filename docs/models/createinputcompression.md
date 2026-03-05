# CreateInputCompression

Controls whether to support reading compressed data from a forwarder. Select 'Automatic' to match the forwarder's configuration, or 'Disabled' to reject compressed connections.

## Example Usage

```python
from cribl_control_plane.models import CreateInputCompression

value = CreateInputCompression.DISABLED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DISABLED` | disabled   |
| `AUTO`     | auto       |
| `ALWAYS`   | always     |