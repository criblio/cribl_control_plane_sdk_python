# SerdeTypeDelimOperationMode

Extract creates new fields. Reserialize extracts and filters fields, and then reserializes.

## Example Usage

```python
from cribl_control_plane.models import SerdeTypeDelimOperationMode

value = SerdeTypeDelimOperationMode.EXTRACT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `EXTRACT`     | extract       |
| `RESERIALIZE` | reserialize   |