# PolicyTemplateDetailsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **List[str]** |  | [optional] 
**config_schema** | **object** |  | [optional] 
**primary_violation_attributes_schema** | **object** |  | [optional] 
**secondary_violation_attributes_schema** | **object** |  | [optional] 
**rule_type** | [**RuleType**](RuleType.md) |  | [optional] 
**rule_definition** | **str** |  | [optional] 
**rule_definition_hash** | **str** |  | [optional] 
**default_policy_config** | **object** |  | [optional] 
**default_policy_config_hash** | **str** |  | [optional] 
**metrics_details** | [**List[MetricsChartConfigInput]**](MetricsChartConfigInput.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.policy_template_details_input import PolicyTemplateDetailsInput

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateDetailsInput from a JSON string
policy_template_details_input_instance = PolicyTemplateDetailsInput.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateDetailsInput.to_json())

# convert the object into a dict
policy_template_details_input_dict = policy_template_details_input_instance.to_dict()
# create an instance of PolicyTemplateDetailsInput from a dict
policy_template_details_input_form_dict = policy_template_details_input.from_dict(policy_template_details_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


