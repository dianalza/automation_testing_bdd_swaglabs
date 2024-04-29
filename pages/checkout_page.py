from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    CHECK_OUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CHECK_OUT_CONTINUE_BTN = (By.ID,"continue")
    FINISH_ORDER_BTN = (By.ID, "finish")
    ORDER_CONFIRMATION_MESSAGE = (By.XPATH,'//h2[@class="complete-header"]')

    def click_checkout_btn(self):
        self.chrome.find_element(*self.CHECK_OUT_BTN).click()

    def verify_order_confirmation(self, message):
        confirmation_message = self.chrome.find_element(*self.ORDER_CONFIRMATION_MESSAGE)
        assert confirmation_message.is_displayed()
        assert message == confirmation_message.text

    def enter_shipping_information(self, first_name, last_name, zip_code):
        self.chrome.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)
        self.chrome.find_element(*self.ZIP_CODE).send_keys(zip_code)

    def click_checkout_continue_btn(self):
        self.chrome.find_element(*self.CHECK_OUT_CONTINUE_BTN).click()

    def finalize_order(self):
        self.chrome.find_element(*self.FINISH_ORDER_BTN).click()



