Feature: Verify Cart Count after Going Back

  @T7
  Scenario: Verify that cart count remains 1 after going back
    Given I am logged in and have added a product to the cart
    When I go back to the inventory page
    Then I should see that the product count in the shopping cart icon is still 1
