# RecommendationEngineServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_recommendation_unit_by_id**](RecommendationEngineServiceApi.md#get_recommendation_unit_by_id) | Retrieves all Tenants with filters.
[**get_recommendation_units**](RecommendationEngineServiceApi.md#get_recommendation_units) | Retrieves all recommendation units by filter
[**get_recommendations**](RecommendationEngineServiceApi.md#get_recommendations) | Get recommendations.


# **get_recommendation_unit_by_id**
> GetRecommendationUnitByIdResponse get_recommendation_unit_by_id(get_recommendation_unit_by_id_request)

Retrieves all Tenants with filters.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_recommendation_unit_by_id_request import GetRecommendationUnitByIdRequest
from onelens_backend_client.models.get_recommendation_unit_by_id_response import GetRecommendationUnitByIdResponse
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
    get_recommendation_unit_by_id_request = onelens_backend_client.GetRecommendationUnitByIdRequest() # GetRecommendationUnitByIdRequest | 

    try:
        # Retrieves all Tenants with filters.
        api_response = api_instance.get_recommendation_unit_by_id(get_recommendation_unit_by_id_request)
        print("The response of RecommendationEngineServiceApi->get_recommendation_unit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->get_recommendation_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_recommendation_unit_by_id_request** | [**GetRecommendationUnitByIdRequest**](GetRecommendationUnitByIdRequest.md)|  | 

### Return type

[**GetRecommendationUnitByIdResponse**](GetRecommendationUnitByIdResponse.md)

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

# **get_recommendation_units**
> GetRecommendationUnitsResponse get_recommendation_units(get_recommendation_units_request)

Retrieves all recommendation units by filter

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_recommendation_units_request import GetRecommendationUnitsRequest
from onelens_backend_client.models.get_recommendation_units_response import GetRecommendationUnitsResponse
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
    get_recommendation_units_request = onelens_backend_client.GetRecommendationUnitsRequest() # GetRecommendationUnitsRequest | 

    try:
        # Retrieves all recommendation units by filter
        api_response = api_instance.get_recommendation_units(get_recommendation_units_request)
        print("The response of RecommendationEngineServiceApi->get_recommendation_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->get_recommendation_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_recommendation_units_request** | [**GetRecommendationUnitsRequest**](GetRecommendationUnitsRequest.md)|  | 

### Return type

[**GetRecommendationUnitsResponse**](GetRecommendationUnitsResponse.md)

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

