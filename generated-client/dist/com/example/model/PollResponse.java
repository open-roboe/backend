package com.example.model;

@javax.annotation.Generated(value = "@openapi-generator-plus/java-retrofit-client-generator", date = "2023-01-22T15:58:09.326Z")
@javax.xml.bind.annotation.XmlRootElement(name = "PollResponse")
public class PollResponse {

	private java.util.List<com.example.model.Course> courses = new java.util.ArrayList<com.example.model.Course>();
	private java.util.List<com.example.model.UserResponse> users = new java.util.ArrayList<com.example.model.UserResponse>();
	private java.util.List<com.example.model.RoboaResponse> roboas = new java.util.ArrayList<com.example.model.RoboaResponse>();
	
	public PollResponse courses(java.util.List<com.example.model.Course> courses) {
		setCourses(courses);
		return this;
	}
	
	/**
	 * Returns the courses, or if it's {@code null} it first creates a new object,
	 * sets the property to the new object, and then returns it.
	 */
	public java.util.List<com.example.model.Course> courses() {
		if (this.courses == null) {
			this.courses = new java.util.ArrayList<com.example.model.Course>();
		}
		return this.courses;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "courses")
	@javax.validation.Valid
	@javax.validation.constraints.NotNull
	public java.util.List<com.example.model.Course> getCourses() {
		return this.courses;
	}
	
	public void setCourses(java.util.List<com.example.model.Course> courses) {
		this.courses = courses;
	}
	
	public PollResponse addCourse(com.example.model.Course course) {
		if (this.courses == null) {
			this.courses = new java.util.ArrayList<com.example.model.Course>();
		}
		this.courses.add(course);
		return this;
	}
	
	public com.example.model.Course addCourse() {
		com.example.model.Course course = new com.example.model.Course();
		addCourse(course);
		return course;
	}
	
	public PollResponse users(java.util.List<com.example.model.UserResponse> users) {
		setUsers(users);
		return this;
	}
	
	/**
	 * Returns the users, or if it's {@code null} it first creates a new object,
	 * sets the property to the new object, and then returns it.
	 */
	public java.util.List<com.example.model.UserResponse> users() {
		if (this.users == null) {
			this.users = new java.util.ArrayList<com.example.model.UserResponse>();
		}
		return this.users;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "users")
	@javax.validation.Valid
	@javax.validation.constraints.NotNull
	public java.util.List<com.example.model.UserResponse> getUsers() {
		return this.users;
	}
	
	public void setUsers(java.util.List<com.example.model.UserResponse> users) {
		this.users = users;
	}
	
	public PollResponse addUser(com.example.model.UserResponse user) {
		if (this.users == null) {
			this.users = new java.util.ArrayList<com.example.model.UserResponse>();
		}
		this.users.add(user);
		return this;
	}
	
	public com.example.model.UserResponse addUser() {
		com.example.model.UserResponse user = new com.example.model.UserResponse();
		addUser(user);
		return user;
	}
	
	public PollResponse roboas(java.util.List<com.example.model.RoboaResponse> roboas) {
		setRoboas(roboas);
		return this;
	}
	
	/**
	 * Returns the roboas, or if it's {@code null} it first creates a new object,
	 * sets the property to the new object, and then returns it.
	 */
	public java.util.List<com.example.model.RoboaResponse> roboas() {
		if (this.roboas == null) {
			this.roboas = new java.util.ArrayList<com.example.model.RoboaResponse>();
		}
		return this.roboas;
	}
	
	@com.fasterxml.jackson.annotation.JsonProperty(value = "roboas")
	@javax.validation.Valid
	@javax.validation.constraints.NotNull
	public java.util.List<com.example.model.RoboaResponse> getRoboas() {
		return this.roboas;
	}
	
	public void setRoboas(java.util.List<com.example.model.RoboaResponse> roboas) {
		this.roboas = roboas;
	}
	
	public PollResponse addRoboa(com.example.model.RoboaResponse roboa) {
		if (this.roboas == null) {
			this.roboas = new java.util.ArrayList<com.example.model.RoboaResponse>();
		}
		this.roboas.add(roboa);
		return this;
	}
	
	public com.example.model.RoboaResponse addRoboa() {
		com.example.model.RoboaResponse roboa = new com.example.model.RoboaResponse();
		addRoboa(roboa);
		return roboa;
	}
	
	@Override
	public boolean equals(java.lang.Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		PollResponse pollResponse = (PollResponse) o;
		return java.util.Objects.equals(this.courses, pollResponse.courses)
				&& java.util.Objects.equals(this.users, pollResponse.users)
				&& java.util.Objects.equals(this.roboas, pollResponse.roboas);
	}
	
	@Override
	public int hashCode() {
		return java.util.Objects.hash(this.courses, this.users, this.roboas);
	}
	
	@Override
	public java.lang.String toString() {
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("class PollResponse {\n");
		sb.append("    courses: ").append(toIndentedString(this.courses)).append("\n");
		sb.append("    users: ").append(toIndentedString(this.users)).append("\n");
		sb.append("    roboas: ").append(toIndentedString(this.roboas)).append("\n");
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
