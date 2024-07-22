# CreatePolicyTemplateMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The unique identifier of the policy template by alias. | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_branch** | **str** |  | 
**branch_name** | **str** |  | 

## Example

```python
from onelens_backend_client.models.create_policy_template_migration_request import CreatePolicyTemplateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplateMigrationRequest from a JSON string
create_policy_template_migration_request_instance = CreatePolicyTemplateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplateMigrationRequest.to_json())

# convert the object into a dict
create_policy_template_migration_request_dict = create_policy_template_migration_request_instance.to_dict()
# create an instance of CreatePolicyTemplateMigrationRequest from a dict
create_policy_template_migration_request_form_dict = create_policy_template_migration_request.from_dict(create_policy_template_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


