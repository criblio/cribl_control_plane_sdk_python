# DistMode

Distributed deployment mode for this instance.

## Example Usage

```python
from cribl_control_plane.models import DistMode

value = DistMode.EDGE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `EDGE`              | edge                |
| `MANAGED_EDGE`      | managed-edge        |
| `MASTER`            | master              |
| `OUTPOST`           | outpost             |
| `SEARCH_SUPERVISOR` | search-supervisor   |
| `SINGLE`            | single              |
| `WORKER`            | worker              |