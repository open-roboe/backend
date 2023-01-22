package org.openapitools.client.api;

import org.openapitools.client.ApiClient;
import org.openapitools.client.model.Course;
import org.openapitools.client.model.HTTPValidationError;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CourseApi
 */
public class CourseApiTest {

    private CourseApi api;

    @Before
    public void setup() {
        api = new ApiClient().createService(CourseApi.class);
    }

    /**
     * Add Course
     *
     * Add a course
     */
    @Test
    public void addCourseApiCoursePostTest() {
        Course course = null;
        // Course response = api.addCourseApiCoursePost(course);

        // TODO: test validations
    }
    /**
     * Create Marker
     *
     * create a new marker for the specified course ideas: uuid, lat, lon, color
     */
    @Test
    public void createMarkerApiCourseMarkerPostTest() {
        // Object response = api.createMarkerApiCourseMarkerPost();

        // TODO: test validations
    }
    /**
     * Delete Marker
     *
     * delete a marker
     */
    @Test
    public void deleteMarkerApiCourseMarkerDeleteTest() {
        // Object response = api.deleteMarkerApiCourseMarkerDelete();

        // TODO: test validations
    }
    /**
     * Get All Courses
     *
     * get all courses
     */
    @Test
    public void getAllCoursesApiCourseGetTest() {
        // List<Course> response = api.getAllCoursesApiCourseGet();

        // TODO: test validations
    }
    /**
     * Join Course
     *
     * assign current logged user to specified course
     */
    @Test
    public void joinCourseApiCourseJoinCoursePostTest() {
        // Object response = api.joinCourseApiCourseJoinCoursePost();

        // TODO: test validations
    }
    /**
     * Marker Assign Roboa
     *
     * assign specified roboa to specified marker
     */
    @Test
    public void markerAssignRoboaApiCourseMarkerAssignRoboaPostTest() {
        // Object response = api.markerAssignRoboaApiCourseMarkerAssignRoboaPost();

        // TODO: test validations
    }
    /**
     * Update Marker
     *
     * update a marker
     */
    @Test
    public void updateMarkerApiCourseMarkerPutTest() {
        // Object response = api.updateMarkerApiCourseMarkerPut();

        // TODO: test validations
    }
}
