# DeprecatePolicyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the policy template. | 

## Example

```python
from onelens_backend_client.models.deprecate_policy_template_request import DeprecatePolicyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatePolicyTemplateRequest from a JSON string
deprecate_policy_template_request_instance = DeprecatePolicyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(DeprecatePolicyTemplateRequest.to_json())

# convert the object into a dict
deprecate_policy_template_request_dict = deprecate_policy_template_request_instance.to_dict()
# create an instance of DeprecatePolicyTemplateRequest from a dict
deprecate_policy_template_request_form_dict = deprecate_policy_template_request.from_dict(deprecate_policy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


