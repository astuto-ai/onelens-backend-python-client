# QueryExecutorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | sql query | 
**recommendation_unit_id** | **str** | Recommendation Unit ID | 

## Example

```python
from onelens_backend_client.models.query_executor_request import QueryExecutorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryExecutorRequest from a JSON string
query_executor_request_instance = QueryExecutorRequest.from_json(json)
# print the JSON string representation of the object
print(QueryExecutorRequest.to_json())

# convert the object into a dict
query_executor_request_dict = query_executor_request_instance.to_dict()
# create an instance of QueryExecutorRequest from a dict
query_executor_request_form_dict = query_executor_request.from_dict(query_executor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


