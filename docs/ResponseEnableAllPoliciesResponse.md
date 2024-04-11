# ResponseEnableAllPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_enable_all_policies_response import ResponseEnableAllPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseEnableAllPoliciesResponse from a JSON string
response_enable_all_policies_response_instance = ResponseEnableAllPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseEnableAllPoliciesResponse.to_json())

# convert the object into a dict
response_enable_all_policies_response_dict = response_enable_all_policies_response_instance.to_dict()
# create an instance of ResponseEnableAllPoliciesResponse from a dict
response_enable_all_policies_response_form_dict = response_enable_all_policies_response.from_dict(response_enable_all_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


