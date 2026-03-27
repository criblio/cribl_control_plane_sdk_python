# RunnableJobCollectionMode

Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job.

## Example Usage

```python
from cribl_control_plane.models import RunnableJobCollectionMode

value = RunnableJobCollectionMode.LIST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `LIST`    | list      |
| `PREVIEW` | preview   |
| `RUN`     | run       |