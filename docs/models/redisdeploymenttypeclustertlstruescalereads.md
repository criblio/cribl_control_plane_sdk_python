# RedisDeploymentTypeClusterTLSTrueScaleReads

Which nodes read commands should be sent to

## Example Usage

```python
from cribl_control_plane.models import RedisDeploymentTypeClusterTLSTrueScaleReads

value = RedisDeploymentTypeClusterTLSTrueScaleReads.MASTER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `MASTER`  | master    |
| `REPLICA` | replica   |
| `ALL`     | all       |