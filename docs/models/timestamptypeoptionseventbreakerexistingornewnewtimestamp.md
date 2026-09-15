# TimestampTypeOptionsEventBreakerExistingOrNewNewTimestamp

Method to use for timestamp extraction. Use <code>auto</code> for automatic detection, <code>format</code> to specify a strptime format, or <code>current</code> to use the current system time.

## Example Usage

```python
from cribl_control_plane.models import TimestampTypeOptionsEventBreakerExistingOrNewNewTimestamp

value = TimestampTypeOptionsEventBreakerExistingOrNewNewTimestamp.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `AUTO`    | auto      |
| `FORMAT`  | format    |
| `CURRENT` | current   |