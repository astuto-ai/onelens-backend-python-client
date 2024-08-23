# CloudAccountMetadataFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_ids** | **List[str]** |  | [optional] 
**account_names** | **List[str]** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**organization_ids** | **List[str]** |  | [optional] 

## Example

```python
from onelens_backend_client.models.cloud_account_metadata_filters import CloudAccountMetadataFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAccountMetadataFilters from a JSON string
cloud_account_metadata_filters_instance = CloudAccountMetadataFilters.from_json(json)
# print the JSON string representation of the object
print(CloudAccountMetadataFilters.to_json())

# convert the object into a dict
cloud_account_metadata_filters_dict = cloud_account_metadata_filters_instance.to_dict()
# create an instance of CloudAccountMetadataFilters from a dict
cloud_account_metadata_filters_form_dict = cloud_account_metadata_filters.from_dict(cloud_account_metadata_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


