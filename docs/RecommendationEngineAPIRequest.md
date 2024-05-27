# RecommendationEngineAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**resource_id** | **str** | Resource ID | 
**params** | [**RecommendationParams**](RecommendationParams.md) | Recommendation Params | 
**policy_config** | **object** | Policy Config | 

## Example

```python
from onelens_backend_client.models.recommendation_engine_api_request import RecommendationEngineAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationEngineAPIRequest from a JSON string
recommendation_engine_api_request_instance = RecommendationEngineAPIRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendationEngineAPIRequest.to_json())

# convert the object into a dict
recommendation_engine_api_request_dict = recommendation_engine_api_request_instance.to_dict()
# create an instance of RecommendationEngineAPIRequest from a dict
recommendation_engine_api_request_form_dict = recommendation_engine_api_request.from_dict(recommendation_engine_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


