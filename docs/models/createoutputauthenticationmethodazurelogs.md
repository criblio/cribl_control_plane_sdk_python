# CreateOutputAuthenticationMethodAzureLogs

Enter workspace ID and workspace key directly, or select a stored secret

## Example Usage

```python
from cribl_control_plane.models import CreateOutputAuthenticationMethodAzureLogs

value = CreateOutputAuthenticationMethodAzureLogs.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MANUAL` | manual   |
| `SECRET` | secret   |