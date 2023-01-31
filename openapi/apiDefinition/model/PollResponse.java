/*
 * roboe backend
 *  ### backend server for the roboapp, connecting roboe with the android clients 
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package com.example.roboapp2.api.definition.model;

import java.util.Objects;
import java.util.Arrays;
import com.example.roboapp2.api.definition.model.CourseResponse;
import com.example.roboapp2.api.definition.model.RoboaResponse;
import com.example.roboapp2.api.definition.model.UserResponse;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * PollResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-01-31T03:30:17.483114Z[Etc/UTC]")
public class PollResponse {
  public static final String SERIALIZED_NAME_COURSES = "courses";
  @SerializedName(SERIALIZED_NAME_COURSES)
  private List<CourseResponse> courses = new ArrayList<>();

  public static final String SERIALIZED_NAME_USERS = "users";
  @SerializedName(SERIALIZED_NAME_USERS)
  private List<UserResponse> users = new ArrayList<>();

  public static final String SERIALIZED_NAME_ROBOAS = "roboas";
  @SerializedName(SERIALIZED_NAME_ROBOAS)
  private List<RoboaResponse> roboas = new ArrayList<>();

  public PollResponse() {
  }

  public PollResponse courses(List<CourseResponse> courses) {
    
    this.courses = courses;
    return this;
  }

  public PollResponse addCoursesItem(CourseResponse coursesItem) {
    this.courses.add(coursesItem);
    return this;
  }

   /**
   * Get courses
   * @return courses
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "")

  public List<CourseResponse> getCourses() {
    return courses;
  }


  public void setCourses(List<CourseResponse> courses) {
    this.courses = courses;
  }


  public PollResponse users(List<UserResponse> users) {
    
    this.users = users;
    return this;
  }

  public PollResponse addUsersItem(UserResponse usersItem) {
    this.users.add(usersItem);
    return this;
  }

   /**
   * Get users
   * @return users
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "")

  public List<UserResponse> getUsers() {
    return users;
  }


  public void setUsers(List<UserResponse> users) {
    this.users = users;
  }


  public PollResponse roboas(List<RoboaResponse> roboas) {
    
    this.roboas = roboas;
    return this;
  }

  public PollResponse addRoboasItem(RoboaResponse roboasItem) {
    this.roboas.add(roboasItem);
    return this;
  }

   /**
   * Get roboas
   * @return roboas
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "")

  public List<RoboaResponse> getRoboas() {
    return roboas;
  }


  public void setRoboas(List<RoboaResponse> roboas) {
    this.roboas = roboas;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PollResponse pollResponse = (PollResponse) o;
    return Objects.equals(this.courses, pollResponse.courses) &&
        Objects.equals(this.users, pollResponse.users) &&
        Objects.equals(this.roboas, pollResponse.roboas);
  }

  @Override
  public int hashCode() {
    return Objects.hash(courses, users, roboas);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PollResponse {\n");
    sb.append("    courses: ").append(toIndentedString(courses)).append("\n");
    sb.append("    users: ").append(toIndentedString(users)).append("\n");
    sb.append("    roboas: ").append(toIndentedString(roboas)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

