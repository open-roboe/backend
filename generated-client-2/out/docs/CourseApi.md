# CourseApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCourseApiCoursePost**](CourseApi.md#addCourseApiCoursePost) | **POST** api/course/ | Add Course |
| [**createMarkerApiCourseMarkerPost**](CourseApi.md#createMarkerApiCourseMarkerPost) | **POST** api/course/marker | Create Marker |
| [**deleteMarkerApiCourseMarkerDelete**](CourseApi.md#deleteMarkerApiCourseMarkerDelete) | **DELETE** api/course/marker | Delete Marker |
| [**getAllCoursesApiCourseGet**](CourseApi.md#getAllCoursesApiCourseGet) | **GET** api/course/ | Get All Courses |
| [**joinCourseApiCourseJoinCoursePost**](CourseApi.md#joinCourseApiCourseJoinCoursePost) | **POST** api/course/join_course | Join Course |
| [**markerAssignRoboaApiCourseMarkerAssignRoboaPost**](CourseApi.md#markerAssignRoboaApiCourseMarkerAssignRoboaPost) | **POST** api/course/marker/assign_roboa | Marker Assign Roboa |
| [**updateMarkerApiCourseMarkerPut**](CourseApi.md#updateMarkerApiCourseMarkerPut) | **PUT** api/course/marker | Update Marker |



## addCourseApiCoursePost

> Course addCourseApiCoursePost(course)

Add Course

Add a course

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        Course course = new Course(); // Course | 
        try {
            Course result = apiInstance.addCourseApiCoursePost(course);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#addCourseApiCoursePost");
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
| **course** | [**Course**](Course.md)|  | |

### Return type

[**Course**](Course.md)

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


## createMarkerApiCourseMarkerPost

> Object createMarkerApiCourseMarkerPost()

Create Marker

create a new marker for the specified course ideas: uuid, lat, lon, color

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            Object result = apiInstance.createMarkerApiCourseMarkerPost();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#createMarkerApiCourseMarkerPost");
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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## deleteMarkerApiCourseMarkerDelete

> Object deleteMarkerApiCourseMarkerDelete()

Delete Marker

delete a marker

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            Object result = apiInstance.deleteMarkerApiCourseMarkerDelete();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#deleteMarkerApiCourseMarkerDelete");
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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## getAllCoursesApiCourseGet

> List&lt;Course&gt; getAllCoursesApiCourseGet()

Get All Courses

get all courses

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            List<Course> result = apiInstance.getAllCoursesApiCourseGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#getAllCoursesApiCourseGet");
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

[**List&lt;Course&gt;**](Course.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## joinCourseApiCourseJoinCoursePost

> Object joinCourseApiCourseJoinCoursePost()

Join Course

assign current logged user to specified course

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            Object result = apiInstance.joinCourseApiCourseJoinCoursePost();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#joinCourseApiCourseJoinCoursePost");
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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## markerAssignRoboaApiCourseMarkerAssignRoboaPost

> Object markerAssignRoboaApiCourseMarkerAssignRoboaPost()

Marker Assign Roboa

assign specified roboa to specified marker

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            Object result = apiInstance.markerAssignRoboaApiCourseMarkerAssignRoboaPost();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#markerAssignRoboaApiCourseMarkerAssignRoboaPost");
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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |


## updateMarkerApiCourseMarkerPut

> Object updateMarkerApiCourseMarkerPut()

Update Marker

update a marker

### Example

```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");
        
        // Configure OAuth2 access token for authorization: OAuth2PasswordBearer
        OAuth OAuth2PasswordBearer = (OAuth) defaultClient.getAuthentication("OAuth2PasswordBearer");
        OAuth2PasswordBearer.setAccessToken("YOUR ACCESS TOKEN");

        CourseApi apiInstance = new CourseApi(defaultClient);
        try {
            Object result = apiInstance.updateMarkerApiCourseMarkerPut();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CourseApi#updateMarkerApiCourseMarkerPut");
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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

