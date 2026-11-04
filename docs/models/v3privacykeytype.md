# V3PrivacyKeyType

Select Manual to enter the key directly, or Secret to use a stored text secret

## Example Usage

```python
from cribl_control_plane.models import V3PrivacyKeyType

value = V3PrivacyKeyType.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MANUAL` | manual   |
| `SECRET` | secret   |