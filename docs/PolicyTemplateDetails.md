# PolicyTemplateDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **List[str]** |  | [optional] 
**config_schema** | **object** |  | [optional] 
**output_violation_schema** | **object** |  | [optional] 
**rule_type** | [**RuleType**](RuleType.md) |  | [optional] 
**rule_definition** | **str** |  | [optional] 
**default_policy_config** | **object** |  | [optional] 

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


