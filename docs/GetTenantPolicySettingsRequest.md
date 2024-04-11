# GetTenantPolicySettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**TenantPolicySettingsFilters**](TenantPolicySettingsFilters.md) | Filters to apply to the tenant policy settings. | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policy_settings_request import GetTenantPolicySettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicySettingsRequest from a JSON string
get_tenant_policy_settings_request_instance = GetTenantPolicySettingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicySettingsRequest.to_json())

# convert the object into a dict
get_tenant_policy_settings_request_dict = get_tenant_policy_settings_request_instance.to_dict()
# create an instance of GetTenantPolicySettingsRequest from a dict
get_tenant_policy_settings_request_form_dict = get_tenant_policy_settings_request.from_dict(get_tenant_policy_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


