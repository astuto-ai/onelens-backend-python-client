# GetTenantUsersWithoutUserContextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**users** | [**List[BaseUser]**](BaseUser.md) | List of tenant users | 

## Example

```python
from onelens_backend_client.models.get_tenant_users_without_user_context_response import GetTenantUsersWithoutUserContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUsersWithoutUserContextResponse from a JSON string
get_tenant_users_without_user_context_response_instance = GetTenantUsersWithoutUserContextResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantUsersWithoutUserContextResponse.to_json())

# convert the object into a dict
get_tenant_users_without_user_context_response_dict = get_tenant_users_without_user_context_response_instance.to_dict()
# create an instance of GetTenantUsersWithoutUserContextResponse from a dict
get_tenant_users_without_user_context_response_form_dict = get_tenant_users_without_user_context_response.from_dict(get_tenant_users_without_user_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


