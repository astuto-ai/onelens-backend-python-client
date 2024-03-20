# GetTenantByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetTenantByIDRequest**](GetTenantByIDRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_tenant_by_id_request import GetTenantByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantByIdRequest from a JSON string
get_tenant_by_id_request_instance = GetTenantByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantByIdRequest.to_json())

# convert the object into a dict
get_tenant_by_id_request_dict = get_tenant_by_id_request_instance.to_dict()
# create an instance of GetTenantByIdRequest from a dict
get_tenant_by_id_request_form_dict = get_tenant_by_id_request.from_dict(get_tenant_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


