# CreatePolicyTemplatePackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The alias of the policy template pack | 
**category** | [**PolicyCategory**](PolicyCategory.md) | The category of the policy template pack | 
**provider** | [**Provider**](Provider.md) | The provider of the policy template pack | 
**details** | [**PolicyTemplatePackDetails**](PolicyTemplatePackDetails.md) | The details of the policy template pack | 

## Example

```python
from openapi_client.models.create_policy_template_pack_request import CreatePolicyTemplatePackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyTemplatePackRequest from a JSON string
create_policy_template_pack_request_instance = CreatePolicyTemplatePackRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyTemplatePackRequest.to_json())

# convert the object into a dict
create_policy_template_pack_request_dict = create_policy_template_pack_request_instance.to_dict()
# create an instance of CreatePolicyTemplatePackRequest from a dict
create_policy_template_pack_request_form_dict = create_policy_template_pack_request.from_dict(create_policy_template_pack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


