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
   * Add a course, with its jury and buoys.  Courses are the same thing as Regattas. It&#39;s just a synonym
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
   * Buoy Assign Roboa
   * assign a roboa to a buoy. As of now it is not possible to assign a roboa to the jury buoy  This operation will not cause the roboa to move! If you want to move the roboa use the roboa/move endpoint
   * @param courseName  (required)
   * @param buoyId  (required)
   * @param roboaGet  (required)
   * @return Call&lt;Object&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/course/{course_name}/buoy/{buoy_id}/assign_roboa")
  Call<Object> buoyAssignRoboaApiCourseCourseNameBuoyBuoyIdAssignRoboaPost(
    @retrofit2.http.Path("course_name") String courseName, @retrofit2.http.Path("buoy_id") Integer buoyId, @retrofit2.http.Body RoboaGet roboaGet
  );

  /**
   * Get All Courses
   * get all courses
   * @return Call&lt;List&lt;CourseResponse&gt;&gt;
   */
  @GET("api/course/")
  Call<List<CourseResponse>> getAllCoursesApiCourseGet();
    

  /**
   * Update Course
   * 
   * @param courseName  (required)
   * @return Call&lt;Object&gt;
   */
  @DELETE("api/course/{course_name}")
  Call<Object> updateCourseApiCourseCourseNameDelete(
    @retrofit2.http.Path("course_name") String courseName
  );

  /**
   * Update Course
   * update a course  note: course.name, jury.id and buoy.id are identifiers and cannot be changed
   * @param courseUpdate  (required)
   * @return Call&lt;CourseResponse&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @PUT("api/course/")
  Call<CourseResponse> updateCourseApiCoursePut(
    @retrofit2.http.Body CourseUpdate courseUpdate
  );

}
