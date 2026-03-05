# BackpressureBehaviorOptions1

How to handle events when all receivers are exerting backpressure

## Example Usage

```python
from cribl_control_plane.models import BackpressureBehaviorOptions1

value = BackpressureBehaviorOptions1.BLOCK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `BLOCK` | block   |
| `DROP`  | drop    |