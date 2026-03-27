# OutputClickHouseMappingType

How event fields are mapped to ClickHouse columns.

## Example Usage

```python
from cribl_control_plane.models import OutputClickHouseMappingType

value = OutputClickHouseMappingType.AUTOMATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `AUTOMATIC` | automatic   |
| `CUSTOM`    | custom      |