# RecommendationApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_root_node**](RecommendationApi.md#create_root_node) | Create Root Node
[**get_recommendation_by_ticket_id**](RecommendationApi.md#get_recommendation_by_ticket_id) | Get Recommendation By Ticket Id


# **create_root_node**
> ResponseRecommendationTicketResponse create_root_node(recommendation_ticket_api_request_input)

Create Root Node

An API endpoint to create bulk recommendations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.recommendation_ticket_api_request_input import RecommendationTicketAPIRequestInput
from onelens_backend_client.models.response_recommendation_ticket_response import ResponseRecommendationTicketResponse
from onelens_backend_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = onelens_backend_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with onelens_backend_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelens_backend_client.RecommendationApi(api_client)
    recommendation_ticket_api_request_input = [onelens_backend_client.RecommendationTicketAPIRequestInput()] # List[RecommendationTicketAPIRequestInput] | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(recommendation_ticket_api_request_input)
        print("The response of RecommendationApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_ticket_api_request_input** | [**List[RecommendationTicketAPIRequestInput]**](RecommendationTicketAPIRequestInput.md)|  | 

### Return type

[**ResponseRecommendationTicketResponse**](ResponseRecommendationTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_by_ticket_id**
> ResponseRecommendationTicketResponse get_recommendation_by_ticket_id(ticket_id)

Get Recommendation By Ticket Id

An API endpoint to get recommendations by ticket id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_recommendation_ticket_response import ResponseRecommendationTicketResponse
from onelens_backend_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = onelens_backend_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with onelens_backend_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelens_backend_client.RecommendationApi(api_client)
    ticket_id = 'ticket_id_example' # str | 

    try:
        # Get Recommendation By Ticket Id
        api_response = api_instance.get_recommendation_by_ticket_id(ticket_id)
        print("The response of RecommendationApi->get_recommendation_by_ticket_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationApi->get_recommendation_by_ticket_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**ResponseRecommendationTicketResponse**](ResponseRecommendationTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

