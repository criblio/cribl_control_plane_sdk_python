# SampleMode

Defines how sample rate will be derived: log(previousPeriodCount) or sqrt(previousPeriodCount)

## Example Usage

```python
from cribl_control_plane.models import SampleMode

value = SampleMode.LOG

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `LOG`  | log    |
| `SQRT` | sqrt   |