# ResponseDisableTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from openapi_client.models.response_disable_tenant_response import ResponseDisableTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDisableTenantResponse from a JSON string
response_disable_tenant_response_instance = ResponseDisableTenantResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDisableTenantResponse.to_json())

# convert the object into a dict
response_disable_tenant_response_dict = response_disable_tenant_response_instance.to_dict()
# create an instance of ResponseDisableTenantResponse from a dict
response_disable_tenant_response_form_dict = response_disable_tenant_response.from_dict(response_disable_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


