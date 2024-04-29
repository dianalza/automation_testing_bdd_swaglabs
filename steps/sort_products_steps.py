from behave import given, when, then
from selenium import webdriver
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page


@when('I sort products in ascending order by price')
def step_impl(context):
    context.inventory_page.sort_products_by_price_ascending()


@when('I sort products in descending order by price')
def step_impl(context):
    context.inventory_page.sort_products_by_price_descending()


@then('I should see that the products are sorted correctly in ascending order by price')
def step_impl(context):
    context.inventory_page.check_products_are_sorted_by_price_ascending()

@then('I should see that the products are sorted correctly in descending order by price')
def step_impl(context):
    context.inventory_page.check_products_are_sorted_by_price_descending()

@when('I sort products in ascending order by name')
def step_impl(context):
    context.inventory_page.sort_products_by_name_ascending()

@when('I sort products in descending order by name')
def step_impl(context):
    context.inventory_page.sort_products_by_name_descending()

@then('I should see that the products are sorted correctly in ascending order by name')
def step_impl(context):
    context.inventory_page.check_products_are_sorted_by_name_ascending()

@then('I should see that the products are sorted correctly in descending order by name')
def step_impl(context):
    context.inventory_page.check_products_are_sorted_by_name_descending()
