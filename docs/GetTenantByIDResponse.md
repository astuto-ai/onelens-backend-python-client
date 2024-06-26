# GetTenantByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tenant | 
**domains** | **List[str]** | List of domains associated with the tenant | 
**org_id** | **str** |  | 
**timezone** | **str** | Timezone of the tenant | 
**id** | **str** | Unique identifier for the tenant | 
**short_id** | **str** | Unique identifier for the tenant | 
**region** | **str** | Region of the tenant | 
**tenant_state** | [**TenantState**](TenantState.md) | State of the tenant | 
**database_connection_string** | **str** |  | 
**s3_bucket_name** | **str** |  | 
**type** | **List[str]** |  | 
**status_reason** | **str** |  | 
**expiry_date** | **datetime** |  | 
**plan** | **str** |  | 
**plan_config** | **object** |  | 
**billing_owner** | **str** |  | 
**billing_type** | **str** |  | 
**milestones** | **List[object]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 

## Example

```python
from onelens_backend_client.models.get_tenant_by_id_response import GetTenantByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantByIDResponse from a JSON string
get_tenant_by_id_response_instance = GetTenantByIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantByIDResponse.to_json())

# convert the object into a dict
get_tenant_by_id_response_dict = get_tenant_by_id_response_instance.to_dict()
# create an instance of GetTenantByIDResponse from a dict
get_tenant_by_id_response_form_dict = get_tenant_by_id_response.from_dict(get_tenant_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


