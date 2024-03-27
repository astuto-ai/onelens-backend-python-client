# ResponseUpdateTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTenantResponse**](UpdateTenantResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_update_tenant_response import ResponseUpdateTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateTenantResponse from a JSON string
response_update_tenant_response_instance = ResponseUpdateTenantResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateTenantResponse.to_json())

# convert the object into a dict
response_update_tenant_response_dict = response_update_tenant_response_instance.to_dict()
# create an instance of ResponseUpdateTenantResponse from a dict
response_update_tenant_response_form_dict = response_update_tenant_response.from_dict(response_update_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


