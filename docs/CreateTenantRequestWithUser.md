# CreateTenantRequestWithUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tenant | 
**domains** | **List[str]** | List of domains associated with the tenant | 
**org_id** | **str** | Organization id of the tenant | 
**timezone** | **str** | Timezone of the tenant | 
**user_id** | **str** | Unique identifier for the user in onelens | 

## Example

```python
from onelens_backend_client.models.create_tenant_request_with_user import CreateTenantRequestWithUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantRequestWithUser from a JSON string
create_tenant_request_with_user_instance = CreateTenantRequestWithUser.from_json(json)
# print the JSON string representation of the object
print(CreateTenantRequestWithUser.to_json())

# convert the object into a dict
create_tenant_request_with_user_dict = create_tenant_request_with_user_instance.to_dict()
# create an instance of CreateTenantRequestWithUser from a dict
create_tenant_request_with_user_form_dict = create_tenant_request_with_user.from_dict(create_tenant_request_with_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


