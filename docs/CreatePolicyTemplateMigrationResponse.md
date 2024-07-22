# CreatePolicyTemplateMigrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The unique identifier of the policy template by alias. | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_branch** | **str** |  | 
**branch_name** | **str** |  | 
**process_log** | **List[str]** |  | [optional] 
**pr_link** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_policy_template_migration_response import CreatePolicyTemplateMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplateMigrationResponse from a JSON string
create_policy_template_migration_response_instance = CreatePolicyTemplateMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplateMigrationResponse.to_json())

# convert the object into a dict
create_policy_template_migration_response_dict = create_policy_template_migration_response_instance.to_dict()
# create an instance of CreatePolicyTemplateMigrationResponse from a dict
create_policy_template_migration_response_form_dict = create_policy_template_migration_response.from_dict(create_policy_template_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


