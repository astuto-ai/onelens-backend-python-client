# PublishCustomHierarchyRequest

publish custom hierarchy request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.publish_custom_hierarchy_request import PublishCustomHierarchyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishCustomHierarchyRequest from a JSON string
publish_custom_hierarchy_request_instance = PublishCustomHierarchyRequest.from_json(json)
# print the JSON string representation of the object
print(PublishCustomHierarchyRequest.to_json())

# convert the object into a dict
publish_custom_hierarchy_request_dict = publish_custom_hierarchy_request_instance.to_dict()
# create an instance of PublishCustomHierarchyRequest from a dict
publish_custom_hierarchy_request_form_dict = publish_custom_hierarchy_request.from_dict(publish_custom_hierarchy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


