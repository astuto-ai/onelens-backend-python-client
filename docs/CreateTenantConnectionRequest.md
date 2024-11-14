# CreateTenantConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | database connection string | 
**tenant_id** | **str** | Unique identifier for the tenant | 
**connection_type** | **str** | Type of the connection | 

## Example

```python
from onelens_backend_client.models.create_tenant_connection_request import CreateTenantConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantConnectionRequest from a JSON string
create_tenant_connection_request_instance = CreateTenantConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantConnectionRequest.to_json())

# convert the object into a dict
create_tenant_connection_request_dict = create_tenant_connection_request_instance.to_dict()
# create an instance of CreateTenantConnectionRequest from a dict
create_tenant_connection_request_form_dict = create_tenant_connection_request.from_dict(create_tenant_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


