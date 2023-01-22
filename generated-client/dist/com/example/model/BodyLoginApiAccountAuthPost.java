package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "Body_login_api_account_auth_post")
public class BodyLoginApiAccountAuthPost {

	private java.lang.String grantType;
	private java.lang.String username;
	private java.lang.String password;
	private java.lang.String scope = "";
	private java.lang.String clientId;
	private java.lang.String clientSecret;
	
	public BodyLoginApiAccountAuthPost grantType(java.lang.String grantType) {
		setGrantType(grantType);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "grant_type")
	@javax.validation.constraints.Pattern(regexp = "password")
	public java.lang.String getGrantType() {
		return this.grantType;
	}
	
	public void setGrantType(java.lang.String grantType) {
		this.grantType = grantType;
	}
	
	public BodyLoginApiAccountAuthPost username(java.lang.String username) {
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
	
	public BodyLoginApiAccountAuthPost password(java.lang.String password) {
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
	
	public BodyLoginApiAccountAuthPost scope(java.lang.String scope) {
		setScope(scope);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "scope")
	public java.lang.String getScope() {
		return this.scope;
	}
	
	public void setScope(java.lang.String scope) {
		this.scope = scope;
	}
	
	public BodyLoginApiAccountAuthPost clientId(java.lang.String clientId) {
		setClientId(clientId);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "client_id")
	public java.lang.String getClientId() {
		return this.clientId;
	}
	
	public void setClientId(java.lang.String clientId) {
		this.clientId = clientId;
	}
	
	public BodyLoginApiAccountAuthPost clientSecret(java.lang.String clientSecret) {
		setClientSecret(clientSecret);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "client_secret")
	public java.lang.String getClientSecret() {
		return this.clientSecret;
	}
	
	public void setClientSecret(java.lang.String clientSecret) {
		this.clientSecret = clientSecret;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		BodyLoginApiAccountAuthPost bodyLoginApiAccountAuthPost = (BodyLoginApiAccountAuthPost) o;
		return java.util.Objects.equals(this.grantType, bodyLoginApiAccountAuthPost.grantType)
				&& java.util.Objects.equals(this.username, bodyLoginApiAccountAuthPost.username)
				&& java.util.Objects.equals(this.password, bodyLoginApiAccountAuthPost.password)
				&& java.util.Objects.equals(this.scope, bodyLoginApiAccountAuthPost.scope)
				&& java.util.Objects.equals(this.clientId, bodyLoginApiAccountAuthPost.clientId)
				&& java.util.Objects.equals(this.clientSecret, bodyLoginApiAccountAuthPost.clientSecret);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.grantType, this.username, this.password, this.scope, this.clientId, this.clientSecret);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class BodyLoginApiAccountAuthPost {\n");
		sb.append("    grantType: ").append(toIndentedString(this.grantType)).append("\n");
		sb.append("    username: ").append(toIndentedString(this.username)).append("\n");
		sb.append("    password: ").append(toIndentedString(this.password)).append("\n");
		sb.append("    scope: ").append(toIndentedString(this.scope)).append("\n");
		sb.append("    clientId: ").append(toIndentedString(this.clientId)).append("\n");
		sb.append("    clientSecret: ").append(toIndentedString(this.clientSecret)).append("\n");
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
