# TenantAnomalyServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**disable_tenant_anomaly_setting**](TenantAnomalyServiceApi.md#disable_tenant_anomaly_setting) | disables an anomaly for a tenant in the tenant DB.
[**enable_tenant_anomaly_setting**](TenantAnomalyServiceApi.md#enable_tenant_anomaly_setting) | enables an anomaly for a tenant in the tenant DB.
[**get_tenant_anomaly_settings**](TenantAnomalyServiceApi.md#get_tenant_anomaly_settings) | Retrieves all tenant anomaly settings, optionally filtered by the parameters in the request.
[**override_tenant_anomaly_setting_config**](TenantAnomalyServiceApi.md#override_tenant_anomaly_setting_config) | Override the tenant anomaly config with the provided config.


# **disable_tenant_anomaly_setting**
> DisableTenantAnomalySettingsResponse disable_tenant_anomaly_setting(disable_tenant_anomaly_settings_request)

disables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.disable_tenant_anomaly_settings_request import DisableTenantAnomalySettingsRequest
from onelens_backend_client.models.disable_tenant_anomaly_settings_response import DisableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomalyServiceApi(api_client)
    disable_tenant_anomaly_settings_request = onelens_backend_client.DisableTenantAnomalySettingsRequest() # DisableTenantAnomalySettingsRequest | 

    try:
        # disables an anomaly for a tenant in the tenant DB.
        api_response = api_instance.disable_tenant_anomaly_setting(disable_tenant_anomaly_settings_request)
        print("The response of TenantAnomalyServiceApi->disable_tenant_anomaly_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomalyServiceApi->disable_tenant_anomaly_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_tenant_anomaly_settings_request** | [**DisableTenantAnomalySettingsRequest**](DisableTenantAnomalySettingsRequest.md)|  | 

### Return type

[**DisableTenantAnomalySettingsResponse**](DisableTenantAnomalySettingsResponse.md)

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

# **enable_tenant_anomaly_setting**
> EnableTenantAnomalySettingsResponse enable_tenant_anomaly_setting(enable_tenant_anomaly_settings_request)

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.enable_tenant_anomaly_settings_request import EnableTenantAnomalySettingsRequest
from onelens_backend_client.models.enable_tenant_anomaly_settings_response import EnableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomalyServiceApi(api_client)
    enable_tenant_anomaly_settings_request = onelens_backend_client.EnableTenantAnomalySettingsRequest() # EnableTenantAnomalySettingsRequest | 

    try:
        # enables an anomaly for a tenant in the tenant DB.
        api_response = api_instance.enable_tenant_anomaly_setting(enable_tenant_anomaly_settings_request)
        print("The response of TenantAnomalyServiceApi->enable_tenant_anomaly_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomalyServiceApi->enable_tenant_anomaly_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_tenant_anomaly_settings_request** | [**EnableTenantAnomalySettingsRequest**](EnableTenantAnomalySettingsRequest.md)|  | 

### Return type

[**EnableTenantAnomalySettingsResponse**](EnableTenantAnomalySettingsResponse.md)

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

# **get_tenant_anomaly_settings**
> GetTenantAnomalySettingsResponse get_tenant_anomaly_settings(get_tenant_anomaly_settings_request)

Retrieves all tenant anomaly settings, optionally filtered by the parameters in the request.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_anomaly_settings_request import GetTenantAnomalySettingsRequest
from onelens_backend_client.models.get_tenant_anomaly_settings_response import GetTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomalyServiceApi(api_client)
    get_tenant_anomaly_settings_request = onelens_backend_client.GetTenantAnomalySettingsRequest() # GetTenantAnomalySettingsRequest | 

    try:
        # Retrieves all tenant anomaly settings, optionally filtered by the parameters in the request.
        api_response = api_instance.get_tenant_anomaly_settings(get_tenant_anomaly_settings_request)
        print("The response of TenantAnomalyServiceApi->get_tenant_anomaly_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomalyServiceApi->get_tenant_anomaly_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_anomaly_settings_request** | [**GetTenantAnomalySettingsRequest**](GetTenantAnomalySettingsRequest.md)|  | 

### Return type

[**GetTenantAnomalySettingsResponse**](GetTenantAnomalySettingsResponse.md)

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

# **override_tenant_anomaly_setting_config**
> OverrideTenantAnomalyConfigResponse override_tenant_anomaly_setting_config(override_tenant_anomaly_config_request)

Override the tenant anomaly config with the provided config.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_anomaly_config_request import OverrideTenantAnomalyConfigRequest
from onelens_backend_client.models.override_tenant_anomaly_config_response import OverrideTenantAnomalyConfigResponse
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
    api_instance = onelens_backend_client.TenantAnomalyServiceApi(api_client)
    override_tenant_anomaly_config_request = onelens_backend_client.OverrideTenantAnomalyConfigRequest() # OverrideTenantAnomalyConfigRequest | 

    try:
        # Override the tenant anomaly config with the provided config.
        api_response = api_instance.override_tenant_anomaly_setting_config(override_tenant_anomaly_config_request)
        print("The response of TenantAnomalyServiceApi->override_tenant_anomaly_setting_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomalyServiceApi->override_tenant_anomaly_setting_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_tenant_anomaly_config_request** | [**OverrideTenantAnomalyConfigRequest**](OverrideTenantAnomalyConfigRequest.md)|  | 

### Return type

[**OverrideTenantAnomalyConfigResponse**](OverrideTenantAnomalyConfigResponse.md)

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

