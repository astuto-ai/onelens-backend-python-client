# EnableTenantAnomalySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_overrides** | [**AnomalyLogicOperation**](AnomalyLogicOperation.md) |  | [optional] 
**state** | [**TenantAnomalyState**](TenantAnomalyState.md) | The state of the policy template. | 
**id** | **str** | The unique identifier of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.enable_tenant_anomaly_settings_response import EnableTenantAnomalySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnableTenantAnomalySettingsResponse from a JSON string
enable_tenant_anomaly_settings_response_instance = EnableTenantAnomalySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(EnableTenantAnomalySettingsResponse.to_json())

# convert the object into a dict
enable_tenant_anomaly_settings_response_dict = enable_tenant_anomaly_settings_response_instance.to_dict()
# create an instance of EnableTenantAnomalySettingsResponse from a dict
enable_tenant_anomaly_settings_response_form_dict = enable_tenant_anomaly_settings_response.from_dict(enable_tenant_anomaly_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


