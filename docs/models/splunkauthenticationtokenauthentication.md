# SplunkAuthenticationTokenAuthentication

Authentication method for Discover and Collect REST calls

## Example Usage

```python
from cribl_control_plane.models import SplunkAuthenticationTokenAuthentication

value = SplunkAuthenticationTokenAuthentication.NONE

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