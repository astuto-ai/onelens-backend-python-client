# CreateUserTenantMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Unique identifier for the user in onelens. | 
**tenant_id** | **str** | Unique identifier for the tenant. | 

## Example

```python
from onelens_backend_client.models.create_user_tenant_mapping_request import CreateUserTenantMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserTenantMappingRequest from a JSON string
create_user_tenant_mapping_request_instance = CreateUserTenantMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserTenantMappingRequest.to_json())

# convert the object into a dict
create_user_tenant_mapping_request_dict = create_user_tenant_mapping_request_instance.to_dict()
# create an instance of CreateUserTenantMappingRequest from a dict
create_user_tenant_mapping_request_form_dict = create_user_tenant_mapping_request.from_dict(create_user_tenant_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


