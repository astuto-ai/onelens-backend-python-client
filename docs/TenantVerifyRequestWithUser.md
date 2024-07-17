# TenantVerifyRequestWithUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Role name of the tenant | 
**tenant_id** | **str** | Tenant ID | 
**tenant_provider_id** | **str** | Tenant Provider ID | 
**storage_lens_config** | [**StorageLensConfig**](StorageLensConfig.md) |  | [optional] 
**user_id** | **str** | List of users | 

## Example

```python
from onelens_backend_client.models.tenant_verify_request_with_user import TenantVerifyRequestWithUser

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyRequestWithUser from a JSON string
tenant_verify_request_with_user_instance = TenantVerifyRequestWithUser.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyRequestWithUser.to_json())

# convert the object into a dict
tenant_verify_request_with_user_dict = tenant_verify_request_with_user_instance.to_dict()
# create an instance of TenantVerifyRequestWithUser from a dict
tenant_verify_request_with_user_form_dict = tenant_verify_request_with_user.from_dict(tenant_verify_request_with_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


