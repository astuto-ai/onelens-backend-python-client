# GetTenantAnomalySettingsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**TenantAnomalySettingFilters**](TenantAnomalySettingFilters.md) | Filters to apply to the tenant anomalies. | [optional] 

## Example

```python
from onelens_backend_client.models.get_tenant_anomaly_settings_api_request import GetTenantAnomalySettingsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantAnomalySettingsAPIRequest from a JSON string
get_tenant_anomaly_settings_api_request_instance = GetTenantAnomalySettingsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantAnomalySettingsAPIRequest.to_json())

# convert the object into a dict
get_tenant_anomaly_settings_api_request_dict = get_tenant_anomaly_settings_api_request_instance.to_dict()
# create an instance of GetTenantAnomalySettingsAPIRequest from a dict
get_tenant_anomaly_settings_api_request_form_dict = get_tenant_anomaly_settings_api_request.from_dict(get_tenant_anomaly_settings_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


