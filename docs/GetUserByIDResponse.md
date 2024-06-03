# GetUserByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0_id** | **str** | Auth0 user identifier | 
**state** | [**UserCatalogState**](UserCatalogState.md) |  | [optional] 
**details** | [**UserCatalogDetails**](UserCatalogDetails.md) | Details of the user in catalof DB. | 
**id** | **str** | Unique identifier for the user | 

## Example

```python
from onelens_backend_client.models.get_user_by_id_response import GetUserByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserByIDResponse from a JSON string
get_user_by_id_response_instance = GetUserByIDResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserByIDResponse.to_json())

# convert the object into a dict
get_user_by_id_response_dict = get_user_by_id_response_instance.to_dict()
# create an instance of GetUserByIDResponse from a dict
get_user_by_id_response_form_dict = get_user_by_id_response.from_dict(get_user_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


