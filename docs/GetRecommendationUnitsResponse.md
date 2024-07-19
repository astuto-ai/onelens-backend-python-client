# GetRecommendationUnitsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_units** | [**List[RecommendationUnitWithActionType]**](RecommendationUnitWithActionType.md) | Recommendation Unit | 
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields | 

## Example

```python
from onelens_backend_client.models.get_recommendation_units_response import GetRecommendationUnitsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationUnitsResponse from a JSON string
get_recommendation_units_response_instance = GetRecommendationUnitsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationUnitsResponse.to_json())

# convert the object into a dict
get_recommendation_units_response_dict = get_recommendation_units_response_instance.to_dict()
# create an instance of GetRecommendationUnitsResponse from a dict
get_recommendation_units_response_form_dict = get_recommendation_units_response.from_dict(get_recommendation_units_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


