# DisableTenantAnomalySettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_id** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.disable_tenant_anomaly_settings_request import DisableTenantAnomalySettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenantAnomalySettingsRequest from a JSON string
disable_tenant_anomaly_settings_request_instance = DisableTenantAnomalySettingsRequest.from_json(json)
# print the JSON string representation of the object
print(DisableTenantAnomalySettingsRequest.to_json())

# convert the object into a dict
disable_tenant_anomaly_settings_request_dict = disable_tenant_anomaly_settings_request_instance.to_dict()
# create an instance of DisableTenantAnomalySettingsRequest from a dict
disable_tenant_anomaly_settings_request_form_dict = disable_tenant_anomaly_settings_request.from_dict(disable_tenant_anomaly_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


