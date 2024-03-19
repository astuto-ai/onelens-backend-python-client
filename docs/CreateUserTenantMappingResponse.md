# CreateUserTenantMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Unique identifier for the user in onelens. | 
**tenant_id** | **str** | Unique identifier for the tenant. | 

## Example

```python
from openapi_client.models.create_user_tenant_mapping_response import CreateUserTenantMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserTenantMappingResponse from a JSON string
create_user_tenant_mapping_response_instance = CreateUserTenantMappingResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserTenantMappingResponse.to_json())

# convert the object into a dict
create_user_tenant_mapping_response_dict = create_user_tenant_mapping_response_instance.to_dict()
# create an instance of CreateUserTenantMappingResponse from a dict
create_user_tenant_mapping_response_form_dict = create_user_tenant_mapping_response.from_dict(create_user_tenant_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


