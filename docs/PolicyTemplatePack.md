# PolicyTemplatePack


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
from openapi_client.models.policy_template_pack import PolicyTemplatePack

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplatePack from a JSON string
policy_template_pack_instance = PolicyTemplatePack.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplatePack.to_json())

# convert the object into a dict
policy_template_pack_dict = policy_template_pack_instance.to_dict()
# create an instance of PolicyTemplatePack from a dict
policy_template_pack_form_dict = policy_template_pack.from_dict(policy_template_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


