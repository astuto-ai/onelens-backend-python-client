# GetPolicyTemplateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPolicyTemplateByIDRequest**](GetPolicyTemplateByIDRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_policy_template_by_id_request import GetPolicyTemplateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplateByIdRequest from a JSON string
get_policy_template_by_id_request_instance = GetPolicyTemplateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplateByIdRequest.to_json())

# convert the object into a dict
get_policy_template_by_id_request_dict = get_policy_template_by_id_request_instance.to_dict()
# create an instance of GetPolicyTemplateByIdRequest from a dict
get_policy_template_by_id_request_form_dict = get_policy_template_by_id_request.from_dict(get_policy_template_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


