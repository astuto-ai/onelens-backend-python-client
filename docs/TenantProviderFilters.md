# TenantProviderFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_ids** | [**TenantIds**](TenantIds.md) |  | [optional] 
**cloud_ids** | [**CloudIds**](CloudIds.md) |  | [optional] 
**cloud_providers** | [**CloudProviders**](CloudProviders.md) |  | [optional] 
**parent_ids** | [**ParentIds**](ParentIds.md) |  | [optional] 
**is_parent_account** | [**IsParentAccount**](IsParentAccount.md) |  | [optional] 
**is_verified** | [**IsVerified**](IsVerified.md) |  | [optional] 
**states** | [**States**](States.md) |  | [optional] 

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


