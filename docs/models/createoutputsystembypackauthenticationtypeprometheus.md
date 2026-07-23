# CreateOutputSystemByPackAuthenticationTypePrometheus

Remote Write authentication type

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackAuthenticationTypePrometheus

value = CreateOutputSystemByPackAuthenticationTypePrometheus.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `NONE`               | none                 |
| `BASIC`              | basic                |
| `CREDENTIALS_SECRET` | credentialsSecret    |
| `TOKEN`              | token                |
| `TEXT_SECRET`        | textSecret           |
| `AWS_SIGV4`          | aws_sigv4            |