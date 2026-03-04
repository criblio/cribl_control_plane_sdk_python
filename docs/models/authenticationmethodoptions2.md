# AuthenticationMethodOptions2

Select authentication method.

## Example Usage

```python
from cribl_control_plane.models import AuthenticationMethodOptions2

value = AuthenticationMethodOptions2.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `MANUAL`       | manual         |
| `SECRET`       | secret         |
| `OAUTH`        | oauth          |
| `OAUTH_SECRET` | oauthSecret    |
| `OAUTH_CERT`   | oauthCert      |