# ResponseGetUsersNodesCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetUsersNodesCategories**](GetUsersNodesCategories.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_users_nodes_categories import ResponseGetUsersNodesCategories

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetUsersNodesCategories from a JSON string
response_get_users_nodes_categories_instance = ResponseGetUsersNodesCategories.from_json(json)
# print the JSON string representation of the object
print(ResponseGetUsersNodesCategories.to_json())

# convert the object into a dict
response_get_users_nodes_categories_dict = response_get_users_nodes_categories_instance.to_dict()
# create an instance of ResponseGetUsersNodesCategories from a dict
response_get_users_nodes_categories_form_dict = response_get_users_nodes_categories.from_dict(response_get_users_nodes_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


