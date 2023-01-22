package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "UserResponse")
public class UserResponse {

	private java.lang.String username;
	private java.lang.Boolean admin = java.lang.Boolean.valueOf(true);
	private java.lang.Boolean superAdmin = java.lang.Boolean.valueOf(false);
	private int lastUpdate;
	private java.math.BigDecimal lat = new java.math.BigDecimal("0");
	private java.math.BigDecimal lon = new java.math.BigDecimal("0");
	private java.lang.String courseId;
	
	public UserResponse username(java.lang.String username) {
		setUsername(username);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "username")
	@javax.validation.constraints.NotNull
	public java.lang.String getUsername() {
		return this.username;
	}
	
	public void setUsername(java.lang.String username) {
		this.username = username;
	}
	
	public UserResponse admin(java.lang.Boolean admin) {
		setAdmin(admin);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "admin")
	public java.lang.Boolean getAdmin() {
		return this.admin;
	}
	
	public void setAdmin(java.lang.Boolean admin) {
		this.admin = admin;
	}
	
	public UserResponse superAdmin(java.lang.Boolean superAdmin) {
		setSuperAdmin(superAdmin);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "super_admin")
	public java.lang.Boolean getSuperAdmin() {
		return this.superAdmin;
	}
	
	public void setSuperAdmin(java.lang.Boolean superAdmin) {
		this.superAdmin = superAdmin;
	}
	
	/**
	 */
	public UserResponse lastUpdate(int lastUpdate) {
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
	public UserResponse lat(java.math.BigDecimal lat) {
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
	public UserResponse lon(java.math.BigDecimal lon) {
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
	
	public UserResponse courseId(java.lang.String courseId) {
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
		UserResponse userResponse = (UserResponse) o;
		return java.util.Objects.equals(this.username, userResponse.username)
				&& java.util.Objects.equals(this.admin, userResponse.admin)
				&& java.util.Objects.equals(this.superAdmin, userResponse.superAdmin)
				&& java.util.Objects.equals(this.lastUpdate, userResponse.lastUpdate)
				&& java.util.Objects.equals(this.lat, userResponse.lat)
				&& java.util.Objects.equals(this.lon, userResponse.lon)
				&& java.util.Objects.equals(this.courseId, userResponse.courseId);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.username, this.admin, this.superAdmin, this.lastUpdate, this.lat, this.lon, this.courseId);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class UserResponse {\n");
		sb.append("    username: ").append(toIndentedString(this.username)).append("\n");
		sb.append("    admin: ").append(toIndentedString(this.admin)).append("\n");
		sb.append("    superAdmin: ").append(toIndentedString(this.superAdmin)).append("\n");
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
