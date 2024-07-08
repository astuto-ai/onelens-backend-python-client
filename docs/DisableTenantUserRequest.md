# DisableTenantUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.disable_tenant_user_request import DisableTenantUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenantUserRequest from a JSON string
disable_tenant_user_request_instance = DisableTenantUserRequest.from_json(json)
# print the JSON string representation of the object
print(DisableTenantUserRequest.to_json())

# convert the object into a dict
disable_tenant_user_request_dict = disable_tenant_user_request_instance.to_dict()
# create an instance of DisableTenantUserRequest from a dict
disable_tenant_user_request_form_dict = disable_tenant_user_request.from_dict(disable_tenant_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


