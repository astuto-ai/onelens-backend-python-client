# GetPolicyTicketsByPolicyIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**sort_criteria** | [**SortCriteria**](SortCriteria.md) |  | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_policy_tickets_by_policy_id_request import GetPolicyTicketsByPolicyIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketsByPolicyIdRequest from a JSON string
get_policy_tickets_by_policy_id_request_instance = GetPolicyTicketsByPolicyIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketsByPolicyIdRequest.to_json())

# convert the object into a dict
get_policy_tickets_by_policy_id_request_dict = get_policy_tickets_by_policy_id_request_instance.to_dict()
# create an instance of GetPolicyTicketsByPolicyIdRequest from a dict
get_policy_tickets_by_policy_id_request_form_dict = get_policy_tickets_by_policy_id_request.from_dict(get_policy_tickets_by_policy_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


