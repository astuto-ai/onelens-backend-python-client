# CloudAccountMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_id** | **str** | The id of the cloud account metadata. | 
**account_aliases** | **List[str]** |  | [optional] 
**organization_available_policy_types** | **List[object]** |  | [optional] 
**akas** | **List[str]** |  | [optional] 
**organization_master_account_arn** | **str** |  | [optional] 
**organization_master_account_email** | **str** |  | [optional] 
**organization_master_account_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**cloud_id** | **str** |  | [optional] 
**cloud_provider** | **str** |  | [optional] 
**arn** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**organization_arn** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 

## Example

```python
from onelens_backend_client.models.cloud_account_metadata import CloudAccountMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAccountMetadata from a JSON string
cloud_account_metadata_instance = CloudAccountMetadata.from_json(json)
# print the JSON string representation of the object
print(CloudAccountMetadata.to_json())

# convert the object into a dict
cloud_account_metadata_dict = cloud_account_metadata_instance.to_dict()
# create an instance of CloudAccountMetadata from a dict
cloud_account_metadata_form_dict = cloud_account_metadata.from_dict(cloud_account_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


