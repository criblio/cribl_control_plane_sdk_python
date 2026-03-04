# CreateOutputRegion

The SentinelOne region to send events to. In most cases you can find the region by either looking at your SentinelOne URL or knowing what geographic region your SentinelOne instance is contained in.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputRegion

value = CreateOutputRegion.US

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `US`     | US       |
| `CA`     | CA       |
| `EMEA`   | EMEA     |
| `AP`     | AP       |
| `APS`    | APS      |
| `AU`     | AU       |
| `CUSTOM` | Custom   |