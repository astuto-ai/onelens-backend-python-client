# UpdateRecommendationUnitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Recommendation Config ID | 
**service** | **str** | Service AWS etc. | 
**action_type_alias** | **str** |  | [optional] 
**priority** | **int** | Priority | 
**title** | **str** | Title | 
**subtitle** | **str** | Subtitle | [optional] 
**description** | **str** | Description | 
**effort** | [**Effort**](Effort.md) | Effort | 
**query_details** | [**RecommendationQueryDetails**](RecommendationQueryDetails.md) |  | 

## Example

```python
from onelens_backend_client.models.update_recommendation_unit_request import UpdateRecommendationUnitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecommendationUnitRequest from a JSON string
update_recommendation_unit_request_instance = UpdateRecommendationUnitRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecommendationUnitRequest.to_json())

# convert the object into a dict
update_recommendation_unit_request_dict = update_recommendation_unit_request_instance.to_dict()
# create an instance of UpdateRecommendationUnitRequest from a dict
update_recommendation_unit_request_form_dict = update_recommendation_unit_request.from_dict(update_recommendation_unit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


