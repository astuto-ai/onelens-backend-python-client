# GetTenantProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_provider_filter_data** | **object** |  | 
**attributes_data** | **object** |  | 

## Example

```python
from onelens_backend_client.models.get_tenant_providers_response import GetTenantProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantProvidersResponse from a JSON string
get_tenant_providers_response_instance = GetTenantProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantProvidersResponse.to_json())

# convert the object into a dict
get_tenant_providers_response_dict = get_tenant_providers_response_instance.to_dict()
# create an instance of GetTenantProvidersResponse from a dict
get_tenant_providers_response_form_dict = get_tenant_providers_response.from_dict(get_tenant_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


