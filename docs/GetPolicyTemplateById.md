# GetPolicyTemplateById


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPolicyTemplateByIDRequest**](GetPolicyTemplateByIDRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_policy_template_by_id import GetPolicyTemplateById

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplateById from a JSON string
get_policy_template_by_id_instance = GetPolicyTemplateById.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplateById.to_json())

# convert the object into a dict
get_policy_template_by_id_dict = get_policy_template_by_id_instance.to_dict()
# create an instance of GetPolicyTemplateById from a dict
get_policy_template_by_id_form_dict = get_policy_template_by_id.from_dict(get_policy_template_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


