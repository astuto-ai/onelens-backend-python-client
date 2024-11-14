# GetThreadByIdRequest

Request model for getting a thread by its unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Unique identifier of the thread | 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_thread_by_id_request import GetThreadByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetThreadByIdRequest from a JSON string
get_thread_by_id_request_instance = GetThreadByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetThreadByIdRequest.to_json())

# convert the object into a dict
get_thread_by_id_request_dict = get_thread_by_id_request_instance.to_dict()
# create an instance of GetThreadByIdRequest from a dict
get_thread_by_id_request_form_dict = get_thread_by_id_request.from_dict(get_thread_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


