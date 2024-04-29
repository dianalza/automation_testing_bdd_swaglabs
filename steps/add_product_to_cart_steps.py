from behave import given, when, then
from selenium import webdriver
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page
from pages.shopping_cart_page import ShoppingCartPage

@given('I am logged in')
def step_impl(context):
    context.login_page.login()

@when('I open a product and add it to the shopping cart')
def step_impl(context):
    context.inventory_page.click_add_product_to_cart()

@then('I should see the product count in the shopping cart')
def step_impl(context):
    context.shopping_cart_page.check_cart_count()
