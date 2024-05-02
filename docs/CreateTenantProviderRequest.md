# CreateTenantProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | Cloud provider | 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | [**ProviderConfigInput**](ProviderConfigInput.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_tenant_provider_request import CreateTenantProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantProviderRequest from a JSON string
create_tenant_provider_request_instance = CreateTenantProviderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantProviderRequest.to_json())

# convert the object into a dict
create_tenant_provider_request_dict = create_tenant_provider_request_instance.to_dict()
# create an instance of CreateTenantProviderRequest from a dict
create_tenant_provider_request_form_dict = create_tenant_provider_request.from_dict(create_tenant_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


