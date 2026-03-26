# LookupDbLookupFalseMatchModeExactMatchMode

Specifies the matching method based on the format and logic used in the lookup file

## Example Usage

```python
from cribl_control_plane.models import LookupDbLookupFalseMatchModeExactMatchMode

value = LookupDbLookupFalseMatchModeExactMatchMode.EXACT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `EXACT` | exact   |
| `CIDR`  | cidr    |
| `REGEX` | regex   |