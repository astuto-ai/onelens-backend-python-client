# SyncPolicyTemplateMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.sync_policy_template_migration_request import SyncPolicyTemplateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPolicyTemplateMigrationRequest from a JSON string
sync_policy_template_migration_request_instance = SyncPolicyTemplateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(SyncPolicyTemplateMigrationRequest.to_json())

# convert the object into a dict
sync_policy_template_migration_request_dict = sync_policy_template_migration_request_instance.to_dict()
# create an instance of SyncPolicyTemplateMigrationRequest from a dict
sync_policy_template_migration_request_form_dict = sync_policy_template_migration_request.from_dict(sync_policy_template_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


