from behave import given, when, then
from selenium import webdriver
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page
from pages.shopping_cart_page import ShoppingCartPage


@given('I am logged in and have added a product to the cart')
def step_impl(context):
    context.login_page.login()
    context.inventory_page.click_add_product_to_cart()


@when('I go back to the inventory page')
def step_impl(context):
    context.inventory_page.click_shopping_cart_btn()


@then('I should see that the product count in the shopping cart icon is still 1')
def step_impl(context):
    assert context.shopping_cart_page.is_product_count_one
