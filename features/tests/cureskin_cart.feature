# Created by hammadchaudhry at 12/14/22
Feature: Test out different features in Cart Page

  Scenario: Continue Shopping button takes to all products when cart is empty
    Given Open cart page
    When Click to Continue Shopping
    Then Verify user is taken to all products

  Scenario: User can access Login page from an empty cart
    Given Open cart page
    When Click on Login link
    Then Verify user is taken to login