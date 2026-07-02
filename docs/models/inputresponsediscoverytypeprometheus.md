# InputResponseDiscoveryTypePrometheus

Target discovery mechanism. Use static to manually enter a list of targets.

## Example Usage

```python
from cribl_control_plane.models import InputResponseDiscoveryTypePrometheus

value = InputResponseDiscoveryTypePrometheus.STATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `STATIC`  | static    |
| `DNS`     | dns       |
| `EC2`     | ec2       |
| `HTTP_SD` | http_sd   |