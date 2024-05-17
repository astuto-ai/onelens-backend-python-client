# TenantsTenantTicketsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_tickets**](TenantsTenantTicketsApi.md#create_tenant_tickets) | Create Tenant Tickets
[**get_tenant_tickets**](TenantsTenantTicketsApi.md#get_tenant_tickets) | Get Tenant Tickets
[**update_tenant_ticket_user_state**](TenantsTenantTicketsApi.md#update_tenant_ticket_user_state) | Update Tenant Ticket User State
[**update_tenant_tickets**](TenantsTenantTicketsApi.md#update_tenant_tickets) | Update Tenant Tickets


# **create_tenant_tickets**
> ResponseNoneType create_tenant_tickets(tenant_id, tenant_ticket_creation_api_request)

Create Tenant Tickets

An API endpoint to create new tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_none_type import ResponseNoneType
from onelens_backend_client.models.tenant_ticket_creation_api_request import TenantTicketCreationAPIRequest
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
    tenant_ticket_creation_api_request = onelens_backend_client.TenantTicketCreationAPIRequest() # TenantTicketCreationAPIRequest | 

    try:
        # Create Tenant Tickets
        api_response = api_instance.create_tenant_tickets(tenant_id, tenant_ticket_creation_api_request)
        print("The response of TenantsTenantTicketsApi->create_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->create_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_ticket_creation_api_request** | [**TenantTicketCreationAPIRequest**](TenantTicketCreationAPIRequest.md)|  | 

### Return type

[**ResponseNoneType**](ResponseNoneType.md)

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
> ResponseGetTenantTicketsResponse get_tenant_tickets(tenant_id, tenant_tickets_api_request)

Get Tenant Tickets

An API endpoint that retrieves active tickets for a tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_tickets_response import ResponseGetTenantTicketsResponse
from onelens_backend_client.models.tenant_tickets_api_request import TenantTicketsAPIRequest
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
    tenant_tickets_api_request = onelens_backend_client.TenantTicketsAPIRequest() # TenantTicketsAPIRequest | 

    try:
        # Get Tenant Tickets
        api_response = api_instance.get_tenant_tickets(tenant_id, tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->get_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_tickets_api_request** | [**TenantTicketsAPIRequest**](TenantTicketsAPIRequest.md)|  | 

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

# **update_tenant_ticket_user_state**
> object update_tenant_ticket_user_state(tenant_id, ticket_id, tenant_ticket_update_user_state_api_request)

Update Tenant Ticket User State

An API endpoint to update the user state of a ticket

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.tenant_ticket_update_user_state_api_request import TenantTicketUpdateUserStateAPIRequest
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
    tenant_ticket_update_user_state_api_request = onelens_backend_client.TenantTicketUpdateUserStateAPIRequest() # TenantTicketUpdateUserStateAPIRequest | 

    try:
        # Update Tenant Ticket User State
        api_response = api_instance.update_tenant_ticket_user_state(tenant_id, ticket_id, tenant_ticket_update_user_state_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_ticket_user_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_ticket_user_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ticket_id** | **str**|  | 
 **tenant_ticket_update_user_state_api_request** | [**TenantTicketUpdateUserStateAPIRequest**](TenantTicketUpdateUserStateAPIRequest.md)|  | 

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
> ResponseUpdateTenantTicketsResponse update_tenant_tickets(tenant_id, tenant_ticket_updation_api_request)

Update Tenant Tickets

An API endpoint to update tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_tickets_response import ResponseUpdateTenantTicketsResponse
from onelens_backend_client.models.tenant_ticket_updation_api_request import TenantTicketUpdationAPIRequest
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
    tenant_ticket_updation_api_request = onelens_backend_client.TenantTicketUpdationAPIRequest() # TenantTicketUpdationAPIRequest | 

    try:
        # Update Tenant Tickets
        api_response = api_instance.update_tenant_tickets(tenant_id, tenant_ticket_updation_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_ticket_updation_api_request** | [**TenantTicketUpdationAPIRequest**](TenantTicketUpdationAPIRequest.md)|  | 

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

