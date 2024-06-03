# GetAllPolicyViolationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policy_violations** | [**List[GetSinglePolicyViolationsResponse]**](GetSinglePolicyViolationsResponse.md) | List of policy violations | 

## Example

```python
from onelens_backend_client.models.get_all_policy_violations_response import GetAllPolicyViolationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPolicyViolationsResponse from a JSON string
get_all_policy_violations_response_instance = GetAllPolicyViolationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllPolicyViolationsResponse.to_json())

# convert the object into a dict
get_all_policy_violations_response_dict = get_all_policy_violations_response_instance.to_dict()
# create an instance of GetAllPolicyViolationsResponse from a dict
get_all_policy_violations_response_form_dict = get_all_policy_violations_response.from_dict(get_all_policy_violations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


