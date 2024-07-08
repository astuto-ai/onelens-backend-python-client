# GetTenantUsersWithFilterAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**TenantUsersFilters**](TenantUsersFilters.md) | Get tenant users with filters | [optional] 

## Example

```python
from onelens_backend_client.models.get_tenant_users_with_filter_api_request import GetTenantUsersWithFilterAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUsersWithFilterAPIRequest from a JSON string
get_tenant_users_with_filter_api_request_instance = GetTenantUsersWithFilterAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantUsersWithFilterAPIRequest.to_json())

# convert the object into a dict
get_tenant_users_with_filter_api_request_dict = get_tenant_users_with_filter_api_request_instance.to_dict()
# create an instance of GetTenantUsersWithFilterAPIRequest from a dict
get_tenant_users_with_filter_api_request_form_dict = get_tenant_users_with_filter_api_request.from_dict(get_tenant_users_with_filter_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


