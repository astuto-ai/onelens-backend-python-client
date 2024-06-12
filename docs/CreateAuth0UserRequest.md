# CreateAuth0UserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the user in Auth0. | 
**password** | **str** | The password of the user in Auth0. | 
**email_verified** | **bool** |  | [optional] 
**app_metadata** | [**Auth0CreateUserAppMetadata**](Auth0CreateUserAppMetadata.md) | The app_metadata of the user in Auth0. | 
**connection** | [**Auth0UserConnection**](Auth0UserConnection.md) | The connection of the user in Auth0. | 

## Example

```python
from onelens_backend_client.models.create_auth0_user_request import CreateAuth0UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuth0UserRequest from a JSON string
create_auth0_user_request_instance = CreateAuth0UserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAuth0UserRequest.to_json())

# convert the object into a dict
create_auth0_user_request_dict = create_auth0_user_request_instance.to_dict()
# create an instance of CreateAuth0UserRequest from a dict
create_auth0_user_request_form_dict = create_auth0_user_request.from_dict(create_auth0_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


