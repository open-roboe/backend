package com.example.roboapp2.api.definition.api;

import com.example.roboapp2.api.definition.CollectionFormats.*;

import retrofit2.Call;
import retrofit2.http.*;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import okhttp3.MultipartBody;

import com.example.roboapp2.api.definition.model.Course;
import com.example.roboapp2.api.definition.model.HTTPValidationError;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public interface CourseApi {
  /**
   * Add Course
   * Add a course
   * @param course  (required)
   * @return Call&lt;Course&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/course/")
  Call<Course> addCourseApiCoursePost(
    @retrofit2.http.Body Course course
  );

  /**
   * Create Marker
   * create a new marker for the specified course ideas: uuid, lat, lon, color
   * @return Call&lt;Object&gt;
   */
  @POST("api/course/marker")
  Call<Object> createMarkerApiCourseMarkerPost();
    

  /**
   * Delete Marker
   * delete a marker
   * @return Call&lt;Object&gt;
   */
  @DELETE("api/course/marker")
  Call<Object> deleteMarkerApiCourseMarkerDelete();
    

  /**
   * Get All Courses
   * get all courses
   * @return Call&lt;List&lt;Course&gt;&gt;
   */
  @GET("api/course/")
  Call<List<Course>> getAllCoursesApiCourseGet();
    

  /**
   * Join Course
   * assign current logged user to specified course
   * @return Call&lt;Object&gt;
   */
  @POST("api/course/join_course")
  Call<Object> joinCourseApiCourseJoinCoursePost();
    

  /**
   * Marker Assign Roboa
   * assign specified roboa to specified marker
   * @return Call&lt;Object&gt;
   */
  @POST("api/course/marker/assign_roboa")
  Call<Object> markerAssignRoboaApiCourseMarkerAssignRoboaPost();
    

  /**
   * Update Marker
   * update a marker
   * @return Call&lt;Object&gt;
   */
  @PUT("api/course/marker")
  Call<Object> updateMarkerApiCourseMarkerPut();
    

}
