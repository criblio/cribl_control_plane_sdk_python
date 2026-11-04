# OutputResponseStorageClass

Storage class to select for uploaded objects

## Example Usage

```python
from cribl_control_plane.models import OutputResponseStorageClass

value = OutputResponseStorageClass.STANDARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `STANDARD`   | STANDARD     |
| `ONEZONE_IA` | ONEZONE_IA   |
| `GLACIER`    | GLACIER      |