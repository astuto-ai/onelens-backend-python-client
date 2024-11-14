# GetAllThreadsResponse

Response model for getting all threads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**threads** | [**List[Thread]**](Thread.md) | List of threads for the tenant | 

## Example

```python
from onelens_backend_client.models.get_all_threads_response import GetAllThreadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllThreadsResponse from a JSON string
get_all_threads_response_instance = GetAllThreadsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllThreadsResponse.to_json())

# convert the object into a dict
get_all_threads_response_dict = get_all_threads_response_instance.to_dict()
# create an instance of GetAllThreadsResponse from a dict
get_all_threads_response_form_dict = get_all_threads_response.from_dict(get_all_threads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


