# ResponsePasswordChangeEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PasswordChangeEmailResponse**](PasswordChangeEmailResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_password_change_email_response import ResponsePasswordChangeEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsePasswordChangeEmailResponse from a JSON string
response_password_change_email_response_instance = ResponsePasswordChangeEmailResponse.from_json(json)
# print the JSON string representation of the object
print(ResponsePasswordChangeEmailResponse.to_json())

# convert the object into a dict
response_password_change_email_response_dict = response_password_change_email_response_instance.to_dict()
# create an instance of ResponsePasswordChangeEmailResponse from a dict
response_password_change_email_response_form_dict = response_password_change_email_response.from_dict(response_password_change_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


