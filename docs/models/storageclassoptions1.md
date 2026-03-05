# StorageClassOptions1

Storage class to select for uploaded objects

## Example Usage

```python
from cribl_control_plane.models import StorageClassOptions1

value = StorageClassOptions1.STANDARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `STANDARD` | STANDARD   |
| `NEARLINE` | NEARLINE   |
| `COLDLINE` | COLDLINE   |
| `ARCHIVE`  | ARCHIVE    |