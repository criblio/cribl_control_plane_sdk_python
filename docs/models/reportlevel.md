# ReportLevel

Level of ingestion status reporting. Defaults to FailuresOnly.

## Example Usage

```python
from cribl_control_plane.models import ReportLevel

value = ReportLevel.FAILURES_ONLY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `FAILURES_ONLY`          | failuresOnly             |
| `DO_NOT_REPORT`          | doNotReport              |
| `FAILURES_AND_SUCCESSES` | failuresAndSuccesses     |