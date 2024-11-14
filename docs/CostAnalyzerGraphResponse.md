# CostAnalyzerGraphResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | List of dictionaries containing cost analyzer stats | 

## Example

```python
from onelens_backend_client.models.cost_analyzer_graph_response import CostAnalyzerGraphResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostAnalyzerGraphResponse from a JSON string
cost_analyzer_graph_response_instance = CostAnalyzerGraphResponse.from_json(json)
# print the JSON string representation of the object
print(CostAnalyzerGraphResponse.to_json())

# convert the object into a dict
cost_analyzer_graph_response_dict = cost_analyzer_graph_response_instance.to_dict()
# create an instance of CostAnalyzerGraphResponse from a dict
cost_analyzer_graph_response_form_dict = cost_analyzer_graph_response.from_dict(cost_analyzer_graph_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


