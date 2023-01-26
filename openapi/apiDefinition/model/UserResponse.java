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
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.math.BigDecimal;

/**
 * UserResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-01-26T15:54:11.750536Z[Etc/UTC]")
public class UserResponse {
  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public static final String SERIALIZED_NAME_ADMIN = "admin";
  @SerializedName(SERIALIZED_NAME_ADMIN)
  private Boolean admin = true;

  public static final String SERIALIZED_NAME_SUPER_ADMIN = "super_admin";
  @SerializedName(SERIALIZED_NAME_SUPER_ADMIN)
  private Boolean superAdmin = false;

  public static final String SERIALIZED_NAME_LAST_UPDATE = "last_update";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE)
  private Integer lastUpdate;

  public static final String SERIALIZED_NAME_LAT = "lat";
  @SerializedName(SERIALIZED_NAME_LAT)
  private BigDecimal lat = new BigDecimal("0");

  public static final String SERIALIZED_NAME_LON = "lon";
  @SerializedName(SERIALIZED_NAME_LON)
  private BigDecimal lon = new BigDecimal("0");

  public static final String SERIALIZED_NAME_COURSE_ID = "course_id";
  @SerializedName(SERIALIZED_NAME_COURSE_ID)
  private String courseId;

  public UserResponse() {
  }

  public UserResponse username(String username) {
    
    this.username = username;
    return this;
  }

   /**
   * Get username
   * @return username
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "")

  public String getUsername() {
    return username;
  }


  public void setUsername(String username) {
    this.username = username;
  }


  public UserResponse admin(Boolean admin) {
    
    this.admin = admin;
    return this;
  }

   /**
   * Get admin
   * @return admin
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getAdmin() {
    return admin;
  }


  public void setAdmin(Boolean admin) {
    this.admin = admin;
  }


  public UserResponse superAdmin(Boolean superAdmin) {
    
    this.superAdmin = superAdmin;
    return this;
  }

   /**
   * Get superAdmin
   * @return superAdmin
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getSuperAdmin() {
    return superAdmin;
  }


  public void setSuperAdmin(Boolean superAdmin) {
    this.superAdmin = superAdmin;
  }


  public UserResponse lastUpdate(Integer lastUpdate) {
    
    this.lastUpdate = lastUpdate;
    return this;
  }

   /**
   * Get lastUpdate
   * @return lastUpdate
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "")

  public Integer getLastUpdate() {
    return lastUpdate;
  }


  public void setLastUpdate(Integer lastUpdate) {
    this.lastUpdate = lastUpdate;
  }


  public UserResponse lat(BigDecimal lat) {
    
    this.lat = lat;
    return this;
  }

   /**
   * Get lat
   * @return lat
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getLat() {
    return lat;
  }


  public void setLat(BigDecimal lat) {
    this.lat = lat;
  }


  public UserResponse lon(BigDecimal lon) {
    
    this.lon = lon;
    return this;
  }

   /**
   * Get lon
   * @return lon
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getLon() {
    return lon;
  }


  public void setLon(BigDecimal lon) {
    this.lon = lon;
  }


  public UserResponse courseId(String courseId) {
    
    this.courseId = courseId;
    return this;
  }

   /**
   * Get courseId
   * @return courseId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getCourseId() {
    return courseId;
  }


  public void setCourseId(String courseId) {
    this.courseId = courseId;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserResponse userResponse = (UserResponse) o;
    return Objects.equals(this.username, userResponse.username) &&
        Objects.equals(this.admin, userResponse.admin) &&
        Objects.equals(this.superAdmin, userResponse.superAdmin) &&
        Objects.equals(this.lastUpdate, userResponse.lastUpdate) &&
        Objects.equals(this.lat, userResponse.lat) &&
        Objects.equals(this.lon, userResponse.lon) &&
        Objects.equals(this.courseId, userResponse.courseId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(username, admin, superAdmin, lastUpdate, lat, lon, courseId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserResponse {\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    admin: ").append(toIndentedString(admin)).append("\n");
    sb.append("    superAdmin: ").append(toIndentedString(superAdmin)).append("\n");
    sb.append("    lastUpdate: ").append(toIndentedString(lastUpdate)).append("\n");
    sb.append("    lat: ").append(toIndentedString(lat)).append("\n");
    sb.append("    lon: ").append(toIndentedString(lon)).append("\n");
    sb.append("    courseId: ").append(toIndentedString(courseId)).append("\n");
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

