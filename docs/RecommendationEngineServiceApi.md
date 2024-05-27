# RecommendationEngineServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_recommendations**](RecommendationEngineServiceApi.md#get_recommendations) | Get recommendations.


# **get_recommendations**
> RecommendationEngineResponse get_recommendations(recommendation_engine_request)

Get recommendations.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.recommendation_engine_request import RecommendationEngineRequest
from onelens_backend_client.models.recommendation_engine_response import RecommendationEngineResponse
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
    api_instance = onelens_backend_client.RecommendationEngineServiceApi(api_client)
    recommendation_engine_request = onelens_backend_client.RecommendationEngineRequest() # RecommendationEngineRequest | 

    try:
        # Get recommendations.
        api_response = api_instance.get_recommendations(recommendation_engine_request)
        print("The response of RecommendationEngineServiceApi->get_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->get_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_engine_request** | [**RecommendationEngineRequest**](RecommendationEngineRequest.md)|  | 

### Return type

[**RecommendationEngineResponse**](RecommendationEngineResponse.md)

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

