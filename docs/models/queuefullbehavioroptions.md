# QueueFullBehaviorOptions

How to handle events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged.

## Example Usage

```python
from cribl_control_plane.models import QueueFullBehaviorOptions

value = QueueFullBehaviorOptions.BLOCK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `BLOCK` | block   |
| `DROP`  | drop    |