# ShardLoadBalancing

The load-balancing algorithm to use for spreading out shards across Workers and Worker Processes

## Example Usage

```python
from cribl_control_plane.models import ShardLoadBalancing

value = ShardLoadBalancing.CONSISTENT_HASHING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `CONSISTENT_HASHING` | ConsistentHashing    |
| `ROUND_ROBIN`        | RoundRobin           |