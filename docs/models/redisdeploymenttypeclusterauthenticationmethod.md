# RedisDeploymentTypeClusterAuthenticationMethod

## Example Usage

```python
from cribl_control_plane.models import RedisDeploymentTypeClusterAuthenticationMethod

value = RedisDeploymentTypeClusterAuthenticationMethod.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `NONE`               | none                 |
| `MANUAL`             | manual               |
| `CREDENTIALS_SECRET` | credentialsSecret    |
| `TEXT_SECRET`        | textSecret           |