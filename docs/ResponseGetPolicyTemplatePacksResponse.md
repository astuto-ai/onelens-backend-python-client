# ResponseGetPolicyTemplatePacksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetPolicyTemplatePacksResponse**](GetPolicyTemplatePacksResponse.md) |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from onelens_backend_client.models.response_get_policy_template_packs_response import ResponseGetPolicyTemplatePacksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetPolicyTemplatePacksResponse from a JSON string
response_get_policy_template_packs_response_instance = ResponseGetPolicyTemplatePacksResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetPolicyTemplatePacksResponse.to_json())

# convert the object into a dict
response_get_policy_template_packs_response_dict = response_get_policy_template_packs_response_instance.to_dict()
# create an instance of ResponseGetPolicyTemplatePacksResponse from a dict
response_get_policy_template_packs_response_form_dict = response_get_policy_template_packs_response.from_dict(response_get_policy_template_packs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


