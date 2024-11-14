# CostAnalyzerTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**data** | **List[object]** | List of dictionaries containing cost analyzer stats | 

## Example

```python
from onelens_backend_client.models.cost_analyzer_table_response import CostAnalyzerTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostAnalyzerTableResponse from a JSON string
cost_analyzer_table_response_instance = CostAnalyzerTableResponse.from_json(json)
# print the JSON string representation of the object
print(CostAnalyzerTableResponse.to_json())

# convert the object into a dict
cost_analyzer_table_response_dict = cost_analyzer_table_response_instance.to_dict()
# create an instance of CostAnalyzerTableResponse from a dict
cost_analyzer_table_response_form_dict = cost_analyzer_table_response.from_dict(cost_analyzer_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


