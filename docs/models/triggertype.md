# TriggerType

Type of the trigger condition. custom applies a kusto expression over the results, and results count applies a comparison over results count

## Example Usage

```python
from cribl_control_plane.models import TriggerType

value = TriggerType.CUSTOM

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `CUSTOM`        | custom          |
| `RESULTS_COUNT` | resultsCount    |