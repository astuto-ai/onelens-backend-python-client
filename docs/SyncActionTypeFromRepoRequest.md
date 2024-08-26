# SyncActionTypeFromRepoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The unique identifier of the action type template. | 

## Example

```python
from onelens_backend_client.models.sync_action_type_from_repo_request import SyncActionTypeFromRepoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncActionTypeFromRepoRequest from a JSON string
sync_action_type_from_repo_request_instance = SyncActionTypeFromRepoRequest.from_json(json)
# print the JSON string representation of the object
print(SyncActionTypeFromRepoRequest.to_json())

# convert the object into a dict
sync_action_type_from_repo_request_dict = sync_action_type_from_repo_request_instance.to_dict()
# create an instance of SyncActionTypeFromRepoRequest from a dict
sync_action_type_from_repo_request_form_dict = sync_action_type_from_repo_request.from_dict(sync_action_type_from_repo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


