# PolicyRecommendationsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_root_node**](PolicyRecommendationsApi.md#create_root_node) | Create Root Node


# **create_root_node**
> ResponseListRecommendationTicketResponse create_root_node(tenant_id, recommendation_ticket_api_request)

Create Root Node

An API endpoint to create bulk recommendations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.recommendation_ticket_api_request import RecommendationTicketAPIRequest
from onelens_backend_client.models.response_list_recommendation_ticket_response import ResponseListRecommendationTicketResponse
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
    api_instance = onelens_backend_client.PolicyRecommendationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    recommendation_ticket_api_request = [onelens_backend_client.RecommendationTicketAPIRequest()] # List[RecommendationTicketAPIRequest] | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(tenant_id, recommendation_ticket_api_request)
        print("The response of PolicyRecommendationsApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyRecommendationsApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **recommendation_ticket_api_request** | [**List[RecommendationTicketAPIRequest]**](RecommendationTicketAPIRequest.md)|  | 

### Return type

[**ResponseListRecommendationTicketResponse**](ResponseListRecommendationTicketResponse.md)

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

