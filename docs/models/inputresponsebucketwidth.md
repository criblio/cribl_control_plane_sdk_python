# InputResponseBucketWidth

Time bucket size for aggregated results. Smaller buckets yield more events per collection run.

## Example Usage

```python
from cribl_control_plane.models import InputResponseBucketWidth

value = InputResponseBucketWidth.ONED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `ONED` | 1d     |
| `ONEH` | 1h     |
| `ONEM` | 1m     |