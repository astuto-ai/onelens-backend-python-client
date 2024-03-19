# GetPolicyTemplatePackByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The alias of the policy template pack | 
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template pack | 
**provider** | [**Provider**](Provider.md) | The provider of the policy template pack | 
**details** | [**PolicyTemplatePackDetails**](PolicyTemplatePackDetails.md) | The details of the policy template pack | 
**id** | **str** | The unique identifier of the policy template pack | 
**state** | [**PolicyTemplatePackState**](PolicyTemplatePackState.md) | The state of the policy template pack | 

## Example

```python
from onelens_backend_client.models.get_policy_template_pack_by_id_response import GetPolicyTemplatePackByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplatePackByIdResponse from a JSON string
get_policy_template_pack_by_id_response_instance = GetPolicyTemplatePackByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplatePackByIdResponse.to_json())

# convert the object into a dict
get_policy_template_pack_by_id_response_dict = get_policy_template_pack_by_id_response_instance.to_dict()
# create an instance of GetPolicyTemplatePackByIdResponse from a dict
get_policy_template_pack_by_id_response_form_dict = get_policy_template_pack_by_id_response.from_dict(get_policy_template_pack_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


