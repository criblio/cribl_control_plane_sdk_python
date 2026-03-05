# BackpressureBehaviorOptionsBlockDrop

How to handle events when all receivers are exerting backpressure

## Example Usage

```python
from cribl_control_plane.models import BackpressureBehaviorOptionsBlockDrop

value = BackpressureBehaviorOptionsBlockDrop.BLOCK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `BLOCK` | block   |
| `DROP`  | drop    |