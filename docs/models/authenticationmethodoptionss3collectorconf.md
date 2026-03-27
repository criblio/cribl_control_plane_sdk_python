# AuthenticationMethodOptionsS3CollectorConf

AWS authentication method. Choose Auto to use IAM roles.

## Example Usage

```python
from cribl_control_plane.models import AuthenticationMethodOptionsS3CollectorConf

value = AuthenticationMethodOptionsS3CollectorConf.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `MANUAL` | manual   |
| `SECRET` | secret   |