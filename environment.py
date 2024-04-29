from browser import Browser
from pages.inventory_page import Inventory_page
from pages.login_page import Login_page
from pages.checkout_page import OrderPage
from pages.shopping_cart_page import ShoppingCartPage



def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.inventory_page = Inventory_page()
    context.order_page = OrderPage()
    context.shopping_cart_page = ShoppingCartPage()




def after_all(context):
    context.browser.close()
