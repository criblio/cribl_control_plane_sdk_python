# InputResponseCertOptions


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `certificate_name`                                             | *Optional[str]*                                                | :heavy_minus_sign:                                             | The name of a predefined certificate                           |
| `priv_key_path`                                                | *str*                                                          | :heavy_check_mark:                                             | Path to the private key (PEM format). Can reference $ENV_VARS. |
| `passphrase`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Passphrase to decrypt the private key                          |
| `cert_path`                                                    | *str*                                                          | :heavy_check_mark:                                             | Path to the certificate (PEM format). Can reference $ENV_VARS. |