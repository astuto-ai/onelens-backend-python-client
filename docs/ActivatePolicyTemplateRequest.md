# ActivatePolicyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the policy template. | 

## Example

```python
from onelens_backend_client.models.activate_policy_template_request import ActivatePolicyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivatePolicyTemplateRequest from a JSON string
activate_policy_template_request_instance = ActivatePolicyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivatePolicyTemplateRequest.to_json())

# convert the object into a dict
activate_policy_template_request_dict = activate_policy_template_request_instance.to_dict()
# create an instance of ActivatePolicyTemplateRequest from a dict
activate_policy_template_request_form_dict = activate_policy_template_request.from_dict(activate_policy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


