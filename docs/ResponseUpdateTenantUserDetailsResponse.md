# ResponseUpdateTenantUserDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTenantUserDetailsResponse**](UpdateTenantUserDetailsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_update_tenant_user_details_response import ResponseUpdateTenantUserDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateTenantUserDetailsResponse from a JSON string
response_update_tenant_user_details_response_instance = ResponseUpdateTenantUserDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateTenantUserDetailsResponse.to_json())

# convert the object into a dict
response_update_tenant_user_details_response_dict = response_update_tenant_user_details_response_instance.to_dict()
# create an instance of ResponseUpdateTenantUserDetailsResponse from a dict
response_update_tenant_user_details_response_form_dict = response_update_tenant_user_details_response.from_dict(response_update_tenant_user_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


