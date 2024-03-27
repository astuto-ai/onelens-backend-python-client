# TenantProviderFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_ids** | **object** |  | [optional] 
**cloud_ids** | **object** |  | [optional] 
**cloud_providers** | **object** |  | [optional] 
**parent_ids** | **object** |  | [optional] 
**is_parent_account** | **bool** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**states** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_provider_filters import TenantProviderFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantProviderFilters from a JSON string
tenant_provider_filters_instance = TenantProviderFilters.from_json(json)
# print the JSON string representation of the object
print(TenantProviderFilters.to_json())

# convert the object into a dict
tenant_provider_filters_dict = tenant_provider_filters_instance.to_dict()
# create an instance of TenantProviderFilters from a dict
tenant_provider_filters_form_dict = tenant_provider_filters.from_dict(tenant_provider_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


