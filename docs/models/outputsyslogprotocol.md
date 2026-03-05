# OutputSyslogProtocol

The network protocol to use for sending out syslog messages

## Example Usage

```python
from cribl_control_plane.models import OutputSyslogProtocol

value = OutputSyslogProtocol.TCP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `TCP` | tcp   |
| `UDP` | udp   |