import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()               # открываем страницу
    page.add_to_cart()        # добавляем товар в корзину
    page.solve_quiz_and_get_code()
    time.sleep(100)
    page.should_be_added_to_cart()
    page.should_be_message_in_cart_total()
    time.sleep(10)
