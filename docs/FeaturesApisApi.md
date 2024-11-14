# FeaturesApisApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all_features**](FeaturesApisApi.md#get_all_features) | Get All Features
[**get_features_by_scope**](FeaturesApisApi.md#get_features_by_scope) | Get Features By Scope
[**update_feature_status_disabled**](FeaturesApisApi.md#update_feature_status_disabled) | Update Feature Status Disabled
[**update_feature_status_enabled**](FeaturesApisApi.md#update_feature_status_enabled) | Update Feature Status Enabled


# **get_all_features**
> GetAllFeaturesResponse get_all_features()

Get All Features

Get all features

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
    api_instance = onelens_backend_client.FeaturesApisApi(api_client)

    try:
        # Get All Features
        api_response = api_instance.get_all_features()
        print("The response of FeaturesApisApi->get_all_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApisApi->get_all_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllFeaturesResponse**](GetAllFeaturesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_features_by_scope**
> GetFeaturesByFiltersResponse get_features_by_scope(api_get_features_by_filters_request)

Get Features By Scope

Get features by scope

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
    api_instance = onelens_backend_client.FeaturesApisApi(api_client)
    api_get_features_by_filters_request = onelens_backend_client.APIGetFeaturesByFiltersRequest() # APIGetFeaturesByFiltersRequest | 

    try:
        # Get Features By Scope
        api_response = api_instance.get_features_by_scope(api_get_features_by_filters_request)
        print("The response of FeaturesApisApi->get_features_by_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApisApi->get_features_by_scope: %s\n" % e)
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

# **update_feature_status_disabled**
> APIUpdateFeatureStatusUpdateResponse update_feature_status_disabled(api_update_feature_status_enabled_request)

Update Feature Status Disabled

Update feature status to disabled

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.api_update_feature_status_enabled_request import APIUpdateFeatureStatusEnabledRequest
from onelens_backend_client.models.api_update_feature_status_update_response import APIUpdateFeatureStatusUpdateResponse
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
    api_instance = onelens_backend_client.FeaturesApisApi(api_client)
    api_update_feature_status_enabled_request = onelens_backend_client.APIUpdateFeatureStatusEnabledRequest() # APIUpdateFeatureStatusEnabledRequest | 

    try:
        # Update Feature Status Disabled
        api_response = api_instance.update_feature_status_disabled(api_update_feature_status_enabled_request)
        print("The response of FeaturesApisApi->update_feature_status_disabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApisApi->update_feature_status_disabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_update_feature_status_enabled_request** | [**APIUpdateFeatureStatusEnabledRequest**](APIUpdateFeatureStatusEnabledRequest.md)|  | 

### Return type

[**APIUpdateFeatureStatusUpdateResponse**](APIUpdateFeatureStatusUpdateResponse.md)

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

# **update_feature_status_enabled**
> APIUpdateFeatureStatusUpdateResponse update_feature_status_enabled(api_update_feature_status_enabled_request)

Update Feature Status Enabled

Update feature status to external enabled

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.api_update_feature_status_enabled_request import APIUpdateFeatureStatusEnabledRequest
from onelens_backend_client.models.api_update_feature_status_update_response import APIUpdateFeatureStatusUpdateResponse
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
    api_instance = onelens_backend_client.FeaturesApisApi(api_client)
    api_update_feature_status_enabled_request = onelens_backend_client.APIUpdateFeatureStatusEnabledRequest() # APIUpdateFeatureStatusEnabledRequest | 

    try:
        # Update Feature Status Enabled
        api_response = api_instance.update_feature_status_enabled(api_update_feature_status_enabled_request)
        print("The response of FeaturesApisApi->update_feature_status_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApisApi->update_feature_status_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_update_feature_status_enabled_request** | [**APIUpdateFeatureStatusEnabledRequest**](APIUpdateFeatureStatusEnabledRequest.md)|  | 

### Return type

[**APIUpdateFeatureStatusUpdateResponse**](APIUpdateFeatureStatusUpdateResponse.md)

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

