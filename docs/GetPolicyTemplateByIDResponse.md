# GetPolicyTemplateByIDResponse


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
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template. | 
**provider** | [**Provider**](Provider.md) | The cloud provider of the policy template. | 
**id** | **str** | The unique identifier of the policy template. | 
**state** | [**PolicyTemplateState**](PolicyTemplateState.md) | The state of the policy template. | 
**requirements** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_template_by_id_response import GetPolicyTemplateByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplateByIDResponse from a JSON string
get_policy_template_by_id_response_instance = GetPolicyTemplateByIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplateByIDResponse.to_json())

# convert the object into a dict
get_policy_template_by_id_response_dict = get_policy_template_by_id_response_instance.to_dict()
# create an instance of GetPolicyTemplateByIDResponse from a dict
get_policy_template_by_id_response_form_dict = get_policy_template_by_id_response.from_dict(get_policy_template_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


