# TenantVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Role name of the tenant | 

## Example

```python
from onelens_backend_client.models.tenant_verify_request import TenantVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyRequest from a JSON string
tenant_verify_request_instance = TenantVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyRequest.to_json())

# convert the object into a dict
tenant_verify_request_dict = tenant_verify_request_instance.to_dict()
# create an instance of TenantVerifyRequest from a dict
tenant_verify_request_form_dict = tenant_verify_request.from_dict(tenant_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


