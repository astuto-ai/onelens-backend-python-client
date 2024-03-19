# PolicyTemplateServiceUpdatePolicyTemplateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdatePolicyTemplateRequest**](UpdatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.policy_template_service_update_policy_template_model import PolicyTemplateServiceUpdatePolicyTemplateModel

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateServiceUpdatePolicyTemplateModel from a JSON string
policy_template_service_update_policy_template_model_instance = PolicyTemplateServiceUpdatePolicyTemplateModel.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateServiceUpdatePolicyTemplateModel.to_json())

# convert the object into a dict
policy_template_service_update_policy_template_model_dict = policy_template_service_update_policy_template_model_instance.to_dict()
# create an instance of PolicyTemplateServiceUpdatePolicyTemplateModel from a dict
policy_template_service_update_policy_template_model_form_dict = policy_template_service_update_policy_template_model.from_dict(policy_template_service_update_policy_template_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


