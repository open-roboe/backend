package org.openapitools.client.api;

import org.openapitools.client.ApiClient;
import org.openapitools.client.model.HTTPValidationError;
import org.openapitools.client.model.UserCreate;
import org.openapitools.client.model.UserResponse;
import org.junit.Before;
import org.junit.Test;

import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AccountApi
 */
public class AccountApiTest {

    private AccountApi api;

    @Before
    public void setup() {
        api = new ApiClient().createService(AccountApi.class);
    }

    /**
     * Get Logged Admin User
     *
     * Returns account info, requires authentication in an admin account. Used to test if the current account is admin
     */
    @Test
    public void getLoggedAdminUserApiAccountAdminGetTest() {
        // UserResponse response = api.getLoggedAdminUserApiAccountAdminGet();

        // TODO: test validations
    }
    /**
     * Get Logged Super Admin User
     *
     * Returns account info, requires authentication in a super admin account. Used to test if the current account is super admin
     */
    @Test
    public void getLoggedSuperAdminUserApiAccountSuperAdminGetTest() {
        // UserResponse response = api.getLoggedSuperAdminUserApiAccountSuperAdminGet();

        // TODO: test validations
    }
    /**
     * Get Logged User
     *
     * Returns account info, requires authentication
     */
    @Test
    public void getLoggedUserApiAccountGetTest() {
        // UserResponse response = api.getLoggedUserApiAccountGet();

        // TODO: test validations
    }
    /**
     * Login
     *
     * 
     */
    @Test
    public void loginApiAccountAuthPostTest() {
        String username = null;
        String password = null;
        String grantType = null;
        String scope = null;
        String clientId = null;
        String clientSecret = null;
        // Object response = api.loginApiAccountAuthPost(username, password, grantType, scope, clientId, clientSecret);

        // TODO: test validations
    }
    /**
     * Register
     *
     * TODO: require super admin permissions  Register a new user. Requires authentication in a super admin account
     */
    @Test
    public void registerApiAccountRegisterPostTest() {
        UserCreate userCreate = null;
        // Object response = api.registerApiAccountRegisterPost(userCreate);

        // TODO: test validations
    }
}
