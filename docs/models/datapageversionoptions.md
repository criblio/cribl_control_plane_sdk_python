# DataPageVersionOptions

Serialization format of data pages. Note that some reader implementations use Data page V2's attributes to work more efficiently, while others ignore it.

## Example Usage

```python
from cribl_control_plane.models import DataPageVersionOptions

value = DataPageVersionOptions.DATA_PAGE_V1

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `DATA_PAGE_V1` | DATA_PAGE_V1   |
| `DATA_PAGE_V2` | DATA_PAGE_V2   |