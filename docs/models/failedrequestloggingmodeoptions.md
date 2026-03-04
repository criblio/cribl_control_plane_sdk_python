# FailedRequestLoggingModeOptions

Data to log when a request fails. All headers are redacted by default, unless listed as safe headers below.

## Example Usage

```python
from cribl_control_plane.models import FailedRequestLoggingModeOptions

value = FailedRequestLoggingModeOptions.PAYLOAD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `PAYLOAD`             | payload               |
| `PAYLOAD_AND_HEADERS` | payloadAndHeaders     |
| `NONE`                | none                  |