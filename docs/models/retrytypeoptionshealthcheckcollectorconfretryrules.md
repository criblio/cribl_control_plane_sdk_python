# RetryTypeOptionsHealthCheckCollectorConfRetryRules

The algorithm to use when performing HTTP retries

## Example Usage

```python
from cribl_control_plane.models import RetryTypeOptionsHealthCheckCollectorConfRetryRules

value = RetryTypeOptionsHealthCheckCollectorConfRetryRules.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `NONE`    | none      |
| `BACKOFF` | backoff   |
| `STATIC`  | static    |