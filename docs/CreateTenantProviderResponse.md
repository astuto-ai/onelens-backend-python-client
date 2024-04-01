# CreateTenantProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | Cloud provider | 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | **object** | provider config | 
**id** | **str** | Unique ID for the Tenant Provider | 
**is_parent_account** | **bool** | billing account | 
**is_verified** | **bool** | is verified | 
**state** | [**TenantProviderState**](TenantProviderState.md) | state | 

## Example

```python
from onelens_backend_client.models.create_tenant_provider_response import CreateTenantProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantProviderResponse from a JSON string
create_tenant_provider_response_instance = CreateTenantProviderResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTenantProviderResponse.to_json())

# convert the object into a dict
create_tenant_provider_response_dict = create_tenant_provider_response_instance.to_dict()
# create an instance of CreateTenantProviderResponse from a dict
create_tenant_provider_response_form_dict = create_tenant_provider_response.from_dict(create_tenant_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


