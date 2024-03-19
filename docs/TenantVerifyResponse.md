# TenantVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** | verified status | 
**accounts** | **object** | accounts | 

## Example

```python
from openapi_client.models.tenant_verify_response import TenantVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyResponse from a JSON string
tenant_verify_response_instance = TenantVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyResponse.to_json())

# convert the object into a dict
tenant_verify_response_dict = tenant_verify_response_instance.to_dict()
# create an instance of TenantVerifyResponse from a dict
tenant_verify_response_form_dict = tenant_verify_response.from_dict(tenant_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


