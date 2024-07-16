# PasswordChangeEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message for password change email response | 

## Example

```python
from onelens_backend_client.models.password_change_email_response import PasswordChangeEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChangeEmailResponse from a JSON string
password_change_email_response_instance = PasswordChangeEmailResponse.from_json(json)
# print the JSON string representation of the object
print(PasswordChangeEmailResponse.to_json())

# convert the object into a dict
password_change_email_response_dict = password_change_email_response_instance.to_dict()
# create an instance of PasswordChangeEmailResponse from a dict
password_change_email_response_form_dict = password_change_email_response.from_dict(password_change_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


