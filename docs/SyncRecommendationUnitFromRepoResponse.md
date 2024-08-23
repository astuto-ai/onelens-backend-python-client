# SyncRecommendationUnitFromRepoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The recommendation unit which got updated. | 

## Example

```python
from onelens_backend_client.models.sync_recommendation_unit_from_repo_response import SyncRecommendationUnitFromRepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncRecommendationUnitFromRepoResponse from a JSON string
sync_recommendation_unit_from_repo_response_instance = SyncRecommendationUnitFromRepoResponse.from_json(json)
# print the JSON string representation of the object
print(SyncRecommendationUnitFromRepoResponse.to_json())

# convert the object into a dict
sync_recommendation_unit_from_repo_response_dict = sync_recommendation_unit_from_repo_response_instance.to_dict()
# create an instance of SyncRecommendationUnitFromRepoResponse from a dict
sync_recommendation_unit_from_repo_response_form_dict = sync_recommendation_unit_from_repo_response.from_dict(sync_recommendation_unit_from_repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


