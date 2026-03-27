# GoogleCloudStorageAuthTypeSecretAuthenticationMethod

Enter account credentials manually, select a secret that references your credentials, or use Google Application Default Credentials

## Example Usage

```python
from cribl_control_plane.models import GoogleCloudStorageAuthTypeSecretAuthenticationMethod

value = GoogleCloudStorageAuthTypeSecretAuthenticationMethod.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `MANUAL` | manual   |
| `SECRET` | secret   |