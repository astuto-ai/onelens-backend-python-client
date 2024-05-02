# UpdateTenantProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | [optional] 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | [**ProviderConfigInput**](ProviderConfigInput.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_provider_request import UpdateTenantProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantProviderRequest from a JSON string
update_tenant_provider_request_instance = UpdateTenantProviderRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantProviderRequest.to_json())

# convert the object into a dict
update_tenant_provider_request_dict = update_tenant_provider_request_instance.to_dict()
# create an instance of UpdateTenantProviderRequest from a dict
update_tenant_provider_request_form_dict = update_tenant_provider_request.from_dict(update_tenant_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


