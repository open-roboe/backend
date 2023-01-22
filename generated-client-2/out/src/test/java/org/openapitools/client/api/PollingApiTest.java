package org.openapitools.client.api;

import org.openapitools.client.ApiClient;
import org.openapitools.client.model.HTTPValidationError;
import org.openapitools.client.model.PollResponse;
import org.openapitools.client.model.PollRoboaUpdate;
import org.openapitools.client.model.PollUserUpdate;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PollingApi
 */
public class PollingApiTest {

    private PollingApi api;

    @Before
    public void setup() {
        api = new ApiClient().createService(PollingApi.class);
    }

    /**
     * Poll
     *
     * Polling endpoint, called repeatedly by an authenticated user to get data updates. This endpoint does not update user metrics
     */
    @Test
    public void pollApiPollingGetTest() {
        // PollResponse response = api.pollApiPollingGet();

        // TODO: test validations
    }
    /**
     * Poll Roboa Update
     *
     * Polling endpoint, called repeatedly by an authenticated roboa to send its metrics, and receive back commands
     */
    @Test
    public void pollRoboaUpdateApiPollingRoboaPostTest() {
        PollRoboaUpdate pollRoboaUpdate = null;
        // Object response = api.pollRoboaUpdateApiPollingRoboaPost(pollRoboaUpdate);

        // TODO: test validations
    }
    /**
     * Poll User Update
     *
     * Polling endpoint, called repeatedly by an authenticated user to send its metrics and get data updates
     */
    @Test
    public void pollUserUpdateApiPollingUserPostTest() {
        PollUserUpdate pollUserUpdate = null;
        // PollResponse response = api.pollUserUpdateApiPollingUserPost(pollUserUpdate);

        // TODO: test validations
    }
}
