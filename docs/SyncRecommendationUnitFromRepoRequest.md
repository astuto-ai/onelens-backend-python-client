# SyncRecommendationUnitFromRepoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the recommendation unit template by alias. | 

## Example

```python
from onelens_backend_client.models.sync_recommendation_unit_from_repo_request import SyncRecommendationUnitFromRepoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncRecommendationUnitFromRepoRequest from a JSON string
sync_recommendation_unit_from_repo_request_instance = SyncRecommendationUnitFromRepoRequest.from_json(json)
# print the JSON string representation of the object
print(SyncRecommendationUnitFromRepoRequest.to_json())

# convert the object into a dict
sync_recommendation_unit_from_repo_request_dict = sync_recommendation_unit_from_repo_request_instance.to_dict()
# create an instance of SyncRecommendationUnitFromRepoRequest from a dict
sync_recommendation_unit_from_repo_request_form_dict = sync_recommendation_unit_from_repo_request.from_dict(sync_recommendation_unit_from_repo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


