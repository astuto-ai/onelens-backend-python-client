# GetTenantUserByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_tenant_user_by_id_request import GetTenantUserByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUserByIDRequest from a JSON string
get_tenant_user_by_id_request_instance = GetTenantUserByIDRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantUserByIDRequest.to_json())

# convert the object into a dict
get_tenant_user_by_id_request_dict = get_tenant_user_by_id_request_instance.to_dict()
# create an instance of GetTenantUserByIDRequest from a dict
get_tenant_user_by_id_request_form_dict = get_tenant_user_by_id_request.from_dict(get_tenant_user_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


