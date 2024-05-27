# RecommendationEngineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**resource_id** | **str** | Resource ID | 
**params** | [**RecommendationParams**](RecommendationParams.md) | Recommendation Params | 
**policy_config** | **object** | Policy Config | 
**tenant_id** | **str** | Tenant ID | 

## Example

```python
from onelens_backend_client.models.recommendation_engine_request import RecommendationEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationEngineRequest from a JSON string
recommendation_engine_request_instance = RecommendationEngineRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendationEngineRequest.to_json())

# convert the object into a dict
recommendation_engine_request_dict = recommendation_engine_request_instance.to_dict()
# create an instance of RecommendationEngineRequest from a dict
recommendation_engine_request_form_dict = recommendation_engine_request.from_dict(recommendation_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


