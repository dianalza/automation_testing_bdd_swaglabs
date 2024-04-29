Feature: Create and verify "Thank you for your order" message

  @T2
  Scenario: User creates an order and verifies "Thank you for your order" message
    Given I am logged in
    When I open a product and add it to the shopping cart
    And I go to the shopping cart
    And I proceed to checkout
    And I enter my shipping information:"John" "Doe" "12345"
    And I click continue
    And I finalize the order
    Then I should see the "Thank you for your order!" message

