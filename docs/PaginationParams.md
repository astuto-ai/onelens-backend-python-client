# PaginationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page number (1-indexed). | [optional] [default to 1]
**page_size** | **int** | Number of items per page. | [optional] [default to 10]

## Example

```python
from onelens_backend_client.models.pagination_params import PaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationParams from a JSON string
pagination_params_instance = PaginationParams.from_json(json)
# print the JSON string representation of the object
print(PaginationParams.to_json())

# convert the object into a dict
pagination_params_dict = pagination_params_instance.to_dict()
# create an instance of PaginationParams from a dict
pagination_params_form_dict = pagination_params.from_dict(pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


