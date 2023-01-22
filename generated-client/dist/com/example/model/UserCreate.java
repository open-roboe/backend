package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "UserCreate")
public class UserCreate {

	private java.lang.String username;
	private java.lang.String password;
	private java.lang.Boolean admin = java.lang.Boolean.valueOf(false);
	private java.lang.Boolean superAdmin = java.lang.Boolean.valueOf(false);
	
	public UserCreate username(java.lang.String username) {
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
	
	public UserCreate password(java.lang.String password) {
		setPassword(password);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "password")
	@javax.validation.constraints.NotNull
	public java.lang.String getPassword() {
		return this.password;
	}
	
	public void setPassword(java.lang.String password) {
		this.password = password;
	}
	
	public UserCreate admin(java.lang.Boolean admin) {
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
	
	public UserCreate superAdmin(java.lang.Boolean superAdmin) {
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
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		UserCreate userCreate = (UserCreate) o;
		return java.util.Objects.equals(this.username, userCreate.username)
				&& java.util.Objects.equals(this.password, userCreate.password)
				&& java.util.Objects.equals(this.admin, userCreate.admin)
				&& java.util.Objects.equals(this.superAdmin, userCreate.superAdmin);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.username, this.password, this.admin, this.superAdmin);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class UserCreate {\n");
		sb.append("    username: ").append(toIndentedString(this.username)).append("\n");
		sb.append("    password: ").append(toIndentedString(this.password)).append("\n");
		sb.append("    admin: ").append(toIndentedString(this.admin)).append("\n");
		sb.append("    superAdmin: ").append(toIndentedString(this.superAdmin)).append("\n");
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
