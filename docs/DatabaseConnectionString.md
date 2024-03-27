# DatabaseConnectionString

DB connection string for tenant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from onelens_backend_client.models.database_connection_string import DatabaseConnectionString

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConnectionString from a JSON string
database_connection_string_instance = DatabaseConnectionString.from_json(json)
# print the JSON string representation of the object
print(DatabaseConnectionString.to_json())

# convert the object into a dict
database_connection_string_dict = database_connection_string_instance.to_dict()
# create an instance of DatabaseConnectionString from a dict
database_connection_string_form_dict = database_connection_string.from_dict(database_connection_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


