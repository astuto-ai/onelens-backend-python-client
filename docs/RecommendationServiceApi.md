# RecommendationServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**bulk_create**](RecommendationServiceApi.md#bulk_create) | Creates bulk recommendations.


# **bulk_create**
> RecommendationTicketResponse bulk_create(recommendation_ticket_request)

Creates bulk recommendations.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.recommendation_ticket_request import RecommendationTicketRequest
from onelens_backend_client.models.recommendation_ticket_response import RecommendationTicketResponse
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
    api_instance = onelens_backend_client.RecommendationServiceApi(api_client)
    recommendation_ticket_request = onelens_backend_client.RecommendationTicketRequest() # RecommendationTicketRequest | 

    try:
        # Creates bulk recommendations.
        api_response = api_instance.bulk_create(recommendation_ticket_request)
        print("The response of RecommendationServiceApi->bulk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationServiceApi->bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_ticket_request** | [**RecommendationTicketRequest**](RecommendationTicketRequest.md)|  | 

### Return type

[**RecommendationTicketResponse**](RecommendationTicketResponse.md)

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

