# UpdateTenantProviderResponse


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
**state** | **str** | state | 

## Example

```python
from onelens_backend_client.models.update_tenant_provider_response import UpdateTenantProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantProviderResponse from a JSON string
update_tenant_provider_response_instance = UpdateTenantProviderResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantProviderResponse.to_json())

# convert the object into a dict
update_tenant_provider_response_dict = update_tenant_provider_response_instance.to_dict()
# create an instance of UpdateTenantProviderResponse from a dict
update_tenant_provider_response_form_dict = update_tenant_provider_response.from_dict(update_tenant_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


