# GetAllThreadsFilters

Filters for getting all threads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | [optional] 
**agent_types** | [**List[AgentType]**](AgentType.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_all_threads_filters import GetAllThreadsFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllThreadsFilters from a JSON string
get_all_threads_filters_instance = GetAllThreadsFilters.from_json(json)
# print the JSON string representation of the object
print(GetAllThreadsFilters.to_json())

# convert the object into a dict
get_all_threads_filters_dict = get_all_threads_filters_instance.to_dict()
# create an instance of GetAllThreadsFilters from a dict
get_all_threads_filters_form_dict = get_all_threads_filters.from_dict(get_all_threads_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


