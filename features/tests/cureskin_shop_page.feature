# Created by hammadchaudhry at 12/19/22
Feature: To test out different features in shop pages

  Scenario: Verify that no test products are visible on screen
    Given Open main page
    When Click to Shop All
    And Click to Page 2
    Then Verify that there are no test products