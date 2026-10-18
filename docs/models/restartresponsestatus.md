# RestartResponseStatus

Result of the restart request for this Node (<code>Restarting</code> or <code>Error</code>).

## Example Usage

```python
from cribl_control_plane.models import RestartResponseStatus

value = RestartResponseStatus.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `ERROR`      | Error        |
| `RESTARTING` | Restarting   |