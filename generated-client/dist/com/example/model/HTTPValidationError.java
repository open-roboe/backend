package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "HTTPValidationError")
public class HTTPValidationError {

	private java.util.List<com.example.model.ValidationError> detail;
	
	public HTTPValidationError detail(java.util.List<com.example.model.ValidationError> detail) {
		setDetail(detail);
		return this;
	}
	
	/**
	 * Returns the detail, or if it's {@code null} it first creates a new object,
	 * sets the property to the new object, and then returns it.
	 */
	public java.util.List<com.example.model.ValidationError> detail() {
		if (this.detail == null) {
			this.detail = new java.util.ArrayList<com.example.model.ValidationError>();
		}
		return this.detail;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "detail")
	@javax.validation.Valid
	public java.util.List<com.example.model.ValidationError> getDetail() {
		return this.detail;
	}
	
	public void setDetail(java.util.List<com.example.model.ValidationError> detail) {
		this.detail = detail;
	}
	
	public HTTPValidationError addDetail(com.example.model.ValidationError detail) {
		if (this.detail == null) {
			this.detail = new java.util.ArrayList<com.example.model.ValidationError>();
		}
		this.detail.add(detail);
		return this;
	}
	
	public com.example.model.ValidationError addDetail() {
		com.example.model.ValidationError detail = new com.example.model.ValidationError();
		addDetail(detail);
		return detail;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		HTTPValidationError httpValidationError = (HTTPValidationError) o;
		return java.util.Objects.equals(this.detail, httpValidationError.detail);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.detail);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class HTTPValidationError {\n");
		sb.append("    detail: ").append(toIndentedString(this.detail)).append("\n");
		sb.append("}");
		return sb.toString();
	}
	
	/**
	 * Convert the given object to string with each line indented by 4 spaces
	 * (except the first line).
	 */
	private String toIndentedString(java.lang.Object o) {
		if (o == null) {
			return "null";
		}
		return o.toString().replace("\n", "\n    ");
	}
	
}
