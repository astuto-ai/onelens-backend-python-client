# GetTenantPoliciesWithSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_with_settings_request import GetTenantPoliciesWithSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesWithSettingsRequest from a JSON string
get_tenant_policies_with_settings_request_instance = GetTenantPoliciesWithSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesWithSettingsRequest.to_json())

# convert the object into a dict
get_tenant_policies_with_settings_request_dict = get_tenant_policies_with_settings_request_instance.to_dict()
# create an instance of GetTenantPoliciesWithSettingsRequest from a dict
get_tenant_policies_with_settings_request_form_dict = get_tenant_policies_with_settings_request.from_dict(get_tenant_policies_with_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


