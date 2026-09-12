# InputResponseInputWefAuthenticationMethod

How to authenticate incoming client connections

## Example Usage

```python
from cribl_control_plane.models import InputResponseInputWefAuthenticationMethod

value = InputResponseInputWefAuthenticationMethod.CLIENT_CERT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CLIENT_CERT` | clientCert    |
| `KERBEROS`    | kerberos      |
| `NEGOTIATE`   | negotiate     |