Feature: Resource function
  Scenario: I want to create a resource
    Given i'm on the home page
    When I click on the add resource button
    And I fill out the form
    And Click Submit
    Then I should see the resource added to the home page

  Scenario: I want to create a resource
    Given i'm on the home page
    When I delete the resource named 'Google'
    Then I should see the resource added to the home page