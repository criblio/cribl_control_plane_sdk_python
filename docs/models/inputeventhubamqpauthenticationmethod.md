# InputEventhubAmqpAuthenticationMethod

Enter connection string directly, or select a stored secret

## Example Usage

```python
from cribl_control_plane.models import InputEventhubAmqpAuthenticationMethod

value = InputEventhubAmqpAuthenticationMethod.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MANUAL` | manual   |
| `SECRET` | secret   |