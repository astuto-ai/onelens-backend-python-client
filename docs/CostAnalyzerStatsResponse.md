# CostAnalyzerStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | List of dictionaries containing cost analyzer stats | 

## Example

```python
from onelens_backend_client.models.cost_analyzer_stats_response import CostAnalyzerStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostAnalyzerStatsResponse from a JSON string
cost_analyzer_stats_response_instance = CostAnalyzerStatsResponse.from_json(json)
# print the JSON string representation of the object
print(CostAnalyzerStatsResponse.to_json())

# convert the object into a dict
cost_analyzer_stats_response_dict = cost_analyzer_stats_response_instance.to_dict()
# create an instance of CostAnalyzerStatsResponse from a dict
cost_analyzer_stats_response_form_dict = cost_analyzer_stats_response.from_dict(cost_analyzer_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


