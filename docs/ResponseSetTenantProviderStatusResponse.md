# ResponseSetTenantProviderStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_set_tenant_provider_status_response import ResponseSetTenantProviderStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSetTenantProviderStatusResponse from a JSON string
response_set_tenant_provider_status_response_instance = ResponseSetTenantProviderStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseSetTenantProviderStatusResponse.to_json())

# convert the object into a dict
response_set_tenant_provider_status_response_dict = response_set_tenant_provider_status_response_instance.to_dict()
# create an instance of ResponseSetTenantProviderStatusResponse from a dict
response_set_tenant_provider_status_response_form_dict = response_set_tenant_provider_status_response.from_dict(response_set_tenant_provider_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


