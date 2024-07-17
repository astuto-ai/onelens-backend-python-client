# RecommendationUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Recommendation Config ID | 
**service** | **str** | Service AWS etc. | 
**action_type_id** | **int** |  | [optional] 
**priority** | **int** | Priority | 
**title** | **str** | Title | 
**subtitle** | **str** |  | [optional] 
**description** | **str** | Description | 
**effort** | [**Effort**](Effort.md) | Effort | 
**query_details** | [**RecommendationQueryDetails**](RecommendationQueryDetails.md) |  | 

## Example

```python
from onelens_backend_client.models.recommendation_unit import RecommendationUnit

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationUnit from a JSON string
recommendation_unit_instance = RecommendationUnit.from_json(json)
# print the JSON string representation of the object
print(RecommendationUnit.to_json())

# convert the object into a dict
recommendation_unit_dict = recommendation_unit_instance.to_dict()
# create an instance of RecommendationUnit from a dict
recommendation_unit_form_dict = recommendation_unit.from_dict(recommendation_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


