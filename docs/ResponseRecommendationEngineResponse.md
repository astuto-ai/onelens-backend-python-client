# ResponseRecommendationEngineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RecommendationEngineResponse**](RecommendationEngineResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_recommendation_engine_response import ResponseRecommendationEngineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseRecommendationEngineResponse from a JSON string
response_recommendation_engine_response_instance = ResponseRecommendationEngineResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseRecommendationEngineResponse.to_json())

# convert the object into a dict
response_recommendation_engine_response_dict = response_recommendation_engine_response_instance.to_dict()
# create an instance of ResponseRecommendationEngineResponse from a dict
response_recommendation_engine_response_form_dict = response_recommendation_engine_response.from_dict(response_recommendation_engine_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


