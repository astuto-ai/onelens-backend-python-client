# CreatePolicyTemplatePackResponse


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
from onelens_backend_client.models.create_policy_template_pack_response import CreatePolicyTemplatePackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplatePackResponse from a JSON string
create_policy_template_pack_response_instance = CreatePolicyTemplatePackResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplatePackResponse.to_json())

# convert the object into a dict
create_policy_template_pack_response_dict = create_policy_template_pack_response_instance.to_dict()
# create an instance of CreatePolicyTemplatePackResponse from a dict
create_policy_template_pack_response_form_dict = create_policy_template_pack_response.from_dict(create_policy_template_pack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


