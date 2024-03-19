# PolicyTemplateUpdateFieldsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**Title**](Title.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**services** | [**Services**](Services.md) |  | [optional] 
**execution_type** | [**PolicyTemplateUpdateFieldsMixinExecutionType**](PolicyTemplateUpdateFieldsMixinExecutionType.md) |  | [optional] 
**details** | [**PolicyTemplateUpdateFieldsMixinDetails**](PolicyTemplateUpdateFieldsMixinDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_template_update_fields_mixin import PolicyTemplateUpdateFieldsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateUpdateFieldsMixin from a JSON string
policy_template_update_fields_mixin_instance = PolicyTemplateUpdateFieldsMixin.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateUpdateFieldsMixin.to_json())

# convert the object into a dict
policy_template_update_fields_mixin_dict = policy_template_update_fields_mixin_instance.to_dict()
# create an instance of PolicyTemplateUpdateFieldsMixin from a dict
policy_template_update_fields_mixin_form_dict = policy_template_update_fields_mixin.from_dict(policy_template_update_fields_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


