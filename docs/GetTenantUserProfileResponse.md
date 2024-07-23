# GetTenantUserProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_pic_url** | [**ProfilePicUrl**](ProfilePicUrl.md) |  | [optional] 
**last_login** | [**LastLogin**](LastLogin.md) |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) | Status of the user like ACTIVE, BLOCKED etc. | [optional] 
**first_name** | [**FirstName**](FirstName.md) |  | 
**middle_name** | [**MiddleName**](MiddleName.md) |  | [optional] 
**last_name** | [**LastName**](LastName.md) |  | 
**email** | [**Email**](Email.md) |  | [optional] 
**mobile_country_code** | [**MobileCountryCode**](MobileCountryCode.md) |  | [optional] 
**mobile_number** | [**MobileNumber**](MobileNumber.md) |  | [optional] 
**persona** | [**CreateTenantUserRequestPersona**](CreateTenantUserRequestPersona.md) |  | [optional] 
**role** | [**UserRole**](UserRole.md) | Role of the user in the tenant | [optional] 
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
**sources** | [**Sources**](Sources.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**ol_user_id** | **object** | Unique onelens identifier for the user | 

## Example

```python
from onelens_backend_client.models.get_tenant_user_profile_response import GetTenantUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUserProfileResponse from a JSON string
get_tenant_user_profile_response_instance = GetTenantUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantUserProfileResponse.to_json())

# convert the object into a dict
get_tenant_user_profile_response_dict = get_tenant_user_profile_response_instance.to_dict()
# create an instance of GetTenantUserProfileResponse from a dict
get_tenant_user_profile_response_form_dict = get_tenant_user_profile_response.from_dict(get_tenant_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


