package com.example.roboapp2.api.definition.api;

import com.example.roboapp2.api.definition.CollectionFormats.*;

import retrofit2.Call;
import retrofit2.http.*;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import okhttp3.MultipartBody;

import com.example.roboapp2.api.definition.model.HTTPValidationError;
import com.example.roboapp2.api.definition.model.RoboaCreate;
import com.example.roboapp2.api.definition.model.RoboaResponse;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public interface RoboaApi {
  /**
   * Add Roboa
   * Register a new roboa in the system
   * @param roboaCreate  (required)
   * @return Call&lt;RoboaResponse&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("api/roboa/")
  Call<RoboaResponse> addRoboaApiRoboaPost(
    @retrofit2.http.Body RoboaCreate roboaCreate
  );

  /**
   * Delete Roboa
   * TOIMPLEMENT delete a roboa
   * @param name  (required)
   * @return Call&lt;Object&gt;
   */
  @DELETE("api/roboa/{name}")
  Call<Object> deleteRoboaApiRoboaNameDelete(
    @retrofit2.http.Path("name") String name
  );

  /**
   * Get All Roboas
   * get all roboas
   * @return Call&lt;List&lt;RoboaResponse&gt;&gt;
   */
  @GET("api/roboa/")
  Call<List<RoboaResponse>> getAllRoboasApiRoboaGet();
    

  /**
   * Move To Assigned Buoy
   * TOIMPLEMENT set the target coordinates of the specified roboa, causing it to move to the location
   * @param name  (required)
   * @return Call&lt;Object&gt;
   */
  @PUT("api/roboa/{name}/move_to_buoy")
  Call<Object> moveToAssignedBuoyApiRoboaNameMoveToBuoyPut(
    @retrofit2.http.Path("name") String name
  );

}
