# SetTenantStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the tenant | 

## Example

```python
from onelens_backend_client.models.set_tenant_status_request import SetTenantStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTenantStatusRequest from a JSON string
set_tenant_status_request_instance = SetTenantStatusRequest.from_json(json)
# print the JSON string representation of the object
print(SetTenantStatusRequest.to_json())

# convert the object into a dict
set_tenant_status_request_dict = set_tenant_status_request_instance.to_dict()
# create an instance of SetTenantStatusRequest from a dict
set_tenant_status_request_form_dict = set_tenant_status_request.from_dict(set_tenant_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


