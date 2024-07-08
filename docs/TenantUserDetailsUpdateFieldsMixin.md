# TenantUserDetailsUpdateFieldsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from onelens_backend_client.models.tenant_user_details_update_fields_mixin import TenantUserDetailsUpdateFieldsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserDetailsUpdateFieldsMixin from a JSON string
tenant_user_details_update_fields_mixin_instance = TenantUserDetailsUpdateFieldsMixin.from_json(json)
# print the JSON string representation of the object
print(TenantUserDetailsUpdateFieldsMixin.to_json())

# convert the object into a dict
tenant_user_details_update_fields_mixin_dict = tenant_user_details_update_fields_mixin_instance.to_dict()
# create an instance of TenantUserDetailsUpdateFieldsMixin from a dict
tenant_user_details_update_fields_mixin_form_dict = tenant_user_details_update_fields_mixin.from_dict(tenant_user_details_update_fields_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


