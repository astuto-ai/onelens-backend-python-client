# UpdateUserAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**UserCatalogState**](UserCatalogState.md) |  | [optional] 
**details** | [**UserCatalogDetails**](UserCatalogDetails.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_user_api_request import UpdateUserAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserAPIRequest from a JSON string
update_user_api_request_instance = UpdateUserAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserAPIRequest.to_json())

# convert the object into a dict
update_user_api_request_dict = update_user_api_request_instance.to_dict()
# create an instance of UpdateUserAPIRequest from a dict
update_user_api_request_form_dict = update_user_api_request.from_dict(update_user_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


