# NodeSkippedUpgradeStatus

## Example Usage

```python
from cribl_control_plane.models import NodeSkippedUpgradeStatus

value = NodeSkippedUpgradeStatus.DOWNLOAD_ERROR

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `DOWNLOAD_ERROR`  | 0                 |
| `INSTALL_TYPE`    | 1                 |
| `MISSING_PACKAGE` | 2                 |
| `TOO_OLD`         | 3                 |