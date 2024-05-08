# ResponseSetTenantStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_set_tenant_status_response import ResponseSetTenantStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSetTenantStatusResponse from a JSON string
response_set_tenant_status_response_instance = ResponseSetTenantStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseSetTenantStatusResponse.to_json())

# convert the object into a dict
response_set_tenant_status_response_dict = response_set_tenant_status_response_instance.to_dict()
# create an instance of ResponseSetTenantStatusResponse from a dict
response_set_tenant_status_response_form_dict = response_set_tenant_status_response.from_dict(response_set_tenant_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


