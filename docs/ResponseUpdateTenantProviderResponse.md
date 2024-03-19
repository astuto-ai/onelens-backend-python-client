# ResponseUpdateTenantProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTenantProviderResponse**](UpdateTenantProviderResponse.md) |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from openapi_client.models.response_update_tenant_provider_response import ResponseUpdateTenantProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateTenantProviderResponse from a JSON string
response_update_tenant_provider_response_instance = ResponseUpdateTenantProviderResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateTenantProviderResponse.to_json())

# convert the object into a dict
response_update_tenant_provider_response_dict = response_update_tenant_provider_response_instance.to_dict()
# create an instance of ResponseUpdateTenantProviderResponse from a dict
response_update_tenant_provider_response_form_dict = response_update_tenant_provider_response.from_dict(response_update_tenant_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


