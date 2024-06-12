# CreateAuth0UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0_data** | **object** | The data of the user in Auth0. | 
**onelens_data** | [**CreateUserResponse**](CreateUserResponse.md) | The data of the user in onelens. | 

## Example

```python
from onelens_backend_client.models.create_auth0_user_response import CreateAuth0UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuth0UserResponse from a JSON string
create_auth0_user_response_instance = CreateAuth0UserResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAuth0UserResponse.to_json())

# convert the object into a dict
create_auth0_user_response_dict = create_auth0_user_response_instance.to_dict()
# create an instance of CreateAuth0UserResponse from a dict
create_auth0_user_response_form_dict = create_auth0_user_response.from_dict(create_auth0_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


