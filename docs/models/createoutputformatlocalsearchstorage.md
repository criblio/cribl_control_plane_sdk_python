# CreateOutputFormatLocalSearchStorage

Data format to use when sending data. Defaults to JSON Compact.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputFormatLocalSearchStorage

value = CreateOutputFormatLocalSearchStorage.JSON_COMPACT_EACH_ROW_WITH_NAMES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                               | Value                              |
| ---------------------------------- | ---------------------------------- |
| `JSON_COMPACT_EACH_ROW_WITH_NAMES` | json-compact-each-row-with-names   |
| `JSON_EACH_ROW`                    | json-each-row                      |