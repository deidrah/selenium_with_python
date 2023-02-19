import string
from random import choice
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Constant:
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='top-account']")
    REG_BUTTON = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    HELLO_MESSAGE = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='reg_email']")
    LOGIN_INPUT = (By.ID, "username")
    LOGIN_PASSWORD_INPUT = (By.ID, "password")
    REGISTER_PASSWORD_INPUT = (By.ID, "reg_password")
    LOGIN_BUTTON = (By.XPATH, "//input[@name='login']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href*='https://skleptest.pl/my-account/customer-logout/?']")
    REGISTER_BUTTON = (By.XPATH, "//h2[contains(text(),'Register')]")
    PAGE_TITLE = (By.XPATH, "//title")
    ORDERS_TAB = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/nav/ul/li[2]")
    TAB_TITLE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[1]/div/header/h1")
    ORDERS = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/div/div")
    DOWNLOADS_TAB = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/nav/ul/li[3]/a")
    DOWNLOADS = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/div/div")
    ADDRESSES_TAB = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/nav/ul/li[4]/a")
    DETAILS_TAB = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/article/div[2]/nav/ul/li[5]/a")


def fill_login_form(web_driver):
    user = "dominika.python"
    web_driver.find_element(*Constant.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constant.LOGIN_INPUT).send_keys(user + "@gmail.com")
    web_driver.find_element(*Constant.LOGIN_PASSWORD_INPUT).send_keys("Test123456789!")
    web_driver.find_element(*Constant.LOGIN_BUTTON).click()


def check_page_title(web_driver):
    fill_login_form(web_driver)
    return web_driver.title


def register_user(web_driver, user):
    web_driver.find_element(*Constant.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constant.EMAIL_INPUT).send_keys(user + "@gmail.com")
    web_driver.find_element(*Constant.REGISTER_PASSWORD_INPUT).send_keys(
        user.join(choice(string.punctuation) for i in range(10)))
    web_driver.find_element(*Constant.REGISTER_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constant.REG_BUTTON))
    web_driver.find_element(*Constant.REG_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constant.HELLO_MESSAGE).text
    return hello_message


def login_user(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constant.HELLO_MESSAGE).text
    return hello_message


def logout_user(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    web_driver.find_element(*Constant.LOGOUT_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.PAGE_TITLE))
    page_title = web_driver.title
    return page_title


def check_user_orders(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    web_driver.find_element(*Constant.ORDERS_TAB).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.TAB_TITLE))
    orders = web_driver.find_element(*Constant.ORDERS).text
    return orders


def check_user_downloads(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    web_driver.find_element(*Constant.DOWNLOADS_TAB).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.TAB_TITLE))
    downloads = web_driver.find_element(*Constant.DOWNLOADS).text
    return downloads


def check_user_addresses(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    web_driver.find_element(*Constant.ADDRESSES_TAB).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.TAB_TITLE))
    tab_title = web_driver.find_element(*Constant.TAB_TITLE).text
    return tab_title


def check_user_details(web_driver):
    fill_login_form(web_driver)
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    web_driver.find_element(*Constant.DETAILS_TAB).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.TAB_TITLE))
    tab_title = web_driver.find_element(*Constant.TAB_TITLE).text
    return tab_title
