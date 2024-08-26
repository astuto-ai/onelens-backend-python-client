# GetAllNaviraLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**navira_logs** | [**List[NaviraLogResponse]**](NaviraLogResponse.md) | List of Navira Logs. | 

## Example

```python
from onelens_backend_client.models.get_all_navira_log_response import GetAllNaviraLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllNaviraLogResponse from a JSON string
get_all_navira_log_response_instance = GetAllNaviraLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllNaviraLogResponse.to_json())

# convert the object into a dict
get_all_navira_log_response_dict = get_all_navira_log_response_instance.to_dict()
# create an instance of GetAllNaviraLogResponse from a dict
get_all_navira_log_response_form_dict = get_all_navira_log_response.from_dict(get_all_navira_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


