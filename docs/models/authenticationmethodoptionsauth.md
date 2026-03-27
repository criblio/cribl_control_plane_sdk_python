# AuthenticationMethodOptionsAuth

Enter credentials directly, or select a stored secret

## Example Usage

```python
from cribl_control_plane.models import AuthenticationMethodOptionsAuth

value = AuthenticationMethodOptionsAuth.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `MANUAL`         | manual           |
| `SECRET`         | secret           |
| `MANUAL_API_KEY` | manualAPIKey     |
| `TEXT_SECRET`    | textSecret       |