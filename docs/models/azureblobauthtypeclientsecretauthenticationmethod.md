# AzureBlobAuthTypeClientSecretAuthenticationMethod

Enter authentication data directly, or select a secret referencing your auth data

## Example Usage

```python
from cribl_control_plane.models import AzureBlobAuthTypeClientSecretAuthenticationMethod

value = AzureBlobAuthTypeClientSecretAuthenticationMethod.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `MANUAL`        | manual          |
| `SECRET`        | secret          |
| `CLIENT_SECRET` | clientSecret    |
| `CLIENT_CERT`   | clientCert      |