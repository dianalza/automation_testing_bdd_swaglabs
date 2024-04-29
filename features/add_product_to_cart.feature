Feature: Add Product to Shopping Cart

  @T1
  Scenario: Add a product to the shopping cart
    Given I am logged in
    When I open a product and add it to the shopping cart
    And I go to the shopping cart
    Then I should see the product count in the shopping cart
