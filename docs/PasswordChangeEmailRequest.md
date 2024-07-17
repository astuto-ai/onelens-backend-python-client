# PasswordChangeEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.password_change_email_request import PasswordChangeEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChangeEmailRequest from a JSON string
password_change_email_request_instance = PasswordChangeEmailRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordChangeEmailRequest.to_json())

# convert the object into a dict
password_change_email_request_dict = password_change_email_request_instance.to_dict()
# create an instance of PasswordChangeEmailRequest from a dict
password_change_email_request_form_dict = password_change_email_request.from_dict(password_change_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


