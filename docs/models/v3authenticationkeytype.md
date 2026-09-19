# V3AuthenticationKeyType

Select Manual to enter the key directly, or Secret to use a stored text secret

## Example Usage

```python
from cribl_control_plane.models import V3AuthenticationKeyType

value = V3AuthenticationKeyType.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MANUAL` | manual   |
| `SECRET` | secret   |