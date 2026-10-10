# CreateOutputOutputInfluxdbAuthenticationType

InfluxDB authentication type

## Example Usage

```python
from cribl_control_plane.models import CreateOutputOutputInfluxdbAuthenticationType

value = CreateOutputOutputInfluxdbAuthenticationType.NONE

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