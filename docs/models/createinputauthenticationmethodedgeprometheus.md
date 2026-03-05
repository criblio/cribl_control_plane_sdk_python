# CreateInputAuthenticationMethodEdgePrometheus

Enter credentials directly, or select a stored secret

## Example Usage

```python
from cribl_control_plane.models import CreateInputAuthenticationMethodEdgePrometheus

value = CreateInputAuthenticationMethodEdgePrometheus.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `MANUAL`     | manual       |
| `SECRET`     | secret       |
| `KUBERNETES` | kubernetes   |