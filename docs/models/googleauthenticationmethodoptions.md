# GoogleAuthenticationMethodOptions

Choose Auto to use Google Application Default Credentials (ADC), Manual to enter Google service account credentials directly, or Secret to select or create a stored secret that references Google service account credentials.

## Example Usage

```python
from cribl_control_plane.models import GoogleAuthenticationMethodOptions

value = GoogleAuthenticationMethodOptions.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `MANUAL` | manual   |
| `SECRET` | secret   |