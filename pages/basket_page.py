from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUBMIT_BUTTON), (
            "Basket is not empty")

    def empty_basket_message_appears(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TABLE), (
            "'Basket is empty' text is not present")
