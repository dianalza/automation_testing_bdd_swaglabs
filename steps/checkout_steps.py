from behave import given, when, then
from selenium import webdriver
from pages.checkout_page import OrderPage

@when('I proceed to checkout')
def step_impl(context):
    context.order_page.click_checkout_btn()

@when('I enter my shipping information:"{first_name}" "{last_name}" "{zip_code}"')
def step_impl(context, first_name, last_name, zip_code):
    context.order_page.enter_shipping_information(first_name, last_name, zip_code)

@when('I click continue')
def step_impl(context):
    context.order_page.click_checkout_continue_btn()

@when('I finalize the order')
def step_impl(context):
    context.order_page.finalize_order()

@then('I should see the "{message}" message')
def step_impl(context,message):
    context.order_page.verify_order_confirmation(message)




