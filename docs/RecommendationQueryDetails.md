# RecommendationQueryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**derived_variables** | [**List[QueryDetailsDerivedVariables]**](QueryDetailsDerivedVariables.md) | Actual | 
**query** | **str** | Sql Query to get the recommendation | 

## Example

```python
from onelens_backend_client.models.recommendation_query_details import RecommendationQueryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationQueryDetails from a JSON string
recommendation_query_details_instance = RecommendationQueryDetails.from_json(json)
# print the JSON string representation of the object
print(RecommendationQueryDetails.to_json())

# convert the object into a dict
recommendation_query_details_dict = recommendation_query_details_instance.to_dict()
# create an instance of RecommendationQueryDetails from a dict
recommendation_query_details_form_dict = recommendation_query_details.from_dict(recommendation_query_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


