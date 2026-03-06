# DiskSpaceProtectionOptions

How to handle events when disk space is below the global 'Min free disk space' limit

## Example Usage

```python
from cribl_control_plane.models import DiskSpaceProtectionOptions

value = DiskSpaceProtectionOptions.BLOCK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `BLOCK` | block   |
| `DROP`  | drop    |