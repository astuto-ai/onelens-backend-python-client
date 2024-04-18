# GetTenantAnomalySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**anomaly_settings** | [**List[TenantAnomalySettings]**](TenantAnomalySettings.md) | List of tenant anomalies. | 

## Example

```python
from onelens_backend_client.models.get_tenant_anomaly_settings_response import GetTenantAnomalySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantAnomalySettingsResponse from a JSON string
get_tenant_anomaly_settings_response_instance = GetTenantAnomalySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantAnomalySettingsResponse.to_json())

# convert the object into a dict
get_tenant_anomaly_settings_response_dict = get_tenant_anomaly_settings_response_instance.to_dict()
# create an instance of GetTenantAnomalySettingsResponse from a dict
get_tenant_anomaly_settings_response_form_dict = get_tenant_anomaly_settings_response.from_dict(get_tenant_anomaly_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


