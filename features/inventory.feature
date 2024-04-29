Feature: Test add to cart and remove functionality

  @T3
  Scenario: Test add to cart and remove functionality for one item
    Given I am logged in
    When I open a product and add it to the shopping cart
    Then The cart icon shows there is one item in cart
    When I go to the shopping cart
    Then The Remove button is displayed
    Then The item is displayed in basket
    When I remove the item from the cart
    When I go back to shopping list
    Then The Add to cart button is displayed for the item

