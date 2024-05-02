# UpdatePolicyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**services** | [**List[CreatePolicyTemplateRequestServicesInner]**](CreatePolicyTemplateRequestServicesInner.md) |  | [optional] 
**execution_type** | [**PolicyExecutionType**](PolicyExecutionType.md) |  | [optional] 
**details** | [**PolicyTemplateDetails**](PolicyTemplateDetails.md) |  | [optional] 
**id** | **str** | The unique identifier of the policy template. | 

## Example

```python
from onelens_backend_client.models.update_policy_template_request import UpdatePolicyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyTemplateRequest from a JSON string
update_policy_template_request_instance = UpdatePolicyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyTemplateRequest.to_json())

# convert the object into a dict
update_policy_template_request_dict = update_policy_template_request_instance.to_dict()
# create an instance of UpdatePolicyTemplateRequest from a dict
update_policy_template_request_form_dict = update_policy_template_request.from_dict(update_policy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


