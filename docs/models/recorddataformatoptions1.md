# RecordDataFormatOptions1

Format to use to serialize events before writing to Kafka.

## Example Usage

```python
from cribl_control_plane.models import RecordDataFormatOptions1

value = RecordDataFormatOptions1.JSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `JSON`     | json       |
| `RAW`      | raw        |
| `PROTOBUF` | protobuf   |