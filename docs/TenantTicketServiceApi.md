# TenantTicketServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**bulk_update_tenant_tickets**](TenantTicketServiceApi.md#bulk_update_tenant_tickets) | Bulk update tenant tickets
[**create_tenant_tickets**](TenantTicketServiceApi.md#create_tenant_tickets) | Creates policy tickets in bulk
[**export_policy_tickets**](TenantTicketServiceApi.md#export_policy_tickets) | Exports policy tickets to CSV format.
[**get_all_policy_violations**](TenantTicketServiceApi.md#get_all_policy_violations) | Get All Policy Violations
[**get_policy_ticket_stats**](TenantTicketServiceApi.md#get_policy_ticket_stats) | Get Policy Ticket Stats
[**get_policy_ticket_stats_v2**](TenantTicketServiceApi.md#get_policy_ticket_stats_v2) | Get Policy Ticket Stats V2
[**get_policy_tickets_by_entity_id**](TenantTicketServiceApi.md#get_policy_tickets_by_entity_id) | Get Policy Tickets By Entity Id
[**get_policy_tickets_by_policy_id**](TenantTicketServiceApi.md#get_policy_tickets_by_policy_id) | Get Policy Tickets By Policy Id
[**get_tenant_ticket_by_id_with_policy_details**](TenantTicketServiceApi.md#get_tenant_ticket_by_id_with_policy_details) | Retrieves all active tickets of a tenant.
[**get_tenant_tickets**](TenantTicketServiceApi.md#get_tenant_tickets) | Retrieves all active tickets of a tenant.
[**update_tenant_ticket**](TenantTicketServiceApi.md#update_tenant_ticket) | Update tenant policy ticket user state
[**update_tenant_tickets**](TenantTicketServiceApi.md#update_tenant_tickets) | Updates policy tickets in bulk


# **bulk_update_tenant_tickets**
> BulkUpdateTenantTicketsResponse bulk_update_tenant_tickets(bulk_update_tenant_tickets_request)

Bulk update tenant tickets

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.bulk_update_tenant_tickets_request import BulkUpdateTenantTicketsRequest
from onelens_backend_client.models.bulk_update_tenant_tickets_response import BulkUpdateTenantTicketsResponse
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
    bulk_update_tenant_tickets_request = onelens_backend_client.BulkUpdateTenantTicketsRequest() # BulkUpdateTenantTicketsRequest | 

    try:
        # Bulk update tenant tickets
        api_response = api_instance.bulk_update_tenant_tickets(bulk_update_tenant_tickets_request)
        print("The response of TenantTicketServiceApi->bulk_update_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->bulk_update_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_tenant_tickets_request** | [**BulkUpdateTenantTicketsRequest**](BulkUpdateTenantTicketsRequest.md)|  | 

### Return type

[**BulkUpdateTenantTicketsResponse**](BulkUpdateTenantTicketsResponse.md)

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

# **export_policy_tickets**
> GetPolicyTicketsExportToResponseType export_policy_tickets(get_policy_tickets_export_request)

Exports policy tickets to CSV format.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_export_request import GetPolicyTicketsExportRequest
from onelens_backend_client.models.get_policy_tickets_export_to_response_type import GetPolicyTicketsExportToResponseType
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
    get_policy_tickets_export_request = onelens_backend_client.GetPolicyTicketsExportRequest() # GetPolicyTicketsExportRequest | 

    try:
        # Exports policy tickets to CSV format.
        api_response = api_instance.export_policy_tickets(get_policy_tickets_export_request)
        print("The response of TenantTicketServiceApi->export_policy_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->export_policy_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_tickets_export_request** | [**GetPolicyTicketsExportRequest**](GetPolicyTicketsExportRequest.md)|  | 

### Return type

[**GetPolicyTicketsExportToResponseType**](GetPolicyTicketsExportToResponseType.md)

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

# **get_all_policy_violations**
> GetAllPolicyViolationsResponse get_all_policy_violations(get_all_policy_violations_request)

Get All Policy Violations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_policy_violations_request import GetAllPolicyViolationsRequest
from onelens_backend_client.models.get_all_policy_violations_response import GetAllPolicyViolationsResponse
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
    get_all_policy_violations_request = onelens_backend_client.GetAllPolicyViolationsRequest() # GetAllPolicyViolationsRequest | 

    try:
        # Get All Policy Violations
        api_response = api_instance.get_all_policy_violations(get_all_policy_violations_request)
        print("The response of TenantTicketServiceApi->get_all_policy_violations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_all_policy_violations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_policy_violations_request** | [**GetAllPolicyViolationsRequest**](GetAllPolicyViolationsRequest.md)|  | 

### Return type

[**GetAllPolicyViolationsResponse**](GetAllPolicyViolationsResponse.md)

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

# **get_policy_ticket_stats**
> GetPolicyTicketStatsResponse get_policy_ticket_stats(get_policy_ticket_stats_request)

Get Policy Ticket Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_ticket_stats_request import GetPolicyTicketStatsRequest
from onelens_backend_client.models.get_policy_ticket_stats_response import GetPolicyTicketStatsResponse
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
    get_policy_ticket_stats_request = onelens_backend_client.GetPolicyTicketStatsRequest() # GetPolicyTicketStatsRequest | 

    try:
        # Get Policy Ticket Stats
        api_response = api_instance.get_policy_ticket_stats(get_policy_ticket_stats_request)
        print("The response of TenantTicketServiceApi->get_policy_ticket_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_policy_ticket_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_ticket_stats_request** | [**GetPolicyTicketStatsRequest**](GetPolicyTicketStatsRequest.md)|  | 

### Return type

[**GetPolicyTicketStatsResponse**](GetPolicyTicketStatsResponse.md)

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

# **get_policy_ticket_stats_v2**
> GetPolicyTicketStatsResponse get_policy_ticket_stats_v2(get_policy_ticket_stats_request_v2)

Get Policy Ticket Stats V2

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_ticket_stats_request_v2 import GetPolicyTicketStatsRequestV2
from onelens_backend_client.models.get_policy_ticket_stats_response import GetPolicyTicketStatsResponse
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
    get_policy_ticket_stats_request_v2 = onelens_backend_client.GetPolicyTicketStatsRequestV2() # GetPolicyTicketStatsRequestV2 | 

    try:
        # Get Policy Ticket Stats V2
        api_response = api_instance.get_policy_ticket_stats_v2(get_policy_ticket_stats_request_v2)
        print("The response of TenantTicketServiceApi->get_policy_ticket_stats_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_policy_ticket_stats_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_ticket_stats_request_v2** | [**GetPolicyTicketStatsRequestV2**](GetPolicyTicketStatsRequestV2.md)|  | 

### Return type

[**GetPolicyTicketStatsResponse**](GetPolicyTicketStatsResponse.md)

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

# **get_policy_tickets_by_entity_id**
> GetPolicyTicketsByEntityIdResponse get_policy_tickets_by_entity_id(get_policy_tickets_by_entity_id_request)

Get Policy Tickets By Entity Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_entity_id_request import GetPolicyTicketsByEntityIdRequest
from onelens_backend_client.models.get_policy_tickets_by_entity_id_response import GetPolicyTicketsByEntityIdResponse
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
    get_policy_tickets_by_entity_id_request = onelens_backend_client.GetPolicyTicketsByEntityIdRequest() # GetPolicyTicketsByEntityIdRequest | 

    try:
        # Get Policy Tickets By Entity Id
        api_response = api_instance.get_policy_tickets_by_entity_id(get_policy_tickets_by_entity_id_request)
        print("The response of TenantTicketServiceApi->get_policy_tickets_by_entity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_policy_tickets_by_entity_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_tickets_by_entity_id_request** | [**GetPolicyTicketsByEntityIdRequest**](GetPolicyTicketsByEntityIdRequest.md)|  | 

### Return type

[**GetPolicyTicketsByEntityIdResponse**](GetPolicyTicketsByEntityIdResponse.md)

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

# **get_policy_tickets_by_policy_id**
> GetPolicyTicketsByPolicyIdResponse get_policy_tickets_by_policy_id(get_policy_tickets_by_policy_id_request)

Get Policy Tickets By Policy Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_policy_id_request import GetPolicyTicketsByPolicyIdRequest
from onelens_backend_client.models.get_policy_tickets_by_policy_id_response import GetPolicyTicketsByPolicyIdResponse
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
    get_policy_tickets_by_policy_id_request = onelens_backend_client.GetPolicyTicketsByPolicyIdRequest() # GetPolicyTicketsByPolicyIdRequest | 

    try:
        # Get Policy Tickets By Policy Id
        api_response = api_instance.get_policy_tickets_by_policy_id(get_policy_tickets_by_policy_id_request)
        print("The response of TenantTicketServiceApi->get_policy_tickets_by_policy_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_policy_tickets_by_policy_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_tickets_by_policy_id_request** | [**GetPolicyTicketsByPolicyIdRequest**](GetPolicyTicketsByPolicyIdRequest.md)|  | 

### Return type

[**GetPolicyTicketsByPolicyIdResponse**](GetPolicyTicketsByPolicyIdResponse.md)

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

# **get_tenant_ticket_by_id_with_policy_details**
> GetTicketByIdPolicyDetailsResponse get_tenant_ticket_by_id_with_policy_details(get_ticket_by_id_policy_details_request)

Retrieves all active tickets of a tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_ticket_by_id_policy_details_request import GetTicketByIdPolicyDetailsRequest
from onelens_backend_client.models.get_ticket_by_id_policy_details_response import GetTicketByIdPolicyDetailsResponse
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
    get_ticket_by_id_policy_details_request = onelens_backend_client.GetTicketByIdPolicyDetailsRequest() # GetTicketByIdPolicyDetailsRequest | 

    try:
        # Retrieves all active tickets of a tenant.
        api_response = api_instance.get_tenant_ticket_by_id_with_policy_details(get_ticket_by_id_policy_details_request)
        print("The response of TenantTicketServiceApi->get_tenant_ticket_by_id_with_policy_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->get_tenant_ticket_by_id_with_policy_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_ticket_by_id_policy_details_request** | [**GetTicketByIdPolicyDetailsRequest**](GetTicketByIdPolicyDetailsRequest.md)|  | 

### Return type

[**GetTicketByIdPolicyDetailsResponse**](GetTicketByIdPolicyDetailsResponse.md)

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

# **update_tenant_ticket**
> object update_tenant_ticket(update_tenant_ticket_request)

Update tenant policy ticket user state

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_ticket_request import UpdateTenantTicketRequest
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
    update_tenant_ticket_request = onelens_backend_client.UpdateTenantTicketRequest() # UpdateTenantTicketRequest | 

    try:
        # Update tenant policy ticket user state
        api_response = api_instance.update_tenant_ticket(update_tenant_ticket_request)
        print("The response of TenantTicketServiceApi->update_tenant_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantTicketServiceApi->update_tenant_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_ticket_request** | [**UpdateTenantTicketRequest**](UpdateTenantTicketRequest.md)|  | 

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

