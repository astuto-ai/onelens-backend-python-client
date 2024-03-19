# PaginationFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | Total number of items. | 
**total_pages** | **int** | Total number of pages. | 
**current_page** | **int** | Current page number. | 
**page_size** | **int** | Number of items per page. | 

## Example

```python
from onelens_backend_client.models.pagination_fields import PaginationFields

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationFields from a JSON string
pagination_fields_instance = PaginationFields.from_json(json)
# print the JSON string representation of the object
print(PaginationFields.to_json())

# convert the object into a dict
pagination_fields_dict = pagination_fields_instance.to_dict()
# create an instance of PaginationFields from a dict
pagination_fields_form_dict = pagination_fields.from_dict(pagination_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


