# GetSinglePolicyViolationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The unique identifier of the policy | 
**policy_title** | **str** | Policy name | 
**policy_labels** | **List[str]** | List of policy labels | [optional] [default to []]
**policy_services** | **List[str]** | List of services | 
**potential_savings** | **float** | Potential savings possible for the current policy violation | 
**resources** | **int** | Number of resources affected by the policy violation | 

## Example

```python
from onelens_backend_client.models.get_single_policy_violations_response import GetSinglePolicyViolationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSinglePolicyViolationsResponse from a JSON string
get_single_policy_violations_response_instance = GetSinglePolicyViolationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSinglePolicyViolationsResponse.to_json())

# convert the object into a dict
get_single_policy_violations_response_dict = get_single_policy_violations_response_instance.to_dict()
# create an instance of GetSinglePolicyViolationsResponse from a dict
get_single_policy_violations_response_form_dict = get_single_policy_violations_response.from_dict(get_single_policy_violations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


