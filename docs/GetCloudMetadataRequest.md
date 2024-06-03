# GetCloudMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_cloud_metadata_request import GetCloudMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudMetadataRequest from a JSON string
get_cloud_metadata_request_instance = GetCloudMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(GetCloudMetadataRequest.to_json())

# convert the object into a dict
get_cloud_metadata_request_dict = get_cloud_metadata_request_instance.to_dict()
# create an instance of GetCloudMetadataRequest from a dict
get_cloud_metadata_request_form_dict = get_cloud_metadata_request.from_dict(get_cloud_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


