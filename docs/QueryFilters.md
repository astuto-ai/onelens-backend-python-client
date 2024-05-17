# QueryFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from onelens_backend_client.models.query_filters import QueryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilters from a JSON string
query_filters_instance = QueryFilters.from_json(json)
# print the JSON string representation of the object
print(QueryFilters.to_json())

# convert the object into a dict
query_filters_dict = query_filters_instance.to_dict()
# create an instance of QueryFilters from a dict
query_filters_form_dict = query_filters.from_dict(query_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


