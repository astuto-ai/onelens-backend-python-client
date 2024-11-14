# GetTenantConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Unique identifier for the tenant | 
**connection_type** | **str** | Type of the connection | 

## Example

```python
from onelens_backend_client.models.get_tenant_connection_request import GetTenantConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantConnectionRequest from a JSON string
get_tenant_connection_request_instance = GetTenantConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantConnectionRequest.to_json())

# convert the object into a dict
get_tenant_connection_request_dict = get_tenant_connection_request_instance.to_dict()
# create an instance of GetTenantConnectionRequest from a dict
get_tenant_connection_request_form_dict = get_tenant_connection_request.from_dict(get_tenant_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


