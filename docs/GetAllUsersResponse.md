# GetAllUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0_id** | **str** | Auth0 user identifier | 
**state** | [**UserCatalogState**](UserCatalogState.md) |  | [optional] 
**details** | [**UserCatalogDetails**](UserCatalogDetails.md) | Details of the user in catalof DB. | 
**users** | [**List[GetUserByIDResponse]**](GetUserByIDResponse.md) | List of users | 

## Example

```python
from onelens_backend_client.models.get_all_users_response import GetAllUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllUsersResponse from a JSON string
get_all_users_response_instance = GetAllUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllUsersResponse.to_json())

# convert the object into a dict
get_all_users_response_dict = get_all_users_response_instance.to_dict()
# create an instance of GetAllUsersResponse from a dict
get_all_users_response_form_dict = get_all_users_response.from_dict(get_all_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


