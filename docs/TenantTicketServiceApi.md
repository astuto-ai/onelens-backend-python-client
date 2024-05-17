# TenantTicketServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_tickets**](TenantTicketServiceApi.md#create_tenant_tickets) | Creates policy tickets in bulk
[**get_tenant_tickets**](TenantTicketServiceApi.md#get_tenant_tickets) | Retrieves all active tickets of a tenant.
[**update_tenant_ticket_user_state**](TenantTicketServiceApi.md#update_tenant_ticket_user_state) | Update tenant policy ticket user state
[**update_tenant_tickets**](TenantTicketServiceApi.md#update_tenant_tickets) | Updates policy tickets in bulk


# **create_tenant_tickets**
> object create_tenant_tickets(create_tenant_tickets_request)

Creates policy tickets in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_tickets_request import CreateTenantTicketsRequest
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
    api_instance = onelens_backend_client.TenantTicketServiceApi(api_client)
    create_tenant_tickets_request = onelens_backend_client.CreateTenantTicketsRequest() # CreateTenantTicketsRequest | 

    try:
        # Creates policy tickets in bulk
        api_response = api_instance.create_tenant_tickets(create_tenant_tickets_request)
        print("The response of TenantTicketServiceApi->create_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->create_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_tickets_request** | [**CreateTenantTicketsRequest**](CreateTenantTicketsRequest.md)|  | 

### Return type

**object**

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

# **get_tenant_tickets**
> GetTenantTicketsResponse get_tenant_tickets(get_tenant_tickets_request)

Retrieves all active tickets of a tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_tickets_request import GetTenantTicketsRequest
from onelens_backend_client.models.get_tenant_tickets_response import GetTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantTicketServiceApi(api_client)
    get_tenant_tickets_request = onelens_backend_client.GetTenantTicketsRequest() # GetTenantTicketsRequest | 

    try:
        # Retrieves all active tickets of a tenant.
        api_response = api_instance.get_tenant_tickets(get_tenant_tickets_request)
        print("The response of TenantTicketServiceApi->get_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_tickets_request** | [**GetTenantTicketsRequest**](GetTenantTicketsRequest.md)|  | 

### Return type

[**GetTenantTicketsResponse**](GetTenantTicketsResponse.md)

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

# **update_tenant_ticket_user_state**
> object update_tenant_ticket_user_state(update_tenant_ticket_user_state_request)

Update tenant policy ticket user state

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_ticket_user_state_request import UpdateTenantTicketUserStateRequest
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
    api_instance = onelens_backend_client.TenantTicketServiceApi(api_client)
    update_tenant_ticket_user_state_request = onelens_backend_client.UpdateTenantTicketUserStateRequest() # UpdateTenantTicketUserStateRequest | 

    try:
        # Update tenant policy ticket user state
        api_response = api_instance.update_tenant_ticket_user_state(update_tenant_ticket_user_state_request)
        print("The response of TenantTicketServiceApi->update_tenant_ticket_user_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->update_tenant_ticket_user_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_ticket_user_state_request** | [**UpdateTenantTicketUserStateRequest**](UpdateTenantTicketUserStateRequest.md)|  | 

### Return type

**object**

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

# **update_tenant_tickets**
> object update_tenant_tickets(update_tenant_tickets_request)

Updates policy tickets in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_tickets_request import UpdateTenantTicketsRequest
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
    api_instance = onelens_backend_client.TenantTicketServiceApi(api_client)
    update_tenant_tickets_request = onelens_backend_client.UpdateTenantTicketsRequest() # UpdateTenantTicketsRequest | 

    try:
        # Updates policy tickets in bulk
        api_response = api_instance.update_tenant_tickets(update_tenant_tickets_request)
        print("The response of TenantTicketServiceApi->update_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->update_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_tickets_request** | [**UpdateTenantTicketsRequest**](UpdateTenantTicketsRequest.md)|  | 

### Return type

**object**

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

