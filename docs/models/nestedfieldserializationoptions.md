# NestedFieldSerializationOptions

How to serialize nested fields into index-time fields

## Example Usage

```python
from cribl_control_plane.models import NestedFieldSerializationOptions

value = NestedFieldSerializationOptions.JSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `JSON` | json   |
| `NONE` | none   |