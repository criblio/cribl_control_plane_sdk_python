# DistMode

Distributed deployment mode for the instance.

## Example Usage

```python
from cribl_control_plane.models import DistMode

value = DistMode.DEDICATED_ORG_LEADER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `DEDICATED_ORG_LEADER` | dedicated-org-leader   |
| `EDGE`                 | edge                   |
| `MANAGED_EDGE`         | managed-edge           |
| `MASTER`               | master                 |
| `ORG_LEADER`           | org-leader             |
| `OUTPOST`              | outpost                |
| `SEARCH_SUPERVISOR`    | search-supervisor      |
| `SINGLE`               | single                 |
| `WORKER`               | worker                 |