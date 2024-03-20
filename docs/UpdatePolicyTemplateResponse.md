# UpdatePolicyTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ptp_id** | **str** | The id of the parent policy template pack. | 
**title** | **str** | The title of the policy template. | 
**alias** | **str** | The alias of the policy template. | 
**description** | **str** | The description of the policy template. | [optional] 
**services** | [**List[CreatePolicyTemplateRequestServicesInner]**](CreatePolicyTemplateRequestServicesInner.md) | The list of services associated the policy template. | 
**execution_type** | [**PolicyExecutionType**](PolicyExecutionType.md) | The execution type of the policy template. | 
**details** | [**PolicyTemplateDetails**](PolicyTemplateDetails.md) | The details of the policy template. | 
**id** | **str** | The unique identifier of the policy template. | 
**state** | [**PolicyTemplateState**](PolicyTemplateState.md) | The state of the policy template. | 
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template. | 
**provider** | [**Provider**](Provider.md) | The cloud provider of the policy template. | 

## Example

```python
from onelens_backend_client.models.update_policy_template_response import UpdatePolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyTemplateResponse from a JSON string
update_policy_template_response_instance = UpdatePolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyTemplateResponse.to_json())

# convert the object into a dict
update_policy_template_response_dict = update_policy_template_response_instance.to_dict()
# create an instance of UpdatePolicyTemplateResponse from a dict
update_policy_template_response_form_dict = update_policy_template_response.from_dict(update_policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


