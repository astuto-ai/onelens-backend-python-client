# FeatureServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all**](FeatureServiceApi.md#get_all) | Get all features of the tenant
[**get_features_by_filters**](FeatureServiceApi.md#get_features_by_filters) | Get features by filters
[**register_all_features**](FeatureServiceApi.md#register_all_features) | Register all service features in the tenant
[**update_feature_status**](FeatureServiceApi.md#update_feature_status) | Enable feature by change manager


# **get_all**
> GetAllFeaturesResponse get_all(body)

Get all features of the tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_features_response import GetAllFeaturesResponse
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
    api_instance = onelens_backend_client.FeatureServiceApi(api_client)
    body = None # object | 

    try:
        # Get all features of the tenant
        api_response = api_instance.get_all(body)
        print("The response of FeatureServiceApi->get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureServiceApi->get_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GetAllFeaturesResponse**](GetAllFeaturesResponse.md)

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

# **get_features_by_filters**
> GetFeaturesByFiltersResponse get_features_by_filters(api_get_features_by_filters_request)

Get features by filters

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.api_get_features_by_filters_request import APIGetFeaturesByFiltersRequest
from onelens_backend_client.models.get_features_by_filters_response import GetFeaturesByFiltersResponse
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
    api_instance = onelens_backend_client.FeatureServiceApi(api_client)
    api_get_features_by_filters_request = onelens_backend_client.APIGetFeaturesByFiltersRequest() # APIGetFeaturesByFiltersRequest | 

    try:
        # Get features by filters
        api_response = api_instance.get_features_by_filters(api_get_features_by_filters_request)
        print("The response of FeatureServiceApi->get_features_by_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureServiceApi->get_features_by_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_get_features_by_filters_request** | [**APIGetFeaturesByFiltersRequest**](APIGetFeaturesByFiltersRequest.md)|  | 

### Return type

[**GetFeaturesByFiltersResponse**](GetFeaturesByFiltersResponse.md)

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

# **register_all_features**
> RegisterAllFeaturesResponse register_all_features(register_all_features_request)

Register all service features in the tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.register_all_features_request import RegisterAllFeaturesRequest
from onelens_backend_client.models.register_all_features_response import RegisterAllFeaturesResponse
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
    api_instance = onelens_backend_client.FeatureServiceApi(api_client)
    register_all_features_request = onelens_backend_client.RegisterAllFeaturesRequest() # RegisterAllFeaturesRequest | 

    try:
        # Register all service features in the tenant
        api_response = api_instance.register_all_features(register_all_features_request)
        print("The response of FeatureServiceApi->register_all_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureServiceApi->register_all_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_all_features_request** | [**RegisterAllFeaturesRequest**](RegisterAllFeaturesRequest.md)|  | 

### Return type

[**RegisterAllFeaturesResponse**](RegisterAllFeaturesResponse.md)

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

# **update_feature_status**
> UpdateFeatureStatusResponse update_feature_status(update_feature_status_request)

Enable feature by change manager

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_feature_status_request import UpdateFeatureStatusRequest
from onelens_backend_client.models.update_feature_status_response import UpdateFeatureStatusResponse
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
    api_instance = onelens_backend_client.FeatureServiceApi(api_client)
    update_feature_status_request = onelens_backend_client.UpdateFeatureStatusRequest() # UpdateFeatureStatusRequest | 

    try:
        # Enable feature by change manager
        api_response = api_instance.update_feature_status(update_feature_status_request)
        print("The response of FeatureServiceApi->update_feature_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureServiceApi->update_feature_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_feature_status_request** | [**UpdateFeatureStatusRequest**](UpdateFeatureStatusRequest.md)|  | 

### Return type

[**UpdateFeatureStatusResponse**](UpdateFeatureStatusResponse.md)

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

