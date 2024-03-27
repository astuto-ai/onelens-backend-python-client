# ResponseActivatePolicyTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_activate_policy_template_response import ResponseActivatePolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseActivatePolicyTemplateResponse from a JSON string
response_activate_policy_template_response_instance = ResponseActivatePolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseActivatePolicyTemplateResponse.to_json())

# convert the object into a dict
response_activate_policy_template_response_dict = response_activate_policy_template_response_instance.to_dict()
# create an instance of ResponseActivatePolicyTemplateResponse from a dict
response_activate_policy_template_response_form_dict = response_activate_policy_template_response.from_dict(response_activate_policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


