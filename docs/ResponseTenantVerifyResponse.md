# ResponseTenantVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantVerifyResponse**](TenantVerifyResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_tenant_verify_response import ResponseTenantVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTenantVerifyResponse from a JSON string
response_tenant_verify_response_instance = ResponseTenantVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseTenantVerifyResponse.to_json())

# convert the object into a dict
response_tenant_verify_response_dict = response_tenant_verify_response_instance.to_dict()
# create an instance of ResponseTenantVerifyResponse from a dict
response_tenant_verify_response_form_dict = response_tenant_verify_response.from_dict(response_tenant_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


