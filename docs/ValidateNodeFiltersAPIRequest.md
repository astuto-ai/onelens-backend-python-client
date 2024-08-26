# ValidateNodeFiltersAPIRequest

validate node filters api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) | Resource filters of the node | 
**resource_filter_expression** | **str** | Resource filter expression of the node | 
**node_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.validate_node_filters_api_request import ValidateNodeFiltersAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateNodeFiltersAPIRequest from a JSON string
validate_node_filters_api_request_instance = ValidateNodeFiltersAPIRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateNodeFiltersAPIRequest.to_json())

# convert the object into a dict
validate_node_filters_api_request_dict = validate_node_filters_api_request_instance.to_dict()
# create an instance of ValidateNodeFiltersAPIRequest from a dict
validate_node_filters_api_request_form_dict = validate_node_filters_api_request.from_dict(validate_node_filters_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


