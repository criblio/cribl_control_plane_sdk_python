# CreateOutputDataFormatSumoLogic

Preserve the raw event format instead of JSONifying it

## Example Usage

```python
from cribl_control_plane.models import CreateOutputDataFormatSumoLogic

value = CreateOutputDataFormatSumoLogic.JSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `JSON` | json   |
| `RAW`  | raw    |