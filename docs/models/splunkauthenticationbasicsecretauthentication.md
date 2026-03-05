# SplunkAuthenticationBasicSecretAuthentication

Authentication method for Discover and Collect REST calls

## Example Usage

```python
from cribl_control_plane.models import SplunkAuthenticationBasicSecretAuthentication

value = SplunkAuthenticationBasicSecretAuthentication.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NONE`         | none           |
| `BASIC`        | basic          |
| `BASIC_SECRET` | basicSecret    |
| `TOKEN`        | token          |
| `TOKEN_SECRET` | tokenSecret    |