# TenantsTenantTicketsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_tickets**](TenantsTenantTicketsApi.md#create_tenant_tickets) | Create Tenant Tickets
[**get_tenant_tickets**](TenantsTenantTicketsApi.md#get_tenant_tickets) | Get Tenant Tickets
[**update_tenant_ticket**](TenantsTenantTicketsApi.md#update_tenant_ticket) | Update Tenant Ticket
[**update_tenant_tickets**](TenantsTenantTicketsApi.md#update_tenant_tickets) | Update Tenant Tickets


# **create_tenant_tickets**
> ResponseCreateTenantTicketsResponse create_tenant_tickets(tenant_id, create_tenant_tickets_api_request)

Create Tenant Tickets

An API endpoint to create new tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_tickets_api_request import CreateTenantTicketsAPIRequest
from onelens_backend_client.models.response_create_tenant_tickets_response import ResponseCreateTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_tickets_api_request = onelens_backend_client.CreateTenantTicketsAPIRequest() # CreateTenantTicketsAPIRequest | 

    try:
        # Create Tenant Tickets
        api_response = api_instance.create_tenant_tickets(tenant_id, create_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->create_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->create_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_tenant_tickets_api_request** | [**CreateTenantTicketsAPIRequest**](CreateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseCreateTenantTicketsResponse**](ResponseCreateTenantTicketsResponse.md)

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
> ResponseGetTenantTicketsResponse get_tenant_tickets(tenant_id, get_tenant_tickets_api_request)

Get Tenant Tickets

An API endpoint that retrieves active tickets for a tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_tickets_api_request import GetTenantTicketsAPIRequest
from onelens_backend_client.models.response_get_tenant_tickets_response import ResponseGetTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_tickets_api_request = onelens_backend_client.GetTenantTicketsAPIRequest() # GetTenantTicketsAPIRequest | 

    try:
        # Get Tenant Tickets
        api_response = api_instance.get_tenant_tickets(tenant_id, get_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->get_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_tickets_api_request** | [**GetTenantTicketsAPIRequest**](GetTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantTicketsResponse**](ResponseGetTenantTicketsResponse.md)

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

# **update_tenant_ticket**
> ResponseUpdateTenantTicketResponse update_tenant_ticket(tenant_id, ticket_id, update_tenant_ticket_api_request)

Update Tenant Ticket

An API endpoint to update the user state of a ticket

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_ticket_response import ResponseUpdateTenantTicketResponse
from onelens_backend_client.models.update_tenant_ticket_api_request import UpdateTenantTicketAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ticket_id = 'ticket_id_example' # str | 
    update_tenant_ticket_api_request = onelens_backend_client.UpdateTenantTicketAPIRequest() # UpdateTenantTicketAPIRequest | 

    try:
        # Update Tenant Ticket
        api_response = api_instance.update_tenant_ticket(tenant_id, ticket_id, update_tenant_ticket_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ticket_id** | **str**|  | 
 **update_tenant_ticket_api_request** | [**UpdateTenantTicketAPIRequest**](UpdateTenantTicketAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketResponse**](ResponseUpdateTenantTicketResponse.md)

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
> ResponseUpdateTenantTicketsResponse update_tenant_tickets(tenant_id, update_tenant_tickets_api_request)

Update Tenant Tickets

An API endpoint to update tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_tickets_response import ResponseUpdateTenantTicketsResponse
from onelens_backend_client.models.update_tenant_tickets_api_request import UpdateTenantTicketsAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_tenant_tickets_api_request = onelens_backend_client.UpdateTenantTicketsAPIRequest() # UpdateTenantTicketsAPIRequest | 

    try:
        # Update Tenant Tickets
        api_response = api_instance.update_tenant_tickets(tenant_id, update_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_tenant_tickets_api_request** | [**UpdateTenantTicketsAPIRequest**](UpdateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketsResponse**](ResponseUpdateTenantTicketsResponse.md)

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

