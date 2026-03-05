# OutputDynatraceHTTPFormat

How to format events before sending. Defaults to JSON. Plaintext is not currently supported.

## Example Usage

```python
from cribl_control_plane.models import OutputDynatraceHTTPFormat

value = OutputDynatraceHTTPFormat.JSON_ARRAY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `JSON_ARRAY` | json_array   |
| `PLAINTEXT`  | plaintext    |