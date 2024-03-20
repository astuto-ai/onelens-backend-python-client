# UpdatePolicyTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdatePolicyTemplateRequest**](UpdatePolicyTemplateRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.update_policy_template import UpdatePolicyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyTemplate from a JSON string
update_policy_template_instance = UpdatePolicyTemplate.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyTemplate.to_json())

# convert the object into a dict
update_policy_template_dict = update_policy_template_instance.to_dict()
# create an instance of UpdatePolicyTemplate from a dict
update_policy_template_form_dict = update_policy_template.from_dict(update_policy_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


