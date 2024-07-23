# GetTenantUsersWithFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**sort_criteria** | [**SortCriteria**](SortCriteria.md) |  | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_tenant_users_with_filter_request import GetTenantUsersWithFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUsersWithFilterRequest from a JSON string
get_tenant_users_with_filter_request_instance = GetTenantUsersWithFilterRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantUsersWithFilterRequest.to_json())

# convert the object into a dict
get_tenant_users_with_filter_request_dict = get_tenant_users_with_filter_request_instance.to_dict()
# create an instance of GetTenantUsersWithFilterRequest from a dict
get_tenant_users_with_filter_request_form_dict = get_tenant_users_with_filter_request.from_dict(get_tenant_users_with_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


