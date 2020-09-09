Feature: Resource function
  Scenario: I want to create a resource
    Given i'm on the home page
    When I click on the add resource button
    And I fill out the form
    And Click Submit
    Then I should see the resource added to the home page

  Scenario: I want to update a resource
    Given i'm on the home page
    When I click the edit button on a resource
    And I change the form values
    And Click Submit
    Then I should see the resource has changed

  Scenario: I want to delete a resource
    Given i'm on the home page
    Then I delete a resource and see the list shorten