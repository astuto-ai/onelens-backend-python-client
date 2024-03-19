# ResponseDeprecatePolicyTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from openapi_client.models.response_deprecate_policy_template_response import ResponseDeprecatePolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDeprecatePolicyTemplateResponse from a JSON string
response_deprecate_policy_template_response_instance = ResponseDeprecatePolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDeprecatePolicyTemplateResponse.to_json())

# convert the object into a dict
response_deprecate_policy_template_response_dict = response_deprecate_policy_template_response_instance.to_dict()
# create an instance of ResponseDeprecatePolicyTemplateResponse from a dict
response_deprecate_policy_template_response_form_dict = response_deprecate_policy_template_response.from_dict(response_deprecate_policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


