# CreateOutputOutputGoogleCloudObservabilityGoogleAuthenticationMethod

Choose Auto to use Google Application Default Credentials (ADC). Choose Secret to select or create a stored secret that references Google service account credentials.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputOutputGoogleCloudObservabilityGoogleAuthenticationMethod

value = CreateOutputOutputGoogleCloudObservabilityGoogleAuthenticationMethod.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `SECRET` | secret   |