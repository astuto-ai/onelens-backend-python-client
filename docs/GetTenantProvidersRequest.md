# GetTenantProvidersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**TenantProviderFilters**](TenantProviderFilters.md) | Filters to apply to the policy templates. | [optional] 
**attributes** | [**List[TenantProviderAttributes]**](TenantProviderAttributes.md) | List of items to be returned in the response | [optional] [default to []]

## Example

```python
from openapi_client.models.get_tenant_providers_request import GetTenantProvidersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantProvidersRequest from a JSON string
get_tenant_providers_request_instance = GetTenantProvidersRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantProvidersRequest.to_json())

# convert the object into a dict
get_tenant_providers_request_dict = get_tenant_providers_request_instance.to_dict()
# create an instance of GetTenantProvidersRequest from a dict
get_tenant_providers_request_form_dict = get_tenant_providers_request.from_dict(get_tenant_providers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


