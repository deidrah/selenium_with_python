import string


from pages import my_account_page
from random import choice

from selenium.webdriver.remote.webdriver import WebDriver


def test_page_title(web_driver: WebDriver):
    assert my_account_page.check_page_title(web_driver) == "My account – Generic Shop"


def test_register_user(web_driver: WebDriver):
    user = "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10))
    hello_message = my_account_page.register_user(web_driver, user)
    assert user in hello_message, \
        f"{user} does not present in {hello_message}"


def test_login_user(web_driver: WebDriver):
    user = "dominika.python"
    hello_message = my_account_page.login_user(web_driver)
    assert user in hello_message, \
        f"{user} does not present in {hello_message}"


def test_logout_user(web_driver: WebDriver):
    assert my_account_page.logout_user(web_driver) == "Generic Shop – Just another web shop"


def test_user_orders(web_driver: WebDriver):
    assert my_account_page.check_user_orders(web_driver) == "Go shop\nNo order has been made yet."


def test_user_downloads(web_driver: WebDriver):
    assert my_account_page.check_user_downloads(web_driver) == "Go shop\nNo downloads available yet."


def test_user_addresses(web_driver: WebDriver):
    assert my_account_page.check_user_addresses(web_driver) == 'ADDRESSES'


def test_user_details(web_driver: WebDriver):
    assert my_account_page.check_user_details(web_driver) == 'MY ACCOUNT'
