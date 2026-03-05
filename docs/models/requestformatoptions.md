# RequestFormatOptions

When set to JSON, the event is automatically formatted with required fields before sending. When set to Raw, only the event's `_raw` value is sent.

## Example Usage

```python
from cribl_control_plane.models import RequestFormatOptions

value = RequestFormatOptions.JSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `JSON` | JSON   |
| `RAW`  | raw    |