# GetCloudAccountMetadataResponse

Get Metadata Desponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_accounts_metadata** | [**List[CloudAccountMetadata]**](CloudAccountMetadata.md) | List of cloud accounts | 

## Example

```python
from onelens_backend_client.models.get_cloud_account_metadata_response import GetCloudAccountMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudAccountMetadataResponse from a JSON string
get_cloud_account_metadata_response_instance = GetCloudAccountMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(GetCloudAccountMetadataResponse.to_json())

# convert the object into a dict
get_cloud_account_metadata_response_dict = get_cloud_account_metadata_response_instance.to_dict()
# create an instance of GetCloudAccountMetadataResponse from a dict
get_cloud_account_metadata_response_form_dict = get_cloud_account_metadata_response.from_dict(get_cloud_account_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


