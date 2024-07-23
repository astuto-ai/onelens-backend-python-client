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
**region** | **str** | Region | 
**account_name** | **str** | Account name | 
**cloud_id** | **str** | Cloud id | 
**cloud_provider** | **str** | Cloud provider | 
**arn** | **str** | Arn | 
**organization_id** | **str** | Organization id | 
**organization_arn** | **str** | Organization arn | 
**run_id** | **str** | The run id. | 
**last_updated_at** | **datetime** | The last updated at. | 

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


