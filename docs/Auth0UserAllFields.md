# Auth0UserAllFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**identities** | **List[object]** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **str** | The user_id of the user in Auth0. | 
**user_metadata** | **object** |  | [optional] 
**app_metadata** | **object** | The app_metadata of the user in Auth0. | [optional] 
**last_ip** | **str** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**logins_count** | **int** |  | [optional] 

## Example

```python
from onelens_backend_client.models.auth0_user_all_fields import Auth0UserAllFields

# TODO update the JSON string below
json = "{}"
# create an instance of Auth0UserAllFields from a JSON string
auth0_user_all_fields_instance = Auth0UserAllFields.from_json(json)
# print the JSON string representation of the object
print(Auth0UserAllFields.to_json())

# convert the object into a dict
auth0_user_all_fields_dict = auth0_user_all_fields_instance.to_dict()
# create an instance of Auth0UserAllFields from a dict
auth0_user_all_fields_form_dict = auth0_user_all_fields.from_dict(auth0_user_all_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


