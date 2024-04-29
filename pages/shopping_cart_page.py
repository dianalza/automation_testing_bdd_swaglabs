from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    # Elemente
    REMOVE_BUTTON = (By.XPATH, "//button[@class='btn_secondary cart_button']")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    PRODUCT_CART = (By.XPATH, '//div[@class="inventory_item_name"]')

    # Metode
    def remove_product(self):
        self.chrome.find_element(*self.REMOVE_BUTTON).click()

    def is_product_removed(self):
        return len(self.chrome.find_elements(*self.CART_ITEM)) == 0

    def is_product_count_zero(self):
        cart_count = self.chrome.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        return cart_count == ''

    def check_cart_count(self):
        assert len(self.chrome.find_elements(*self.PRODUCT_CART)) >=1

    def is_product_count_one(self):
        cart_count = self.chrome.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        return cart_count == 1

