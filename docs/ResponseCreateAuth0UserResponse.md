# ResponseCreateAuth0UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAuth0UserResponse**](CreateAuth0UserResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_auth0_user_response import ResponseCreateAuth0UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateAuth0UserResponse from a JSON string
response_create_auth0_user_response_instance = ResponseCreateAuth0UserResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateAuth0UserResponse.to_json())

# convert the object into a dict
response_create_auth0_user_response_dict = response_create_auth0_user_response_instance.to_dict()
# create an instance of ResponseCreateAuth0UserResponse from a dict
response_create_auth0_user_response_form_dict = response_create_auth0_user_response.from_dict(response_create_auth0_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


