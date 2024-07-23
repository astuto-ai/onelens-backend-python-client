# SyncPoliciesFromRepoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The unique identifier of the policy template by alias. | 

## Example

```python
from onelens_backend_client.models.sync_policies_from_repo_request import SyncPoliciesFromRepoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPoliciesFromRepoRequest from a JSON string
sync_policies_from_repo_request_instance = SyncPoliciesFromRepoRequest.from_json(json)
# print the JSON string representation of the object
print(SyncPoliciesFromRepoRequest.to_json())

# convert the object into a dict
sync_policies_from_repo_request_dict = sync_policies_from_repo_request_instance.to_dict()
# create an instance of SyncPoliciesFromRepoRequest from a dict
sync_policies_from_repo_request_form_dict = sync_policies_from_repo_request.from_dict(sync_policies_from_repo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


