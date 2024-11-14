# TenantPolicyWithPolicyDisplayAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ptp_id** | **str** | The id of the parent policy template pack. | 
**title** | **str** | The title of the policy template. | 
**alias** | **str** | The alias of the policy template. | 
**description** | **str** | The description of the policy template. | [optional] 
**services** | [**List[ActionTypeFiltersServicesInner]**](ActionTypeFiltersServicesInner.md) | The list of services associated the policy template. | 
**execution_type** | [**PolicyExecutionType**](PolicyExecutionType.md) | The execution type of the policy template. | 
**details** | [**PolicyTemplateDetailsOutput**](PolicyTemplateDetailsOutput.md) | The details of the policy template. | 
**description2** | **str** | The description2 of the policy template. | [optional] 
**resource_type** | **str** | The resource type of the policy template. | 
**recommendation_details** | [**PolicyTemplateRecommendationDetailsOutput**](PolicyTemplateRecommendationDetailsOutput.md) | The recommendation details for the policy template. | 
**activated_at** | **datetime** |  | [optional] 
**policy_template_id** | **str** | The id of the policy template. | 
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template. | 
**provider** | [**Provider**](Provider.md) | The cloud provider of the policy template. | 
**id** | **str** | The unique identifier of the tenant policy. | 
**state** | [**TenantPolicySystemState**](TenantPolicySystemState.md) | The state of the tenant policy. | 
**policy_display_alias** | **str** | Policy display alias  | 

## Example

```python
from onelens_backend_client.models.tenant_policy_with_policy_display_alias import TenantPolicyWithPolicyDisplayAlias

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyWithPolicyDisplayAlias from a JSON string
tenant_policy_with_policy_display_alias_instance = TenantPolicyWithPolicyDisplayAlias.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyWithPolicyDisplayAlias.to_json())

# convert the object into a dict
tenant_policy_with_policy_display_alias_dict = tenant_policy_with_policy_display_alias_instance.to_dict()
# create an instance of TenantPolicyWithPolicyDisplayAlias from a dict
tenant_policy_with_policy_display_alias_form_dict = tenant_policy_with_policy_display_alias.from_dict(tenant_policy_with_policy_display_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


