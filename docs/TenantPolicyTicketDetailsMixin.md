# TenantPolicyTicketDetailsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy being violated. | 
**policy_template_id** | **str** | The id of the policy template being violated. | 
**policy_config** | **object** | The config of the policy being violated. | 
**policy_config_hash** | **str** |  | [optional] 
**policy_config_version** | **int** | The config version of the policy being violated. | 
**violation_attributes** | **object** | The attributes of the violation. | 
**potential_cost_saving** | **float** | The potential cost accrued because of the violation. | 
**preferred_recommendation_id** | **str** |  | [optional] 
**rule_definition_hash** | **str** |  | [optional] 

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


