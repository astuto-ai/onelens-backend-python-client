# RecommendationUnitWithActionType


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
**action_type_service** | **str** |  | [optional] 
**action_type_title** | **str** |  | [optional] 
**action_type_subtitle** | **str** |  | [optional] 
**action_type_description** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.recommendation_unit_with_action_type import RecommendationUnitWithActionType

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationUnitWithActionType from a JSON string
recommendation_unit_with_action_type_instance = RecommendationUnitWithActionType.from_json(json)
# print the JSON string representation of the object
print(RecommendationUnitWithActionType.to_json())

# convert the object into a dict
recommendation_unit_with_action_type_dict = recommendation_unit_with_action_type_instance.to_dict()
# create an instance of RecommendationUnitWithActionType from a dict
recommendation_unit_with_action_type_form_dict = recommendation_unit_with_action_type.from_dict(recommendation_unit_with_action_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


