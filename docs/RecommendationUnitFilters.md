# RecommendationUnitFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | [optional] 
**ids** | **List[str]** | Filter by recommendation unit id/alias. | [optional] [default to []]
**services** | **List[str]** | Filter by Services | [optional] [default to []]
**action_type_ids** | **List[int]** | Filter by action type. | [optional] [default to []]
**priorities** | **List[int]** | Filter by priorities. | [optional] [default to []]
**efforts** | [**List[Effort]**](Effort.md) | Filter by effort. | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.recommendation_unit_filters import RecommendationUnitFilters

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationUnitFilters from a JSON string
recommendation_unit_filters_instance = RecommendationUnitFilters.from_json(json)
# print the JSON string representation of the object
print(RecommendationUnitFilters.to_json())

# convert the object into a dict
recommendation_unit_filters_dict = recommendation_unit_filters_instance.to_dict()
# create an instance of RecommendationUnitFilters from a dict
recommendation_unit_filters_form_dict = recommendation_unit_filters.from_dict(recommendation_unit_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


