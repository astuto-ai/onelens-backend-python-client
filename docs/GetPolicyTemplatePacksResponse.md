# GetPolicyTemplatePacksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policy_template_packs** | [**List[PolicyTemplatePack]**](PolicyTemplatePack.md) |  | 

## Example

```python
from openapi_client.models.get_policy_template_packs_response import GetPolicyTemplatePacksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplatePacksResponse from a JSON string
get_policy_template_packs_response_instance = GetPolicyTemplatePacksResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplatePacksResponse.to_json())

# convert the object into a dict
get_policy_template_packs_response_dict = get_policy_template_packs_response_instance.to_dict()
# create an instance of GetPolicyTemplatePacksResponse from a dict
get_policy_template_packs_response_form_dict = get_policy_template_packs_response.from_dict(get_policy_template_packs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


