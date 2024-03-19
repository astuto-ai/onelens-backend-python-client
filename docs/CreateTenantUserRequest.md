# CreateTenantUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**role** | [**CreateTenantUserRequestRole**](CreateTenantUserRequestRole.md) |  | [optional] 
**sources** | **List[str]** | Different sources from where user signed up. e.g. social signup, username-password | 

## Example

```python
from onelens_backend_client.models.create_tenant_user_request import CreateTenantUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserRequest from a JSON string
create_tenant_user_request_instance = CreateTenantUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantUserRequest.to_json())

# convert the object into a dict
create_tenant_user_request_dict = create_tenant_user_request_instance.to_dict()
# create an instance of CreateTenantUserRequest from a dict
create_tenant_user_request_form_dict = create_tenant_user_request.from_dict(create_tenant_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


