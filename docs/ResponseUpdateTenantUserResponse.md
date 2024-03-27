# ResponseUpdateTenantUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTenantUserResponse**](UpdateTenantUserResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_update_tenant_user_response import ResponseUpdateTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateTenantUserResponse from a JSON string
response_update_tenant_user_response_instance = ResponseUpdateTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateTenantUserResponse.to_json())

# convert the object into a dict
response_update_tenant_user_response_dict = response_update_tenant_user_response_instance.to_dict()
# create an instance of ResponseUpdateTenantUserResponse from a dict
response_update_tenant_user_response_form_dict = response_update_tenant_user_response.from_dict(response_update_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


