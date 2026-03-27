# Operator

Comparison operator

## Example Usage

```python
from cribl_control_plane.models import Operator

value = Operator.EQUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `EQUAL`           | =                 |
| `NOT_EQUAL`       | !=                |
| `REGEX_MATCH`     | =~                |
| `REGEX_NOT_MATCH` | !~                |