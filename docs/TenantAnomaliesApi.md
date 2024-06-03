# TenantAnomaliesApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**disable_tenant_anomaly_setting**](TenantAnomaliesApi.md#disable_tenant_anomaly_setting) | Disable Tenant Anomaly Setting
[**disable_tenant_anomaly_setting_0**](TenantAnomaliesApi.md#disable_tenant_anomaly_setting_0) | Disable Tenant Anomaly Setting
[**enable_tenant_anomaly_setting**](TenantAnomaliesApi.md#enable_tenant_anomaly_setting) | Enable Tenant Anomaly Setting
[**enable_tenant_anomaly_setting_0**](TenantAnomaliesApi.md#enable_tenant_anomaly_setting_0) | Enable Tenant Anomaly Setting
[**get_tenant_anomaly_settings**](TenantAnomaliesApi.md#get_tenant_anomaly_settings) | Get Tenant Anomaly Settings
[**get_tenant_anomaly_settings_0**](TenantAnomaliesApi.md#get_tenant_anomaly_settings_0) | Get Tenant Anomaly Settings
[**override_tenant_anomaly_config**](TenantAnomaliesApi.md#override_tenant_anomaly_config) | Override Tenant Anomaly Config
[**override_tenant_anomaly_config_0**](TenantAnomaliesApi.md#override_tenant_anomaly_config_0) | Override Tenant Anomaly Config


# **disable_tenant_anomaly_setting**
> ResponseEnableTenantAnomalySettingsResponse disable_tenant_anomaly_setting(tenant_id)

Disable Tenant Anomaly Setting

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_anomaly_settings_response import ResponseEnableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Disable Tenant Anomaly Setting
        api_response = api_instance.disable_tenant_anomaly_setting(tenant_id)
        print("The response of TenantAnomaliesApi->disable_tenant_anomaly_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->disable_tenant_anomaly_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseEnableTenantAnomalySettingsResponse**](ResponseEnableTenantAnomalySettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_tenant_anomaly_setting_0**
> ResponseEnableTenantAnomalySettingsResponse disable_tenant_anomaly_setting_0()

Disable Tenant Anomaly Setting

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_anomaly_settings_response import ResponseEnableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)

    try:
        # Disable Tenant Anomaly Setting
        api_response = api_instance.disable_tenant_anomaly_setting_0()
        print("The response of TenantAnomaliesApi->disable_tenant_anomaly_setting_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->disable_tenant_anomaly_setting_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseEnableTenantAnomalySettingsResponse**](ResponseEnableTenantAnomalySettingsResponse.md)

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

# **enable_tenant_anomaly_setting**
> ResponseEnableTenantAnomalySettingsResponse enable_tenant_anomaly_setting(tenant_id)

Enable Tenant Anomaly Setting

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_anomaly_settings_response import ResponseEnableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Enable Tenant Anomaly Setting
        api_response = api_instance.enable_tenant_anomaly_setting(tenant_id)
        print("The response of TenantAnomaliesApi->enable_tenant_anomaly_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->enable_tenant_anomaly_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseEnableTenantAnomalySettingsResponse**](ResponseEnableTenantAnomalySettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_tenant_anomaly_setting_0**
> ResponseEnableTenantAnomalySettingsResponse enable_tenant_anomaly_setting_0()

Enable Tenant Anomaly Setting

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_anomaly_settings_response import ResponseEnableTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)

    try:
        # Enable Tenant Anomaly Setting
        api_response = api_instance.enable_tenant_anomaly_setting_0()
        print("The response of TenantAnomaliesApi->enable_tenant_anomaly_setting_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->enable_tenant_anomaly_setting_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseEnableTenantAnomalySettingsResponse**](ResponseEnableTenantAnomalySettingsResponse.md)

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

# **get_tenant_anomaly_settings**
> ResponseGetTenantAnomalySettingsResponse get_tenant_anomaly_settings(tenant_id, get_tenant_anomaly_settings_api_request)

Get Tenant Anomaly Settings

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_anomaly_settings_api_request import GetTenantAnomalySettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_anomaly_settings_response import ResponseGetTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_anomaly_settings_api_request = onelens_backend_client.GetTenantAnomalySettingsAPIRequest() # GetTenantAnomalySettingsAPIRequest | 

    try:
        # Get Tenant Anomaly Settings
        api_response = api_instance.get_tenant_anomaly_settings(tenant_id, get_tenant_anomaly_settings_api_request)
        print("The response of TenantAnomaliesApi->get_tenant_anomaly_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->get_tenant_anomaly_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_anomaly_settings_api_request** | [**GetTenantAnomalySettingsAPIRequest**](GetTenantAnomalySettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantAnomalySettingsResponse**](ResponseGetTenantAnomalySettingsResponse.md)

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

# **get_tenant_anomaly_settings_0**
> ResponseGetTenantAnomalySettingsResponse get_tenant_anomaly_settings_0(get_tenant_anomaly_settings_api_request)

Get Tenant Anomaly Settings

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_anomaly_settings_api_request import GetTenantAnomalySettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_anomaly_settings_response import ResponseGetTenantAnomalySettingsResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    get_tenant_anomaly_settings_api_request = onelens_backend_client.GetTenantAnomalySettingsAPIRequest() # GetTenantAnomalySettingsAPIRequest | 

    try:
        # Get Tenant Anomaly Settings
        api_response = api_instance.get_tenant_anomaly_settings_0(get_tenant_anomaly_settings_api_request)
        print("The response of TenantAnomaliesApi->get_tenant_anomaly_settings_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->get_tenant_anomaly_settings_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_anomaly_settings_api_request** | [**GetTenantAnomalySettingsAPIRequest**](GetTenantAnomalySettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantAnomalySettingsResponse**](ResponseGetTenantAnomalySettingsResponse.md)

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

# **override_tenant_anomaly_config**
> ResponseOverrideTenantAnomalyConfigResponse override_tenant_anomaly_config(tenant_id, override_tenant_anomaly_config_api_request)

Override Tenant Anomaly Config

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_anomaly_config_api_request import OverrideTenantAnomalyConfigAPIRequest
from onelens_backend_client.models.response_override_tenant_anomaly_config_response import ResponseOverrideTenantAnomalyConfigResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    override_tenant_anomaly_config_api_request = onelens_backend_client.OverrideTenantAnomalyConfigAPIRequest() # OverrideTenantAnomalyConfigAPIRequest | 

    try:
        # Override Tenant Anomaly Config
        api_response = api_instance.override_tenant_anomaly_config(tenant_id, override_tenant_anomaly_config_api_request)
        print("The response of TenantAnomaliesApi->override_tenant_anomaly_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->override_tenant_anomaly_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **override_tenant_anomaly_config_api_request** | [**OverrideTenantAnomalyConfigAPIRequest**](OverrideTenantAnomalyConfigAPIRequest.md)|  | 

### Return type

[**ResponseOverrideTenantAnomalyConfigResponse**](ResponseOverrideTenantAnomalyConfigResponse.md)

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

# **override_tenant_anomaly_config_0**
> ResponseOverrideTenantAnomalyConfigResponse override_tenant_anomaly_config_0(override_tenant_anomaly_config_api_request)

Override Tenant Anomaly Config

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_anomaly_config_api_request import OverrideTenantAnomalyConfigAPIRequest
from onelens_backend_client.models.response_override_tenant_anomaly_config_response import ResponseOverrideTenantAnomalyConfigResponse
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
    api_instance = onelens_backend_client.TenantAnomaliesApi(api_client)
    override_tenant_anomaly_config_api_request = onelens_backend_client.OverrideTenantAnomalyConfigAPIRequest() # OverrideTenantAnomalyConfigAPIRequest | 

    try:
        # Override Tenant Anomaly Config
        api_response = api_instance.override_tenant_anomaly_config_0(override_tenant_anomaly_config_api_request)
        print("The response of TenantAnomaliesApi->override_tenant_anomaly_config_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantAnomaliesApi->override_tenant_anomaly_config_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_tenant_anomaly_config_api_request** | [**OverrideTenantAnomalyConfigAPIRequest**](OverrideTenantAnomalyConfigAPIRequest.md)|  | 

### Return type

[**ResponseOverrideTenantAnomalyConfigResponse**](ResponseOverrideTenantAnomalyConfigResponse.md)

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

