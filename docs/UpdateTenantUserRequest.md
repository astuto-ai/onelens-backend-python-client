# UpdateTenantUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**persona** | [**UserPersona**](UserPersona.md) |  | [optional] 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.update_tenant_user_request import UpdateTenantUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantUserRequest from a JSON string
update_tenant_user_request_instance = UpdateTenantUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantUserRequest.to_json())

# convert the object into a dict
update_tenant_user_request_dict = update_tenant_user_request_instance.to_dict()
# create an instance of UpdateTenantUserRequest from a dict
update_tenant_user_request_form_dict = update_tenant_user_request.from_dict(update_tenant_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


