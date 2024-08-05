# CreatePolicyTemplatePullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the pull request. | 
**description** | **str** | The description of the pull request. | 
**source_branch** | **str** | The source branch of the pull request. | 
**branch_name** | **str** | The branch name of the pull request. | 
**alias** | **str** | The unique identifier of the policy template by alias. | 
**commit_message** | **str** | Change commit message | 

## Example

```python
from onelens_backend_client.models.create_policy_template_pull_request import CreatePolicyTemplatePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplatePullRequest from a JSON string
create_policy_template_pull_request_instance = CreatePolicyTemplatePullRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplatePullRequest.to_json())

# convert the object into a dict
create_policy_template_pull_request_dict = create_policy_template_pull_request_instance.to_dict()
# create an instance of CreatePolicyTemplatePullRequest from a dict
create_policy_template_pull_request_form_dict = create_policy_template_pull_request.from_dict(create_policy_template_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


