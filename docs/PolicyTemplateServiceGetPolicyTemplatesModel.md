# PolicyTemplateServiceGetPolicyTemplatesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPolicyTemplatesRequest**](GetPolicyTemplatesRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.policy_template_service_get_policy_templates_model import PolicyTemplateServiceGetPolicyTemplatesModel

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateServiceGetPolicyTemplatesModel from a JSON string
policy_template_service_get_policy_templates_model_instance = PolicyTemplateServiceGetPolicyTemplatesModel.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateServiceGetPolicyTemplatesModel.to_json())

# convert the object into a dict
policy_template_service_get_policy_templates_model_dict = policy_template_service_get_policy_templates_model_instance.to_dict()
# create an instance of PolicyTemplateServiceGetPolicyTemplatesModel from a dict
policy_template_service_get_policy_templates_model_form_dict = policy_template_service_get_policy_templates_model.from_dict(policy_template_service_get_policy_templates_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


