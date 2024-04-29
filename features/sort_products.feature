Feature: Sort Products in Inventory

  @ascending_price
  Scenario: Sort products in ascending order by price
    Given I am logged in
    When I sort products in ascending order by price
    Then I should see that the products are sorted correctly in ascending order by price

  @descending_price
  Scenario: Sort products in descending order by price
    Given I am logged in
    When I sort products in descending order by price
    Then I should see that the products are sorted correctly in descending order by price

  @ascending_name
  Scenario: Sort products in ascending order by name
    Given I am logged in
    When I sort products in ascending order by name
    Then I should see that the products are sorted correctly in ascending order by name

  @descending_name
  Scenario: Sort products in descending order by name
    Given I am logged in
    When I sort products in descending order by name
    Then I should see that the products are sorted correctly in descending order by name