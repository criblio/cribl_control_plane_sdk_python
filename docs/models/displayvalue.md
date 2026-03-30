# DisplayValue

ServiceNow reference field display mode. Allows raw values, display values, or both (sysparm_display_value).

## Example Usage

```python
from cribl_control_plane.models import DisplayValue

value = DisplayValue.FALSE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `FALSE` | false   |
| `TRUE`  | true    |
| `ALL`   | all     |