# AccountApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLoggedAdminUserApiAccountAdminGet**](AccountApi.md#getLoggedAdminUserApiAccountAdminGet) | **GET** api/account/admin | Get Logged Admin User |
| [**getLoggedSuperAdminUserApiAccountSuperAdminGet**](AccountApi.md#getLoggedSuperAdminUserApiAccountSuperAdminGet) | **GET** api/account/super_admin | Get Logged Super Admin User |
| [**getLoggedUserApiAccountGet**](AccountApi.md#getLoggedUserApiAccountGet) | **GET** api/account/ | Get Logged User |
| [**loginApiAccountAuthPost**](AccountApi.md#loginApiAccountAuthPost) | **POST** api/account/auth | Login |
| [**registerApiAccountRegisterPost**](AccountApi.md#registerApiAccountRegisterPost) | **POST** api/account/register | Register |



## getLoggedAdminUserApiAccountAdminGet

> UserResponse getLoggedAdminUserApiAccountAdminGet()

Get Logged Admin User

Returns account info, requires authentication in an admin account. Used to test if the current account is admin

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        AccountApi apiInstance = new AccountApi(defaultClient);
        try {
            UserResponse result = apiInstance.getLoggedAdminUserApiAccountAdminGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountApi#getLoggedAdminUserApiAccountAdminGet");
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

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## getLoggedSuperAdminUserApiAccountSuperAdminGet

> UserResponse getLoggedSuperAdminUserApiAccountSuperAdminGet()

Get Logged Super Admin User

Returns account info, requires authentication in a super admin account. Used to test if the current account is super admin

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        AccountApi apiInstance = new AccountApi(defaultClient);
        try {
            UserResponse result = apiInstance.getLoggedSuperAdminUserApiAccountSuperAdminGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountApi#getLoggedSuperAdminUserApiAccountSuperAdminGet");
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

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## getLoggedUserApiAccountGet

> UserResponse getLoggedUserApiAccountGet()

Get Logged User

Returns account info, requires authentication

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        AccountApi apiInstance = new AccountApi(defaultClient);
        try {
            UserResponse result = apiInstance.getLoggedUserApiAccountGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountApi#getLoggedUserApiAccountGet");
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

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## loginApiAccountAuthPost

> Object loginApiAccountAuthPost(username, password, grantType, scope, clientId, clientSecret)

Login

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AccountApi apiInstance = new AccountApi(defaultClient);
        String username = "username_example"; // String | 
        String password = "password_example"; // String | 
        String grantType = "grantType_example"; // String | 
        String scope = ""; // String | 
        String clientId = "clientId_example"; // String | 
        String clientSecret = "clientSecret_example"; // String | 
        try {
            Object result = apiInstance.loginApiAccountAuthPost(username, password, grantType, scope, clientId, clientSecret);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountApi#loginApiAccountAuthPost");
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
| **username** | **String**|  | |
| **password** | **String**|  | |
| **grantType** | **String**|  | [optional] |
| **scope** | **String**|  | [optional] [default to ] |
| **clientId** | **String**|  | [optional] |
| **clientSecret** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |


## registerApiAccountRegisterPost

> Object registerApiAccountRegisterPost(userCreate)

Register

TODO: require super admin permissions  Register a new user. Requires authentication in a super admin account

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AccountApi apiInstance = new AccountApi(defaultClient);
        UserCreate userCreate = new UserCreate(); // UserCreate | 
        try {
            Object result = apiInstance.registerApiAccountRegisterPost(userCreate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountApi#registerApiAccountRegisterPost");
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
| **userCreate** | [**UserCreate**](UserCreate.md)|  | |

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

