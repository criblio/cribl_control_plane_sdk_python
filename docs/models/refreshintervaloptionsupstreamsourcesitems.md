# RefreshIntervalOptionsUpstreamSourcesItems

How often to pull updates. Ignored when ref is a tag or SHA.

## Example Usage

```python
from cribl_control_plane.models import RefreshIntervalOptionsUpstreamSourcesItems

value = RefreshIntervalOptionsUpstreamSourcesItems.NEVER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NEVER`        | never          |
| `FIVEM`        | 5m             |
| `FIFTEENM`     | 15m            |
| `ONEH`         | 1h             |
| `SIXH`         | 6h             |
| `TWENTY_FOURH` | 24h            |