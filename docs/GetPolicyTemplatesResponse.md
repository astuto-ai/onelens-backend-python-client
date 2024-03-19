# GetPolicyTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policy_templates** | [**List[PolicyTemplate]**](PolicyTemplate.md) | List of policy templates. | 

## Example

```python
from openapi_client.models.get_policy_templates_response import GetPolicyTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTemplatesResponse from a JSON string
get_policy_templates_response_instance = GetPolicyTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTemplatesResponse.to_json())

# convert the object into a dict
get_policy_templates_response_dict = get_policy_templates_response_instance.to_dict()
# create an instance of GetPolicyTemplatesResponse from a dict
get_policy_templates_response_form_dict = get_policy_templates_response.from_dict(get_policy_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


