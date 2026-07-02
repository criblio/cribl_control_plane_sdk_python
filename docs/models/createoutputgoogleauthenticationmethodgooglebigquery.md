# CreateOutputGoogleAuthenticationMethodGoogleBigquery

Choose Auto to use Google Application Default Credentials (ADC), or Secret to select or create a stored secret that references Google service account credentials

## Example Usage

```python
from cribl_control_plane.models import CreateOutputGoogleAuthenticationMethodGoogleBigquery

value = CreateOutputGoogleAuthenticationMethodGoogleBigquery.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `SECRET` | secret   |