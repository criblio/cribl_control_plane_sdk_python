# StorageClassOptionsCriblLakeDataset

Storage class used for objects written to the Dataset.

## Example Usage

```python
from cribl_control_plane.models import StorageClassOptionsCriblLakeDataset

value = StorageClassOptionsCriblLakeDataset.DEEP_ARCHIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `DEEP_ARCHIVE`        | DEEP_ARCHIVE          |
| `GLACIER`             | GLACIER               |
| `GLACIER_IR`          | GLACIER_IR            |
| `INTELLIGENT_TIERING` | INTELLIGENT_TIERING   |
| `ONEZONE_IA`          | ONEZONE_IA            |
| `STANDARD`            | STANDARD              |
| `STANDARD_IA`         | STANDARD_IA           |