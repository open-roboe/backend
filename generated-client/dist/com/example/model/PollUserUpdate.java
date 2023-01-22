package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "PollUserUpdate")
public class PollUserUpdate {

	private java.math.BigDecimal lat;
	private java.math.BigDecimal lon;
	
	/**
	 */
	public PollUserUpdate lat(java.math.BigDecimal lat) {
		setLat(lat);
		return this;
	}
	
	/**
	 */
	@com.fasterxml.jackson.annotation.JsonProperty(value = "lat")
	@javax.validation.constraints.NotNull
	public java.math.BigDecimal getLat() {
		return this.lat;
	}
	
	public void setLat(java.math.BigDecimal lat) {
		this.lat = lat;
	}
	
	/**
	 */
	public PollUserUpdate lon(java.math.BigDecimal lon) {
		setLon(lon);
		return this;
	}
	
	/**
	 */
	@com.fasterxml.jackson.annotation.JsonProperty(value = "lon")
	@javax.validation.constraints.NotNull
	public java.math.BigDecimal getLon() {
		return this.lon;
	}
	
	public void setLon(java.math.BigDecimal lon) {
		this.lon = lon;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		PollUserUpdate pollUserUpdate = (PollUserUpdate) o;
		return java.util.Objects.equals(this.lat, pollUserUpdate.lat)
				&& java.util.Objects.equals(this.lon, pollUserUpdate.lon);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.lat, this.lon);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class PollUserUpdate {\n");
		sb.append("    lat: ").append(toIndentedString(this.lat)).append("\n");
		sb.append("    lon: ").append(toIndentedString(this.lon)).append("\n");
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
