from behave import given, when, then
from selenium import webdriver
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page
from pages.shopping_cart_page import ShoppingCartPage

@when('I go to the shopping cart and remove the product')
def step_impl(context):
    context.inventory_page.click_go_to_cart()
    context.shopping_cart_page.remove_product()

@then('I should see that the product is no longer in the shopping cart')
def step_impl(context):
    assert context.shopping_cart_page.is_product_removed()

@then('I should see that the shopping cart icon does not display the product count')
def step_impl(context):
    assert context.shopping_cart_page.is_product_count_zero()
