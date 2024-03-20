# CreatePolicyTemplateRequest


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

## Example

```python
from onelens_backend_client.models.create_policy_template_request import CreatePolicyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplateRequest from a JSON string
create_policy_template_request_instance = CreatePolicyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplateRequest.to_json())

# convert the object into a dict
create_policy_template_request_dict = create_policy_template_request_instance.to_dict()
# create an instance of CreatePolicyTemplateRequest from a dict
create_policy_template_request_form_dict = create_policy_template_request.from_dict(create_policy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


