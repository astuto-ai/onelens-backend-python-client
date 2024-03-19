# GetPolicyTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPolicyTemplatesRequest**](GetPolicyTemplatesRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_policy_templates_request import GetPolicyTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplatesRequest from a JSON string
get_policy_templates_request_instance = GetPolicyTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplatesRequest.to_json())

# convert the object into a dict
get_policy_templates_request_dict = get_policy_templates_request_instance.to_dict()
# create an instance of GetPolicyTemplatesRequest from a dict
get_policy_templates_request_form_dict = get_policy_templates_request.from_dict(get_policy_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


