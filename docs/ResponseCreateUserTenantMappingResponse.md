# ResponseCreateUserTenantMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateUserTenantMappingResponse**](CreateUserTenantMappingResponse.md) |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from onelens_backend_client.models.response_create_user_tenant_mapping_response import ResponseCreateUserTenantMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateUserTenantMappingResponse from a JSON string
response_create_user_tenant_mapping_response_instance = ResponseCreateUserTenantMappingResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateUserTenantMappingResponse.to_json())

# convert the object into a dict
response_create_user_tenant_mapping_response_dict = response_create_user_tenant_mapping_response_instance.to_dict()
# create an instance of ResponseCreateUserTenantMappingResponse from a dict
response_create_user_tenant_mapping_response_form_dict = response_create_user_tenant_mapping_response.from_dict(response_create_user_tenant_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


