# UpdateTenantUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**sources** | **List[str]** | Different sources from where user signed up. e.g. social signup, username-password | 
**id** | **str** | PK in the tenant users table | 

## Example

```python
from onelens_backend_client.models.update_tenant_user_response import UpdateTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantUserResponse from a JSON string
update_tenant_user_response_instance = UpdateTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantUserResponse.to_json())

# convert the object into a dict
update_tenant_user_response_dict = update_tenant_user_response_instance.to_dict()
# create an instance of UpdateTenantUserResponse from a dict
update_tenant_user_response_form_dict = update_tenant_user_response.from_dict(update_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


