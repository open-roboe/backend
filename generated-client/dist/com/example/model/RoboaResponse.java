package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "RoboaResponse")
public class RoboaResponse {

	private java.lang.String name;
	private int lastUpdate;
	private java.math.BigDecimal lat = new java.math.BigDecimal("0");
	private java.math.BigDecimal lon = new java.math.BigDecimal("0");
	private java.lang.String courseId;
	
	public RoboaResponse name(java.lang.String name) {
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
	
	/**
	 */
	public RoboaResponse lastUpdate(int lastUpdate) {
		setLastUpdate(lastUpdate);
		return this;
	}
	
	/**
	 */
	@com.fasterxml.jackson.annotation.JsonProperty(value = "last_update")
	@javax.validation.constraints.NotNull
	public int getLastUpdate() {
		return this.lastUpdate;
	}
	
	public void setLastUpdate(int lastUpdate) {
		this.lastUpdate = lastUpdate;
	}
	
	/**
	 */
	public RoboaResponse lat(java.math.BigDecimal lat) {
		setLat(lat);
		return this;
	}
	
	/**
	 */
	@com.fasterxml.jackson.annotation.JsonProperty(value = "lat")
	public java.math.BigDecimal getLat() {
		return this.lat;
	}
	
	public void setLat(java.math.BigDecimal lat) {
		this.lat = lat;
	}
	
	/**
	 */
	public RoboaResponse lon(java.math.BigDecimal lon) {
		setLon(lon);
		return this;
	}
	
	/**
	 */
	@com.fasterxml.jackson.annotation.JsonProperty(value = "lon")
	public java.math.BigDecimal getLon() {
		return this.lon;
	}
	
	public void setLon(java.math.BigDecimal lon) {
		this.lon = lon;
	}
	
	public RoboaResponse courseId(java.lang.String courseId) {
		setCourseId(courseId);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "course_id")
	public java.lang.String getCourseId() {
		return this.courseId;
	}
	
	public void setCourseId(java.lang.String courseId) {
		this.courseId = courseId;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		RoboaResponse roboaResponse = (RoboaResponse) o;
		return java.util.Objects.equals(this.name, roboaResponse.name)
				&& java.util.Objects.equals(this.lastUpdate, roboaResponse.lastUpdate)
				&& java.util.Objects.equals(this.lat, roboaResponse.lat)
				&& java.util.Objects.equals(this.lon, roboaResponse.lon)
				&& java.util.Objects.equals(this.courseId, roboaResponse.courseId);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.name, this.lastUpdate, this.lat, this.lon, this.courseId);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class RoboaResponse {\n");
		sb.append("    name: ").append(toIndentedString(this.name)).append("\n");
		sb.append("    lastUpdate: ").append(toIndentedString(this.lastUpdate)).append("\n");
		sb.append("    lat: ").append(toIndentedString(this.lat)).append("\n");
		sb.append("    lon: ").append(toIndentedString(this.lon)).append("\n");
		sb.append("    courseId: ").append(toIndentedString(this.courseId)).append("\n");
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
