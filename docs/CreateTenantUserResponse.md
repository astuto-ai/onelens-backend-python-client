# CreateTenantUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CreateTenantUserResponseStatus**](CreateTenantUserResponseStatus.md) |  | [optional] 
**ol_user_id** | **object** | Unique onelens identifier for the user | 
**role** | [**CreateTenantUserRequestRole**](CreateTenantUserRequestRole.md) |  | [optional] 
**sources** | **List[object]** | Different sources from where user signed up. e.g. social signup, username-password | 
**id** | **object** | PK in the tenant users table | 

## Example

```python
from onelens_backend_client.models.create_tenant_user_response import CreateTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserResponse from a JSON string
create_tenant_user_response_instance = CreateTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTenantUserResponse.to_json())

# convert the object into a dict
create_tenant_user_response_dict = create_tenant_user_response_instance.to_dict()
# create an instance of CreateTenantUserResponse from a dict
create_tenant_user_response_form_dict = create_tenant_user_response.from_dict(create_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


