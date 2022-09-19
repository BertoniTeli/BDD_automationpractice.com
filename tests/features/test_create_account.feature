Feature: Test create account functionality

  Scenario: Test create account pozitive
    Given open the authentication page
    When the user types email address
    And the user clicks the create an account button
    Then the user is redirected to create an account page
    When the user types first name
    And the user types last name "George"
    And the user types password "12345"
    And the user types address
    And the user types city "Tucson"
    And the user selects state from dropdown list
    And the user types zip code
    And the user types mobile phone number
    And the user clicks the register button
    Then the user is redirected to account page
    And the welcome message is displayed