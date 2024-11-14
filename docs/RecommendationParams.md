# RecommendationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **object** | Current | 
**target** | **object** | Target | 

## Example

```python
from onelens_backend_client.models.recommendation_params import RecommendationParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationParams from a JSON string
recommendation_params_instance = RecommendationParams.from_json(json)
# print the JSON string representation of the object
print(RecommendationParams.to_json())

# convert the object into a dict
recommendation_params_dict = recommendation_params_instance.to_dict()
# create an instance of RecommendationParams from a dict
recommendation_params_form_dict = recommendation_params.from_dict(recommendation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


