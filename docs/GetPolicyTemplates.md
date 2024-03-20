# GetPolicyTemplates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPolicyTemplatesRequest**](GetPolicyTemplatesRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_policy_templates import GetPolicyTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplates from a JSON string
get_policy_templates_instance = GetPolicyTemplates.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplates.to_json())

# convert the object into a dict
get_policy_templates_dict = get_policy_templates_instance.to_dict()
# create an instance of GetPolicyTemplates from a dict
get_policy_templates_form_dict = get_policy_templates.from_dict(get_policy_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


