# OutputResponseOAuthSecretSource

Enter the OAuth secret directly, or select a stored text secret

## Example Usage

```python
from cribl_control_plane.models import OutputResponseOAuthSecretSource

value = OutputResponseOAuthSecretSource.INLINE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `INLINE` | inline   |
| `SECRET` | secret   |