# ResponseGetTenantProviderByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantProviderByIDResponse**](GetTenantProviderByIDResponse.md) |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from openapi_client.models.response_get_tenant_provider_by_id_response import ResponseGetTenantProviderByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantProviderByIDResponse from a JSON string
response_get_tenant_provider_by_id_response_instance = ResponseGetTenantProviderByIDResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantProviderByIDResponse.to_json())

# convert the object into a dict
response_get_tenant_provider_by_id_response_dict = response_get_tenant_provider_by_id_response_instance.to_dict()
# create an instance of ResponseGetTenantProviderByIDResponse from a dict
response_get_tenant_provider_by_id_response_form_dict = response_get_tenant_provider_by_id_response.from_dict(response_get_tenant_provider_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


