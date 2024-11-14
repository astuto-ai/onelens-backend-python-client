# GetCloudMetadataAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**CloudMetadataFilters**](CloudMetadataFilters.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_cloud_metadata_api_request import GetCloudMetadataAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudMetadataAPIRequest from a JSON string
get_cloud_metadata_api_request_instance = GetCloudMetadataAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetCloudMetadataAPIRequest.to_json())

# convert the object into a dict
get_cloud_metadata_api_request_dict = get_cloud_metadata_api_request_instance.to_dict()
# create an instance of GetCloudMetadataAPIRequest from a dict
get_cloud_metadata_api_request_form_dict = get_cloud_metadata_api_request.from_dict(get_cloud_metadata_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


