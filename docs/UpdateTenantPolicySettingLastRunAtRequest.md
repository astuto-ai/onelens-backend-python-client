# UpdateTenantPolicySettingLastRunAtRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**updates** | [**List[LastRunAtUpdateItem]**](LastRunAtUpdateItem.md) | The list of updates. | 

## Example

```python
from onelens_backend_client.models.update_tenant_policy_setting_last_run_at_request import UpdateTenantPolicySettingLastRunAtRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantPolicySettingLastRunAtRequest from a JSON string
update_tenant_policy_setting_last_run_at_request_instance = UpdateTenantPolicySettingLastRunAtRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantPolicySettingLastRunAtRequest.to_json())

# convert the object into a dict
update_tenant_policy_setting_last_run_at_request_dict = update_tenant_policy_setting_last_run_at_request_instance.to_dict()
# create an instance of UpdateTenantPolicySettingLastRunAtRequest from a dict
update_tenant_policy_setting_last_run_at_request_form_dict = update_tenant_policy_setting_last_run_at_request.from_dict(update_tenant_policy_setting_last_run_at_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


