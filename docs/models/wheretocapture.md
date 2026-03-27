# WhereToCapture

## Example Usage

```python
from cribl_control_plane.models import WhereToCapture

value = WhereToCapture.BEFORE_PRE_PROCESSING_PIPELINE

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name                              | Value                             |
| --------------------------------- | --------------------------------- |
| `BEFORE_PRE_PROCESSING_PIPELINE`  | 0                                 |
| `BEFORE_THE_ROUTES`               | 1                                 |
| `BEFORE_POST_PROCESSING_PIPELINE` | 2                                 |
| `BEFORE_THE_DESTINATION`          | 3                                 |