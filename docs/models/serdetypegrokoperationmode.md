# SerdeTypeGrokOperationMode

Extract creates new fields. Reserialize extracts and filters fields, and then reserializes.

## Example Usage

```python
from cribl_control_plane.models import SerdeTypeGrokOperationMode

value = SerdeTypeGrokOperationMode.EXTRACT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `EXTRACT`     | extract       |
| `RESERIALIZE` | reserialize   |