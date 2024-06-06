# PolicyTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ptp_id** | **str** | The id of the parent policy template pack. | 
**title** | **str** | The title of the policy template. | 
**alias** | **str** | The alias of the policy template. | 
**description** | **str** | The description of the policy template. | [optional] 
**services** | [**List[CreatePolicyTemplateRequestServicesInner]**](CreatePolicyTemplateRequestServicesInner.md) | The list of services associated the policy template. | 
**execution_type** | [**PolicyExecutionType**](PolicyExecutionType.md) | The execution type of the policy template. | 
**details** | [**PolicyTemplateDetailsOutput**](PolicyTemplateDetailsOutput.md) | The details of the policy template. | 
**description2** | **str** | The description2 of the policy template. | [optional] 
**resource_type** | **str** | The resource type of the policy template. | 
**recommendation_details** | [**PolicyTemplateRecommendationDetailsOutput**](PolicyTemplateRecommendationDetailsOutput.md) | The recommendation details for the policy template. | 
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template. | 
**provider** | [**Provider**](Provider.md) | The cloud provider of the policy template. | 
**id** | **str** | The unique identifier of the policy template. | 
**state** | [**PolicyTemplateState**](PolicyTemplateState.md) | The state of the policy template. | 

## Example

```python
from onelens_backend_client.models.policy_template import PolicyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplate from a JSON string
policy_template_instance = PolicyTemplate.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplate.to_json())

# convert the object into a dict
policy_template_dict = policy_template_instance.to_dict()
# create an instance of PolicyTemplate from a dict
policy_template_form_dict = policy_template.from_dict(policy_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


