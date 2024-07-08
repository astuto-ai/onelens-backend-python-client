# EnableTenantUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.enable_tenant_user_request import EnableTenantUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableTenantUserRequest from a JSON string
enable_tenant_user_request_instance = EnableTenantUserRequest.from_json(json)
# print the JSON string representation of the object
print(EnableTenantUserRequest.to_json())

# convert the object into a dict
enable_tenant_user_request_dict = enable_tenant_user_request_instance.to_dict()
# create an instance of EnableTenantUserRequest from a dict
enable_tenant_user_request_form_dict = enable_tenant_user_request.from_dict(enable_tenant_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


