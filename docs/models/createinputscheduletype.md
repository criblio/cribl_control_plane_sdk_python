# CreateInputScheduleType

Select a schedule type; either an interval (in seconds) or a cron-style schedule.

## Example Usage

```python
from cribl_control_plane.models import CreateInputScheduleType

value = CreateInputScheduleType.INTERVAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `INTERVAL`      | interval        |
| `CRON_SCHEDULE` | cronSchedule    |