# GetTenantAnomalySettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**TenantAnomalySettingFilters**](TenantAnomalySettingFilters.md) | Filters to apply to the tenant anomalies. | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_anomaly_settings_request import GetTenantAnomalySettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantAnomalySettingsRequest from a JSON string
get_tenant_anomaly_settings_request_instance = GetTenantAnomalySettingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantAnomalySettingsRequest.to_json())

# convert the object into a dict
get_tenant_anomaly_settings_request_dict = get_tenant_anomaly_settings_request_instance.to_dict()
# create an instance of GetTenantAnomalySettingsRequest from a dict
get_tenant_anomaly_settings_request_form_dict = get_tenant_anomaly_settings_request.from_dict(get_tenant_anomaly_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


