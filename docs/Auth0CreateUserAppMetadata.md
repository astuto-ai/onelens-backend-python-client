# Auth0CreateUserAppMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) | The role of the user in Auth0. | 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.auth0_create_user_app_metadata import Auth0CreateUserAppMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of Auth0CreateUserAppMetadata from a JSON string
auth0_create_user_app_metadata_instance = Auth0CreateUserAppMetadata.from_json(json)
# print the JSON string representation of the object
print(Auth0CreateUserAppMetadata.to_json())

# convert the object into a dict
auth0_create_user_app_metadata_dict = auth0_create_user_app_metadata_instance.to_dict()
# create an instance of Auth0CreateUserAppMetadata from a dict
auth0_create_user_app_metadata_form_dict = auth0_create_user_app_metadata.from_dict(auth0_create_user_app_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


