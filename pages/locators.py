from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span a[href$="/basket/"].btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_BOX = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASS_BOX = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_PASS_BOX_CONFIRM = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_ADD_TO_CART_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]//h1')
    MESSAGE_ABOUT_ADDING = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    BASKET_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'span button[type="submit"].btn.btn-default')
    BASKET_TABLE = (By.CSS_SELECTOR, "div.basket-title.hidden-xs")


