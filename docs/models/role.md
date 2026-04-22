# Role

Leader Node role: <code>primary</code> or <code>standby</code>.

## Example Usage

```python
from cribl_control_plane.models import Role

value = Role.PRIMARY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PRIMARY` | primary   |
| `STANDBY` | standby   |