# CreateInputSystemByPackDiscoveryTypePrometheus

Target discovery mechanism. Use static to manually enter a list of targets.

## Example Usage

```python
from cribl_control_plane.models import CreateInputSystemByPackDiscoveryTypePrometheus

value = CreateInputSystemByPackDiscoveryTypePrometheus.STATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `STATIC` | static   |
| `DNS`    | dns      |
| `EC2`    | ec2      |