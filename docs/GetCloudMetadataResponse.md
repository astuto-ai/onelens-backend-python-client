# GetCloudMetadataResponse

Get Metadata Desponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_ids** | **List[object]** | List of Cloud IDs | 
**regions** | **List[object]** | List of regions | 
**services** | **List[object]** | List of services | 
**tag_keys** | **List[object]** | List of tag keys | 
**tag_values** | **List[object]** | List of tag values | 

## Example

```python
from onelens_backend_client.models.get_cloud_metadata_response import GetCloudMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudMetadataResponse from a JSON string
get_cloud_metadata_response_instance = GetCloudMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(GetCloudMetadataResponse.to_json())

# convert the object into a dict
get_cloud_metadata_response_dict = get_cloud_metadata_response_instance.to_dict()
# create an instance of GetCloudMetadataResponse from a dict
get_cloud_metadata_response_form_dict = get_cloud_metadata_response.from_dict(get_cloud_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


