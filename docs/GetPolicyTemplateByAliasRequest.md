# GetPolicyTemplateByAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The alias of the policy template. | 

## Example

```python
from onelens_backend_client.models.get_policy_template_by_alias_request import GetPolicyTemplateByAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplateByAliasRequest from a JSON string
get_policy_template_by_alias_request_instance = GetPolicyTemplateByAliasRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplateByAliasRequest.to_json())

# convert the object into a dict
get_policy_template_by_alias_request_dict = get_policy_template_by_alias_request_instance.to_dict()
# create an instance of GetPolicyTemplateByAliasRequest from a dict
get_policy_template_by_alias_request_form_dict = get_policy_template_by_alias_request.from_dict(get_policy_template_by_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


