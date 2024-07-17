# RecommendationUnitServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_recommendation_unit**](RecommendationUnitServiceApi.md#create_recommendation_unit) | Create recommendation unit
[**get_recommendation_unit_by_id**](RecommendationUnitServiceApi.md#get_recommendation_unit_by_id) | Retrieves Recommendation unit ID.
[**get_recommendation_units**](RecommendationUnitServiceApi.md#get_recommendation_units) | Retrieves all recommendation units with filters
[**update_recommendation_unit**](RecommendationUnitServiceApi.md#update_recommendation_unit) | Update recommendation unit


# **create_recommendation_unit**
> CreateRecommendationUnitResponse create_recommendation_unit(create_recommendation_unit_request)

Create recommendation unit

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_recommendation_unit_request import CreateRecommendationUnitRequest
from onelens_backend_client.models.create_recommendation_unit_response import CreateRecommendationUnitResponse
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
    api_instance = onelens_backend_client.RecommendationUnitServiceApi(api_client)
    create_recommendation_unit_request = onelens_backend_client.CreateRecommendationUnitRequest() # CreateRecommendationUnitRequest | 

    try:
        # Create recommendation unit
        api_response = api_instance.create_recommendation_unit(create_recommendation_unit_request)
        print("The response of RecommendationUnitServiceApi->create_recommendation_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitServiceApi->create_recommendation_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_recommendation_unit_request** | [**CreateRecommendationUnitRequest**](CreateRecommendationUnitRequest.md)|  | 

### Return type

[**CreateRecommendationUnitResponse**](CreateRecommendationUnitResponse.md)

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

# **get_recommendation_unit_by_id**
> GetRecommendationUnitByIdResponse get_recommendation_unit_by_id(get_recommendation_unit_by_id_request)

Retrieves Recommendation unit ID.

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
    api_instance = onelens_backend_client.RecommendationUnitServiceApi(api_client)
    get_recommendation_unit_by_id_request = onelens_backend_client.GetRecommendationUnitByIdRequest() # GetRecommendationUnitByIdRequest | 

    try:
        # Retrieves Recommendation unit ID.
        api_response = api_instance.get_recommendation_unit_by_id(get_recommendation_unit_by_id_request)
        print("The response of RecommendationUnitServiceApi->get_recommendation_unit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitServiceApi->get_recommendation_unit_by_id: %s\n" % e)
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
> GetRecommendationUnitsResponse get_recommendation_units(get_recommendation_unit_request)

Retrieves all recommendation units with filters

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_recommendation_unit_request import GetRecommendationUnitRequest
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
    api_instance = onelens_backend_client.RecommendationUnitServiceApi(api_client)
    get_recommendation_unit_request = onelens_backend_client.GetRecommendationUnitRequest() # GetRecommendationUnitRequest | 

    try:
        # Retrieves all recommendation units with filters
        api_response = api_instance.get_recommendation_units(get_recommendation_unit_request)
        print("The response of RecommendationUnitServiceApi->get_recommendation_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitServiceApi->get_recommendation_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_recommendation_unit_request** | [**GetRecommendationUnitRequest**](GetRecommendationUnitRequest.md)|  | 

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

# **update_recommendation_unit**
> UpdateRecommendationUnitResponse update_recommendation_unit(update_recommendation_unit_request)

Update recommendation unit

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_recommendation_unit_request import UpdateRecommendationUnitRequest
from onelens_backend_client.models.update_recommendation_unit_response import UpdateRecommendationUnitResponse
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
    api_instance = onelens_backend_client.RecommendationUnitServiceApi(api_client)
    update_recommendation_unit_request = onelens_backend_client.UpdateRecommendationUnitRequest() # UpdateRecommendationUnitRequest | 

    try:
        # Update recommendation unit
        api_response = api_instance.update_recommendation_unit(update_recommendation_unit_request)
        print("The response of RecommendationUnitServiceApi->update_recommendation_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitServiceApi->update_recommendation_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_recommendation_unit_request** | [**UpdateRecommendationUnitRequest**](UpdateRecommendationUnitRequest.md)|  | 

### Return type

[**UpdateRecommendationUnitResponse**](UpdateRecommendationUnitResponse.md)

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

