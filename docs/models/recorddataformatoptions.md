# RecordDataFormatOptions

Format to use to serialize events before writing to the Event Hubs Kafka brokers

## Example Usage

```python
from cribl_control_plane.models import RecordDataFormatOptions

value = RecordDataFormatOptions.JSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `JSON` | json   |
| `RAW`  | raw    |