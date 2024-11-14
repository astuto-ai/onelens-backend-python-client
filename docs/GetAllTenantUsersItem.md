# GetAllTenantUsersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_pic_url** | [**ProfilePicUrl**](ProfilePicUrl.md) |  | [optional] 
**last_login** | [**LastLogin**](LastLogin.md) |  | [optional] 
**first_name** | [**FirstName**](FirstName.md) |  | 
**middle_name** | [**MiddleName**](MiddleName.md) |  | [optional] 
**last_name** | [**LastName**](LastName.md) |  | 
**email** | [**Email**](Email.md) |  | [optional] 
**mobile_country_code** | [**MobileCountryCode**](MobileCountryCode.md) |  | [optional] 
**mobile_number** | [**MobileNumber**](MobileNumber.md) |  | [optional] 
**persona** | [**BaseUserPersona**](BaseUserPersona.md) |  | [optional] 
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
**status** | [**UserStatus**](UserStatus.md) | Status of the user like ACTIVE, BLOCKED etc. | [optional] 
**sources** | [**Sources**](Sources.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**node_ids** | **List[object]** | Hierarchy node ids(cost centers) the user has access to. | 
**ol_user_id** | **object** | Unique onelens identifier for the user | 
**nodes** | [**List[HierarchyNodeEntityWithDetails]**](HierarchyNodeEntityWithDetails.md) | Hierarchy nodes&#39; details the user has access to | 
**action_level** | [**TenantUserActionLevel**](TenantUserActionLevel.md) | Action that can be performed on this user | 

## Example

```python
from onelens_backend_client.models.get_all_tenant_users_item import GetAllTenantUsersItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTenantUsersItem from a JSON string
get_all_tenant_users_item_instance = GetAllTenantUsersItem.from_json(json)
# print the JSON string representation of the object
print(GetAllTenantUsersItem.to_json())

# convert the object into a dict
get_all_tenant_users_item_dict = get_all_tenant_users_item_instance.to_dict()
# create an instance of GetAllTenantUsersItem from a dict
get_all_tenant_users_item_form_dict = get_all_tenant_users_item.from_dict(get_all_tenant_users_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


