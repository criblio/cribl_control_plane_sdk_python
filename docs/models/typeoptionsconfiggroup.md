# TypeOptionsConfigGroup

Explicit type of the Worker Group, Outpost Group, or Edge Fleet.

## Example Usage

```python
from cribl_control_plane.models import TypeOptionsConfigGroup

value = TypeOptionsConfigGroup.EDGE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `EDGE`         | edge           |
| `LAKE_ACCESS`  | lake_access    |
| `LOCAL_SEARCH` | local_search   |
| `OUTPOST`      | outpost        |
| `SEARCH`       | search         |
| `STREAM`       | stream         |