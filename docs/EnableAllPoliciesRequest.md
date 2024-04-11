# EnableAllPoliciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.enable_all_policies_request import EnableAllPoliciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableAllPoliciesRequest from a JSON string
enable_all_policies_request_instance = EnableAllPoliciesRequest.from_json(json)
# print the JSON string representation of the object
print(EnableAllPoliciesRequest.to_json())

# convert the object into a dict
enable_all_policies_request_dict = enable_all_policies_request_instance.to_dict()
# create an instance of EnableAllPoliciesRequest from a dict
enable_all_policies_request_form_dict = enable_all_policies_request.from_dict(enable_all_policies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


