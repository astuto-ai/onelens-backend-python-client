# GetTenantProviderByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Tenant Provider | 
**tenant_id** | **str** | Tenant ID | 

## Example

```python
from onelens_backend_client.models.get_tenant_provider_by_id_request import GetTenantProviderByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantProviderByIDRequest from a JSON string
get_tenant_provider_by_id_request_instance = GetTenantProviderByIDRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantProviderByIDRequest.to_json())

# convert the object into a dict
get_tenant_provider_by_id_request_dict = get_tenant_provider_by_id_request_instance.to_dict()
# create an instance of GetTenantProviderByIDRequest from a dict
get_tenant_provider_by_id_request_form_dict = get_tenant_provider_by_id_request.from_dict(get_tenant_provider_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


