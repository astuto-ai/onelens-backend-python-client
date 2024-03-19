# GetPolicyTemplatePacksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_template_packs_request import GetPolicyTemplatePacksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplatePacksRequest from a JSON string
get_policy_template_packs_request_instance = GetPolicyTemplatePacksRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplatePacksRequest.to_json())

# convert the object into a dict
get_policy_template_packs_request_dict = get_policy_template_packs_request_instance.to_dict()
# create an instance of GetPolicyTemplatePacksRequest from a dict
get_policy_template_packs_request_form_dict = get_policy_template_packs_request.from_dict(get_policy_template_packs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


