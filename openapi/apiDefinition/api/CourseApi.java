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
   * assign a roboa to a buoy. This also works for buoys of type jury. Just pass the id of the jury in the buoy_id parameter  This operation will not cause the roboa to move! If you want to move the roboa use the roboa/move endpoint  TECHNICAL NOTES: this endpoint modifies the assigned_buoy row in the roboa table. assigned buoy has a foreign key of type buoy, not of type jury. when a roboa is a ssigned to a jury we are breaking that constraint. This won&#39;t throw errors because sqlite does not enforce foreign keys by default, but it&#39;s also a problem for us, since we will have to handle manually the fact that an assigned id can be a buoy or a jury. Solution: rewrite the database schema, get rid of the jury table. everything is a buoy
   * @param buoyId  (required)
   * @param roboaGet  (required)
   * @return Call&lt;Object&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/course/buoy/{buoy_id}/assign_roboa")
  Call<Object> buoyAssignRoboaApiCourseBuoyBuoyIdAssignRoboaPost(
    @retrofit2.http.Path("buoy_id") String buoyId, @retrofit2.http.Body RoboaGet roboaGet
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
