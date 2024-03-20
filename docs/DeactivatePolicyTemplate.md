# DeactivatePolicyTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeactivatePolicyTemplateRequest**](DeactivatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.deactivate_policy_template import DeactivatePolicyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivatePolicyTemplate from a JSON string
deactivate_policy_template_instance = DeactivatePolicyTemplate.from_json(json)
# print the JSON string representation of the object
print(DeactivatePolicyTemplate.to_json())

# convert the object into a dict
deactivate_policy_template_dict = deactivate_policy_template_instance.to_dict()
# create an instance of DeactivatePolicyTemplate from a dict
deactivate_policy_template_form_dict = deactivate_policy_template.from_dict(deactivate_policy_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


