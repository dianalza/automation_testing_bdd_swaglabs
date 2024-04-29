from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.login_page import Login_page
import time


class Inventory_page(Login_page):

    items = {"Sauce Labs Backpack": "sauce-labs-backpack",
             "Sauce Labs Bike Light": "sauce-labs-bike-light",
             "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
             "Sauce Labs Fleece Jacket": "sauce-labs-fleece-jacket",
             "Sauce Labs Onesie": "sauce-labs-onesie",
             "Test.allTheThings() T-Shirt (Red)": "test.allthethings()-t-shirt-(red)"}

    ADD_TO_CART_BTN = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
    ITEMS_NUMBER_IN_CART = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    SHOPPING_CART_BTN = (By.XPATH, "//a[@class='shopping_cart_link']")
    REMOVE_BTN = (By.XPATH, '//button[contains(text(),"Remove")]')
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")


    def get_add_cart_locator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='add-to-cart-{item}']")

    def get_remove_locator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='remove-{item}']")

    def click_add_cart_item(self, item):
        for i in self.items.keys():
            if i == item:
                self.get_add_cart_locator(self.items.get(i)).click()

    def click_remove_item_from_cart(self): #este apelat in steps
        remove_button_list = self.chrome.find_elements(*self.REMOVE_BTN)
        for i in range(len(remove_button_list)):
            remove_button_list[i].click()

    def click_shopping_cart_btn(self):
        self.chrome.find_element(*self.SHOPPING_CART_BTN).click()

    def click_continue_shopping_btn(self): #este apelat in steps
        time.sleep(10)
        self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN).click()

    def check_no_of_items_in_cart(self):
        no_of_items = self.chrome.find_element(*self.ITEMS_NUMBER_IN_CART).text
        assert no_of_items == "1", "Fail: There are more than one items in cart."

    def check_item_in_cart(self):
        item_in_cart_text = self.chrome.find_element(*self.ITEMS_NUMBER_IN_CART).text
        assert int(item_in_cart_text) >= 1, f"Fail: The item was not displayed in cart."

    def check_remove_button_is_present(self):
        assert self.chrome.find_element(*self.REMOVE_BTN).is_displayed(),f"Fail:The remove button for the item is not displayed"

    def check_add_cart_button_is_present(self): #este apelat in steps
        assert self.chrome.find_element(*self.ADD_TO_CART_BTN).is_displayed(), f"Fail: The remove button for the item is not displayed"

    def click_add_product_to_cart(self):
        self.chrome.find_element(*self.ADD_TO_CART_BTN).click()

    def click_go_to_cart(self):
        self.chrome.find_element(*self.SHOPPING_CART_BTN).click()

    def sort_products_by_price_ascending(self):
        sort_dropdown = Select(self.chrome.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text("Price (low to high)")

    def sort_products_by_price_descending(self):
        sort_dropdown = Select(self.chrome.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text("Price (high to low)")

    def check_products_are_sorted_by_price_ascending(self):
        prices = self.chrome.find_elements(*self.INVENTORY_ITEM_PRICE)
        is_price_ascending = True
        price_text=[]

        for i in range(len(prices) - 1):
            price_text.append(prices[i].text.replace("$",""))
            if int(prices[i].text.replace("$","")) > int(prices[i + 1].text.replace("$","")):
                is_price_ascending = False
                break
        assert is_price_ascending == True, "Error prices are not sorted ascending"

    def check_products_are_sorted_by_price_descending(self):
        prices = self.chrome.find_elements(*self.INVENTORY_ITEM_PRICE)
        is_price_ascending = True
        for i in range(len(prices) - 1):
            if prices[i].text.replace("$","") < prices[i + 1].text.replace("$",""):
                is_price_ascending = False
                break
        assert is_price_ascending == True, "Error prices are not sorted ascending"

    def sort_products_by_name_ascending(self):
        sort_dropdown = Select(self.chrome.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text("Name (low to high)")

    def sort_products_by_name_descending(self):
        sort_dropdown = Select(self.chrome.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text("Name (high to low)")
    def check_products_are_sorted_by_name_ascending(self):
        pass

    def check_products_are_sorted_by_name_descending(self):
        pass







