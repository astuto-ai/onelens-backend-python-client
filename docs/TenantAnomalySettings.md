# TenantAnomalySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_overrides** | [**AnomalyLogicOperation**](AnomalyLogicOperation.md) |  | [optional] 
**state** | [**TenantAnomalyState**](TenantAnomalyState.md) | The state of the policy template. | 
**id** | **str** | The unique identifier of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.tenant_anomaly_settings import TenantAnomalySettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAnomalySettings from a JSON string
tenant_anomaly_settings_instance = TenantAnomalySettings.from_json(json)
# print the JSON string representation of the object
print(TenantAnomalySettings.to_json())

# convert the object into a dict
tenant_anomaly_settings_dict = tenant_anomaly_settings_instance.to_dict()
# create an instance of TenantAnomalySettings from a dict
tenant_anomaly_settings_form_dict = tenant_anomaly_settings.from_dict(tenant_anomaly_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


