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
import com.example.roboapp2.api.definition.model.ValidationError;
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
 * HTTPValidationError
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-01-26T15:48:41.153258Z[Etc/UTC]")
public class HTTPValidationError {
  public static final String SERIALIZED_NAME_DETAIL = "detail";
  @SerializedName(SERIALIZED_NAME_DETAIL)
  private List<ValidationError> detail = null;

  public HTTPValidationError() {
  }

  public HTTPValidationError detail(List<ValidationError> detail) {
    
    this.detail = detail;
    return this;
  }

  public HTTPValidationError addDetailItem(ValidationError detailItem) {
    if (this.detail == null) {
      this.detail = new ArrayList<>();
    }
    this.detail.add(detailItem);
    return this;
  }

   /**
   * Get detail
   * @return detail
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<ValidationError> getDetail() {
    return detail;
  }


  public void setDetail(List<ValidationError> detail) {
    this.detail = detail;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HTTPValidationError htTPValidationError = (HTTPValidationError) o;
    return Objects.equals(this.detail, htTPValidationError.detail);
  }

  @Override
  public int hashCode() {
    return Objects.hash(detail);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HTTPValidationError {\n");
    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
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

