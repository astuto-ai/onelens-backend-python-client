# GetUsersNodesCategories

get nodes category response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **Dict[str, List[OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2]]** | Dictionary of node categories and their child categories. | 

## Example

```python
from onelens_backend_client.models.get_users_nodes_categories import GetUsersNodesCategories

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersNodesCategories from a JSON string
get_users_nodes_categories_instance = GetUsersNodesCategories.from_json(json)
# print the JSON string representation of the object
print(GetUsersNodesCategories.to_json())

# convert the object into a dict
get_users_nodes_categories_dict = get_users_nodes_categories_instance.to_dict()
# create an instance of GetUsersNodesCategories from a dict
get_users_nodes_categories_form_dict = get_users_nodes_categories.from_dict(get_users_nodes_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


