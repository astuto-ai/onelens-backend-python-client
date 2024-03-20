# CreatePolicyTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreatePolicyTemplateRequest**](CreatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.create_policy_template import CreatePolicyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplate from a JSON string
create_policy_template_instance = CreatePolicyTemplate.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplate.to_json())

# convert the object into a dict
create_policy_template_dict = create_policy_template_instance.to_dict()
# create an instance of CreatePolicyTemplate from a dict
create_policy_template_form_dict = create_policy_template.from_dict(create_policy_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


