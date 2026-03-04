# CreateOutputProtocolSyslog

The network protocol to use for sending out syslog messages

## Example Usage

```python
from cribl_control_plane.models import CreateOutputProtocolSyslog

value = CreateOutputProtocolSyslog.TCP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `TCP` | tcp   |
| `UDP` | udp   |