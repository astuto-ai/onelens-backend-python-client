# GetRecommendationUnitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**RecommendationUnitFilters**](RecommendationUnitFilters.md) | Filters to apply to the Recommendation Unit. | [optional] 

## Example

```python
from onelens_backend_client.models.get_recommendation_unit_request import GetRecommendationUnitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationUnitRequest from a JSON string
get_recommendation_unit_request_instance = GetRecommendationUnitRequest.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationUnitRequest.to_json())

# convert the object into a dict
get_recommendation_unit_request_dict = get_recommendation_unit_request_instance.to_dict()
# create an instance of GetRecommendationUnitRequest from a dict
get_recommendation_unit_request_form_dict = get_recommendation_unit_request.from_dict(get_recommendation_unit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


