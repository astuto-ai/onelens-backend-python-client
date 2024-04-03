# TenantProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | Cloud provider | 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | **object** | provider config | 
**id** | **str** | Unique ID for the Tenant Provider | 
**is_parent_account** | **bool** | billing account | 
**tenant_id** | **str** | Tenant ID | 
**is_verified** | **bool** | is verified | 
**state** | [**TenantProviderState**](TenantProviderState.md) | state | 

## Example

```python
from onelens_backend_client.models.tenant_provider import TenantProvider

# TODO update the JSON string below
json = "{}"
# create an instance of TenantProvider from a JSON string
tenant_provider_instance = TenantProvider.from_json(json)
# print the JSON string representation of the object
print(TenantProvider.to_json())

# convert the object into a dict
tenant_provider_dict = tenant_provider_instance.to_dict()
# create an instance of TenantProvider from a dict
tenant_provider_form_dict = tenant_provider.from_dict(tenant_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


