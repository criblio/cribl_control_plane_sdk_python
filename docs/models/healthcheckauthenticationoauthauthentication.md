# HealthCheckAuthenticationOauthAuthentication

Authentication method for Discover and Collect REST calls. You can specify API Key–based authentication by adding the appropriate Collect headers.

## Example Usage

```python
from cribl_control_plane.models import HealthCheckAuthenticationOauthAuthentication

value = HealthCheckAuthenticationOauthAuthentication.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NONE`         | none           |
| `BASIC`        | basic          |
| `BASIC_SECRET` | basicSecret    |
| `LOGIN`        | login          |
| `LOGIN_SECRET` | loginSecret    |
| `OAUTH`        | oauth          |
| `OAUTH_SECRET` | oauthSecret    |