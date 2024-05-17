# CreateDefaultHierarchyRequest

create default hierarchy request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.create_default_hierarchy_request import CreateDefaultHierarchyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefaultHierarchyRequest from a JSON string
create_default_hierarchy_request_instance = CreateDefaultHierarchyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDefaultHierarchyRequest.to_json())

# convert the object into a dict
create_default_hierarchy_request_dict = create_default_hierarchy_request_instance.to_dict()
# create an instance of CreateDefaultHierarchyRequest from a dict
create_default_hierarchy_request_form_dict = create_default_hierarchy_request.from_dict(create_default_hierarchy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


