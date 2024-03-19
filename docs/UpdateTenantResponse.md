# UpdateTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tenant | 
**domains** | **List[str]** | List of domains associated with the tenant | 
**timezone** | **str** | Timezone of the tenant | 
**id** | **str** | Unique identifier for the tenant | 
**tenant_state** | **str** | State of the tenant | 

## Example

```python
from openapi_client.models.update_tenant_response import UpdateTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantResponse from a JSON string
update_tenant_response_instance = UpdateTenantResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantResponse.to_json())

# convert the object into a dict
update_tenant_response_dict = update_tenant_response_instance.to_dict()
# create an instance of UpdateTenantResponse from a dict
update_tenant_response_form_dict = update_tenant_response.from_dict(update_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


