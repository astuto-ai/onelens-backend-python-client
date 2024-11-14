# CostAnalyzerStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[object]** | Filters for the cost analyzer stats | 
**group_by** | **List[str]** | Group by for the cost analyzer stats | 

## Example

```python
from onelens_backend_client.models.cost_analyzer_stats_request import CostAnalyzerStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CostAnalyzerStatsRequest from a JSON string
cost_analyzer_stats_request_instance = CostAnalyzerStatsRequest.from_json(json)
# print the JSON string representation of the object
print(CostAnalyzerStatsRequest.to_json())

# convert the object into a dict
cost_analyzer_stats_request_dict = cost_analyzer_stats_request_instance.to_dict()
# create an instance of CostAnalyzerStatsRequest from a dict
cost_analyzer_stats_request_form_dict = cost_analyzer_stats_request.from_dict(cost_analyzer_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


