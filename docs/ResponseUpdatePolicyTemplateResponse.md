# ResponseUpdatePolicyTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdatePolicyTemplateResponse**](UpdatePolicyTemplateResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_update_policy_template_response import ResponseUpdatePolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdatePolicyTemplateResponse from a JSON string
response_update_policy_template_response_instance = ResponseUpdatePolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdatePolicyTemplateResponse.to_json())

# convert the object into a dict
response_update_policy_template_response_dict = response_update_policy_template_response_instance.to_dict()
# create an instance of ResponseUpdatePolicyTemplateResponse from a dict
response_update_policy_template_response_form_dict = response_update_policy_template_response.from_dict(response_update_policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


