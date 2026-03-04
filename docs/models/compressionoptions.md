# CompressionOptions

Controls whether the sender should send compressed data to the server. Select 'Disabled' to reject compressed connections or 'Always' to ignore server's configuration and send compressed data.

## Example Usage

```python
from cribl_control_plane.models import CompressionOptions

value = CompressionOptions.DISABLED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DISABLED` | disabled   |
| `AUTO`     | auto       |
| `ALWAYS`   | always     |