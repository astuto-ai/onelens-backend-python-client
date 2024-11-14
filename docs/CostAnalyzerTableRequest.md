# CostAnalyzerTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | **List[object]** | Filters for the cost analyzer table | 
**group_by** | **List[str]** | Group by for the cost analyzer table | 

## Example

```python
from onelens_backend_client.models.cost_analyzer_table_request import CostAnalyzerTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CostAnalyzerTableRequest from a JSON string
cost_analyzer_table_request_instance = CostAnalyzerTableRequest.from_json(json)
# print the JSON string representation of the object
print(CostAnalyzerTableRequest.to_json())

# convert the object into a dict
cost_analyzer_table_request_dict = cost_analyzer_table_request_instance.to_dict()
# create an instance of CostAnalyzerTableRequest from a dict
cost_analyzer_table_request_form_dict = cost_analyzer_table_request.from_dict(cost_analyzer_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


