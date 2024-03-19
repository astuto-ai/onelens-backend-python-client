# UpdatePolicyTemplateRequestDetails

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
from onelens_backend_client.models.update_policy_template_request_details import UpdatePolicyTemplateRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyTemplateRequestDetails from a JSON string
update_policy_template_request_details_instance = UpdatePolicyTemplateRequestDetails.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyTemplateRequestDetails.to_json())

# convert the object into a dict
update_policy_template_request_details_dict = update_policy_template_request_details_instance.to_dict()
# create an instance of UpdatePolicyTemplateRequestDetails from a dict
update_policy_template_request_details_form_dict = update_policy_template_request_details.from_dict(update_policy_template_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


