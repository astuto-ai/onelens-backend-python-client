# GetTenantUsersWithFilterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**users** | [**List[GetAllTenantUsersItem]**](GetAllTenantUsersItem.md) | List of tenant users | 

## Example

```python
from onelens_backend_client.models.get_tenant_users_with_filter_response import GetTenantUsersWithFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUsersWithFilterResponse from a JSON string
get_tenant_users_with_filter_response_instance = GetTenantUsersWithFilterResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantUsersWithFilterResponse.to_json())

# convert the object into a dict
get_tenant_users_with_filter_response_dict = get_tenant_users_with_filter_response_instance.to_dict()
# create an instance of GetTenantUsersWithFilterResponse from a dict
get_tenant_users_with_filter_response_form_dict = get_tenant_users_with_filter_response.from_dict(get_tenant_users_with_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


