# ResourceRecordType

The DNS record type (RR) to return. Defaults to 'A'.

## Example Usage

```python
from cribl_control_plane.models import ResourceRecordType

value = ResourceRecordType.A

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `A`     | A       |
| `AAAA`  | AAAA    |
| `ANY`   | ANY     |
| `CNAME` | CNAME   |
| `MX`    | MX      |
| `NAPTR` | NAPTR   |
| `NS`    | NS      |
| `PTR`   | PTR     |
| `SOA`   | SOA     |
| `SRV`   | SRV     |
| `TXT`   | TXT     |