# CreatePolicyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreatePolicyTemplateRequest**](CreatePolicyTemplateRequest.md) |  | 

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


