# CreateActionTypePullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the pull request. | 
**description** | **str** | The description of the pull request. | 
**source_branch** | **str** | The source branch of the pull request. | 
**branch_name** | **str** | The branch name of the pull request. | 
**alias** | **str** | The unique identifier alias of the action type. | 
**commit_message** | **str** | Action type change commit message | 

## Example

```python
from onelens_backend_client.models.create_action_type_pull_request import CreateActionTypePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActionTypePullRequest from a JSON string
create_action_type_pull_request_instance = CreateActionTypePullRequest.from_json(json)
# print the JSON string representation of the object
print(CreateActionTypePullRequest.to_json())

# convert the object into a dict
create_action_type_pull_request_dict = create_action_type_pull_request_instance.to_dict()
# create an instance of CreateActionTypePullRequest from a dict
create_action_type_pull_request_form_dict = create_action_type_pull_request.from_dict(create_action_type_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


