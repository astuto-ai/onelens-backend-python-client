# ResponseGetAllPolicyViolationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetAllPolicyViolationsResponse**](GetAllPolicyViolationsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_all_policy_violations_response import ResponseGetAllPolicyViolationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetAllPolicyViolationsResponse from a JSON string
response_get_all_policy_violations_response_instance = ResponseGetAllPolicyViolationsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetAllPolicyViolationsResponse.to_json())

# convert the object into a dict
response_get_all_policy_violations_response_dict = response_get_all_policy_violations_response_instance.to_dict()
# create an instance of ResponseGetAllPolicyViolationsResponse from a dict
response_get_all_policy_violations_response_form_dict = response_get_all_policy_violations_response.from_dict(response_get_all_policy_violations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


