package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "ValidationError")
public class ValidationError {

	private java.util.List<java.lang.String> loc = new java.util.ArrayList<java.lang.String>();
	private java.lang.String msg;
	private java.lang.String type;
	
	public ValidationError loc(java.util.List<java.lang.String> loc) {
		setLoc(loc);
		return this;
	}
	
	/**
	 * Returns the loc, or if it's {@code null} it first creates a new object,
	 * sets the property to the new object, and then returns it.
	 */
	public java.util.List<java.lang.String> loc() {
		if (this.loc == null) {
			this.loc = new java.util.ArrayList<java.lang.String>();
		}
		return this.loc;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "loc")
	@javax.validation.Valid
	@javax.validation.constraints.NotNull
	public java.util.List<java.lang.String> getLoc() {
		return this.loc;
	}
	
	public void setLoc(java.util.List<java.lang.String> loc) {
		this.loc = loc;
	}
	
	public ValidationError addLoc(java.lang.String loc) {
		if (this.loc == null) {
			this.loc = new java.util.ArrayList<java.lang.String>();
		}
		this.loc.add(loc);
		return this;
	}
	
	public ValidationError msg(java.lang.String msg) {
		setMsg(msg);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "msg")
	@javax.validation.constraints.NotNull
	public java.lang.String getMsg() {
		return this.msg;
	}
	
	public void setMsg(java.lang.String msg) {
		this.msg = msg;
	}
	
	public ValidationError type(java.lang.String type) {
		setType(type);
		return this;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "type")
	@javax.validation.constraints.NotNull
	public java.lang.String getType() {
		return this.type;
	}
	
	public void setType(java.lang.String type) {
		this.type = type;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		ValidationError validationError = (ValidationError) o;
		return java.util.Objects.equals(this.loc, validationError.loc)
				&& java.util.Objects.equals(this.msg, validationError.msg)
				&& java.util.Objects.equals(this.type, validationError.type);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.loc, this.msg, this.type);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class ValidationError {\n");
		sb.append("    loc: ").append(toIndentedString(this.loc)).append("\n");
		sb.append("    msg: ").append(toIndentedString(this.msg)).append("\n");
		sb.append("    type: ").append(toIndentedString(this.type)).append("\n");
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
