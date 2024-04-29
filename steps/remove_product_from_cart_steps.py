from behave import given, when, then
from selenium import webdriver
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page
from pages.shopping_cart_page import ShoppingCartPage


@when('I click on the remove button in the shopping cart')
def step_impl(context):
    context.shopping_cart_page.remove_product()


