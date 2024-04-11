# DisableTenantPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**policy_id** | **str** | The id of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.disable_tenant_policy_request import DisableTenantPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenantPolicyRequest from a JSON string
disable_tenant_policy_request_instance = DisableTenantPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(DisableTenantPolicyRequest.to_json())

# convert the object into a dict
disable_tenant_policy_request_dict = disable_tenant_policy_request_instance.to_dict()
# create an instance of DisableTenantPolicyRequest from a dict
disable_tenant_policy_request_form_dict = disable_tenant_policy_request.from_dict(disable_tenant_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


