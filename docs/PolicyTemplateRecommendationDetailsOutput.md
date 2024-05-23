# PolicyTemplateRecommendationDetailsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_recommendation_units** | [**List[PolicyTemplateRecommendationUnits]**](PolicyTemplateRecommendationUnits.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.policy_template_recommendation_details_output import PolicyTemplateRecommendationDetailsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateRecommendationDetailsOutput from a JSON string
policy_template_recommendation_details_output_instance = PolicyTemplateRecommendationDetailsOutput.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateRecommendationDetailsOutput.to_json())

# convert the object into a dict
policy_template_recommendation_details_output_dict = policy_template_recommendation_details_output_instance.to_dict()
# create an instance of PolicyTemplateRecommendationDetailsOutput from a dict
policy_template_recommendation_details_output_form_dict = policy_template_recommendation_details_output.from_dict(policy_template_recommendation_details_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


