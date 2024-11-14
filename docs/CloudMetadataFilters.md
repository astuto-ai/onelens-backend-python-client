# CloudMetadataFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**List[CloudMetadataType]**](CloudMetadataType.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.cloud_metadata_filters import CloudMetadataFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudMetadataFilters from a JSON string
cloud_metadata_filters_instance = CloudMetadataFilters.from_json(json)
# print the JSON string representation of the object
print(CloudMetadataFilters.to_json())

# convert the object into a dict
cloud_metadata_filters_dict = cloud_metadata_filters_instance.to_dict()
# create an instance of CloudMetadataFilters from a dict
cloud_metadata_filters_form_dict = cloud_metadata_filters.from_dict(cloud_metadata_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


