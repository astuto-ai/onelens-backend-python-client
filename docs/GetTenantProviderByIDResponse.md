# GetTenantProviderByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | Cloud provider | 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | [**ProviderConfigOutput**](ProviderConfigOutput.md) |  | 
**id** | **str** | Unique ID for the Tenant Provider | 
**is_parent_account** | **bool** | billing account | 
**tenant_id** | **str** | Tenant ID | 
**is_billing_account** | **bool** | is billing account | 
**is_verified** | **bool** | is verified | 
**state** | [**TenantProviderState**](TenantProviderState.md) | State of the tenant | 

## Example

```python
from onelens_backend_client.models.get_tenant_provider_by_id_response import GetTenantProviderByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantProviderByIDResponse from a JSON string
get_tenant_provider_by_id_response_instance = GetTenantProviderByIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantProviderByIDResponse.to_json())

# convert the object into a dict
get_tenant_provider_by_id_response_dict = get_tenant_provider_by_id_response_instance.to_dict()
# create an instance of GetTenantProviderByIDResponse from a dict
get_tenant_provider_by_id_response_form_dict = get_tenant_provider_by_id_response.from_dict(get_tenant_provider_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


