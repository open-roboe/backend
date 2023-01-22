# PollingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pollApiPollingGet**](PollingApi.md#pollApiPollingGet) | **GET** api/polling/ | Poll |
| [**pollRoboaUpdateApiPollingRoboaPost**](PollingApi.md#pollRoboaUpdateApiPollingRoboaPost) | **POST** api/polling/roboa | Poll Roboa Update |
| [**pollUserUpdateApiPollingUserPost**](PollingApi.md#pollUserUpdateApiPollingUserPost) | **POST** api/polling/user | Poll User Update |



## pollApiPollingGet

> PollResponse pollApiPollingGet()

Poll

Polling endpoint, called repeatedly by an authenticated user to get data updates. This endpoint does not update user metrics

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PollingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        PollingApi apiInstance = new PollingApi(defaultClient);
        try {
            PollResponse result = apiInstance.pollApiPollingGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PollingApi#pollApiPollingGet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PollResponse**](PollResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## pollRoboaUpdateApiPollingRoboaPost

> Object pollRoboaUpdateApiPollingRoboaPost(pollRoboaUpdate)

Poll Roboa Update

Polling endpoint, called repeatedly by an authenticated roboa to send its metrics, and receive back commands

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PollingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PollingApi apiInstance = new PollingApi(defaultClient);
        PollRoboaUpdate pollRoboaUpdate = new PollRoboaUpdate(); // PollRoboaUpdate | 
        try {
            Object result = apiInstance.pollRoboaUpdateApiPollingRoboaPost(pollRoboaUpdate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PollingApi#pollRoboaUpdateApiPollingRoboaPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pollRoboaUpdate** | [**PollRoboaUpdate**](PollRoboaUpdate.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |


## pollUserUpdateApiPollingUserPost

> PollResponse pollUserUpdateApiPollingUserPost(pollUserUpdate)

Poll User Update

Polling endpoint, called repeatedly by an authenticated user to send its metrics and get data updates

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PollingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        PollingApi apiInstance = new PollingApi(defaultClient);
        PollUserUpdate pollUserUpdate = new PollUserUpdate(); // PollUserUpdate | 
        try {
            PollResponse result = apiInstance.pollUserUpdateApiPollingUserPost(pollUserUpdate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PollingApi#pollUserUpdateApiPollingUserPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pollUserUpdate** | [**PollUserUpdate**](PollUserUpdate.md)|  | |

### Return type

[**PollResponse**](PollResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

