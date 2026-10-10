# SerdeTypeGrokType

Parser or formatter type to use.

## Example Usage

```python
from cribl_control_plane.models import SerdeTypeGrokType

value = SerdeTypeGrokType.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `AUTO`  | auto    |
| `CSV`   | csv     |
| `ELFF`  | elff    |
| `CLF`   | clf     |
| `KVP`   | kvp     |
| `JSON`  | json    |
| `DELIM` | delim   |
| `REGEX` | regex   |
| `GROK`  | grok    |