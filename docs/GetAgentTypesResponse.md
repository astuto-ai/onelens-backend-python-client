# GetAgentTypesResponse

Response model for getting agent types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_types** | [**List[AgentType]**](AgentType.md) | List of agent types available for the context | 

## Example

```python
from onelens_backend_client.models.get_agent_types_response import GetAgentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentTypesResponse from a JSON string
get_agent_types_response_instance = GetAgentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAgentTypesResponse.to_json())

# convert the object into a dict
get_agent_types_response_dict = get_agent_types_response_instance.to_dict()
# create an instance of GetAgentTypesResponse from a dict
get_agent_types_response_form_dict = get_agent_types_response.from_dict(get_agent_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


