# PolicyRecommendationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **object** |  | [optional] 
**target** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.policy_recommendation_params import PolicyRecommendationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRecommendationParams from a JSON string
policy_recommendation_params_instance = PolicyRecommendationParams.from_json(json)
# print the JSON string representation of the object
print(PolicyRecommendationParams.to_json())

# convert the object into a dict
policy_recommendation_params_dict = policy_recommendation_params_instance.to_dict()
# create an instance of PolicyRecommendationParams from a dict
policy_recommendation_params_form_dict = policy_recommendation_params.from_dict(policy_recommendation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


