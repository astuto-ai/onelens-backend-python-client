# PolicyTemplateRecommendationUnits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**params** | [**PolicyRecommendationParams**](PolicyRecommendationParams.md) | Policy template Recommendation Params | 

## Example

```python
from onelens_backend_client.models.policy_template_recommendation_units import PolicyTemplateRecommendationUnits

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateRecommendationUnits from a JSON string
policy_template_recommendation_units_instance = PolicyTemplateRecommendationUnits.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateRecommendationUnits.to_json())

# convert the object into a dict
policy_template_recommendation_units_dict = policy_template_recommendation_units_instance.to_dict()
# create an instance of PolicyTemplateRecommendationUnits from a dict
policy_template_recommendation_units_form_dict = policy_template_recommendation_units.from_dict(policy_template_recommendation_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


