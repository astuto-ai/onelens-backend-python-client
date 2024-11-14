# GetTenantConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Unique identifier for the tenant | 
**connection_type** | [**ConnectionType**](ConnectionType.md) | Type of the connection | 
**username** | **str** | Username for the connection | 
**password** | **str** | Password for the connection | 
**host** | **str** | Host for the connection | 
**port** | **int** | Port for the connection | 
**database** | **str** | Database name | 
**status** | [**ConnectionStatus**](ConnectionStatus.md) | Status of the connection | 

## Example

```python
from onelens_backend_client.models.get_tenant_connection_response import GetTenantConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantConnectionResponse from a JSON string
get_tenant_connection_response_instance = GetTenantConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantConnectionResponse.to_json())

# convert the object into a dict
get_tenant_connection_response_dict = get_tenant_connection_response_instance.to_dict()
# create an instance of GetTenantConnectionResponse from a dict
get_tenant_connection_response_form_dict = get_tenant_connection_response.from_dict(get_tenant_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


