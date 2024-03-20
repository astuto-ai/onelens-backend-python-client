# GetPolicyTemplateByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the policy template. | 

## Example

```python
from onelens_backend_client.models.get_policy_template_by_id_request import GetPolicyTemplateByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplateByIDRequest from a JSON string
get_policy_template_by_id_request_instance = GetPolicyTemplateByIDRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplateByIDRequest.to_json())

# convert the object into a dict
get_policy_template_by_id_request_dict = get_policy_template_by_id_request_instance.to_dict()
# create an instance of GetPolicyTemplateByIDRequest from a dict
get_policy_template_by_id_request_form_dict = get_policy_template_by_id_request.from_dict(get_policy_template_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


