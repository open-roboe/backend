package com.example.roboapp2.api.definition.api;

import com.example.roboapp2.api.definition.CollectionFormats.*;

import retrofit2.Call;
import retrofit2.http.*;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import okhttp3.MultipartBody;

import com.example.roboapp2.api.definition.model.CourseCreate;
import com.example.roboapp2.api.definition.model.CourseResponse;
import com.example.roboapp2.api.definition.model.CourseUpdate;
import com.example.roboapp2.api.definition.model.HTTPValidationError;
import com.example.roboapp2.api.definition.model.RoboaGet;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public interface CourseApi {
  /**
   * Add Course
   * TOIMPLEMENT Add a course
   * @param courseCreate  (required)
   * @return Call&lt;CourseResponse&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/course/")
  Call<CourseResponse> addCourseApiCoursePost(
    @retrofit2.http.Body CourseCreate courseCreate
  );

  /**
   * Get All Courses
   * get all courses
   * @return Call&lt;List&lt;CourseResponse&gt;&gt;
   */
  @GET("api/course/")
  Call<List<CourseResponse>> getAllCoursesApiCourseGet();
    

  /**
   * Marker Assign Roboa
   * TOIMPLEMENT assign specified roboa to specified buoy. This operation will not cause the roboa to move If you want to move the roboa use the roboa/move endpoint
   * @param id  (required)
   * @param roboaGet  (required)
   * @return Call&lt;Object&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/course/buoy/{id}/assing_roboa")
  Call<Object> markerAssignRoboaApiCourseBuoyIdAssingRoboaPost(
    @retrofit2.http.Path("id") String id, @retrofit2.http.Body RoboaGet roboaGet
  );

  /**
   * Update Course
   * TOIMPLEMENT create a new buoy for the specified course
   * @param course  (required)
   * @param courseUpdate  (required)
   * @return Call&lt;CourseResponse&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @PUT("api/course/{course}")
  Call<CourseResponse> updateCourseApiCourseCoursePut(
    @retrofit2.http.Path("course") String course, @retrofit2.http.Body CourseUpdate courseUpdate
  );

}
