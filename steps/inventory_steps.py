from behave import *


@given("I am logged into the app")
def step_impl(context):
    context.login_page.login()

@when('I click Add to cart button to the item')
def step_impl(context):
    context.inventory_page.click_add_product_to_cart()

@then('The cart icon shows there is one item in cart')
def step_impl(context):
    context.inventory_page.check_no_of_items_in_cart()

@when('I go to the shopping cart')
def step_impl(context):
    context.inventory_page.click_shopping_cart_btn()

@then('The Remove button is displayed')
def step_impl(context):
    context.inventory_page.check_remove_button_is_present()

@then('The item is displayed in basket')
def step_impl(context):
    context.inventory_page.check_item_in_cart()

@when('I remove the item from the cart')
def step_impl(context):
    context.inventory_page.click_remove_item_from_cart()


@when('I go back to shopping list')
def step_impl(context):
    context.inventory_page.click_continue_shopping_btn()


@then('The Add to cart button is displayed for the item')
def step_impl(context):
    context.inventory_page.check_add_cart_button_is_present()