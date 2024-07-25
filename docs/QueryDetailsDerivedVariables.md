# QueryDetailsDerivedVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key | 
**value_type** | **str** | Value Type | 
**source_key** | **str** | Source Key | 

## Example

```python
from onelens_backend_client.models.query_details_derived_variables import QueryDetailsDerivedVariables

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDetailsDerivedVariables from a JSON string
query_details_derived_variables_instance = QueryDetailsDerivedVariables.from_json(json)
# print the JSON string representation of the object
print(QueryDetailsDerivedVariables.to_json())

# convert the object into a dict
query_details_derived_variables_dict = query_details_derived_variables_instance.to_dict()
# create an instance of QueryDetailsDerivedVariables from a dict
query_details_derived_variables_form_dict = query_details_derived_variables.from_dict(query_details_derived_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


