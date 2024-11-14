# GetPolicyTicketsExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**sort_criteria** | [**SortCriteria**](SortCriteria.md) |  | [optional] 
**selected_fields** | [**List[TicketsSelectedField]**](TicketsSelectedField.md) |  | [optional] 
**file_extension** | [**ExportFileType**](ExportFileType.md) | export file type | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_policy_tickets_export_request import GetPolicyTicketsExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketsExportRequest from a JSON string
get_policy_tickets_export_request_instance = GetPolicyTicketsExportRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketsExportRequest.to_json())

# convert the object into a dict
get_policy_tickets_export_request_dict = get_policy_tickets_export_request_instance.to_dict()
# create an instance of GetPolicyTicketsExportRequest from a dict
get_policy_tickets_export_request_form_dict = get_policy_tickets_export_request.from_dict(get_policy_tickets_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


