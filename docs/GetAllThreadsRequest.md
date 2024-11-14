# GetAllThreadsRequest

Request model for getting all threads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**tenant_id** | **str** |  | [optional] 
**filters** | [**GetAllThreadsFilters**](GetAllThreadsFilters.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_all_threads_request import GetAllThreadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllThreadsRequest from a JSON string
get_all_threads_request_instance = GetAllThreadsRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllThreadsRequest.to_json())

# convert the object into a dict
get_all_threads_request_dict = get_all_threads_request_instance.to_dict()
# create an instance of GetAllThreadsRequest from a dict
get_all_threads_request_form_dict = get_all_threads_request.from_dict(get_all_threads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


