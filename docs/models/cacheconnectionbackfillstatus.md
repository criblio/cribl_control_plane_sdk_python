# CacheConnectionBackfillStatus

## Example Usage

```python
from cribl_control_plane.models import CacheConnectionBackfillStatus

value = CacheConnectionBackfillStatus.SCHEDULED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `SCHEDULED`  | scheduled    |
| `PENDING`    | pending      |
| `STARTED`    | started      |
| `FINISHED`   | finished     |
| `INCOMPLETE` | incomplete   |