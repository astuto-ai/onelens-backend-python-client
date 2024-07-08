# CreateTenantUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **object** | Unique onelens identifier for the user | 
**first_name** | [**FirstName**](FirstName.md) |  | 
**middle_name** | [**MiddleName**](MiddleName.md) |  | [optional] 
**last_name** | [**LastName**](LastName.md) |  | 
**email** | [**Email**](Email.md) |  | [optional] 
**mobile_country_code** | [**MobileCountryCode**](MobileCountryCode.md) |  | [optional] 
**mobile_number** | [**MobileNumber**](MobileNumber.md) |  | [optional] 
**persona** | [**BaseUserPersona**](BaseUserPersona.md) |  | [optional] 
**role** | [**BaseUserRole**](BaseUserRole.md) |  | [optional] 
**job_title** | [**JobTitle**](JobTitle.md) |  | [optional] 
**manager** | [**Manager**](Manager.md) |  | [optional] 
**city** | [**City**](City.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**display_language** | [**DisplayLanguage**](DisplayLanguage.md) |  | [optional] 
**preferred_currency** | [**PreferredCurrency**](PreferredCurrency.md) |  | [optional] 
**timezone** | [**Timezone**](Timezone.md) |  | [optional] 
**display_date_format** | [**DisplayDateFormat**](DisplayDateFormat.md) |  | [optional] 
**display_time_format** | [**DisplayTimeFormat**](DisplayTimeFormat.md) |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) | Status of the user like ACTIVE, BLOCKED etc. | [optional] 
**sources** | **List[object]** | Different sources from where user signed up. e.g. social signup, username-password | 

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


