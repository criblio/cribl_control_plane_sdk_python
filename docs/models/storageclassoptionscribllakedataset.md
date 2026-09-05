# StorageClassOptionsCriblLakeDataset

Storage class used for objects written to the Dataset.

## Example Usage

```python
from cribl_control_plane.models import StorageClassOptionsCriblLakeDataset

value = StorageClassOptionsCriblLakeDataset.ARCHIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `ARCHIVE`             | Archive               |
| `COLD`                | Cold                  |
| `COOL`                | Cool                  |
| `DEEP_ARCHIVE`        | DEEP_ARCHIVE          |
| `GLACIER`             | GLACIER               |
| `GLACIER_IR`          | GLACIER_IR            |
| `HOT`                 | Hot                   |
| `INFERRED`            | Inferred              |
| `INTELLIGENT_TIERING` | INTELLIGENT_TIERING   |
| `ONEZONE_IA`          | ONEZONE_IA            |
| `STANDARD`            | STANDARD              |
| `STANDARD_IA`         | STANDARD_IA           |