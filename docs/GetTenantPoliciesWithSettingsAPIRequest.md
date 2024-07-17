# GetTenantPoliciesWithSettingsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**sort_criteria** | [**SortCriteria**](SortCriteria.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_with_settings_api_request import GetTenantPoliciesWithSettingsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesWithSettingsAPIRequest from a JSON string
get_tenant_policies_with_settings_api_request_instance = GetTenantPoliciesWithSettingsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesWithSettingsAPIRequest.to_json())

# convert the object into a dict
get_tenant_policies_with_settings_api_request_dict = get_tenant_policies_with_settings_api_request_instance.to_dict()
# create an instance of GetTenantPoliciesWithSettingsAPIRequest from a dict
get_tenant_policies_with_settings_api_request_form_dict = get_tenant_policies_with_settings_api_request.from_dict(get_tenant_policies_with_settings_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


