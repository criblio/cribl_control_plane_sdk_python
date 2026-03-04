# State

State of the Job

## Example Usage

```python
from cribl_control_plane.models import State

value = State.INITIALIZING

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `INITIALIZING` | 0              |
| `PENDING`      | 1              |
| `RUNNING`      | 2              |
| `PAUSED`       | 3              |
| `CANCELLED`    | 4              |
| `FINISHED`     | 5              |
| `FAILED`       | 6              |
| `ORPHANED`     | 7              |
| `UNKNOWN`      | 8              |
| `LENGTH`       | 9              |