# PolicyTemplateServiceActivatePolicyTemplateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ActivatePolicyTemplateRequest**](ActivatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.policy_template_service_activate_policy_template_model import PolicyTemplateServiceActivatePolicyTemplateModel

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateServiceActivatePolicyTemplateModel from a JSON string
policy_template_service_activate_policy_template_model_instance = PolicyTemplateServiceActivatePolicyTemplateModel.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateServiceActivatePolicyTemplateModel.to_json())

# convert the object into a dict
policy_template_service_activate_policy_template_model_dict = policy_template_service_activate_policy_template_model_instance.to_dict()
# create an instance of PolicyTemplateServiceActivatePolicyTemplateModel from a dict
policy_template_service_activate_policy_template_model_form_dict = policy_template_service_activate_policy_template_model.from_dict(policy_template_service_activate_policy_template_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


