# OutputResponseOutputWebhookAuthenticationType2

Authentication method to use for the HTTP request

## Example Usage

```python
from cribl_control_plane.models import OutputResponseOutputWebhookAuthenticationType2

value = OutputResponseOutputWebhookAuthenticationType2.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `NONE`               | none                 |
| `BASIC`              | basic                |
| `CREDENTIALS_SECRET` | credentialsSecret    |
| `TOKEN`              | token                |
| `TEXT_SECRET`        | textSecret           |
| `OAUTH`              | oauth                |