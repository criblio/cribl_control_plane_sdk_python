# RedisDeploymentTypeClusterDeploymentType

How the Redis server is configured. Defaults to Standalone

## Example Usage

```python
from cribl_control_plane.models import RedisDeploymentTypeClusterDeploymentType

value = RedisDeploymentTypeClusterDeploymentType.STANDALONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `STANDALONE` | standalone   |
| `CLUSTER`    | cluster      |
| `SENTINEL`   | sentinel     |