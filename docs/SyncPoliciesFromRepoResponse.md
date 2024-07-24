# SyncPoliciesFromRepoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The policy which got updated. | 

## Example

```python
from onelens_backend_client.models.sync_policies_from_repo_response import SyncPoliciesFromRepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPoliciesFromRepoResponse from a JSON string
sync_policies_from_repo_response_instance = SyncPoliciesFromRepoResponse.from_json(json)
# print the JSON string representation of the object
print(SyncPoliciesFromRepoResponse.to_json())

# convert the object into a dict
sync_policies_from_repo_response_dict = sync_policies_from_repo_response_instance.to_dict()
# create an instance of SyncPoliciesFromRepoResponse from a dict
sync_policies_from_repo_response_form_dict = sync_policies_from_repo_response.from_dict(sync_policies_from_repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


