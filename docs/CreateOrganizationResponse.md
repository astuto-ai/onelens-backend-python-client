# CreateOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the organization | 
**id** | **str** | ID of the organization | 
**short_id** | **int** | Unique identifier for the organization | 
**status** | [**OrganizationState**](OrganizationState.md) |  | 
**total_tenants** | **int** |  | 
**country** | **str** |  | 
**industry** | **List[str]** |  | 
**monthly_cloud_spend** | **int** |  | 
**cloud_service_providers** | **List[str]** |  | 
**website** | **str** |  | 
**changelogs** | **List[object]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 

## Example

```python
from onelens_backend_client.models.create_organization_response import CreateOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationResponse from a JSON string
create_organization_response_instance = CreateOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationResponse.to_json())

# convert the object into a dict
create_organization_response_dict = create_organization_response_instance.to_dict()
# create an instance of CreateOrganizationResponse from a dict
create_organization_response_form_dict = create_organization_response.from_dict(create_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


