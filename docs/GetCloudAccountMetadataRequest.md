# GetCloudAccountMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**CloudAccountMetadataFilters**](CloudAccountMetadataFilters.md) | Filters | 

## Example

```python
from onelens_backend_client.models.get_cloud_account_metadata_request import GetCloudAccountMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudAccountMetadataRequest from a JSON string
get_cloud_account_metadata_request_instance = GetCloudAccountMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(GetCloudAccountMetadataRequest.to_json())

# convert the object into a dict
get_cloud_account_metadata_request_dict = get_cloud_account_metadata_request_instance.to_dict()
# create an instance of GetCloudAccountMetadataRequest from a dict
get_cloud_account_metadata_request_form_dict = get_cloud_account_metadata_request.from_dict(get_cloud_account_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


