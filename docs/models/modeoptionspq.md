# ModeOptionsPq

With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine.

## Example Usage

```python
from cribl_control_plane.models import ModeOptionsPq

value = ModeOptionsPq.SMART

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `SMART`  | smart    |
| `ALWAYS` | always   |