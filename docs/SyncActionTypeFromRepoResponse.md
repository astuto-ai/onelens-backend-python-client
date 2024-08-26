# SyncActionTypeFromRepoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The action type which got updated. | 

## Example

```python
from onelens_backend_client.models.sync_action_type_from_repo_response import SyncActionTypeFromRepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncActionTypeFromRepoResponse from a JSON string
sync_action_type_from_repo_response_instance = SyncActionTypeFromRepoResponse.from_json(json)
# print the JSON string representation of the object
print(SyncActionTypeFromRepoResponse.to_json())

# convert the object into a dict
sync_action_type_from_repo_response_dict = sync_action_type_from_repo_response_instance.to_dict()
# create an instance of SyncActionTypeFromRepoResponse from a dict
sync_action_type_from_repo_response_form_dict = sync_action_type_from_repo_response.from_dict(sync_action_type_from_repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


