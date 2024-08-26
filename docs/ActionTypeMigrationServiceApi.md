# ActionTypeMigrationServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_action_type_pull_request**](ActionTypeMigrationServiceApi.md#create_action_type_pull_request) | Create a pull request for the action_type template
[**sync_action_type_from_repo**](ActionTypeMigrationServiceApi.md#sync_action_type_from_repo) | Sync action_type from repo


# **create_action_type_pull_request**
> CreateActionTypePullResponse create_action_type_pull_request(create_action_type_pull_request)

Create a pull request for the action_type template

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_action_type_pull_request import CreateActionTypePullRequest
from onelens_backend_client.models.create_action_type_pull_response import CreateActionTypePullResponse
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
    api_instance = onelens_backend_client.ActionTypeMigrationServiceApi(api_client)
    create_action_type_pull_request = onelens_backend_client.CreateActionTypePullRequest() # CreateActionTypePullRequest | 

    try:
        # Create a pull request for the action_type template
        api_response = api_instance.create_action_type_pull_request(create_action_type_pull_request)
        print("The response of ActionTypeMigrationServiceApi->create_action_type_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionTypeMigrationServiceApi->create_action_type_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_action_type_pull_request** | [**CreateActionTypePullRequest**](CreateActionTypePullRequest.md)|  | 

### Return type

[**CreateActionTypePullResponse**](CreateActionTypePullResponse.md)

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

# **sync_action_type_from_repo**
> SyncActionTypeFromRepoResponse sync_action_type_from_repo(sync_action_type_from_repo_request)

Sync action_type from repo

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.sync_action_type_from_repo_request import SyncActionTypeFromRepoRequest
from onelens_backend_client.models.sync_action_type_from_repo_response import SyncActionTypeFromRepoResponse
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
    api_instance = onelens_backend_client.ActionTypeMigrationServiceApi(api_client)
    sync_action_type_from_repo_request = onelens_backend_client.SyncActionTypeFromRepoRequest() # SyncActionTypeFromRepoRequest | 

    try:
        # Sync action_type from repo
        api_response = api_instance.sync_action_type_from_repo(sync_action_type_from_repo_request)
        print("The response of ActionTypeMigrationServiceApi->sync_action_type_from_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionTypeMigrationServiceApi->sync_action_type_from_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_action_type_from_repo_request** | [**SyncActionTypeFromRepoRequest**](SyncActionTypeFromRepoRequest.md)|  | 

### Return type

[**SyncActionTypeFromRepoResponse**](SyncActionTypeFromRepoResponse.md)

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

