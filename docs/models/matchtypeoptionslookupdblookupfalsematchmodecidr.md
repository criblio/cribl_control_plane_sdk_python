# MatchTypeOptionsLookupDbLookupFalseMatchModeCidr

Further defines how to handle multiple matches: return the first match, the most specific match, or all matches

## Example Usage

```python
from cribl_control_plane.models import MatchTypeOptionsLookupDbLookupFalseMatchModeCidr

value = MatchTypeOptionsLookupDbLookupFalseMatchModeCidr.FIRST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `FIRST`    | first      |
| `SPECIFIC` | specific   |
| `ALL`      | all        |