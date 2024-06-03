# UserCatalogDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | **List[str]** | List of user auth connections. | 

## Example

```python
from onelens_backend_client.models.user_catalog_details import UserCatalogDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserCatalogDetails from a JSON string
user_catalog_details_instance = UserCatalogDetails.from_json(json)
# print the JSON string representation of the object
print(UserCatalogDetails.to_json())

# convert the object into a dict
user_catalog_details_dict = user_catalog_details_instance.to_dict()
# create an instance of UserCatalogDetails from a dict
user_catalog_details_form_dict = user_catalog_details.from_dict(user_catalog_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


