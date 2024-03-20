# DisableTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DisableTenantRequest**](DisableTenantRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.disable_tenant_request import DisableTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenantRequest from a JSON string
disable_tenant_request_instance = DisableTenantRequest.from_json(json)
# print the JSON string representation of the object
print(DisableTenantRequest.to_json())

# convert the object into a dict
disable_tenant_request_dict = disable_tenant_request_instance.to_dict()
# create an instance of DisableTenantRequest from a dict
disable_tenant_request_form_dict = disable_tenant_request.from_dict(disable_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


