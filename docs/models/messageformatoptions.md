# MessageFormatOptions

Format to use when sending logs to Loki (Protobuf or JSON)

## Example Usage

```python
from cribl_control_plane.models import MessageFormatOptions

value = MessageFormatOptions.PROTOBUF

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PROTOBUF` | protobuf   |
| `JSON`     | json       |