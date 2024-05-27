# RecommendationEngineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[RecommendationEngine]**](RecommendationEngine.md) | Recommendations | 

## Example

```python
from onelens_backend_client.models.recommendation_engine_response import RecommendationEngineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationEngineResponse from a JSON string
recommendation_engine_response_instance = RecommendationEngineResponse.from_json(json)
# print the JSON string representation of the object
print(RecommendationEngineResponse.to_json())

# convert the object into a dict
recommendation_engine_response_dict = recommendation_engine_response_instance.to_dict()
# create an instance of RecommendationEngineResponse from a dict
recommendation_engine_response_form_dict = recommendation_engine_response.from_dict(recommendation_engine_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


