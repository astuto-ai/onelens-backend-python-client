# ResponseCreatePolicyTemplatePackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreatePolicyTemplatePackResponse**](CreatePolicyTemplatePackResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_policy_template_pack_response import ResponseCreatePolicyTemplatePackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreatePolicyTemplatePackResponse from a JSON string
response_create_policy_template_pack_response_instance = ResponseCreatePolicyTemplatePackResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreatePolicyTemplatePackResponse.to_json())

# convert the object into a dict
response_create_policy_template_pack_response_dict = response_create_policy_template_pack_response_instance.to_dict()
# create an instance of ResponseCreatePolicyTemplatePackResponse from a dict
response_create_policy_template_pack_response_form_dict = response_create_policy_template_pack_response.from_dict(response_create_policy_template_pack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


