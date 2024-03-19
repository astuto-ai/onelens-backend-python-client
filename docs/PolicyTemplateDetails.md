# PolicyTemplateDetails


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
from onelens_backend_client.models.policy_template_details import PolicyTemplateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateDetails from a JSON string
policy_template_details_instance = PolicyTemplateDetails.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateDetails.to_json())

# convert the object into a dict
policy_template_details_dict = policy_template_details_instance.to_dict()
# create an instance of PolicyTemplateDetails from a dict
policy_template_details_form_dict = policy_template_details.from_dict(policy_template_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


