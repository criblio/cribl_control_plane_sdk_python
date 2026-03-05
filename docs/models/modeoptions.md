# ModeOptions

In Error mode, PQ writes events to the filesystem if the Destination is unavailable. In Backpressure mode, PQ writes events to the filesystem when it detects backpressure from the Destination. In Always On mode, PQ always writes events to the filesystem.

## Example Usage

```python
from cribl_control_plane.models import ModeOptions

value = ModeOptions.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ERROR`        | error          |
| `ALWAYS`       | always         |
| `BACKPRESSURE` | backpressure   |