# NodeUpgradeState

## Example Usage

```python
from cribl_control_plane.models import NodeUpgradeState

value = NodeUpgradeState.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ACTIVE`  | 0         |
| `CURRENT` | 1         |
| `FAILED`  | 2         |
| `SKIPPED` | 3         |