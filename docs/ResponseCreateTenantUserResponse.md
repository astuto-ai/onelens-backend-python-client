# ResponseCreateTenantUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTenantUserResponse**](CreateTenantUserResponse.md) |  | 
**message** | [**Message**](Message.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_tenant_user_response import ResponseCreateTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateTenantUserResponse from a JSON string
response_create_tenant_user_response_instance = ResponseCreateTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateTenantUserResponse.to_json())

# convert the object into a dict
response_create_tenant_user_response_dict = response_create_tenant_user_response_instance.to_dict()
# create an instance of ResponseCreateTenantUserResponse from a dict
response_create_tenant_user_response_form_dict = response_create_tenant_user_response.from_dict(response_create_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


