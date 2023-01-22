package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "Course")
public class Course {

	private java.lang.String name;
	private java.lang.String data = "";
	
	public Course name(java.lang.String name) {
		setName(name);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "name")
	@javax.validation.constraints.NotNull
	public java.lang.String getName() {
		return this.name;
	}
	
	public void setName(java.lang.String name) {
		this.name = name;
	}
	
	public Course data(java.lang.String data) {
		setData(data);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "data")
	public java.lang.String getData() {
		return this.data;
	}
	
	public void setData(java.lang.String data) {
		this.data = data;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		Course course = (Course) o;
		return java.util.Objects.equals(this.name, course.name)
				&& java.util.Objects.equals(this.data, course.data);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.name, this.data);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class Course {\n");
		sb.append("    name: ").append(toIndentedString(this.name)).append("\n");
		sb.append("    data: ").append(toIndentedString(this.data)).append("\n");
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
