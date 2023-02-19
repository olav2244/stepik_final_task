import pytest

from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        check_login_url = str(self.browser.current_url)
        assert 'login' in check_login_url, "The url in not for the login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no registration form"

    pytest.fixture()

    def register_new_user(self, email, password):
        mail_box = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_BOX)
        mail_box.send_keys(email)
        pass_box = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_BOX)
        pass_confirm_box = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_BOX_CONFIRM)
        pass_box.send_keys(password)
        pass_confirm_box.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()
