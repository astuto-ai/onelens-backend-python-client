# DeactivatePolicyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the policy template. | 

## Example

```python
from onelens_backend_client.models.deactivate_policy_template_request import DeactivatePolicyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivatePolicyTemplateRequest from a JSON string
deactivate_policy_template_request_instance = DeactivatePolicyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(DeactivatePolicyTemplateRequest.to_json())

# convert the object into a dict
deactivate_policy_template_request_dict = deactivate_policy_template_request_instance.to_dict()
# create an instance of DeactivatePolicyTemplateRequest from a dict
deactivate_policy_template_request_form_dict = deactivate_policy_template_request.from_dict(deactivate_policy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


