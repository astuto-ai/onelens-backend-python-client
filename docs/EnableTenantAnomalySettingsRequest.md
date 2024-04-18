# EnableTenantAnomalySettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_id** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.enable_tenant_anomaly_settings_request import EnableTenantAnomalySettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableTenantAnomalySettingsRequest from a JSON string
enable_tenant_anomaly_settings_request_instance = EnableTenantAnomalySettingsRequest.from_json(json)
# print the JSON string representation of the object
print(EnableTenantAnomalySettingsRequest.to_json())

# convert the object into a dict
enable_tenant_anomaly_settings_request_dict = enable_tenant_anomaly_settings_request_instance.to_dict()
# create an instance of EnableTenantAnomalySettingsRequest from a dict
enable_tenant_anomaly_settings_request_form_dict = enable_tenant_anomaly_settings_request.from_dict(enable_tenant_anomaly_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


