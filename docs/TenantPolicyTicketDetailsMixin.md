# TenantPolicyTicketDetailsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy being violated. | 
**entity_id** | **str** | The id of the resource experiencing policy violation. | 
**entity_type** | **str** | The type of the resource experiencing policy violation. | 
**policy_template_id** | **str** | The id of the policy template being violated. | 
**policy_config** | **str** | The config of the policy being violated. | 
**policy_config_version** | **str** | The config version of the policy being violated. | 
**violation_attributes** | **str** | The attributes of the violation. | 

## Example

```python
from onelens_backend_client.models.tenant_policy_ticket_details_mixin import TenantPolicyTicketDetailsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyTicketDetailsMixin from a JSON string
tenant_policy_ticket_details_mixin_instance = TenantPolicyTicketDetailsMixin.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyTicketDetailsMixin.to_json())

# convert the object into a dict
tenant_policy_ticket_details_mixin_dict = tenant_policy_ticket_details_mixin_instance.to_dict()
# create an instance of TenantPolicyTicketDetailsMixin from a dict
tenant_policy_ticket_details_mixin_form_dict = tenant_policy_ticket_details_mixin.from_dict(tenant_policy_ticket_details_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

