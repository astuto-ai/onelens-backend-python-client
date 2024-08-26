# GetCurDataAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**CURDataQuery**](CURDataQuery.md) |  | 

## Example

```python
from onelens_backend_client.models.get_cur_data_api_request import GetCurDataAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurDataAPIRequest from a JSON string
get_cur_data_api_request_instance = GetCurDataAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetCurDataAPIRequest.to_json())

# convert the object into a dict
get_cur_data_api_request_dict = get_cur_data_api_request_instance.to_dict()
# create an instance of GetCurDataAPIRequest from a dict
get_cur_data_api_request_form_dict = get_cur_data_api_request.from_dict(get_cur_data_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


