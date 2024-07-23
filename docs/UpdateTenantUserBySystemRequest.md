# UpdateTenantUserBySystemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_login** | **datetime** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**mobile_country_code** | **str** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**persona** | [**UserPersona**](UserPersona.md) |  | [optional] 
**job_title** | **str** |  | [optional] 
**manager** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**display_language** | **str** |  | [optional] 
**preferred_currency** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**display_date_format** | **str** |  | [optional] 
**display_time_format** | **str** |  | [optional] 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.update_tenant_user_by_system_request import UpdateTenantUserBySystemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantUserBySystemRequest from a JSON string
update_tenant_user_by_system_request_instance = UpdateTenantUserBySystemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantUserBySystemRequest.to_json())

# convert the object into a dict
update_tenant_user_by_system_request_dict = update_tenant_user_by_system_request_instance.to_dict()
# create an instance of UpdateTenantUserBySystemRequest from a dict
update_tenant_user_by_system_request_form_dict = update_tenant_user_by_system_request.from_dict(update_tenant_user_by_system_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


