# ActivatePolicyTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ActivatePolicyTemplateRequest**](ActivatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.activate_policy_template import ActivatePolicyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ActivatePolicyTemplate from a JSON string
activate_policy_template_instance = ActivatePolicyTemplate.from_json(json)
# print the JSON string representation of the object
print(ActivatePolicyTemplate.to_json())

# convert the object into a dict
activate_policy_template_dict = activate_policy_template_instance.to_dict()
# create an instance of ActivatePolicyTemplate from a dict
activate_policy_template_form_dict = activate_policy_template.from_dict(activate_policy_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


