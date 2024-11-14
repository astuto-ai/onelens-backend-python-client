# TenantUserUpdateFieldsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**persona** | [**UserPersona**](UserPersona.md) |  | [optional] 
**node_ids** | **List[str]** |  | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_user_update_fields_mixin import TenantUserUpdateFieldsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserUpdateFieldsMixin from a JSON string
tenant_user_update_fields_mixin_instance = TenantUserUpdateFieldsMixin.from_json(json)
# print the JSON string representation of the object
print(TenantUserUpdateFieldsMixin.to_json())

# convert the object into a dict
tenant_user_update_fields_mixin_dict = tenant_user_update_fields_mixin_instance.to_dict()
# create an instance of TenantUserUpdateFieldsMixin from a dict
tenant_user_update_fields_mixin_form_dict = tenant_user_update_fields_mixin.from_dict(tenant_user_update_fields_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


