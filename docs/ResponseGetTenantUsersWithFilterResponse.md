# ResponseGetTenantUsersWithFilterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantUsersWithFilterResponse**](GetTenantUsersWithFilterResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_users_with_filter_response import ResponseGetTenantUsersWithFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantUsersWithFilterResponse from a JSON string
response_get_tenant_users_with_filter_response_instance = ResponseGetTenantUsersWithFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantUsersWithFilterResponse.to_json())

# convert the object into a dict
response_get_tenant_users_with_filter_response_dict = response_get_tenant_users_with_filter_response_instance.to_dict()
# create an instance of ResponseGetTenantUsersWithFilterResponse from a dict
response_get_tenant_users_with_filter_response_form_dict = response_get_tenant_users_with_filter_response.from_dict(response_get_tenant_users_with_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


