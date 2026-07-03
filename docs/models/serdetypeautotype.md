# SerdeTypeAutoType

Parser or formatter type to use

## Example Usage

```python
from cribl_control_plane.models import SerdeTypeAutoType

value = SerdeTypeAutoType.CSV

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `CSV`   | csv     |
| `ELFF`  | elff    |
| `CLF`   | clf     |
| `KVP`   | kvp     |
| `JSON`  | json    |
| `DELIM` | delim   |
| `REGEX` | regex   |
| `GROK`  | grok    |
| `AUTO`  | auto    |