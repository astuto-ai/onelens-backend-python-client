# DisableTenantAnomalySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_overrides** | [**AnomalyLogicOperationOutput**](AnomalyLogicOperationOutput.md) |  | [optional] 
**state** | [**TenantAnomalyState**](TenantAnomalyState.md) | The state of the policy template. | 
**id** | **str** | The unique identifier of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.disable_tenant_anomaly_settings_response import DisableTenantAnomalySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenantAnomalySettingsResponse from a JSON string
disable_tenant_anomaly_settings_response_instance = DisableTenantAnomalySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(DisableTenantAnomalySettingsResponse.to_json())

# convert the object into a dict
disable_tenant_anomaly_settings_response_dict = disable_tenant_anomaly_settings_response_instance.to_dict()
# create an instance of DisableTenantAnomalySettingsResponse from a dict
disable_tenant_anomaly_settings_response_form_dict = disable_tenant_anomaly_settings_response.from_dict(disable_tenant_anomaly_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


