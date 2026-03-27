# BackpressureBehaviorOptions

How to handle events when all receivers are exerting backpressure

## Example Usage

```python
from cribl_control_plane.models import BackpressureBehaviorOptions

value = BackpressureBehaviorOptions.BLOCK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `BLOCK` | block   |
| `DROP`  | drop    |
| `QUEUE` | queue   |