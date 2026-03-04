# InputOffice365MsgTraceAuthenticationMethod

Select authentication method.

## Example Usage

```python
from cribl_control_plane.models import InputOffice365MsgTraceAuthenticationMethod

value = InputOffice365MsgTraceAuthenticationMethod.MANUAL

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