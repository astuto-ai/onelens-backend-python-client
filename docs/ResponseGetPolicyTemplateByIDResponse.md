# ResponseGetPolicyTemplateByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetPolicyTemplateByIDResponse**](GetPolicyTemplateByIDResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_policy_template_by_id_response import ResponseGetPolicyTemplateByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetPolicyTemplateByIDResponse from a JSON string
response_get_policy_template_by_id_response_instance = ResponseGetPolicyTemplateByIDResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetPolicyTemplateByIDResponse.to_json())

# convert the object into a dict
response_get_policy_template_by_id_response_dict = response_get_policy_template_by_id_response_instance.to_dict()
# create an instance of ResponseGetPolicyTemplateByIDResponse from a dict
response_get_policy_template_by_id_response_form_dict = response_get_policy_template_by_id_response.from_dict(response_get_policy_template_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


