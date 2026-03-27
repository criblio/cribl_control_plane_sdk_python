# SaslMechanismOptionsSasl

## Example Usage

```python
from cribl_control_plane.models import SaslMechanismOptionsSasl

value = SaslMechanismOptionsSasl.PLAIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `PLAIN`         | plain           |
| `SCRAM_SHA_256` | scram-sha-256   |
| `SCRAM_SHA_512` | scram-sha-512   |
| `KERBEROS`      | kerberos        |