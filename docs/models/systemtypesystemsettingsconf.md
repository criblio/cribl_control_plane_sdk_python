# SystemTypeSystemSettingsConf

System-level operational settings for the Cribl instance.


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `intercom`                                                                                                         | *bool*                                                                                                             | :heavy_check_mark:                                                                                                 | If <code>true</code>, enable Intercom integration for in-product messaging. Otherwise, <code>false</code>.         |
| `upgrade`                                                                                                          | [models.UpgradeOptionsSystemSettingsConfSystem](../models/upgradeoptionssystemsettingsconfsystem.md)               | :heavy_check_mark:                                                                                                 | Upgrade permission policy: <code>api</code> to allow upgrades from the UI or API or <code>false</code> to disable. |