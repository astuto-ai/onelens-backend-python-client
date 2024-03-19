# PolicyTemplateUpdateFieldsMixinDetails

The details of the policy template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**Inputs**](Inputs.md) |  | [optional] 
**config_schema** | [**ConfigSchema**](ConfigSchema.md) |  | [optional] 
**output_violation_schema** | [**OutputViolationSchema**](OutputViolationSchema.md) |  | [optional] 
**rule_type** | [**PolicyTemplateDetailsRuleType**](PolicyTemplateDetailsRuleType.md) |  | [optional] 
**rule_definition** | [**RuleDefinition**](RuleDefinition.md) |  | [optional] 
**default_policy_config** | [**DefaultPolicyConfig**](DefaultPolicyConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_template_update_fields_mixin_details import PolicyTemplateUpdateFieldsMixinDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateUpdateFieldsMixinDetails from a JSON string
policy_template_update_fields_mixin_details_instance = PolicyTemplateUpdateFieldsMixinDetails.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateUpdateFieldsMixinDetails.to_json())

# convert the object into a dict
policy_template_update_fields_mixin_details_dict = policy_template_update_fields_mixin_details_instance.to_dict()
# create an instance of PolicyTemplateUpdateFieldsMixinDetails from a dict
policy_template_update_fields_mixin_details_form_dict = policy_template_update_fields_mixin_details.from_dict(policy_template_update_fields_mixin_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


