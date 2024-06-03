# ResponseCreateUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateUserResponse**](CreateUserResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_user_response import ResponseCreateUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateUserResponse from a JSON string
response_create_user_response_instance = ResponseCreateUserResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateUserResponse.to_json())

# convert the object into a dict
response_create_user_response_dict = response_create_user_response_instance.to_dict()
# create an instance of ResponseCreateUserResponse from a dict
response_create_user_response_form_dict = response_create_user_response.from_dict(response_create_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


