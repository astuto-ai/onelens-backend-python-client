# SyncPolicyTemplateMigrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_log** | **List[str]** |  | [optional] 

## Example

```python
from onelens_backend_client.models.sync_policy_template_migration_response import SyncPolicyTemplateMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPolicyTemplateMigrationResponse from a JSON string
sync_policy_template_migration_response_instance = SyncPolicyTemplateMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(SyncPolicyTemplateMigrationResponse.to_json())

# convert the object into a dict
sync_policy_template_migration_response_dict = sync_policy_template_migration_response_instance.to_dict()
# create an instance of SyncPolicyTemplateMigrationResponse from a dict
sync_policy_template_migration_response_form_dict = sync_policy_template_migration_response.from_dict(sync_policy_template_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


