# CreatePolicyTemplatePullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pr_link** | **str** | The policy pull request link. | 

## Example

```python
from onelens_backend_client.models.create_policy_template_pull_response import CreatePolicyTemplatePullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplatePullResponse from a JSON string
create_policy_template_pull_response_instance = CreatePolicyTemplatePullResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplatePullResponse.to_json())

# convert the object into a dict
create_policy_template_pull_response_dict = create_policy_template_pull_response_instance.to_dict()
# create an instance of CreatePolicyTemplatePullResponse from a dict
create_policy_template_pull_response_form_dict = create_policy_template_pull_response.from_dict(create_policy_template_pull_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


