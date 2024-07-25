# RecommendationEngineServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_action_type**](RecommendationEngineServiceApi.md#create_action_type) | Create Action Type
[**get_action_types**](RecommendationEngineServiceApi.md#get_action_types) | Get Action Types
[**get_recommendations**](RecommendationEngineServiceApi.md#get_recommendations) | Get recommendations.
[**update_action_type**](RecommendationEngineServiceApi.md#update_action_type) | Update Action Type


# **create_action_type**
> CreateActionTypeResponse create_action_type(create_action_type_request)

Create Action Type

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_action_type_request import CreateActionTypeRequest
from onelens_backend_client.models.create_action_type_response import CreateActionTypeResponse
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
    create_action_type_request = onelens_backend_client.CreateActionTypeRequest() # CreateActionTypeRequest | 

    try:
        # Create Action Type
        api_response = api_instance.create_action_type(create_action_type_request)
        print("The response of RecommendationEngineServiceApi->create_action_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->create_action_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_action_type_request** | [**CreateActionTypeRequest**](CreateActionTypeRequest.md)|  | 

### Return type

[**CreateActionTypeResponse**](CreateActionTypeResponse.md)

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

# **get_action_types**
> GetActionTypeResponse get_action_types(get_action_type_request)

Get Action Types

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_action_type_request import GetActionTypeRequest
from onelens_backend_client.models.get_action_type_response import GetActionTypeResponse
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
    get_action_type_request = onelens_backend_client.GetActionTypeRequest() # GetActionTypeRequest | 

    try:
        # Get Action Types
        api_response = api_instance.get_action_types(get_action_type_request)
        print("The response of RecommendationEngineServiceApi->get_action_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->get_action_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_action_type_request** | [**GetActionTypeRequest**](GetActionTypeRequest.md)|  | 

### Return type

[**GetActionTypeResponse**](GetActionTypeResponse.md)

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

# **update_action_type**
> UpdateActionTypeResponse update_action_type(update_action_type_request)

Update Action Type

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_action_type_request import UpdateActionTypeRequest
from onelens_backend_client.models.update_action_type_response import UpdateActionTypeResponse
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
    update_action_type_request = onelens_backend_client.UpdateActionTypeRequest() # UpdateActionTypeRequest | 

    try:
        # Update Action Type
        api_response = api_instance.update_action_type(update_action_type_request)
        print("The response of RecommendationEngineServiceApi->update_action_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationEngineServiceApi->update_action_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_action_type_request** | [**UpdateActionTypeRequest**](UpdateActionTypeRequest.md)|  | 

### Return type

[**UpdateActionTypeResponse**](UpdateActionTypeResponse.md)

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

