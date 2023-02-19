from selenium.webdriver.remote.webdriver import WebDriver
from pages import main_page


def test_check_page_title(web_driver: WebDriver):
    assert main_page.check_page_title(web_driver).lower() == "black top"
