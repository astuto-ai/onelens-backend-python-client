# UpdateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**org_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_request import UpdateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantRequest from a JSON string
update_tenant_request_instance = UpdateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantRequest.to_json())

# convert the object into a dict
update_tenant_request_dict = update_tenant_request_instance.to_dict()
# create an instance of UpdateTenantRequest from a dict
update_tenant_request_form_dict = update_tenant_request.from_dict(update_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


