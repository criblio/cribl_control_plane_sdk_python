# WriteAction

Action to use when writing events. Must be set to `Create` when writing to a data stream.

## Example Usage

```python
from cribl_control_plane.models import WriteAction

value = WriteAction.INDEX

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `INDEX`  | index    |
| `CREATE` | create   |