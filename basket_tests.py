from selenium.webdriver.remote.webdriver import WebDriver
from pages import basket_page


def test_check_basket_quantity(web_driver: WebDriver):
    assert basket_page.add_to_basket(web_driver)[1] != basket_page.add_to_basket(web_driver)[0], "Warning koszyk"