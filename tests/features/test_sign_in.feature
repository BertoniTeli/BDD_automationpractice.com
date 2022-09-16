Feature: Test login functionality

  Scenario: Test login pozitive
    Given open the login page
    When the user types username "testDaniel@yahoo.com"
    And the user types password "123456"
    And the user clicks the signin button
    Then the user is redirected to account page
    And the welcome message is displayed
    And the signout button is displayed

  Scenario Outline: check error message with wrong credentials
    Given open the login page
    When the user types username "<username>"
    And the user types password "<password>"
    And the user clicks the signin button
    Then the user is on the alert signin page
    And "<alert>" error message is displayed

    Examples: Username and passwords and message error
      | username             | password | alert                      |
      | testDaniel@yahoo.com | 12r43td  | Authentication failed.     |
      | testDaniel@yahoo.com | 1234     | Invalid password.          |
      | testDaniel@yahoo.com | \\       | Password is required.      |
      | bestDaniel@yahoo.com | 123456   | Authentication failed.     |
      | testDaniel           | 123456   | Invalid email address.     |
      | \\                   | 123456   | An email address required. |
    # Figured out that "\\" prints "\" which is fed as blank space to the site