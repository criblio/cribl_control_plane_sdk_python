# CreateOutputUDMType

Defines the specific format for UDM events sent to Google SecOps. This must match the type of UDM data being sent.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputUDMType

value = CreateOutputUDMType.ENTITIES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ENTITIES` | entities   |
| `LOGS`     | logs       |