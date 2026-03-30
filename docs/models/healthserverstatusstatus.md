# HealthServerStatusStatus

Health state: <code>healthy</code>, <code>standby</code>, or <code>shutting down</code>.

## Example Usage

```python
from cribl_control_plane.models import HealthServerStatusStatus

value = HealthServerStatusStatus.HEALTHY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `HEALTHY`       | healthy         |
| `SHUTTING_DOWN` | shutting down   |
| `STANDBY`       | standby         |