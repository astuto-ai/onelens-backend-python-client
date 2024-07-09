# ResponseCreateAuth0AndOnelensUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAuth0AndOnelensUserResponse**](CreateAuth0AndOnelensUserResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_auth0_and_onelens_user_response import ResponseCreateAuth0AndOnelensUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateAuth0AndOnelensUserResponse from a JSON string
response_create_auth0_and_onelens_user_response_instance = ResponseCreateAuth0AndOnelensUserResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateAuth0AndOnelensUserResponse.to_json())

# convert the object into a dict
response_create_auth0_and_onelens_user_response_dict = response_create_auth0_and_onelens_user_response_instance.to_dict()
# create an instance of ResponseCreateAuth0AndOnelensUserResponse from a dict
response_create_auth0_and_onelens_user_response_form_dict = response_create_auth0_and_onelens_user_response.from_dict(response_create_auth0_and_onelens_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


