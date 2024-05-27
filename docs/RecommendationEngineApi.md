# RecommendationEngineApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_recommendations**](RecommendationEngineApi.md#get_recommendations) | Get Recommendations


# **get_recommendations**
> ResponseRecommendationEngineResponse get_recommendations(tenant_id, recommendation_engine_api_request)

Get Recommendations

An API endpoint that retrieves all recommendations for voilations.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.recommendation_engine_api_request import RecommendationEngineAPIRequest
from onelens_backend_client.models.response_recommendation_engine_response import ResponseRecommendationEngineResponse
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
    api_instance = onelens_backend_client.RecommendationEngineApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    recommendation_engine_api_request = onelens_backend_client.RecommendationEngineAPIRequest() # RecommendationEngineAPIRequest | 

    try:
        # Get Recommendations
        api_response = api_instance.get_recommendations(tenant_id, recommendation_engine_api_request)
        print("The response of RecommendationEngineApi->get_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineApi->get_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **recommendation_engine_api_request** | [**RecommendationEngineAPIRequest**](RecommendationEngineAPIRequest.md)|  | 

### Return type

[**ResponseRecommendationEngineResponse**](ResponseRecommendationEngineResponse.md)

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
